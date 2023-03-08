::: {md-component="skip"}
[Skip to content](#welcome-to-mkdocs){.md-skip}
:::

::: {md-component="announce"}
:::

::: {.md-header md-component="header"}
[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDhhMyAzIDAgMCAwIDMtMyAzIDMgMCAwIDAtMy0zIDMgMyAwIDAgMC0zIDMgMyAzIDAgMCAwIDMgM20wIDMuNTRDOS42NCA5LjM1IDYuNSA4IDMgOHYxMWMzLjUgMCA2LjY0IDEuMzUgOSAzLjU0IDIuMzYtMi4xOSA1LjUtMy41NCA5LTMuNTRWOGMtMy41IDAtNi42NCAxLjM1LTkgMy41NFoiPjwvcGF0aD48L3N2Zz4=)](. "My Docs"){.md-header__button
.md-logo aria-label="My Docs" md-component="logo"}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTMgNmgxOHYySDNWNm0wIDVoMTh2Mkgzdi0ybTAgNWgxOHYySDN2LTJaIj48L3BhdGg+PC9zdmc+)

::: {.md-header__title md-component="header-title"}
::: md-header__ellipsis
::: md-header__topic
[ My Docs ]{.md-ellipsis}
:::

::: {.md-header__topic md-component="header-topic"}
[ Welcome to MkDocs ]{.md-ellipsis}
:::
:::
:::
:::

::: {.md-container md-component="container"}
::: {.md-main role="main" md-component="main"}
::: {.md-main__inner .md-grid}
::: {.md-sidebar .md-sidebar--primary md-component="sidebar" md-type="navigation"}
::: md-sidebar__scrollwrap
::: md-sidebar__inner
[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDhhMyAzIDAgMCAwIDMtMyAzIDMgMCAwIDAtMy0zIDMgMyAwIDAgMC0zIDMgMyAzIDAgMCAwIDMgM20wIDMuNTRDOS42NCA5LjM1IDYuNSA4IDMgOHYxMWMzLjUgMCA2LjY0IDEuMzUgOSAzLjU0IDIuMzYtMi4xOSA1LjUtMy41NCA5LTMuNTRWOGMtMy41IDAtNi42NCAxLjM1LTkgMy41NFoiPjwvcGF0aD48L3N2Zz4=)](. "My Docs"){.md-nav__button
.md-logo aria-label="My Docs" md-component="logo"} My Docs

-   Welcome to MkDocs []{.md-nav__icon .md-icon} [Welcome to
    MkDocs](.){.md-nav__link .md-nav__link--active}
    []{.md-nav__icon .md-icon} Table of contents
    -   [Commands](#commands){.md-nav__link}
    -   [Project layout](#project-layout){.md-nav__link}
    -   [validmind](#validmind){.md-nav__link}
    -   [Dataset](#validmind.Dataset){.md-nav__link}
        -   [transformed_dataset](#validmind.vm_models.dataset.Dataset.transformed_dataset){.md-nav__link}
        -   [x](#validmind.vm_models.dataset.Dataset.x){.md-nav__link}
        -   [y](#validmind.vm_models.dataset.Dataset.y){.md-nav__link}
        -   [\_\_post_init\_\_()](#validmind.vm_models.dataset.Dataset.__post_init__){.md-nav__link}
        -   [describe()](#validmind.vm_models.dataset.Dataset.describe){.md-nav__link}
        -   [get_correlation_plots()](#validmind.vm_models.dataset.Dataset.get_correlation_plots){.md-nav__link}
        -   [get_correlations()](#validmind.vm_models.dataset.Dataset.get_correlations){.md-nav__link}
        -   [get_feature_by_id()](#validmind.vm_models.dataset.Dataset.get_feature_by_id){.md-nav__link}
        -   [get_feature_type()](#validmind.vm_models.dataset.Dataset.get_feature_type){.md-nav__link}
        -   [serialize()](#validmind.vm_models.dataset.Dataset.serialize){.md-nav__link}
    -   [DatasetTargets](#validmind.DatasetTargets){.md-nav__link}
    -   [Figure](#validmind.Figure){.md-nav__link}
        -   [serialize()](#validmind.vm_models.figure.Figure.serialize){.md-nav__link}
    -   [Metric](#validmind.Metric){.md-nav__link}
        -   [\_\_post_init\_\_()](#validmind.vm_models.metric.Metric.__post_init__){.md-nav__link}
        -   [cache_results()](#validmind.vm_models.metric.Metric.cache_results){.md-nav__link}
        -   [run()](#validmind.vm_models.metric.Metric.run){.md-nav__link}
    -   [Model](#validmind.Model){.md-nav__link}
        -   [is_supported_model()](#validmind.vm_models.model.Model.is_supported_model){.md-nav__link}
        -   [predict()](#validmind.vm_models.model.Model.predict){.md-nav__link}
        -   [serialize()](#validmind.vm_models.model.Model.serialize){.md-nav__link}
    -   [ModelAttributes](#validmind.ModelAttributes){.md-nav__link}
    -   [ThresholdTest](#validmind.ThresholdTest){.md-nav__link}
        -   [\_\_post_init\_\_()](#validmind.vm_models.threshold_test.ThresholdTest.__post_init__){.md-nav__link}
        -   [cache_results()](#validmind.vm_models.threshold_test.ThresholdTest.cache_results){.md-nav__link}
        -   [run()](#validmind.vm_models.threshold_test.ThresholdTest.run){.md-nav__link}
    -   [init()](#validmind.init){.md-nav__link}
    -   [init_dataset()](#validmind.init_dataset){.md-nav__link}
    -   [init_model()](#validmind.init_model){.md-nav__link}
    -   [log_dataset()](#validmind.log_dataset){.md-nav__link}
    -   [log_figure()](#validmind.log_figure){.md-nav__link}
    -   [log_metadata()](#validmind.log_metadata){.md-nav__link}
    -   [log_metrics()](#validmind.log_metrics){.md-nav__link}
    -   [log_model()](#validmind.log_model){.md-nav__link}
    -   [log_test_results()](#validmind.log_test_results){.md-nav__link}
:::
:::
:::

::: {.md-sidebar .md-sidebar--secondary md-component="sidebar" md-type="toc"}
::: md-sidebar__scrollwrap
::: md-sidebar__inner
[]{.md-nav__icon .md-icon} Table of contents

-   [Commands](#commands){.md-nav__link}
-   [Project layout](#project-layout){.md-nav__link}
-   [validmind](#validmind){.md-nav__link}
-   [Dataset](#validmind.Dataset){.md-nav__link}
    -   [transformed_dataset](#validmind.vm_models.dataset.Dataset.transformed_dataset){.md-nav__link}
    -   [x](#validmind.vm_models.dataset.Dataset.x){.md-nav__link}
    -   [y](#validmind.vm_models.dataset.Dataset.y){.md-nav__link}
    -   [\_\_post_init\_\_()](#validmind.vm_models.dataset.Dataset.__post_init__){.md-nav__link}
    -   [describe()](#validmind.vm_models.dataset.Dataset.describe){.md-nav__link}
    -   [get_correlation_plots()](#validmind.vm_models.dataset.Dataset.get_correlation_plots){.md-nav__link}
    -   [get_correlations()](#validmind.vm_models.dataset.Dataset.get_correlations){.md-nav__link}
    -   [get_feature_by_id()](#validmind.vm_models.dataset.Dataset.get_feature_by_id){.md-nav__link}
    -   [get_feature_type()](#validmind.vm_models.dataset.Dataset.get_feature_type){.md-nav__link}
    -   [serialize()](#validmind.vm_models.dataset.Dataset.serialize){.md-nav__link}
-   [DatasetTargets](#validmind.DatasetTargets){.md-nav__link}
-   [Figure](#validmind.Figure){.md-nav__link}
    -   [serialize()](#validmind.vm_models.figure.Figure.serialize){.md-nav__link}
-   [Metric](#validmind.Metric){.md-nav__link}
    -   [\_\_post_init\_\_()](#validmind.vm_models.metric.Metric.__post_init__){.md-nav__link}
    -   [cache_results()](#validmind.vm_models.metric.Metric.cache_results){.md-nav__link}
    -   [run()](#validmind.vm_models.metric.Metric.run){.md-nav__link}
-   [Model](#validmind.Model){.md-nav__link}
    -   [is_supported_model()](#validmind.vm_models.model.Model.is_supported_model){.md-nav__link}
    -   [predict()](#validmind.vm_models.model.Model.predict){.md-nav__link}
    -   [serialize()](#validmind.vm_models.model.Model.serialize){.md-nav__link}
-   [ModelAttributes](#validmind.ModelAttributes){.md-nav__link}
-   [ThresholdTest](#validmind.ThresholdTest){.md-nav__link}
    -   [\_\_post_init\_\_()](#validmind.vm_models.threshold_test.ThresholdTest.__post_init__){.md-nav__link}
    -   [cache_results()](#validmind.vm_models.threshold_test.ThresholdTest.cache_results){.md-nav__link}
    -   [run()](#validmind.vm_models.threshold_test.ThresholdTest.run){.md-nav__link}
-   [init()](#validmind.init){.md-nav__link}
-   [init_dataset()](#validmind.init_dataset){.md-nav__link}
-   [init_model()](#validmind.init_model){.md-nav__link}
-   [log_dataset()](#validmind.log_dataset){.md-nav__link}
-   [log_figure()](#validmind.log_figure){.md-nav__link}
-   [log_metadata()](#validmind.log_metadata){.md-nav__link}
-   [log_metrics()](#validmind.log_metrics){.md-nav__link}
-   [log_model()](#validmind.log_model){.md-nav__link}
-   [log_test_results()](#validmind.log_test_results){.md-nav__link}
:::
:::
:::

::: {.md-content md-component="content"}
# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

-   `mkdocs new [dir-name]` - Create a new project.
-   `mkdocs serve` - Start the live-reloading docs server.
-   `mkdocs build` - Build the documentation site.
-   `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

::: {.doc .doc-object .doc-module}
[]{#validmind}

::: {.doc .doc-contents .first}
Exports

::: {.doc .doc-children}
::: {.doc .doc-object .doc-class}
## `Dataset` [ [`dataclass`]{.small} ]{.doc .doc-labels} {#validmind.Dataset .doc .doc-heading}

::: {.doc .doc-contents}
Model class wrapper

Source code in `validmind/vm_models/dataset.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|      27                           |                                   |
|      28                           |     @dataclass()                  |
|      29                           |     class Dataset:                |
|      30                           |         """                       |
|      31                           |         Model class wrapper       |
|      32                           |         """                       |
|      33                           |                                   |
|      34                           |         raw_dataset: object       |
|      35                           |         fields: list              |
|      36                           |         variables: list           |
|      37                           |         sample: list              |
|      38                           |         shape: dict               |
|      39                           |                                   |
|      40                           | correlation_matrix: object = None |
|      41                           |         correlations: dict = None |
|      42                           |         type: str = None          |
|      43                           |         options: dict = None      |
|      44                           |         statistics: dict = None   |
|      45                           |                                   |
|      46                           |         # Specif                  |
|      47                           | y targets via DatasetTargets or v |
|      48                           | ia target_column and class_labels |
|      49                           |         targets: dict = None      |
|      50                           |         target_column: str = ""   |
|      51                           |         class_labels: dict = None |
|      52                           |                                   |
|      53                           |         __feature_lookup: d       |
|      54                           | ict = field(default_factory=dict) |
|      55                           |                                   |
|      56                           |   __transformed_df: object = None |
|      57                           |                                   |
|      58                           |         def __post_init__(self):  |
|      59                           |             """                   |
|      60                           |             Set target_column and |
|      61                           |  class_labels from DatasetTargets |
|      62                           |             """                   |
|      63                           |             if self.targets:      |
|      64                           |                 self.target_co    |
|      65                           | lumn = self.targets.target_column |
|      66                           |                 self.class_l      |
|      67                           | abels = self.targets.class_labels |
|      68                           |                                   |
|      69                           |         @property                 |
|      70                           |         def x(self):              |
|      71                           |             """                   |
|      72                           |                                   |
|      73                           |    Returns the dataset's features |
|      74                           |             """                   |
|      75                           |                                   |
|      76                           |           return self.raw_dataset |
|      77                           | .drop(self.target_column, axis=1) |
|      78                           |                                   |
|      79                           |         @property                 |
|      80                           |         def y(self):              |
|      81                           |             """                   |
|      82                           |             Re                    |
|      83                           | turns the dataset's target column |
|      84                           |             """                   |
|      85                           |             return sel            |
|      86                           | f.raw_dataset[self.target_column] |
|      87                           |                                   |
|      88                           |         def get                   |
|      89                           | _feature_by_id(self, feature_id): |
|      90                           |             """                   |
|      91                           |                                   |
|      92                           |        Returns the feature with t |
|      93                           | he given id. We also build a lazy |
|      94                           |                                   |
|      95                           | lookup cache in case the same fea |
|      96                           | ture is requested multiple times. |
|      97                           |             """                   |
|      98                           |             if feature            |
|      99                           | _id not in self.__feature_lookup: |
|     100                           |                                   |
|     101                           |       for feature in self.fields: |
|     102                           |                                   |
|     103                           |   if feature["id"] == feature_id: |
|     104                           |                                   |
|     105                           |                        self.__fea |
|     106                           | ture_lookup[feature_id] = feature |
|     107                           |                                   |
|     108                           |                    return feature |
|     109                           |                                   |
|     110                           |   raise ValueError(f"Feature with |
|     111                           |  id {feature_id} does not exist") |
|     112                           |                                   |
|     113                           |             return                |
|     114                           | self.__feature_lookup[feature_id] |
|     115                           |                                   |
|     116                           |         def ge                    |
|     117                           | t_feature_type(self, feature_id): |
|     118                           |             """                   |
|     119                           |             Returns the type      |
|     120                           |  of the feature with the given id |
|     121                           |             """                   |
|     122                           |             feature = s           |
|     123                           | elf.get_feature_by_id(feature_id) |
|     124                           |                                   |
|     125                           |            return feature["type"] |
|     126                           |                                   |
|     127                           |         def serialize(self):      |
|     128                           |             """                   |
|     129                           |                                   |
|     130                           |  Serializes the model to a dictio |
|     131                           | nary so it can be sent to the API |
|     132                           |             """                   |
|     133                           |             dataset_dict = {      |
|     134                           |                                   |
|     135                           |              "shape": self.shape, |
|     136                           |                                   |
|     137                           |                "type": self.type, |
|     138                           |             }                     |
|     139                           |                                   |
|     140                           |             # Data                |
|     141                           | set with no targets can be logged |
|     142                           |             if self.targets:      |
|     143                           |                 dataset_dict["    |
|     144                           | targets"] = self.targets.__dict__ |
|     145                           |             else:                 |
|     146                           |                                   |
|     147                           |       dataset_dict["targets"] = { |
|     148                           |                     "ta           |
|     149                           | rget_column": self.target_column, |
|     150                           |                     "             |
|     151                           | class_labels": self.class_labels, |
|     152                           |                 }                 |
|     153                           |                                   |
|     154                           |             return dataset_dict   |
|     155                           |                                   |
|     156                           |         def describe(self):       |
|     157                           |             """                   |
|     158                           |                                   |
|     159                           |      Extracts descriptive statist |
|     160                           | ics for each field in the dataset |
|     161                           |             """                   |
|     162                           |             transfor              |
|     163                           | med_df = self.transformed_dataset |
|     164                           |                                   |
|     165                           |                                   |
|     166                           |      for ds_field in self.fields: |
|     167                           |                 describe_datase   |
|     168                           | t_field(transformed_df, ds_field) |
|     169                           |                                   |
|     170                           |                                   |
|     171                           |       def get_correlations(self): |
|     172                           |             """                   |
|     173                           |             Extracts correlati    |
|     174                           | ons for each field in the dataset |
|     175                           |             """                   |
|     176                           |             # Ignore field        |
|     177                           | s that have very high cardinality |
|     178                           |                                   |
|     179                           |       fields_for_correlation = [] |
|     180                           |                                   |
|     181                           |      for ds_field in self.fields: |
|     182                           |                 if                |
|     183                           | "statistics" in ds_field and "dis |
|     184                           | tinct" in ds_field["statistics"]: |
|     185                           |                     if ds_field   |
|     186                           | ["statistics"]["distinct"] < 0.1: |
|     187                           |                                   |
|     188                           |                      fields_for_c |
|     189                           | orrelation.append(ds_field["id"]) |
|     190                           |                                   |
|     191                           |             self.c                |
|     192                           | orrelation_matrix = associations( |
|     193                           |                 self.transformed  |
|     194                           | _dataset[fields_for_correlation], |
|     195                           |                                   |
|     196                           |                compute_only=True, |
|     197                           |                 plot=False,       |
|     198                           |             )["corr"]             |
|     199                           |                                   |
|     200                           |             # Transform to the    |
|     201                           | current format expected by the UI |
|     202                           |             self.correlations = [ |
|     203                           |                 [                 |
|     204                           |                     {             |
|     205                           |                                   |
|     206                           |                     "field": key, |
|     207                           |                                   |
|     208                           |                   "value": value, |
|     209                           |                     }             |
|     210                           |                     for key,      |
|     211                           |  value in correlation_row.items() |
|     212                           |                 ]                 |
|     213                           |                 for co            |
|     214                           | rrelation_row in self.correlation |
|     215                           | _matrix.to_dict(orient="records") |
|     216                           |             ]                     |
|     217                           |                                   |
|     218                           |         def get_c                 |
|     219                           | orrelation_plots(self, n_top=15): |
|     220                           |             """                   |
|     221                           |             Ex                    |
|     222                           | tracts correlation plots for the  |
|     223                           | n_top correlations in the dataset |
|     224                           |             """                   |
|     225                           |                                   |
|     226                           |        correlation_plots = genera |
|     227                           | te_correlation_plots(self, n_top) |
|     228                           |                                   |
|     229                           |          return correlation_plots |
|     230                           |                                   |
|     231                           |         @property                 |
|     232                           |         def transformed_da        |
|     233                           | taset(self, force_refresh=False): |
|     234                           |             """                   |
|     235                           |             Ret                   |
|     236                           | urns a transformed dataset that u |
|     237                           | ses the features from vm_dataset. |
|     238                           |                                   |
|     239                           | Some of the features in vm_datase |
|     240                           | t are of type Dummy so we need to |
|     241                           |                                   |
|     242                           | reverse the one hot encoding and  |
|     243                           | drop the individual dummy columns |
|     244                           |             """                   |
|     245                           |                                   |
| :::                               |   if self.__transformed_df is not |
|                                   |  None and force_refresh is False: |
|                                   |                                   |
|                                   |      return self.__transformed_df |
|                                   |                                   |
|                                   |             # Get the list o      |
|                                   | f features that are of type Dummy |
|                                   |                                   |
|                                   |    dataset_options = self.options |
|                                   |             dummy_variables = (   |
|                                   |                 dat               |
|                                   | aset_options.get("dummy_variables |
|                                   | ", []) if dataset_options else [] |
|                                   |             )                     |
|                                   |             # Exc                 |
|                                   | lude columns that have prefixes t |
|                                   | hat are in the dummy feature list |
|                                   |                                   |
|                                   |            dummy_column_names = [ |
|                                   |                 column_name       |
|                                   |                 for column        |
|                                   | _name in self.raw_dataset.columns |
|                                   |                 if any(           |
|                                   |                     colum         |
|                                   | n_name.startswith(dummy_variable) |
|                                   |                     for           |
|                                   | dummy_variable in dummy_variables |
|                                   |                 )                 |
|                                   |             ]                     |
|                                   |                                   |
|                                   | transformed_df = self.raw_dataset |
|                                   | .drop(dummy_column_names, axis=1) |
|                                   |                                   |
|                                   |                                   |
|                                   |           # Add reversed dummy fe |
|                                   | atures to the transformed dataset |
|                                   |             for d                 |
|                                   | ummy_variable in dummy_variables: |
|                                   |                                   |
|                                   |     columns_with_dummy_prefix = [ |
|                                   |                     col           |
|                                   |                     fo            |
|                                   | r col in self.raw_dataset.columns |
|                                   |                                   |
|                                   | if col.startswith(dummy_variable) |
|                                   |                 ]                 |
|                                   |                 t                 |
|                                   | ransformed_df[dummy_variable] = ( |
|                                   |                     self.raw_d    |
|                                   | ataset[columns_with_dummy_prefix] |
|                                   |                                   |
|                                   |                   .idxmax(axis=1) |
|                                   |                                   |
|                                   |                 .replace(f"{dummy |
|                                   | _variable}[-_:]", "", regex=True) |
|                                   |                 )                 |
|                                   |                                   |
|                                   |             return transformed_df |
|                                   |                                   |
|                                   |         @classmethod              |
|                                   |                                   |
|                                   | def create_from_dict(cls, dict_): |
|                                   |             class_field           |
|                                   | s = {f.name for f in fields(cls)} |
|                                   |             retur                 |
|                                   | n Dataset(**{k: v for k, v in dic |
|                                   | t_.items() if k in class_fields}) |
|                                   |                                   |
|                                   |         # TODO: Accept var        |
|                                   | iable descriptions from framework |
|                                   |         # TODO: Acc               |
|                                   | ept type overrides from framework |
|                                   |         @classmethod              |
|                                   |         def init_from_pd_dataset( |
|                                   |             cls, df,              |
|                                   |  options=None, targets=None, targ |
|                                   | et_column=None, class_labels=None |
|                                   |         ):                        |
|                                   |             pr                    |
|                                   | int("Inferring dataset types...") |
|                                   |                                   |
|                                   |        vm_dataset_variables = par |
|                                   | se_dataset_variables(df, options) |
|                                   |                                   |
|                                   |             shape = {             |
|                                   |                                   |
|                                   |              "rows": df.shape[0], |
|                                   |                                   |
|                                   |           "columns": df.shape[1], |
|                                   |             }                     |
|                                   |             df_head = df          |
|                                   | .head().to_dict(orient="records") |
|                                   |             df_tail = df          |
|                                   | .tail().to_dict(orient="records") |
|                                   |                                   |
|                                   |             # TODO: validate wi   |
|                                   | th target_column and class_labels |
|                                   |             if targets:           |
|                                   |                 validat           |
|                                   | e_pd_dataset_targets(df, targets) |
|                                   |                                   |
|                                   |             return Dataset(       |
|                                   |                 raw_dataset=df,   |
|                                   |                 fields=vm_d       |
|                                   | ataset_variables,  # TODO - depre |
|                                   | cate naming in favor of variables |
|                                   |                                   |
|                                   |   variables=vm_dataset_variables, |
|                                   |                 sample=[          |
|                                   |                     {             |
|                                   |                                   |
|                                   |                     "id": "head", |
|                                   |                                   |
|                                   |                  "data": df_head, |
|                                   |                     },            |
|                                   |                     {             |
|                                   |                                   |
|                                   |                     "id": "tail", |
|                                   |                                   |
|                                   |                  "data": df_tail, |
|                                   |                     },            |
|                                   |                 ],                |
|                                   |                 shape=shape,      |
|                                   |                 targets=targets,  |
|                                   |                                   |
|                                   |      target_column=target_column, |
|                                   |                                   |
|                                   |        class_labels=class_labels, |
|                                   |                 options=options,  |
|                                   |             )                     |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::

::: {.doc .doc-children}
::: {.doc .doc-object .doc-attribute}
### [`transformed_dataset`{.highlight .language-python}]{.n} [ [`property`]{.small} ]{.doc .doc-labels} {#validmind.vm_models.dataset.Dataset.transformed_dataset .doc .doc-heading}

::: {.doc .doc-contents}
Returns a transformed dataset that uses the features from vm_dataset.
Some of the features in vm_dataset are of type Dummy so we need to
reverse the one hot encoding and drop the individual dummy columns
:::
:::

::: {.doc .doc-object .doc-attribute}
### [`x`{.highlight .language-python}]{.n} [ [`property`]{.small} ]{.doc .doc-labels} {#validmind.vm_models.dataset.Dataset.x .doc .doc-heading}

::: {.doc .doc-contents}
Returns the dataset\'s features
:::
:::

::: {.doc .doc-object .doc-attribute}
### [`y`{.highlight .language-python}]{.n} [ [`property`]{.small} ]{.doc .doc-labels} {#validmind.vm_models.dataset.Dataset.y .doc .doc-heading}

::: {.doc .doc-contents}
Returns the dataset\'s target column
:::
:::

::: {.doc .doc-object .doc-function}
### [`__post_init__`{.highlight .language-python}]{.n}[`()`{.highlight .language-python}]{.p} {#validmind.vm_models.dataset.Dataset.__post_init__ .doc .doc-heading}

::: {.doc .doc-contents}
Set target_column and class_labels from DatasetTargets

Source code in `validmind/vm_models/dataset.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     52                            |                                   |
|     53                            |     def __post_init__(self):      |
|     54                            |         """                       |
|     55                            |         Set target_column and     |
|     56                            |  class_labels from DatasetTargets |
|     57                            |         """                       |
|     58                            |         if self.targets:          |
| :::                               |             self.target_co        |
|                                   | lumn = self.targets.target_column |
|                                   |             self.class_l          |
|                                   | abels = self.targets.class_labels |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
### [`describe`{.highlight .language-python}]{.n}[`()`{.highlight .language-python}]{.p} {#validmind.vm_models.dataset.Dataset.describe .doc .doc-heading}

::: {.doc .doc-contents}
Extracts descriptive statistics for each field in the dataset

Source code in `validmind/vm_models/dataset.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     115                           |                                   |
|     116                           |     def describe(self):           |
|     117                           |         """                       |
|     118                           |                                   |
|     119                           |      Extracts descriptive statist |
|     120                           | ics for each field in the dataset |
|     121                           |         """                       |
|     122                           |         transfor                  |
| :::                               | med_df = self.transformed_dataset |
|                                   |                                   |
|                                   |                                   |
|                                   |      for ds_field in self.fields: |
|                                   |             describe_datase       |
|                                   | t_field(transformed_df, ds_field) |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
### [`get_correlation_plots`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`n_top`{.highlight .language-python}]{.n}[`=`{.highlight .language-python}]{.o}[`15`{.highlight .language-python}]{.mi}[`)`{.highlight .language-python}]{.p} {#validmind.vm_models.dataset.Dataset.get_correlation_plots .doc .doc-heading}

::: {.doc .doc-contents}
Extracts correlation plots for the n_top correlations in the dataset

Source code in `validmind/vm_models/dataset.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     153                           |                                   |
|     154                           |     def get_c                     |
|     155                           | orrelation_plots(self, n_top=15): |
|     156                           |         """                       |
|     157                           |         Ex                        |
|     158                           | tracts correlation plots for the  |
| :::                               | n_top correlations in the dataset |
|                                   |         """                       |
|                                   |                                   |
|                                   |        correlation_plots = genera |
|                                   | te_correlation_plots(self, n_top) |
|                                   |         return correlation_plots  |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
### [`get_correlations`{.highlight .language-python}]{.n}[`()`{.highlight .language-python}]{.p} {#validmind.vm_models.dataset.Dataset.get_correlations .doc .doc-heading}

::: {.doc .doc-contents}
Extracts correlations for each field in the dataset

Source code in `validmind/vm_models/dataset.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     124                           |                                   |
|     125                           |     def get_correlations(self):   |
|     126                           |         """                       |
|     127                           |         Extracts correlati        |
|     128                           | ons for each field in the dataset |
|     129                           |         """                       |
|     130                           |         # Ignore field            |
|     131                           | s that have very high cardinality |
|     132                           |                                   |
|     133                           |       fields_for_correlation = [] |
|     134                           |                                   |
|     135                           |      for ds_field in self.fields: |
|     136                           |             if                    |
|     137                           | "statistics" in ds_field and "dis |
|     138                           | tinct" in ds_field["statistics"]: |
|     139                           |                 if ds_field       |
|     140                           | ["statistics"]["distinct"] < 0.1: |
|     141                           |                     fields_for_c  |
|     142                           | orrelation.append(ds_field["id"]) |
|     143                           |                                   |
|     144                           |         self.c                    |
|     145                           | orrelation_matrix = associations( |
|     146                           |             self.transformed      |
|     147                           | _dataset[fields_for_correlation], |
|     148                           |             compute_only=True,    |
|     149                           |             plot=False,           |
|     150                           |         )["corr"]                 |
|     151                           |                                   |
| :::                               |         # Transform to the        |
|                                   | current format expected by the UI |
|                                   |         self.correlations = [     |
|                                   |             [                     |
|                                   |                 {                 |
|                                   |                     "field": key, |
|                                   |                                   |
|                                   |                   "value": value, |
|                                   |                 }                 |
|                                   |                 for key,          |
|                                   |  value in correlation_row.items() |
|                                   |             ]                     |
|                                   |             for co                |
|                                   | rrelation_row in self.correlation |
|                                   | _matrix.to_dict(orient="records") |
|                                   |         ]                         |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
### [`get_feature_by_id`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`feature_id`{.highlight .language-python}]{.n}[`)`{.highlight .language-python}]{.p} {#validmind.vm_models.dataset.Dataset.get_feature_by_id .doc .doc-heading}

::: {.doc .doc-contents}
Returns the feature with the given id. We also build a lazy lookup cache
in case the same feature is requested multiple times.

Source code in `validmind/vm_models/dataset.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     74                            |                                   |
|     75                            |     def get                       |
|     76                            | _feature_by_id(self, feature_id): |
|     77                            |         """                       |
|     78                            |                                   |
|     79                            |        Returns the feature with t |
|     80                            | he given id. We also build a lazy |
|     81                            |                                   |
|     82                            | lookup cache in case the same fea |
|     83                            | ture is requested multiple times. |
|     84                            |         """                       |
|     85                            |         if feature                |
|     86                            | _id not in self.__feature_lookup: |
| :::                               |                                   |
|                                   |       for feature in self.fields: |
|                                   |                                   |
|                                   |   if feature["id"] == feature_id: |
|                                   |                     self.__fea    |
|                                   | ture_lookup[feature_id] = feature |
|                                   |                                   |
|                                   |                    return feature |
|                                   |                                   |
|                                   |   raise ValueError(f"Feature with |
|                                   |  id {feature_id} does not exist") |
|                                   |                                   |
|                                   |         return                    |
|                                   | self.__feature_lookup[feature_id] |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
### [`get_feature_type`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`feature_id`{.highlight .language-python}]{.n}[`)`{.highlight .language-python}]{.p} {#validmind.vm_models.dataset.Dataset.get_feature_type .doc .doc-heading}

::: {.doc .doc-contents}
Returns the type of the feature with the given id

Source code in `validmind/vm_models/dataset.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     88                            |                                   |
|     89                            |     def ge                        |
|     90                            | t_feature_type(self, feature_id): |
|     91                            |         """                       |
|     92                            |         Returns the type          |
|     93                            |  of the feature with the given id |
| :::                               |         """                       |
|                                   |         feature = s               |
|                                   | elf.get_feature_by_id(feature_id) |
|                                   |         return feature["type"]    |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
### [`serialize`{.highlight .language-python}]{.n}[`()`{.highlight .language-python}]{.p} {#validmind.vm_models.dataset.Dataset.serialize .doc .doc-heading}

::: {.doc .doc-contents}
Serializes the model to a dictionary so it can be sent to the API

Source code in `validmind/vm_models/dataset.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|      95                           |                                   |
|      96                           |     def serialize(self):          |
|      97                           |         """                       |
|      98                           |                                   |
|      99                           |  Serializes the model to a dictio |
|     100                           | nary so it can be sent to the API |
|     101                           |         """                       |
|     102                           |         dataset_dict = {          |
|     103                           |             "shape": self.shape,  |
|     104                           |             "type": self.type,    |
|     105                           |         }                         |
|     106                           |                                   |
|     107                           |         # Data                    |
|     108                           | set with no targets can be logged |
|     109                           |         if self.targets:          |
|     110                           |             dataset_dict["        |
|     111                           | targets"] = self.targets.__dict__ |
|     112                           |         else:                     |
|     113                           |                                   |
| :::                               |       dataset_dict["targets"] = { |
|                                   |                 "ta               |
|                                   | rget_column": self.target_column, |
|                                   |                 "                 |
|                                   | class_labels": self.class_labels, |
|                                   |             }                     |
|                                   |                                   |
|                                   |         return dataset_dict       |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::
:::
:::
:::

::: {.doc .doc-object .doc-class}
## `DatasetTargets` [ [`dataclass`]{.small} ]{.doc .doc-labels} {#validmind.DatasetTargets .doc .doc-heading}

::: {.doc .doc-contents}
Dataset targets definition

Source code in `validmind/vm_models/dataset.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     16                            |                                   |
|     17                            |     @dataclass()                  |
|     18                            |     class DatasetTargets:         |
|     19                            |         """                       |
|     20                            |                                   |
|     21                            |        Dataset targets definition |
|     22                            |         """                       |
|     23                            |                                   |
|     24                            |         target_column: str        |
| :::                               |         description: str = None   |
|                                   |         class_labels: dict = None |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::

::: {.doc .doc-children}
:::
:::
:::

::: {.doc .doc-object .doc-class}
## `Figure` [ [`dataclass`]{.small} ]{.doc .doc-labels} {#validmind.Figure .doc .doc-heading}

::: {.doc .doc-contents}
Figure objects track the schema supported by the ValidMind API

Source code in `validmind/vm_models/figure.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|      9                            |                                   |
|     10                            |     @dataclass                    |
|     11                            |     class Figure:                 |
|     12                            |         """                       |
|     13                            |                                   |
|     14                            |     Figure objects track the sche |
|     15                            | ma supported by the ValidMind API |
|     16                            |         """                       |
|     17                            |                                   |
|     18                            |         key: str                  |
|     19                            |         metadata: dict            |
|     20                            |         figure: object            |
|     21                            |                                   |
|     22                            |         def serialize(self):      |
|     23                            |             """                   |
|     24                            |                                   |
|     25                            | Serializes the Figure to a dictio |
|     26                            | nary so it can be sent to the API |
|     27                            |             """                   |
| :::                               |             return {              |
|                                   |                 "key": self.key,  |
|                                   |                                   |
|                                   |        "metadata": self.metadata, |
|                                   |                                   |
|                                   |            "figure": self.figure, |
|                                   |             }                     |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::

::: {.doc .doc-children}
::: {.doc .doc-object .doc-function}
### [`serialize`{.highlight .language-python}]{.n}[`()`{.highlight .language-python}]{.p} {#validmind.vm_models.figure.Figure.serialize .doc .doc-heading}

::: {.doc .doc-contents}
Serializes the Figure to a dictionary so it can be sent to the API

Source code in `validmind/vm_models/figure.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     19                            |                                   |
|     20                            |     def serialize(self):          |
|     21                            |         """                       |
|     22                            |                                   |
|     23                            | Serializes the Figure to a dictio |
|     24                            | nary so it can be sent to the API |
|     25                            |         """                       |
|     26                            |         return {                  |
|     27                            |             "key": self.key,      |
| :::                               |                                   |
|                                   |        "metadata": self.metadata, |
|                                   |                                   |
|                                   |            "figure": self.figure, |
|                                   |         }                         |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::
:::
:::
:::

::: {.doc .doc-object .doc-class}
## `Metric` [ [`dataclass`]{.small} ]{.doc .doc-labels} {#validmind.Metric .doc .doc-heading}

::: {.doc .doc-contents}
Bases:
[`TestContextUtils`]{title="validmind.vm_models.test_context.TestContextUtils"}

Metric objects track the schema supported by the ValidMind API

Source code in `validmind/vm_models/metric.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     15                            |                                   |
|     16                            |     @dataclass                    |
|     17                            |                                   |
|     18                            |   class Metric(TestContextUtils): |
|     19                            |         """                       |
|     20                            |                                   |
|     21                            |     Metric objects track the sche |
|     22                            | ma supported by the ValidMind API |
|     23                            |         """                       |
|     24                            |                                   |
|     25                            |         # Test Context            |
|     26                            |         test_context: TestContext |
|     27                            |                                   |
|     28                            |         # Class Variables         |
|     29                            |         te                        |
|     30                            | st_type: ClassVar[str] = "Metric" |
|     31                            |         type: Cl                  |
|     32                            | assVar[str] = ""  # type of metri |
|     33                            | c: "training", "evaluation", etc. |
|     34                            |                                   |
|     35                            |   scope: ClassVar[str] = ""  # sc |
|     36                            | ope of metric: "training_dataset" |
|     37                            |                                   |
|     38                            | key: ClassVar[str] = ""  # unique |
|     39                            |  identifer for metric: "accuracy" |
|     40                            |         value_form                |
|     41                            | atter: ClassVar[Optional[str]] =  |
|     42                            | None  # "records" or "key_values" |
|     43                            |         de                        |
|     44                            | fault_params: ClassVar[dict] = {} |
|     45                            |                                   |
|     46                            |         # Instance Variables      |
|     47                            |         params: dict = None       |
|     48                            |                                   |
|     49                            |     result: TestPlanResult = None |
|     50                            |                                   |
|     51                            |         def __post_init__(self):  |
|     52                            |             """                   |
|     53                            |             S                     |
|     54                            | et default params if not provided |
|     55                            |             """                   |
|     56                            |                                   |
|     57                            |           if self.params is None: |
|     58                            |                                   |
|     59                            | self.params = self.default_params |
|     60                            |                                   |
|     61                            |         @property                 |
|     62                            |         def name(self):           |
|     63                            |             return self.key       |
|     64                            |                                   |
|     65                            |                                   |
|     66                            |   def run(self, *args, **kwargs): |
|     67                            |             """                   |
|     68                            |             Run the metric        |
|     69                            | calculation and cache its results |
|     70                            |             """                   |
|     71                            |                                   |
|     72                            |         raise NotImplementedError |
|     73                            |                                   |
|     74                            |         def cache_results(        |
|     75                            |             self,                 |
|     76                            |             metric_value:         |
|     77                            |  Union[dict, list, pd.DataFrame], |
| :::                               |                                   |
|                                   | figures: Optional[object] = None, |
|                                   |         ):                        |
|                                   |             """                   |
|                                   |             Cache the resu        |
|                                   | lts of the metric calculation and |
|                                   |  do any post-processing if needed |
|                                   |             """                   |
|                                   |             t                     |
|                                   | est_plan_result = TestPlanResult( |
|                                   |                                   |
|                                   |              metric=MetricResult( |
|                                   |                                   |
|                                   |                   type=self.type, |
|                                   |                                   |
|                                   |                 scope=self.scope, |
|                                   |                     key=self.key, |
|                                   |                                   |
|                                   |               value=metric_value, |
|                                   |                     valu          |
|                                   | e_formatter=self.value_formatter, |
|                                   |                 )                 |
|                                   |             )                     |
|                                   |                                   |
|                                   |                                   |
|                                   |          # Allow metrics to attac |
|                                   | h figures to the test plan result |
|                                   |             if figures:           |
|                                   |                 t                 |
|                                   | est_plan_result.figures = figures |
|                                   |                                   |
|                                   |                                   |
|                                   |    self.result = test_plan_result |
|                                   |                                   |
|                                   |             return self.result    |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::

::: {.doc .doc-children}
::: {.doc .doc-object .doc-function}
### [`__post_init__`{.highlight .language-python}]{.n}[`()`{.highlight .language-python}]{.p} {#validmind.vm_models.metric.Metric.__post_init__ .doc .doc-heading}

::: {.doc .doc-contents}
Set default params if not provided

Source code in `validmind/vm_models/metric.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     36                            |                                   |
|     37                            |     def __post_init__(self):      |
|     38                            |         """                       |
|     39                            |         S                         |
|     40                            | et default params if not provided |
|     41                            |         """                       |
| :::                               |         if self.params is None:   |
|                                   |                                   |
|                                   | self.params = self.default_params |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
### [`cache_results`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`metric_value`{.highlight .language-python}]{.n}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`figures`{.highlight .language-python}]{.n}[`=`{.highlight .language-python}]{.o}[`None`{.highlight .language-python}]{.kc}[`)`{.highlight .language-python}]{.p} {#validmind.vm_models.metric.Metric.cache_results .doc .doc-heading}

::: {.doc .doc-contents}
Cache the results of the metric calculation and do any post-processing
if needed

Source code in `validmind/vm_models/metric.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     53                            |                                   |
|     54                            |     def cache_results(            |
|     55                            |         self,                     |
|     56                            |         metric_value:             |
|     57                            |  Union[dict, list, pd.DataFrame], |
|     58                            |                                   |
|     59                            | figures: Optional[object] = None, |
|     60                            |     ):                            |
|     61                            |         """                       |
|     62                            |         Cache the resu            |
|     63                            | lts of the metric calculation and |
|     64                            |  do any post-processing if needed |
|     65                            |         """                       |
|     66                            |         t                         |
|     67                            | est_plan_result = TestPlanResult( |
|     68                            |             metric=MetricResult(  |
|     69                            |                 type=self.type,   |
|     70                            |                 scope=self.scope, |
|     71                            |                 key=self.key,     |
|     72                            |                                   |
|     73                            |               value=metric_value, |
|     74                            |                 valu              |
|     75                            | e_formatter=self.value_formatter, |
|     76                            |             )                     |
|     77                            |         )                         |
| :::                               |                                   |
|                                   |         # Allow metrics to attac  |
|                                   | h figures to the test plan result |
|                                   |         if figures:               |
|                                   |             t                     |
|                                   | est_plan_result.figures = figures |
|                                   |                                   |
|                                   |                                   |
|                                   |    self.result = test_plan_result |
|                                   |                                   |
|                                   |         return self.result        |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
### [`run`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`*`{.highlight .language-python}]{.o}[`args`{.highlight .language-python}]{.n}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`**`{.highlight .language-python}]{.o}[`kwargs`{.highlight .language-python}]{.n}[`)`{.highlight .language-python}]{.p} {#validmind.vm_models.metric.Metric.run .doc .doc-heading}

::: {.doc .doc-contents}
Run the metric calculation and cache its results

Source code in `validmind/vm_models/metric.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     47                            |                                   |
|     48                            |                                   |
|     49                            |   def run(self, *args, **kwargs): |
|     50                            |         """                       |
|     51                            |         Run the metric            |
| :::                               | calculation and cache its results |
|                                   |         """                       |
|                                   |         raise NotImplementedError |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::
:::
:::
:::

::: {.doc .doc-object .doc-class}
## `Model` [ [`dataclass`]{.small} ]{.doc .doc-labels} {#validmind.Model .doc .doc-heading}

::: {.doc .doc-contents}
Model class wrapper

Source code in `validmind/vm_models/model.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     26                            |                                   |
|     27                            |     @dataclass                    |
|     28                            |     class Model:                  |
|     29                            |         """                       |
|     30                            |         Model class wrapper       |
|     31                            |         """                       |
|     32                            |                                   |
|     33                            |         a                         |
|     34                            | ttributes: ModelAttributes = None |
|     35                            |         task: str = None          |
|     36                            |         subtask: str = None       |
|     37                            |         params: dict = None       |
|     38                            |         model_id: str = "main"    |
|     39                            |         model: object             |
|     40                            |  = None  # Trained model instance |
|     41                            |                                   |
|     42                            |         def serialize(self):      |
|     43                            |             """                   |
|     44                            |                                   |
|     45                            |  Serializes the model to a dictio |
|     46                            | nary so it can be sent to the API |
|     47                            |             """                   |
|     48                            |             return {              |
|     49                            |                                   |
|     50                            |        "model_id": self.model_id, |
|     51                            |                 "attri            |
|     52                            | butes": self.attributes.__dict__, |
|     53                            |                                   |
|     54                            |                "task": self.task, |
|     55                            |                                   |
|     56                            |          "subtask": self.subtask, |
|     57                            |                                   |
|     58                            |            "params": self.params, |
|     59                            |             }                     |
|     60                            |                                   |
|     61                            |         de                        |
|     62                            | f predict(self, *args, **kwargs): |
|     63                            |             """                   |
|     64                            |                                   |
|     65                            | Predict method for the model. Thi |
|     66                            | s is a wrapper around the model's |
|     67                            |             pre                   |
|     68                            | dict_proba (for classification) o |
|     69                            | r predict (for regression) method |
|     70                            |                                   |
|     71                            |                                   |
|     72                            |  NOTE: This only works for sklear |
|     73                            | n or xgboost models at the moment |
|     74                            |             """                   |
|     75                            |                                   |
|     76                            |            predict_fn = getattr(s |
|     77                            | elf.model, "predict_proba", None) |
|     78                            |                                   |
|     79                            |          if callable(predict_fn): |
| :::                               |                                   |
|                                   |             return self.model.pre |
|                                   | dict_proba(*args, **kwargs)[:, 1] |
|                                   |             else:                 |
|                                   |                 return se         |
|                                   | lf.model.predict(*args, **kwargs) |
|                                   |                                   |
|                                   |         @classmethod              |
|                                   |         de                        |
|                                   | f is_supported_model(cls, model): |
|                                   |             """                   |
|                                   |             Checks if             |
|                                   | the model is supported by the API |
|                                   |             """                   |
|                                   |             model                 |
|                                   | _class = model.__class__.__name__ |
|                                   |                                   |
|                                   |             if model_cl           |
|                                   | ass not in SUPPORTED_MODEL_TYPES: |
|                                   |                 return False      |
|                                   |                                   |
|                                   |             return True           |
|                                   |                                   |
|                                   |         @classmethod              |
|                                   |                                   |
|                                   | def create_from_dict(cls, dict_): |
|                                   |             class_field           |
|                                   | s = {f.name for f in fields(cls)} |
|                                   |             ret                   |
|                                   | urn Model(**{k: v for k, v in dic |
|                                   | t_.items() if k in class_fields}) |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::

::: {.doc .doc-children}
::: {.doc .doc-object .doc-function}
### [`is_supported_model`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`model`{.highlight .language-python}]{.n}[`)`{.highlight .language-python}]{.p} [ [`classmethod`]{.small} ]{.doc .doc-labels} {#validmind.vm_models.model.Model.is_supported_model .doc .doc-heading}

::: {.doc .doc-contents}
Checks if the model is supported by the API

Source code in `validmind/vm_models/model.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     64                            |                                   |
|     65                            |     @classmethod                  |
|     66                            |     de                            |
|     67                            | f is_supported_model(cls, model): |
|     68                            |         """                       |
|     69                            |         Checks if                 |
|     70                            | the model is supported by the API |
|     71                            |         """                       |
|     72                            |         model                     |
|     73                            | _class = model.__class__.__name__ |
|     74                            |                                   |
| :::                               |         if model_cl               |
|                                   | ass not in SUPPORTED_MODEL_TYPES: |
|                                   |             return False          |
|                                   |                                   |
|                                   |         return True               |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
### [`predict`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`*`{.highlight .language-python}]{.o}[`args`{.highlight .language-python}]{.n}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`**`{.highlight .language-python}]{.o}[`kwargs`{.highlight .language-python}]{.n}[`)`{.highlight .language-python}]{.p} {#validmind.vm_models.model.Model.predict .doc .doc-heading}

::: {.doc .doc-contents}
Predict method for the model. This is a wrapper around the model\'s
predict_proba (for classification) or predict (for regression) method

NOTE: This only works for sklearn or xgboost models at the moment

Source code in `validmind/vm_models/model.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     51                            |                                   |
|     52                            |     de                            |
|     53                            | f predict(self, *args, **kwargs): |
|     54                            |         """                       |
|     55                            |                                   |
|     56                            | Predict method for the model. Thi |
|     57                            | s is a wrapper around the model's |
|     58                            |         pre                       |
|     59                            | dict_proba (for classification) o |
|     60                            | r predict (for regression) method |
|     61                            |                                   |
|     62                            |                                   |
| :::                               |  NOTE: This only works for sklear |
|                                   | n or xgboost models at the moment |
|                                   |         """                       |
|                                   |         predict_fn = getattr(s    |
|                                   | elf.model, "predict_proba", None) |
|                                   |         if callable(predict_fn):  |
|                                   |             return self.model.pre |
|                                   | dict_proba(*args, **kwargs)[:, 1] |
|                                   |         else:                     |
|                                   |             return se             |
|                                   | lf.model.predict(*args, **kwargs) |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
### [`serialize`{.highlight .language-python}]{.n}[`()`{.highlight .language-python}]{.p} {#validmind.vm_models.model.Model.serialize .doc .doc-heading}

::: {.doc .doc-contents}
Serializes the model to a dictionary so it can be sent to the API

Source code in `validmind/vm_models/model.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     39                            |                                   |
|     40                            |     def serialize(self):          |
|     41                            |         """                       |
|     42                            |                                   |
|     43                            |  Serializes the model to a dictio |
|     44                            | nary so it can be sent to the API |
|     45                            |         """                       |
|     46                            |         return {                  |
|     47                            |                                   |
|     48                            |        "model_id": self.model_id, |
|     49                            |             "attri                |
| :::                               | butes": self.attributes.__dict__, |
|                                   |             "task": self.task,    |
|                                   |                                   |
|                                   |          "subtask": self.subtask, |
|                                   |                                   |
|                                   |            "params": self.params, |
|                                   |         }                         |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::
:::
:::
:::

::: {.doc .doc-object .doc-class}
## `ModelAttributes` [ [`dataclass`]{.small} ]{.doc .doc-labels} {#validmind.ModelAttributes .doc .doc-heading}

::: {.doc .doc-contents}
Model attributes definition

Source code in `validmind/vm_models/model.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     15                            |                                   |
|     16                            |     @dataclass()                  |
|     17                            |     class ModelAttributes:        |
|     18                            |         """                       |
|     19                            |                                   |
|     20                            |       Model attributes definition |
|     21                            |         """                       |
|     22                            |                                   |
|     23                            |         architecture: str = None  |
| :::                               |         framework: str = None     |
|                                   |                                   |
|                                   |     framework_version: str = None |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::

::: {.doc .doc-children}
:::
:::
:::

::: {.doc .doc-object .doc-class}
## `ThresholdTest` [ [`dataclass`]{.small} ]{.doc .doc-labels} {#validmind.ThresholdTest .doc .doc-heading}

::: {.doc .doc-contents}
Bases:
[`TestContextUtils`]{title="validmind.vm_models.test_context.TestContextUtils"}

A threshold test is a combination of a metric/plot we track and a
corresponding set of parameters and thresholds values that allow us to
determine whether the metric/plot passes or fails.

Source code in `validmind/vm_models/threshold_test.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     17                            |                                   |
|     18                            |     @dataclass                    |
|     19                            |     class                         |
|     20                            |  ThresholdTest(TestContextUtils): |
|     21                            |         """                       |
|     22                            |                                   |
|     23                            |  A threshold test is a combinatio |
|     24                            | n of a metric/plot we track and a |
|     25                            |                                   |
|     26                            |   corresponding set of parameters |
|     27                            |  and thresholds values that allow |
|     28                            |         us to determine whether   |
|     29                            |  the metric/plot passes or fails. |
|     30                            |         """                       |
|     31                            |                                   |
|     32                            |         # Test Context            |
|     33                            |         test_context: TestContext |
|     34                            |                                   |
|     35                            |         # Class Variables         |
|     36                            |         test_type                 |
|     37                            | : ClassVar[str] = "ThresholdTest" |
|     38                            |                                   |
|     39                            |      category: ClassVar[str] = "" |
|     40                            |         name: ClassVar[str] = ""  |
|     41                            |         de                        |
|     42                            | fault_params: ClassVar[dict] = {} |
|     43                            |                                   |
|     44                            |         # Instance Variables      |
|     45                            |         params: dict = None       |
|     46                            |                                   |
|     47                            |  test_results: TestResults = None |
|     48                            |                                   |
|     49                            |         def __post_init__(self):  |
|     50                            |             """                   |
|     51                            |             S                     |
|     52                            | et default params if not provided |
|     53                            |             """                   |
|     54                            |                                   |
|     55                            |           if self.params is None: |
|     56                            |                                   |
|     57                            | self.params = self.default_params |
|     58                            |                                   |
|     59                            |                                   |
|     60                            |   def run(self, *args, **kwargs): |
|     61                            |             """                   |
|     62                            |             R                     |
|     63                            | un the test and cache its results |
|     64                            |             """                   |
| :::                               |                                   |
|                                   |         raise NotImplementedError |
|                                   |                                   |
|                                   |                                   |
|                                   |  def cache_results(self, results: |
|                                   |  List[TestResult], passed: bool): |
|                                   |             """                   |
|                                   |             Cache the indivi      |
|                                   | dual results of the threshold tes |
|                                   | t as a list of TestResult objects |
|                                   |             """                   |
|                                   |             se                    |
|                                   | lf.test_results = TestPlanResult( |
|                                   |                                   |
|                                   |         test_results=TestResults( |
|                                   |                                   |
|                                   |           category=self.category, |
|                                   |                                   |
|                                   |              test_name=self.name, |
|                                   |                                   |
|                                   |               params=self.params, |
|                                   |                                   |
|                                   |                    passed=passed, |
|                                   |                                   |
|                                   |                  results=results, |
|                                   |                 )                 |
|                                   |             )                     |
|                                   |                                   |
|                                   |          return self.test_results |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::

::: {.doc .doc-children}
::: {.doc .doc-object .doc-function}
### [`__post_init__`{.highlight .language-python}]{.n}[`()`{.highlight .language-python}]{.p} {#validmind.vm_models.threshold_test.ThresholdTest.__post_init__ .doc .doc-heading}

::: {.doc .doc-contents}
Set default params if not provided

Source code in `validmind/vm_models/threshold_test.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     38                            |                                   |
|     39                            |     def __post_init__(self):      |
|     40                            |         """                       |
|     41                            |         S                         |
|     42                            | et default params if not provided |
|     43                            |         """                       |
| :::                               |         if self.params is None:   |
|                                   |                                   |
|                                   | self.params = self.default_params |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
### [`cache_results`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`results`{.highlight .language-python}]{.n}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`passed`{.highlight .language-python}]{.n}[`)`{.highlight .language-python}]{.p} {#validmind.vm_models.threshold_test.ThresholdTest.cache_results .doc .doc-heading}

::: {.doc .doc-contents}
Cache the individual results of the threshold test as a list of
TestResult objects

Source code in `validmind/vm_models/threshold_test.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     51                            |                                   |
|     52                            |                                   |
|     53                            |  def cache_results(self, results: |
|     54                            |  List[TestResult], passed: bool): |
|     55                            |         """                       |
|     56                            |         Cache the indivi          |
|     57                            | dual results of the threshold tes |
|     58                            | t as a list of TestResult objects |
|     59                            |         """                       |
|     60                            |         se                        |
|     61                            | lf.test_results = TestPlanResult( |
|     62                            |                                   |
|     63                            |         test_results=TestResults( |
|     64                            |                                   |
| :::                               |           category=self.category, |
|                                   |                                   |
|                                   |              test_name=self.name, |
|                                   |                                   |
|                                   |               params=self.params, |
|                                   |                 passed=passed,    |
|                                   |                 results=results,  |
|                                   |             )                     |
|                                   |         )                         |
|                                   |         return self.test_results  |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
### [`run`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`*`{.highlight .language-python}]{.o}[`args`{.highlight .language-python}]{.n}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`**`{.highlight .language-python}]{.o}[`kwargs`{.highlight .language-python}]{.n}[`)`{.highlight .language-python}]{.p} {#validmind.vm_models.threshold_test.ThresholdTest.run .doc .doc-heading}

::: {.doc .doc-contents}
Run the test and cache its results

Source code in `validmind/vm_models/threshold_test.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     45                            |                                   |
|     46                            |                                   |
|     47                            |   def run(self, *args, **kwargs): |
|     48                            |         """                       |
|     49                            |         R                         |
| :::                               | un the test and cache its results |
|                                   |         """                       |
|                                   |         raise NotImplementedError |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::
:::
:::
:::

::: {.doc .doc-object .doc-function}
## [`init`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`project`{.highlight .language-python}]{.n}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`api_key`{.highlight .language-python}]{.n}[`=`{.highlight .language-python}]{.o}[`None`{.highlight .language-python}]{.kc}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`api_secret`{.highlight .language-python}]{.n}[`=`{.highlight .language-python}]{.o}[`None`{.highlight .language-python}]{.kc}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`api_host`{.highlight .language-python}]{.n}[`=`{.highlight .language-python}]{.o}[`None`{.highlight .language-python}]{.kc}[`)`{.highlight .language-python}]{.p} {#validmind.init .doc .doc-heading}

::: {.doc .doc-contents}
Initializes the API client instances and /pings the API to ensure the
provided credentials are valid.

Source code in `validmind/api_client.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     51                            |                                   |
|     52                            |                                   |
|     53                            |   def init(project, api_key=None, |
|     54                            |  api_secret=None, api_host=None): |
|     55                            |         """                       |
|     56                            |         Initializes the API cl    |
|     57                            | ient instances and /pings the API |
|     58                            |         to ensure th              |
|     59                            | e provided credentials are valid. |
|     60                            |         """                       |
|     61                            |         global API_HOST           |
|     62                            |                                   |
|     63                            |         ENV_API_K                 |
|     64                            | EY = os.environ.get("VM_API_KEY") |
|     65                            |         ENV_API_SECRET            |
|     66                            | = os.environ.get("VM_API_SECRET") |
|     67                            |                                   |
|     68                            |         vm                        |
|     69                            | _api_key = api_key or ENV_API_KEY |
|     70                            |         vm_api_secr               |
|     71                            | et = api_secret or ENV_API_SECRET |
|     72                            |                                   |
|     73                            |         if api_host is not None:  |
|     74                            |             API_HOST = api_host   |
|     75                            |                                   |
|     76                            |         if vm_api_key             |
|     77                            | is None or vm_api_secret is None: |
|     78                            |             raise ValueError(     |
|     79                            |                                   |
|     80                            |      "API key and secret must be  |
| :::                               | provided either as environment va |
|                                   | riables or as arguments to init." |
|                                   |             )                     |
|                                   |                                   |
|                                   |                                   |
|                                   |       api_session.headers.update( |
|                                   |             {                     |
|                                   |                                   |
|                                   |          "X-API-KEY": vm_api_key, |
|                                   |                                   |
|                                   |    "X-API-SECRET": vm_api_secret, |
|                                   |                                   |
|                                   |        "X-PROJECT-CUID": project, |
|                                   |             }                     |
|                                   |         )                         |
|                                   |                                   |
|                                   |         return __ping()           |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
## [`init_dataset`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`dataset`{.highlight .language-python}]{.n}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`type`{.highlight .language-python}]{.nb}[`=`{.highlight .language-python}]{.o}[`'training'`{.highlight .language-python}]{.s1}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`options`{.highlight .language-python}]{.n}[`=`{.highlight .language-python}]{.o}[`None`{.highlight .language-python}]{.kc}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`targets`{.highlight .language-python}]{.n}[`=`{.highlight .language-python}]{.o}[`None`{.highlight .language-python}]{.kc}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`target_column`{.highlight .language-python}]{.n}[`=`{.highlight .language-python}]{.o}[`None`{.highlight .language-python}]{.kc}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`class_labels`{.highlight .language-python}]{.n}[`=`{.highlight .language-python}]{.o}[`None`{.highlight .language-python}]{.kc}[`)`{.highlight .language-python}]{.p} {#validmind.init_dataset .doc .doc-heading}

::: {.doc .doc-contents}
Initializes a VM Dataset, which can then be passed to other functions
that can perform additional analysis and tests on the data. This
function also ensures we are reading a valid dataset type. We only
support Pandas DataFrames at the moment.

:param pd.DataFrame dataset: We only support Pandas DataFrames at the
moment :param str type: The dataset split type is necessary for mapping
and relating multiple datasets together. Can be one of training,
validation, test or generic :param dict options: A dictionary of options
for the dataset :param vm.vm.DatasetTargets targets: A list of target
variables :param str target_column: The name of the target column in the
dataset :param dict class_labels: A list of class labels for
classification problems

Source code in `validmind/client.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|      9                            |                                   |
|     10                            |     def init_dataset(             |
|     11                            |         dataset,                  |
|     12                            |         type="training",          |
|     13                            |         options=None,             |
|     14                            |         targets=None,             |
|     15                            |         target_column=None,       |
|     16                            |         class_labels=None,        |
|     17                            |     ):                            |
|     18                            |         """                       |
|     19                            |         Ini                       |
|     20                            | tializes a VM Dataset, which can  |
|     21                            | then be passed to other functions |
|     22                            |         that ca                   |
|     23                            | n perform additional analysis and |
|     24                            |  tests on the data. This function |
|     25                            |         also e                    |
|     26                            | nsures we are reading a valid dat |
|     27                            | aset type. We only support Pandas |
|     28                            |         DataFrames at the moment. |
|     29                            |                                   |
|     30                            |         :param pd.                |
|     31                            | DataFrame dataset: We only suppor |
|     32                            | t Pandas DataFrames at the moment |
|     33                            |         :param str type: The      |
|     34                            |  dataset split type is necessary  |
|     35                            | for mapping and relating multiple |
|     36                            |             data                  |
|     37                            | sets together. Can be one of trai |
|     38                            | ning, validation, test or generic |
|     39                            |                                   |
|     40                            |       :param dict options: A dict |
|     41                            | ionary of options for the dataset |
|     42                            |                                   |
|     43                            |    :param vm.vm.DatasetTargets ta |
|     44                            | rgets: A list of target variables |
| :::                               |         :par                      |
|                                   | am str target_column: The name of |
|                                   |  the target column in the dataset |
|                                   |         :param dic                |
|                                   | t class_labels: A list of class l |
|                                   | abels for classification problems |
|                                   |         """                       |
|                                   |         dataset_c                 |
|                                   | lass = dataset.__class__.__name__ |
|                                   |                                   |
|                                   |         # TODO                    |
|                                   | : when we accept numpy datasets w |
|                                   | e can convert them to/from pandas |
|                                   |                                   |
|                                   |  if dataset_class == "DataFrame": |
|                                   |             pri                   |
|                                   | nt("Pandas dataset detected. Init |
|                                   | ializing VM Dataset instance...") |
|                                   |             vm_datase             |
|                                   | t = Dataset.init_from_pd_dataset( |
|                                   |                                   |
|                                   |             dataset, options, tar |
|                                   | gets, target_column, class_labels |
|                                   |             )                     |
|                                   |         else:                     |
|                                   |             rai                   |
|                                   | se ValueError("Only Pandas datase |
|                                   | ts are supported at the moment.") |
|                                   |                                   |
|                                   |         vm_dataset.type = type    |
|                                   |                                   |
|                                   |         return vm_dataset         |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
## [`init_model`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`model`{.highlight .language-python}]{.n}[`)`{.highlight .language-python}]{.p} {#validmind.init_model .doc .doc-heading}

::: {.doc .doc-contents}
Initializes a VM Model, which can then be passed to other functions that
can perform additional analysis and tests on the data. This function
also ensures we are reading a supported model type.

:param model: A trained model instance

Source code in `validmind/client.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     47                            |                                   |
|     48                            |     def init_model(model):        |
|     49                            |         """                       |
|     50                            |         I                         |
|     51                            | nitializes a VM Model, which can  |
|     52                            | then be passed to other functions |
|     53                            |         that ca                   |
|     54                            | n perform additional analysis and |
|     55                            |  tests on the data. This function |
|     56                            |         also ensures we ar        |
|     57                            | e reading a supported model type. |
|     58                            |                                   |
|     59                            |         :para                     |
|     60                            | m model: A trained model instance |
|     61                            |         """                       |
|     62                            |                                   |
|     63                            |         if not                    |
|     64                            |  Model.is_supported_model(model): |
|     65                            |             raise ValueError(     |
| :::                               |                                   |
|                                   |            "Model type {} is not  |
|                                   | supported at the moment.".format( |
|                                   |                                   |
|                                   |          model.__class__.__name__ |
|                                   |                 )                 |
|                                   |             )                     |
|                                   |                                   |
|                                   |                                   |
|                                   |        vm_model = Model(model=mod |
|                                   | el, attributes=ModelAttributes()) |
|                                   |                                   |
|                                   |         return vm_model           |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
## [`log_dataset`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`vm_dataset`{.highlight .language-python}]{.n}[`)`{.highlight .language-python}]{.p} {#validmind.log_dataset .doc .doc-heading}

::: {.doc .doc-contents}
Logs metadata and statistics about a dataset to ValidMind API.

:param dataset: A VM dataset object :param dataset_type: The type of
dataset. Can be one of \"training\", \"test\", or \"validation\". :param
dataset_options: Additional dataset options for analysis :param
dataset_targets: A list of targets for the dataset. :param features:
Optional. A list of features metadata. :type dataset_targets:
validmind.DatasetTargets, optional

Source code in `validmind/api_client.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|      83                           |                                   |
|      84                           |     def log_dataset(vm_dataset):  |
|      85                           |         """                       |
|      86                           |                                   |
|      87                           |     Logs metadata and statistics  |
|      88                           | about a dataset to ValidMind API. |
|      89                           |                                   |
|      90                           |         :p                        |
|      91                           | aram dataset: A VM dataset object |
|      92                           |                                   |
|      93                           |        :param dataset_type: The t |
|      94                           | ype of dataset. Can be one of "tr |
|      95                           | aining", "test", or "validation". |
|      96                           |                                   |
|      97                           |    :param dataset_options: Additi |
|      98                           | onal dataset options for analysis |
|      99                           |         :param dataset_targets: A |
|     100                           |  list of targets for the dataset. |
|     101                           |         :param features: Optio    |
|     102                           | nal. A list of features metadata. |
|     103                           |         :type dataset_targets: v  |
|     104                           | alidmind.DatasetTargets, optional |
|     105                           |         """                       |
|     106                           |                                   |
|     107                           |     payload = json.dumps(vm_datas |
| :::                               | et.serialize(), cls=NumpyEncoder) |
|                                   |         r = api_session.post(     |
|                                   |                                   |
|                                   |        f"{API_HOST}/log_dataset", |
|                                   |             data=payload,         |
|                                   |             headers={"Co          |
|                                   | ntent-Type": "application/json"}, |
|                                   |         )                         |
|                                   |                                   |
|                                   |         if r.status_code != 200:  |
|                                   |             print("Could n        |
|                                   | ot log dataset to ValidMind API") |
|                                   |                                   |
|                                   |           raise Exception(r.text) |
|                                   |                                   |
|                                   |                                   |
|                                   |      print("Successfully logged d |
|                                   | ataset metadata and statistics.") |
|                                   |                                   |
|                                   |         return vm_dataset         |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
## [`log_figure`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`data_or_path`{.highlight .language-python}]{.n}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`key`{.highlight .language-python}]{.n}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`metadata`{.highlight .language-python}]{.n}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`run_cuid`{.highlight .language-python}]{.n}[`=`{.highlight .language-python}]{.o}[`None`{.highlight .language-python}]{.kc}[`)`{.highlight .language-python}]{.p} {#validmind.log_figure .doc .doc-heading}

::: {.doc .doc-contents}
Logs a figure

:param data_or_path: the path of the image or the data of the plot
:param key: identifier of the figure :param metadata: python data
structure :param run_cuid: run cuid from start_run

Source code in `validmind/api_client.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     273                           |                                   |
|     274                           |     def log_figure(data_or_pat    |
|     275                           | h, key, metadata, run_cuid=None): |
|     276                           |         """                       |
|     277                           |         Logs a figure             |
|     278                           |                                   |
|     279                           |                                   |
|     280                           | :param data_or_path: the path of  |
|     281                           | the image or the data of the plot |
|     282                           |         :pa                       |
|     283                           | ram key: identifier of the figure |
|     284                           |         :para                     |
|     285                           | m metadata: python data structure |
|     286                           |         :param                    |
|     287                           | run_cuid: run cuid from start_run |
|     288                           |         """                       |
|     289                           |         if not run_cuid:          |
|     290                           |             run                   |
|     291                           | _cuid = _get_or_create_run_cuid() |
|     292                           |                                   |
|     293                           |         url = f"{API_HOST         |
|     294                           | }/log_figure?run_cuid={run_cuid}" |
|     295                           |                                   |
|     296                           |                                   |
|     297                           | if isinstance(data_or_path, str): |
|     298                           |             type_ = "file_path"   |
|     299                           |             _, extension          |
|     300                           |  = os.path.splitext(data_or_path) |
|     301                           |                                   |
|     302                           | files = {"image": (f"{key}{extens |
|     303                           | ion}", open(data_or_path, "rb"))} |
|     304                           |                                   |
|     305                           |      elif is_matplotlib_typename( |
|     306                           | get_full_typename(data_or_path)): |
|     307                           |             type_ = "plot"        |
|     308                           |             buffer = BytesIO()    |
|     309                           |             data_or_path.sav      |
|     310                           | efig(buffer, bbox_inches="tight") |
|     311                           |             buffer.seek(0)        |
| :::                               |             files = {"image": (f" |
|                                   | {key}.png", buffer, "image/png")} |
|                                   |         else:                     |
|                                   |             raise ValueError(     |
|                                   |                 f"dat             |
|                                   | a_or_path type not supported: {ge |
|                                   | t_full_typename(data_or_path)}. " |
|                                   |                                   |
|                                   |            f"Available supported  |
|                                   | types: string path or matplotlib" |
|                                   |             )                     |
|                                   |                                   |
|                                   |         try:                      |
|                                   |             met                   |
|                                   | adata_json = json.dumps(metadata) |
|                                   |         except TypeError:         |
|                                   |             raise                 |
|                                   |                                   |
|                                   |         res = api_session.post(   |
|                                   |             url, files=           |
|                                   | files, data={"key": key, "type":  |
|                                   | type_, "metadata": metadata_json} |
|                                   |         )                         |
|                                   |         return res.json()         |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
## [`log_metadata`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`content_id`{.highlight .language-python}]{.n}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`text`{.highlight .language-python}]{.n}[`=`{.highlight .language-python}]{.o}[`None`{.highlight .language-python}]{.kc}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`extra_json`{.highlight .language-python}]{.n}[`=`{.highlight .language-python}]{.o}[`None`{.highlight .language-python}]{.kc}[`)`{.highlight .language-python}]{.p} {#validmind.log_metadata .doc .doc-heading}

::: {.doc .doc-contents}
Logs free-form metadata to ValidMind API.

:param content_id: Unique content identifier for the metadata :param
text: Free-form text to assign to the metadata :param extra_json:
Free-form key-value pairs to assign to the metadata

Source code in `validmind/api_client.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     110                           |                                   |
|     111                           |     def log_metadata(content      |
|     112                           | _id, text=None, extra_json=None): |
|     113                           |         """                       |
|     114                           |         Logs fre                  |
|     115                           | e-form metadata to ValidMind API. |
|     116                           |                                   |
|     117                           |                                   |
|     118                           |      :param content_id: Unique co |
|     119                           | ntent identifier for the metadata |
|     120                           |         :param text: Free-fo      |
|     121                           | rm text to assign to the metadata |
|     122                           |         :par                      |
|     123                           | am extra_json: Free-form key-valu |
|     124                           | e pairs to assign to the metadata |
|     125                           |         """                       |
|     126                           |         metadata_dict = {         |
|     127                           |                                   |
|     128                           |         "content_id": content_id, |
|     129                           |         }                         |
|     130                           |                                   |
|     131                           |         if text is not None:      |
|     132                           |                                   |
|     133                           |      metadata_dict["text"] = text |
|     134                           |                                   |
|     135                           |        if extra_json is not None: |
|     136                           |             m                     |
|     137                           | etadata_dict["json"] = extra_json |
|     138                           |                                   |
|     139                           |         r = api_session.post(     |
| :::                               |                                   |
|                                   |       f"{API_HOST}/log_metadata", |
|                                   |             data=json.dumps(      |
|                                   | metadata_dict, cls=NumpyEncoder), |
|                                   |             headers={"Co          |
|                                   | ntent-Type": "application/json"}, |
|                                   |         )                         |
|                                   |                                   |
|                                   |         if r.status_code != 200:  |
|                                   |             print("Could no       |
|                                   | t log metadata to ValidMind API") |
|                                   |                                   |
|                                   |           raise Exception(r.text) |
|                                   |                                   |
|                                   |         prin                      |
|                                   | t("Successfully logged metadata") |
|                                   |                                   |
|                                   |         return True               |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
## [`log_metrics`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`metrics`{.highlight .language-python}]{.n}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`run_cuid`{.highlight .language-python}]{.n}[`=`{.highlight .language-python}]{.o}[`None`{.highlight .language-python}]{.kc}[`)`{.highlight .language-python}]{.p} {#validmind.log_metrics .doc .doc-heading}

::: {.doc .doc-contents}
Logs metrics to ValidMind API.

:param metrics: A list of Metric objects. :param run_cuid: The run CUID.
If not provided, a new run will be created.

Source code in `validmind/api_client.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     179                           |                                   |
|     180                           |     def log                       |
|     181                           | _metrics(metrics, run_cuid=None): |
|     182                           |         """                       |
|     183                           |                                   |
|     184                           |    Logs metrics to ValidMind API. |
|     185                           |                                   |
|     186                           |         :param m                  |
|     187                           | etrics: A list of Metric objects. |
|     188                           |         :param r                  |
|     189                           | un_cuid: The run CUID. If not pro |
|     190                           | vided, a new run will be created. |
|     191                           |         """                       |
|     192                           |         if run_cuid is None:      |
|     193                           |                                   |
|     194                           |            run_cuid = start_run() |
|     195                           |                                   |
|     196                           |         serialized_metrics =      |
|     197                           |  [m.serialize() for m in metrics] |
|     198                           |                                   |
|     199                           |         r = api_session.post(     |
|     200                           |             f"{API_HOST}/         |
|     201                           | log_metrics?run_cuid={run_cuid}", |
|     202                           |             data=json.dumps(seria |
|     203                           | lized_metrics, cls=NumpyEncoder), |
| :::                               |             headers={"Co          |
|                                   | ntent-Type": "application/json"}, |
|                                   |         )                         |
|                                   |                                   |
|                                   |         if r.status_code != 200:  |
|                                   |             print("Could n        |
|                                   | ot log metrics to ValidMind API") |
|                                   |                                   |
|                                   |           raise Exception(r.text) |
|                                   |                                   |
|                                   |         pri                       |
|                                   | nt("Successfully logged metrics") |
|                                   |                                   |
|                                   |         return True               |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
## [`log_model`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`vm_model`{.highlight .language-python}]{.n}[`)`{.highlight .language-python}]{.p} {#validmind.log_model .doc .doc-heading}

::: {.doc .doc-contents}
Logs model metadata and hyperparameters to ValidMind API. :param
vm_model: A ValidMind Model wrapper instance.

Source code in `validmind/api_client.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     142                           |                                   |
|     143                           |     def log_model(vm_model):      |
|     144                           |         """                       |
|     145                           |         Logs model metadata and   |
|     146                           | hyperparameters to ValidMind API. |
|     147                           |         :param vm_model: A        |
|     148                           | ValidMind Model wrapper instance. |
|     149                           |         """                       |
|     150                           |         r = api_session.post(     |
|     151                           |                                   |
|     152                           |          f"{API_HOST}/log_model", |
|     153                           |                                   |
|     154                           |           data=json.dumps(vm_mode |
|     155                           | l.serialize(), cls=NumpyEncoder), |
|     156                           |             headers={"Co          |
|     157                           | ntent-Type": "application/json"}, |
| :::                               |         )                         |
|                                   |                                   |
|                                   |         if r.status_code != 200:  |
|                                   |             print("Could          |
|                                   |  not log model to ValidMind API") |
|                                   |                                   |
|                                   |           raise Exception(r.text) |
|                                   |                                   |
|                                   |         return True               |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.doc .doc-object .doc-function}
## [`log_test_results`{.highlight .language-python}]{.n}[`(`{.highlight .language-python}]{.p}[`results`{.highlight .language-python}]{.n}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`run_cuid`{.highlight .language-python}]{.n}[`=`{.highlight .language-python}]{.o}[`None`{.highlight .language-python}]{.kc}[`,`{.highlight .language-python}]{.p}` `{.highlight .language-python}[`dataset_type`{.highlight .language-python}]{.n}[`=`{.highlight .language-python}]{.o}[`'training'`{.highlight .language-python}]{.s1}[`)`{.highlight .language-python}]{.p} {#validmind.log_test_results .doc .doc-heading}

::: {.doc .doc-contents}
Logs test results information. This method will be called automatically
be any function running tests but can also be called directly if the
user wants to run tests on their own.

:param results: A list of TestResults objects :param run_cuid: The run
CUID. If not provided, a new run will be created.

Source code in `validmind/api_client.py`

::: highlight
+-----------------------------------+-----------------------------------+
| ::: linenodiv                     | <div>                             |
|     233                           |                                   |
|     234                           |     def                           |
|     235                           | log_test_results(results, run_cui |
|     236                           | d=None, dataset_type="training"): |
|     237                           |         """                       |
|     238                           |         Logs test results inf     |
|     239                           | ormation. This method will be cal |
|     240                           | led automatically be any function |
|     241                           |         running tests but can al  |
|     242                           | so be called directly if the user |
|     243                           |  wants to run tests on their own. |
|     244                           |                                   |
|     245                           |         :param resul              |
|     246                           | ts: A list of TestResults objects |
|     247                           |         :param r                  |
|     248                           | un_cuid: The run CUID. If not pro |
| :::                               | vided, a new run will be created. |
|                                   |         """                       |
|                                   |         if run_cuid is None:      |
|                                   |                                   |
|                                   |            run_cuid = start_run() |
|                                   |                                   |
|                                   |                                   |
|                                   |  # TBD - parallelize API requests |
|                                   |         for result in results:    |
|                                   |             log_test_resul        |
|                                   | t(result, run_cuid, dataset_type) |
|                                   |                                   |
|                                   |         return True               |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::
:::
:::
:::
:::
:::
:::
:::
:::

::: {.md-footer-meta .md-typeset}
::: {.md-footer-meta__inner .md-grid}
::: md-copyright
Made with [Material for
MkDocs](https://squidfunk.github.io/mkdocs-material/){target="_blank"
rel="noopener"}
:::
:::
:::
:::

::: {.md-dialog md-component="dialog"}
::: {.md-dialog__inner .md-typeset}
:::
:::
