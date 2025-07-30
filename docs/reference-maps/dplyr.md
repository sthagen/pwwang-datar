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

Reference map of `r-tidyverse-dplyr` can be found [here][1].

<u>**Legend:**</u>

|Sample|Status|
|---|---|
|[normal]()|API that is regularly ported|
|<s>[strike-through]()</s>|API that is not ported, or not an API originally|
|[**bold**]()|API that is unique in `datar`|
|[_italic_]()|Working in process|

### One table verbs

|API|Description|Notebook example|
|---|---|---:|
|[arrange()][2]|Arrange rows by column values| [:material-notebook:][3] |
|[count()][4] [tally()][5] [add_count()][6] [add_tally()][7]|Count observations by group| [:material-notebook:][8] |
|[distinct()][9]|Subset distinct/unique rows| [:material-notebook:][10] |
|[filter()][11]|Subset rows using column values| [:material-notebook:][12] |
|[mutate()][13] [transmute()][14]|Create, modify, and delete columns| [:material-notebook:][15] |
|[pull()][16]|Extract a single column| [:material-notebook:][17] |
|[reframe()][142]|Reframe a data frame| [:material-notebook:][142] |
|[relocate()][18]|Change column order| [:material-notebook:][19] |
|[rename()][20] [rename_with()][21]|Rename columns| [:material-notebook:][22] |
|[select()][23]|	Subset columns using their names and types| [:material-notebook:][24] |
|[summarise() summarize()][25]| Summarise each group to fewer rows| [:material-notebook:][26] |
|[slice()][27] [slice_head()][28] [slice_tail()][29] [slice_min()][30] [slice_max()][31] [slice_sample()][32]| Subset rows using their positions| [:material-notebook:][33] |

### Two table verbs

|API|Description|Notebook example|
|---|---|---:|
|[bind_rows()][34] [bind_cols()][35]|Efficiently bind multiple data frames by row and column|[:material-notebook:][36]|
|[intersect()][37] [setdiff()][38] [setequal()][39] [union()][40]|Set operations on data frame|[:material-notebook:][41]|
|[all_of()][42] [any_of()][43] [contains()][44] [ends_with()][45] [everything()][46] [last_col()][47] [matches()][48] [num_range()][49] [one_of()][50] [starts_with()][51]|Select variables from character vectors|[:material-notebook:][52]|
|[union_all()][53]|Set operations|[:material-notebook:][54]|
|[inner_join()][55] [left_join()][56] [right_join()][57] [full_join()][58]|Mutating joins|[:material-notebook:][59]|
|[nest_join()][60]|Nest join|[:material-notebook:][61]|
|[semi_join()][62] [anti_join()][63]|Filtering joins|[:material-notebook:][64]|

### Grouping

|API|Description|Notebook example|
|---|---|---:|
|[group_by()][65] [ungroup()][66]|Group by one or more variables|[:material-notebook:][67]|
|[group_cols() group_vars()][68]|Select grouping variables|[:material-notebook:][69]|
|[rowwise()][70]|Group input by rows|[:material-notebook:][71]|

### Vector functions

|API|Description|Notebook example|
|---|---|---:|
|[across()][72] [if_any()][73] [if_all()][74]|Apply a function (or functions) across multiple columns|[:material-notebook:][75]|
|[c_across()][76]|Combine values from multiple columns|[:material-notebook:][77]|
|[between()][78]|Do values in a numeric vector fall in specified range?|[:material-notebook:][79]|
|[case_when()][80]|A general vectorised if|[:material-notebook:][81]|
|[coalesce()][82]|Find first non-missing element|[:material-notebook:][83]|
|[cumall()][84] [cumany()][85] [cummean()][86]|Cumulativate versions of any, all, and mean|[:material-notebook:][87]|
|[desc()][88]|Descending order|[:material-notebook:][89]|
|[if_else()][90]|Vectorised if|[:material-notebook:][91]|
|[lag()][92] [lead()][93]|Compute lagged or leading values|[:material-notebook:][94]|
|[order_by()][95]|A helper function for ordering window function output|[:material-notebook:][96]|
|[n()][97] [cur_data()][98] [cur_data_all()][99] [cur_group()][100] [cur_group_id()][101] [cur_group_rows()][102] [cur_column()][103]|Context dependent expressions|[:material-notebook:][104]|
|[n_distinct()][105]|Efficiently count the number of unique values in a set of vectors|[:material-notebook:][106]|
|[na_if()][107]|Convert values to NA|[:material-notebook:][108]|
|[near()][109]|Compare two numeric vectors|[:material-notebook:][110]|
|[nth()][111] [first()][112] [last()][113]|Extract the first, last or nth value from a vector|[:material-notebook:][114]|
|[row_number()][115] [ntile()][116] [min_rank()][117] [dense_rank()][118] [percent_rank()][119] [cume_dist()][120]|Windowed rank functions.|[:material-notebook:][121]|
|[recode()][122] [recode_factor()][123]|Recode values|[:material-notebook:][124]|

### Data

See [datasets][125]

### <s>Remote tables</s>

### Experimental

|API|Description|Notebook example|
|---|---|---:|
|[group_map()][126] [group_modify()][127] [group_walk()][128]|Apply a function to each group|[:material-notebook:][129]|
|[group_trim()][130]|Trim grouping structure|[:material-notebook:][131]|
|[group_split()][132]|Split data frame by groups|[:material-notebook:][133]|
|[with_groups()][134]|Perform an operation with temporary groups|[:material-notebook:][135]|
|[rows_insert()][136] [rows_update()][137] [rows_patch()][138] [rows_upsert()][139] [rows_delete()][140]|Manipulate individual rows|[:material-notebook:][141]|

### <s>Questioning</s>

### <s>Superseded</s>


[1]: https://dplyr.tidyverse.org/reference/index.html
[2]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.arrange
[3]: ../../notebooks/arrange
[4]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.count
[5]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.tally
[6]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.add_count
[7]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.add_tally
[8]: ../../notebooks/count
[9]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.distinct
[10]: ../../notebooks/distinct
[11]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.filter
[12]: ../../notebooks/filter
[13]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.mutate
[14]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.transmutate
[15]: ../../notebooks/mutate
[16]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.pull
[17]: ../../notebooks/pull
[18]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.relocate
[19]: ../../notebooks/relocate
[20]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.rename
[21]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.rename_with
[22]: ../../notebooks/rename
[23]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.select
[24]: ../../notebooks/select
[25]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.summarise
[26]: ../../notebooks/summarise
[27]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.slice
[28]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.slice_head
[29]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.slice_tail
[30]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.slice_min
[31]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.slice_max
[32]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.slice_sample
[33]: ../../notebooks/slice
[34]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.bind_rows
[35]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.bind_cols
[36]: ../../notebooks/bind
[37]: ../../api/datar.base.verbs/#datar.base.verbs.intersect
[38]: ../../api/datar.base.verbs/#datar.base.verbs.setdiff
[39]: ../../api/datar.base.verbs/#datar.base.verbs.seqequal
[40]: ../../api/datar.base.verbs/#datar.base.verbs.union
[41]: ../../notebooks/setops
[42]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.all_of
[43]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.any_of
[44]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.contains
[45]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.ends_with
[46]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.everything
[47]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.last_col
[48]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.matches
[49]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.num_range
[50]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.one_of
[51]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.starts_with
[52]: ../../notebooks/select
[53]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.union_all
[54]: ../../notebooks/select
[55]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.inner_join
[56]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.left_join
[57]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.right_join
[58]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.full_join
[59]: ../../notebooks/mutate-joins
[60]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.nest_join
[61]: ../../notebooks/nest-join
[62]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.semi_join
[63]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.anti_join
[64]: ../../notebooks/filter-joins
[65]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.group_by
[66]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.ungroup
[67]: ../../notebooks/group_by
[68]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.group_vars
[69]: ../../notebooks/group_by
[70]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.rowwise
[71]: ../../notebooks/rowwise
[72]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.across
[73]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.if_any
[74]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.if_all
[75]: ../../notebooks/across
[76]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.c_across
[77]: ../../notebooks/across
[78]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.between
[79]: ../../notebooks/between
[80]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.case_when
[81]: ../../notebooks/case_when
[82]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.coalesce
[83]: ../../notebooks/coalesce
[84]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.cumall
[85]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.cumany
[86]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.cummean
[87]: ../../notebooks/cumall
[88]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.desc
[89]: ../../notebooks/desc
[90]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.if_else
[91]: ../../notebooks/case_when
[92]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.lag
[93]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.lead
[94]: ../../notebooks/lead-lag
[95]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.order_by
[96]: ../../notebooks/lead-lag
[97]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.n
[98]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.cur_data
[99]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.cur_data_all
[100]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.cur_group
[101]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.cur_group_id
[102]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.cur_group_rows
[103]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.cur_column
[104]: ../../notebooks/context
[105]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.n_distinct
[106]: ../../notebooks/distinct
[107]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.na_if
[108]: ../../notebooks/na_if
[109]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.near
[110]: ../../notebooks/near
[111]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.nth
[112]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.first
[113]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.last
[114]: ../../notebooks/nth
[115]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.row_number
[116]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.ntile
[117]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.min_rank
[118]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.dense_rank
[119]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.percent_rank
[120]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.cume_dist
[121]: ../../notebooks/ranking
[122]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.recode
[123]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.recode_factor
[124]: ../../notebooks/recode
[125]: ../datasets
[126]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.group_map
[127]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.group_modify
[128]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.group_walk
[129]: ../../notebooks/group_map
[130]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.group_trim
[131]: ../../notebooks/group_trim
[132]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.group_split
[133]: ../../notebooks/group_split
[134]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.with_groups
[135]: ../../notebooks/with_groups
[136]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.rows_insert
[137]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.rows_update
[138]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.rows_patch
[139]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.rows_upsert
[140]: ../../api/datar.apis.dplyr/#datar.apis.dplyr.rows_delete
[141]: ../../notebooks/rows
[142]: ../../notebooks/reframe
