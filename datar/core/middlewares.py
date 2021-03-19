import builtins

from typing import (
    Any, Callable, Iterable, List, Mapping, Optional, Set, Tuple, Union
)
from abc import ABC
from threading import Lock

from pandas import DataFrame
from pandas.core.series import Series
from pipda.symbolic import DirectRefAttr
from pipda.context import Context, ContextBase, ContextSelect
from pipda.utils import DataContext, Expression, functype

from .utils import (
    align_value, df_assign_item, objectize, expand_collections, list_diff, sanitize_slice, select_columns,
    logger, to_df
)
from .contexts import ContextSelectSlice
from .types import DataFrameType, is_scalar

LOCK = Lock()

class MiddleWare(ABC):
    ...

class Collection(list):
    """Mimic the c function in R

    All elements will be flattened

    Args:
        *args: The elements
    """
    def __init__(self, *args: Any) -> None:
        super().__init__(expand_collections(args))

    def expand_slice(
            self,
            total: Union[int, Iterable[int]]
    ) -> Union[List[int], List[List[int]]]:
        """Expand the slice in the list in a groupby-aware way"""


class Inverted:
    """Inverted object, pending for next action"""

    def __init__(
            self,
            elems: Any,
            data: DataFrameType,
            context: ContextBase = Context.SELECT.value
    ) -> None:
        self.data = objectize(data)
        self.context = context
        if isinstance(elems, slice):
            if isinstance(context, ContextSelectSlice):
                self.elems = [elems]
            else:
                columns = self.data.columns.tolist()
                self.elems = columns[sanitize_slice(elems, columns)]
        elif not isinstance(elems, Collection):
            if is_scalar(elems):
                self.elems = Collection(elems)
            else:
                self.elems = Collection(*elems)
        elif not isinstance(context, ContextSelectSlice):
            columns = self.data.columns.to_list()
            self.elems = [
                columns[elem] if isinstance(elem, int) else elem
                for elem in elems
            ]
        else:
            self.elems = elems
        self._complements = None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Inverted):
            return False
        return self.elem == other.elem and self.data == other.data

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    @property
    def complements(self):
        if isinstance(self.context, ContextSelectSlice):
            # slice literal not being expanded
            return self
        if self._complements is None:
            self._complements = list_diff(self.data.columns, self.elems)
        return self._complements

    def __repr__(self) -> str:
        return f"Inverted({self.elems})"

class Negated:

    def __init__(self, elems: Union[slice, list]) -> None:
        """In case of -[1,2,3] or -c(1,2,3) or -f[1:3]"""
        self.elems = [elems] if isinstance(elems, slice) else elems

    def __repr__(self) -> str:
        return f"Negated({self.elems})"

class DescSeries(Series):

    @property
    def _constructor(self):
        return DescSeries

class CurColumn:

    @classmethod
    def replace_args(cls, args: Tuple[Any], column: str) -> Tuple[Any]:
        return tuple(column if isinstance(arg, cls) else arg for arg in args)

    @classmethod
    def replace_kwargs(
            cls,
            kwargs: Mapping[str, Any],
            column: str
    ) -> Mapping[str, Any]:
        return {
            key: column if isinstance(val, cls) else val
            for key, val in kwargs.items()
        }

class Across(MiddleWare):

    def __init__(
            self,
            data: DataFrameType,
            cols: Optional[Iterable[str]] = None,
            fns: Optional[Union[
                Callable,
                Iterable[Callable],
                Mapping[str, Callable]
            ]] = None,
            names: Optional[str] = None,
            args: Tuple[Any] = (),
            kwargs: Optional[Mapping[str, Any]] = None
    ) -> None:
        from ..dplyr.funcs import everything
        cols = everything(data) if cols is None else cols
        if not isinstance(cols, (list, tuple)):
            cols = [cols]
        cols = select_columns(objectize(data).columns, *cols)

        fns_list = []
        if callable(fns):
            fns_list.append({'fn': fns})
        elif isinstance(fns, (list, tuple)):
            fns_list.extend(
                {'fn': fn, '_fn': i, '_fn1': i+1}
                for i, fn in enumerate(fns)
            )
        elif isinstance(fns, dict):
            fns_list.extend(
                {'fn': value, '_fn': key}
                for key, value in fns.items()
            )
        elif fns is not None:
            raise ValueError(
                'Argument `_fns` of across must be None, a function, '
                'a formula, or a dict of functions.'
            )

        self.data = data
        self.cols = cols
        self.fns = fns_list
        self.names = names
        self.args = args
        self.kwargs = kwargs or {}
        self.context = None

    def desc_cols(self) -> Set[str]:
        from ..dplyr.funcs import desc
        if len(self.fns) != 1:
            return set()
        if self.fns[0]['fn'] is not desc:
            return set()
        return set(self.cols)

    def evaluate(
            self,
            data: Optional[DataFrameType] = None,
            context: Optional[Union[Context, ContextBase]] = None
    ) -> Union[List[str], DataFrame]:
        if data is None:
            data = self.data

        if isinstance(context, Context):
            context = context.value

        if context.name == 'select':
            if not self.fns:
                return self.cols
            fn = self.fns[0]['fn']
            # todo: check # fns
            pipda_type = functype(fn)
            return [
                fn(col, *self.args, **self.kwargs) if pipda_type == 'plain'
                else fn(
                    col,
                    *CurColumn.replace_args(self.args, col),
                    **CurColumn.replace_kwargs(self.kwargs, col),
                    _calling_type='piping'
                ).evaluate(data)
                for col in self.cols
            ]

        if not self.fns:
            self.fns = [{'fn': lambda x: x}]

        ret = None
        for column in self.cols:
            for fn_info in self.fns:
                render_data = fn_info.copy()
                render_data['_col'] = column
                fn = render_data.pop('fn')
                name_format = self.names
                if not name_format:
                    name_format = (
                        '{_col}_{_fn}' if '_fn' in render_data
                        else '{_col}'
                    )

                name = name_format.format(**render_data)
                if functype(fn) == 'plain':
                    value = fn(
                        context.getattr(data, column),
                        *CurColumn.replace_args(self.args, column),
                        **CurColumn.replace_kwargs(self.kwargs, column)
                    )
                else:
                    # use fn's own context
                    value = fn(
                        DirectRefAttr(data, column),
                        *CurColumn.replace_args(self.args, column),
                        **CurColumn.replace_kwargs(self.kwargs, column),
                        _calling_type='piping'
                    ).evaluate(data)
                if ret is None:
                    ret = to_df(value, name)
                else:
                    df_assign_item(ret, name, value)
        return DataFrame() if ret is None else ret

class CAcross(Across):

    def __init__(
            self,
            data: DataFrameType,
            cols: Optional[Iterable[str]] = None,
            fns: Optional[Union[
                Callable,
                Iterable[Callable],
                Mapping[str, Callable]
            ]] = None,
            names: Optional[str] = None,
            args: Tuple[Any] = (),
            kwargs: Optional[Mapping[str, Any]] = None
    ) -> None:
        super().__init__(data, cols, fns, names, args, kwargs)

        if not self.fns:
            raise ValueError(
                "No functions specified for c_across. "
                "Note that the usage of c_across is different from R's. "
                "You have to specify the function inside c_across, instead of "
                "calling it with c_across(...) as arguments."
            )

        if len(self.fns) > 1:
            raise ValueError("Only a single function is allowed in c_across.")

        self.fn = self.fns[0]['fn']

    def evaluate(
            self,
            data: Optional[DataFrameType] = None,
            context: Optional[Union[Context, ContextBase]] = None
    ) -> Union[List[str], DataFrame]:
        if isinstance(context, Context):
            context = context.value

        if data is None:
            data = self.data

        if not isinstance(data, RowwiseDataFrame):
            return super().evaluate(data, context)

        return DataFrame(
            data[self.cols].apply(
                self.fn,
                axis=1,
                args=self.args,
                **self.kwargs
            ),
            columns=[self.names] if isinstance(self.names, str) else self.names
        )

class IfCross(Across, ABC):

    if_type = None

    def __init__(
            self,
            data: DataFrameType,
            cols: Optional[Iterable[str]] = None,
            fns: Optional[Union[
                Callable,
                Iterable[Callable],
                Mapping[str, Callable]
            ]] = None,
            names: Optional[str] = None,
            args: Tuple[Any] = (),
            kwargs: Optional[Mapping[str, Any]] = None
    ) -> None:
        super().__init__(data, cols, fns, names, args, kwargs)

        func_name = f"if_{self.__class__.if_type}"
        if not self.fns:
            raise ValueError(f"No functions specified for {func_name!r}.")

        if len(self.fns) > 1:
            raise ValueError(
                f"Only a single function is allowed in {func_name!r}."
            )

        self.fn = self.fns[0]['fn']

    def evaluate(
            self,
            data: Optional[DataFrameType] = None,
            context: Optional[Union[Context, ContextBase]] = None
    ) -> Union[List[str], DataFrame]:
        if not self.fns:
            raise ValueError("No functions specified for if_any.")

        if isinstance(context, Context):
            context = context.value

        if data is None:
            data = self.data

        agg_func = getattr(builtins, self.__class__.if_type)

        pipda_type = getattr(self.fn, '__pipda__', None)
        if pipda_type not in (None, 'PlainFunction'):
            def transform_fn(*args, **kwargs):
                return self.fn(data, *args, **kwargs)
            transform_fn = lambda *args, **kwargs: self.fn(
                data, *args, **kwargs
            )
        else:
            transform_fn = self.fn

        def if_fn(_series, *args, **kwargs):
            return agg_func(
                _series.transform(transform_fn, *args, **kwargs
            ).fillna(False).astype('boolean'))

        return data[self.cols].apply(
            if_fn,
            axis=1,
            args=self.args,
            **self.kwargs
        )

class IfAny(IfCross):

    if_type = 'any'

class IfAll(IfCross):

    if_type = 'all'

class RowwiseDataFrame(DataFrame):

    def __init__(
            self,
            *args: Any,
            rowwise: Optional[Iterable[str]] = None,
            **kwargs: Any
    ) -> None:
        super().__init__(*args, **kwargs)
        self.flags.rowwise = rowwise or True

class ContextWithData:

    def __init__(self, data: Any) -> None:
        self.data = DataContext(data)

    def __enter__(self) -> Any:
        return self.data

    def __exit__(self, *exc_info) -> None:
        self.data.delete()

class Nesting:

    def __init__(self, *columns: Any, **kwargs: Any) -> None:
        self.columns = []
        self.names = []

        id_prefix = hex(id(self))[2:6]
        for i, column in enumerate(columns):
            self.columns.append(column)
            if isinstance(column, str):
                self.names.append(column)
                continue
            try:
                # series
                name = column.name
            except AttributeError:
                name = f'_tmp{id_prefix}_{i}'
                logger.warning(
                    'Temporary name used for a nesting column, use '
                    'keyword argument instead to specify the key as name.'
                )
            self.names.append(name)

        for key, val in kwargs.items():
            self.columns.append(val)
            self.names.append(key)

    def __len__(self):
        return len(self.columns)
