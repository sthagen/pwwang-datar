<style>
.md-typeset__table {
   min-width: 100%;
}

.md-typeset table:not([class]) {
    display: table;
    max-width: 80%;
}
</style>

## Reference of `datar.dplyr`

Reference map of `r-tidyverse-tidyr` can be found [here][1].

<u>**Legend:**</u>

|Sample|Status|
|---|---|
|[normal]()|API that is regularly ported|
|<s>[strike-through]()</s>|API that is not ported, or not an API originally|
|[**bold**]()|API that is unique in `datar`|
|[_italic_]()|Working in process|

### Pivoting

|API|Description|Notebook example|
|---|---|---:|
|[pivot_longer()][26]|Pivot data from wide to long|[:material-notebook:][27]|
|[pivot_wider()][28]|Pivot data from long to wide|[:material-notebook:][29]|

### Rectangling

|API|Description|Notebook example|
|---|---|---:|
|_`hoist()`_ _`unnest_longer()`_ _`unnest_wider()`_ _`unnest_auto()`_|Rectangle a nested list into a tidy tibble||

### Nesting

|API|Description|Notebook example|
|---|---|---:|
|[`nest()`][9] [`unnest()`][10]|Nest and unnest|[:material-notebook:][11]|

### Character vectors

|API|Description|Notebook example|
|---|---|---:|
|[`extract()`][22]|Extract a character column into multiple columns using regular expression groups|[:material-notebook:][23]|
|[`separate()`][30]|Separate a character column into multiple columns with a regular expression or numeric locations|[:material-notebook:][31]|
|[`separate_rows()`][34]|Separate a collapsed column into multiple rows|[:material-notebook:][35]|
|[`unite()`][36]|Unite multiple columns into one by pasting strings together|[:material-notebook:][37]|

### Missing values

|API|Description|Notebook example|
|---|---|---:|
|[`complete()`][18]|Complete a data frame with missing combinations of data|[:material-notebook:][19]|
|[`drop_na()`][20]|Drop rows containing missing values|[:material-notebook:][21]|
|[`expand()`][12] [`crossing()`][13] [`nesting()`][14]|Expand data frame to include all possible combinations of values|[:material-notebook:][15]|
|[`expand_grid()`][16]|
|[`fill()`][24]|Fill in missing values with previous or next value|[:material-notebook:][25]|
|[`full_seq()`][40]|Create the full sequence of values in a vector|[:material-notebook:][41]|
|[`replace_na()`][38]|Replace NAs with specified values|[:material-notebook:][39]|

### Miscellanea

|API|Description|Notebook example|
|---|---|---:|
|[`chop()`][3] [`unchop()`][4]|Chop and unchop|[:material-notebook:][5]|
|[`pack()`][6] [`unpack()`][7]|Pack and unpack|[:material-notebook:][8]|
|[`uncount()`][32]|"Uncount" a data frame|[:material-notebook:][33]|

### Data

See [datasets][2]

[1]: https://tidyr.tidyverse.org/reference/index.html
[2]: ../datasets
[3]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.chop
[4]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.unchop
[5]: ../../notebooks/chop
[6]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.pack
[7]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.unpack
[8]: ../../notebooks/chop
[9]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.nest
[10]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.unnest
[11]: ../../notebooks/nest
[12]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.expand
[13]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.crossing
[14]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.nesting
[15]: ../../notebooks/expand
[16]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.expand_grid
[17]: ../../notebooks/expand_grid
[18]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.complete
[19]: ../../notebooks/complete
[20]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.drop_na
[21]: ../../notebooks/drop_na
[22]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.extract
[23]: ../../notebooks/extract
[24]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.fill
[25]: ../../notebooks/fill
[26]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.pivot_longer
[27]: ../../notebooks/pivot_longer
[28]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.pivot_wider
[29]: ../../notebooks/pivot_wider
[30]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.separate
[31]: ../../notebooks/separate
[32]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.uncount
[33]: ../../notebooks/uncount
[34]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.separate_rows
[35]: ../../notebooks/separate
[36]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.unite
[37]: ../../notebooks/unite
[38]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.replace_na
[39]: ../../notebooks/replace_na
[40]: ../../api/datar.apis.tidyr/#datar.apis.tidyr.full_seq
[41]: ../../notebooks/full_seq
