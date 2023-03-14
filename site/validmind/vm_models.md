# ValidMind Models

Models entrypoint


### _class_ validmind.vm_models.Dataset(raw_dataset: object, fields: list, variables: list, sample: list, shape: dict, correlation_matrix: ~typing.Optional[object] = None, correlations: ~typing.Optional[dict] = None, type: ~typing.Optional[str] = None, options: ~typing.Optional[dict] = None, statistics: ~typing.Optional[dict] = None, targets: ~typing.Optional[dict] = None, target_column: str = '', class_labels: ~typing.Optional[dict] = None, _Dataset__feature_lookup: dict = <factory>, _Dataset__transformed_df: ~typing.Optional[object] = None)
Bases: `object`

Model class wrapper


#### raw_dataset(_: objec_ )

#### fields(_: lis_ )

#### variables(_: lis_ )

#### sample(_: lis_ )

#### shape(_: dic_ )

#### correlation_matrix(_: objec_ _ = Non_ )

#### correlations(_: dic_ _ = Non_ )

#### type(_: st_ _ = Non_ )

#### options(_: dic_ _ = Non_ )

#### statistics(_: dic_ _ = Non_ )

#### targets(_: dic_ _ = Non_ )

#### target_column(_: st_ _ = '_ )

#### class_labels(_: dic_ _ = Non_ )

#### _property_ x()
Returns the dataset’s features


#### _property_ y()
Returns the dataset’s target column


#### get_feature_by_id(feature_id)
Returns the feature with the given id. We also build a lazy
lookup cache in case the same feature is requested multiple times.


* **Parameters**

    **feature_id** (*str*) – The id of the feature to return



* **Raises**

    **ValueError** – If the feature with the given id does not exist



* **Returns**

    The feature with the given id



* **Return type**

    dict



#### get_feature_type(feature_id)
Returns the type of the feature with the given id


* **Parameters**

    **feature_id** (*str*) – The id of the feature to return



* **Returns**

    The type of the feature with the given id



* **Return type**

    str



#### serialize()
Serializes the model to a dictionary so it can be sent to the API


#### describe()
Extracts descriptive statistics for each field in the dataset


#### get_correlations()
Extracts correlations for each field in the dataset


#### get_correlation_plots(n_top=15)
Extracts correlation plots for the n_top correlations in the dataset


* **Parameters**

    **n_top** (*int**, **optional*) – The number of top correlations to extract. Defaults to 15.



* **Returns**

    A list of correlation plots



* **Return type**

    list



#### _property_ transformed_dataset()
Returns a transformed dataset that uses the features from vm_dataset.
Some of the features in vm_dataset are of type Dummy so we need to
reverse the one hot encoding and drop the individual dummy columns


* **Parameters**

    **force_refresh** (*bool**, **optional*) – Whether to force a refresh of the transformed dataset. Defaults to False.



* **Returns**

    The transformed dataset



* **Return type**

    pd.DataFrame



#### _classmethod_ create_from_dict(dict_)
Creates a Dataset object from a dictionary


* **Parameters**

    **dict** (*dict*) – The dictionary to create the Dataset object from



* **Returns**

    The Dataset object



* **Return type**

    Dataset



#### _classmethod_ init_from_pd_dataset(df, options=None, targets=None, target_column=None, class_labels=None)
Initializes a Dataset object from a pandas DataFrame


* **Parameters**

    
    * **df** (*pd.DataFrame*) – The pandas DataFrame to initialize the Dataset object from


    * **options** (*dict**, **optional*) – The options to use when initializing the Dataset object. Defaults to None.


    * **targets** (*list**, **optional*) – The targets to use when initializing the Dataset object. Defaults to None.


    * **target_column** (*str**, **optional*) – The target column to use when initializing the Dataset object. Defaults to None.


    * **class_labels** (*list**, **optional*) – The class labels to use when initializing the Dataset object. Defaults to None.



* **Returns**

    The Dataset object



* **Return type**

    Dataset



### _class_ validmind.vm_models.DatasetTargets(target_column: str, description: Optional[str] = None, class_labels: Optional[dict] = None)
Bases: `object`

Dataset targets definition


#### target_column(_: st_ )

#### description(_: st_ _ = Non_ )

#### class_labels(_: dic_ _ = Non_ )

### _class_ validmind.vm_models.Figure(key: str, metadata: dict, figure: object, extras: Optional[dict] = None)
Bases: `object`

Figure objects track the schema supported by the ValidMind API


#### key(_: st_ )

#### metadata(_: dic_ )

#### figure(_: objec_ )

#### extras(_: Optional[dict_ _ = Non_ )

#### serialize()
Serializes the Figure to a dictionary so it can be sent to the API


### _class_ validmind.vm_models.Metric(test_context: TestContext, params: Optional[dict] = None, result: Optional[TestPlanMetricResult] = None)
Bases: `TestContextUtils`

Metric objects track the schema supported by the ValidMind API


#### test_context(_: TestContex_ )

#### test_type(_: ClassVar[str_ _ = 'Metric_ )

#### type(_: ClassVar[str_ _ = '_ )

#### scope(_: ClassVar[str_ _ = '_ )

#### key(_: ClassVar[str_ _ = '_ )

#### value_formatter(_: ClassVar[Optional[str]_ _ = Non_ )

#### default_params(_: ClassVar[dict_ _ = {_ )

#### params(_: dic_ _ = Non_ )

#### result(_: TestPlanMetricResul_ _ = Non_ )

#### _property_ name()

#### run(\*args, \*\*kwargs)
Run the metric calculation and cache its results


#### cache_results(metric_value: Union[dict, list, DataFrame], figures: Optional[List[Figure]] = None)
Cache the results of the metric calculation and do any post-processing if needed


* **Parameters**

    
    * **metric_value** (*Union**[**dict**, **list**, **pd.DataFrame**]*) – The value of the metric


    * **figures** (*Optional**[**object**]*) – Any figures to attach to the test plan result



* **Returns**

    The test plan result object



* **Return type**

    TestPlanResult



### _class_ validmind.vm_models.MetricResult(type: str, scope: str, key: dict, value: Union[dict, list, DataFrame], value_formatter: Optional[str] = None)
Bases: `object`

MetricResult class definition. A MetricResult is returned by any internal method
that extracts metrics from a dataset or model, and returns 1) Metric and Figure
objects that can be sent to the API and 2) and plots and metadata for display purposes


#### type(_: st_ )

#### scope(_: st_ )

#### key(_: dic_ )

#### value(_: Union[dict, list, DataFrame_ )

#### value_formatter(_: Optional[str_ _ = Non_ )

#### serialize()
Serializes the Metric to a dictionary so it can be sent to the API


### _class_ validmind.vm_models.Model(attributes: Optional[ModelAttributes] = None, task: Optional[str] = None, subtask: Optional[str] = None, params: Optional[dict] = None, model_id: str = 'main', model: Optional[object] = None)
Bases: `object`

Model class wrapper


#### attributes(_: ModelAttribute_ _ = Non_ )

#### task(_: st_ _ = Non_ )

#### subtask(_: st_ _ = Non_ )

#### params(_: dic_ _ = Non_ )

#### model_id(_: st_ _ = 'main_ )

#### model(_: objec_ _ = Non_ )

#### serialize()
Serializes the model to a dictionary so it can be sent to the API


#### predict(\*args, \*\*kwargs)
Predict method for the model. This is a wrapper around the model’s
predict_proba (for classification) or predict (for regression) method

NOTE: This only works for sklearn or xgboost models at the moment


#### _classmethod_ is_supported_model(model)
Checks if the model is supported by the API


* **Parameters**

    **model** (*object*) – The trained model instance to check



* **Returns**

    True if the model is supported, False otherwise



* **Return type**

    bool



#### _classmethod_ create_from_dict(dict_)
Creates a Model instance from a dictionary


* **Parameters**

    **dict** (*dict*) – The dictionary to create the Model instance from



* **Returns**

    The Model instance created from the dictionary



* **Return type**

    Model



### _class_ validmind.vm_models.ModelAttributes(architecture: Optional[str] = None, framework: Optional[str] = None, framework_version: Optional[str] = None)
Bases: `object`

Model attributes definition


#### architecture(_: st_ _ = Non_ )

#### framework(_: st_ _ = Non_ )

#### framework_version(_: st_ _ = Non_ )

### _class_ validmind.vm_models.TestContext(dataset: Optional[Dataset] = None, model: Optional[Model] = None, train_ds: Optional[Dataset] = None, test_ds: Optional[Dataset] = None, y_train_predict: Optional[object] = None, y_test_predict: Optional[object] = None)
Bases: `object`

Holds context that can be used by tests to run.
Allows us to store data that needs to be reused
across different tests/metrics such as model predictions,
shared dataset metrics, etc.


#### dataset(_: Datase_ _ = Non_ )

#### model(_: Mode_ _ = Non_ )

#### train_ds(_: Datase_ _ = Non_ )

#### test_ds(_: Datase_ _ = Non_ )

#### y_train_predict(_: objec_ _ = Non_ )

#### y_test_predict(_: objec_ _ = Non_ )

### _class_ validmind.vm_models.TestContextUtils()
Bases: `object`

Utility methods for classes that receive a TestContext

TODO: more validation


#### test_context(_: TestContex_ )

#### _property_ dataset()

#### _property_ model()

#### _property_ train_ds()

#### _property_ test_ds()

#### _property_ y_train_predict()

#### _property_ y_test_predict()

#### class_predictions(y_predict)
Converts a set of probability predictions to class predictions


* **Parameters**

    **y_predict** (*np.array**, **pd.DataFrame*) – Predictions to convert



* **Returns**

    Class predictions



* **Return type**

    (np.array, pd.DataFrame)



#### _property_ df()
Returns a Pandas DataFrame for the dataset, first checking if
we passed in a Dataset or a DataFrame


### _class_ validmind.vm_models.TestPlan(config: {} = None, test_context: TestContext = None, dataset: Dataset = None, model: Model = None, train_ds: Dataset = None, test_ds: Dataset = None, pbar: tqdm = None)
Bases: `object`

Base class for test plans. Test plans are used to define any
arbitrary grouping of tests that will be run on a dataset or model.


#### name(_: ClassVar[str_ )

#### required_context(_: ClassVar[List[str]_ )

#### tests(_: ClassVar[List[object]_ _ = [_ )

#### test_plans(_: ClassVar[List[object]_ _ = [_ )

#### results(_: ClassVar[List[TestPlanResult]_ _ = [_ )

#### config(_: {_ _ = Non_ )

#### test_context(_: TestContex_ _ = Non_ )

#### dataset(_: Datase_ _ = Non_ )

#### model(_: Mode_ _ = Non_ )

#### train_ds(_: Datase_ _ = Non_ )

#### test_ds(_: Datase_ _ = Non_ )

#### pbar(_: tqd_ _ = Non_ )

#### validate_context()
Validates that the context elements are present
in the instance so that the test plan can be run


#### run(send=True)
Runs the test plan


#### log_results()
Logs the results of the test plan to ValidMind

This method will be called after the test plan has been run and all results have been
collected. This method will log the results to ValidMind.


#### summarize()
Summarizes the results of the test plan

This method will be called after the test plan has been run and all results have been
logged to ValidMind. It will summarize the results of the test plan by creating an
html table with the results of each test. This html table will be displayed in an
VS Code, Jupyter or other notebook environment.


### _class_ validmind.vm_models.TestPlanDatasetResult(dataset: Optional[Dataset] = None)
Bases: `TestPlanResult`

Result wrapper for datasets that run as part of a test plan


#### dataset(_: Datase_ _ = Non_ )

#### log()
Log the result… Must be overridden by subclasses


### _class_ validmind.vm_models.TestPlanMetricResult(figures: Optional[List[Figure]] = None, metric: Optional[MetricResult] = None)
Bases: `TestPlanResult`

Result wrapper for metrics that run as part of a test plan


#### figures(_: Optional[List[Figure]_ _ = Non_ )

#### metric(_: Optional[MetricResult_ _ = Non_ )

#### log()
Log the result… Must be overridden by subclasses


### _class_ validmind.vm_models.TestPlanModelResult(model: Optional[Model] = None)
Bases: `TestPlanResult`

Result wrapper for models that run as part of a test plan


#### model(_: Mode_ _ = Non_ )

#### log()
Log the result… Must be overridden by subclasses


### _class_ validmind.vm_models.TestPlanTestResult(test_results: Optional[TestResults] = None)
Bases: `TestPlanResult`

Result wrapper for test results produced by the tests that run as part of a test plan


#### test_results(_: TestResult_ _ = Non_ )

#### log()
Log the result… Must be overridden by subclasses


### _class_ validmind.vm_models.TestResult(\*, test_name: Optional[str] = None, column: Optional[str] = None, passed: Optional[bool] = None, values: dict)
Bases: `BaseResultModel`

TestResult model


#### test_name(_: Optional[str_ )

#### column(_: Optional[str_ )

#### passed(_: Optional[bool_ )

#### values(_: dic_ )

### _class_ validmind.vm_models.TestResults(\*, category: str, test_name: str, params: dict, passed: bool, results: List[TestResult])
Bases: `BaseResultModel`

TestResults model


#### category(_: st_ )

#### test_name(_: st_ )

#### params(_: dic_ )

#### passed(_: boo_ )

#### results(_: List[TestResult_ )

### _class_ validmind.vm_models.ThresholdTest(test_context: TestContext, params: Optional[dict] = None, test_results: Optional[TestResults] = None)
Bases: `TestContextUtils`

A threshold test is a combination of a metric/plot we track and a
corresponding set of parameters and thresholds values that allow
us to determine whether the metric/plot passes or fails.


#### test_context(_: TestContex_ )

#### test_type(_: ClassVar[str_ _ = 'ThresholdTest_ )

#### category(_: ClassVar[str_ _ = '_ )

#### name(_: ClassVar[str_ _ = '_ )

#### default_params(_: ClassVar[dict_ _ = {_ )

#### params(_: dic_ _ = Non_ )

#### test_results(_: TestResult_ _ = Non_ )

#### run(\*args, \*\*kwargs)
Run the test and cache its results


#### cache_results(results: List[TestResult], passed: bool)
Cache the individual results of the threshold test as a list of TestResult objects


* **Parameters**

    
    * **results** (*List**[**TestResult**]*) – The results of the threshold test


    * **passed** (*bool*) – Whether the threshold test passed or failed



* **Returns**

    The test plan result object



* **Return type**

    TestPlanResult
