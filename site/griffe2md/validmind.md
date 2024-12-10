## ValidMind (griffe2md)

The ValidMind Library is a suite of developer tools and methods designed to automate the documentation and validation of your models.

Designed to be model agnostic, the ValidMind Library provides all the standard functionality without requiring you to rewrite any functions as long as your model is built in Python.

With a rich array of documentation tools and test suites, from documenting descriptions of your datasets to testing your models for weak spots and overfit areas, the ValidMind Library helps you automate model documentation by feeding the ValidMind Platform with documentation artifacts and test results.

To install the client library:

```bash
pip install validmind
```

To initialize the client library, paste the code snippet with the client integration details directly into your
development source code, replacing this example with your own:

```python
import validmind as vm

vm.init(
  api_host = "https://api.dev.vm.validmind.ai/api/v1/tracking/tracking",
  api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  api_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  project = "<project-identifier>"
)
```

After you have pasted the code snippet into your development source code and executed the code, the Python client
library will register with ValidMind. You can now use the ValidMind Library to document and test your models,
and to upload to the ValidMind Platform.

**Modules:**

- [**api_client**](#validmind.api_client) – ValidMind API client
- [**client**](#validmind.client) – Client interface for all data and model validation functions
- [**client_config**](#validmind.client_config) – Central class to track configuration of the ValidMind Library
- [**datasets**](#validmind.datasets) – Example datasets that can be used with the ValidMind Library.
- [**errors**](#validmind.errors) – This module contains all the custom errors that are used in the ValidMind Library.
- [**html_templates**](#validmind.html_templates) –
- [**input_registry**](#validmind.input_registry) – Central class to register inputs
- [**logging**](#validmind.logging) – ValidMind logging module.
- [**models**](#validmind.models) –
- [**template**](#validmind.template) –
- [**test_suites**](#validmind.test_suites) – Entrypoint for test suites.
- [**tests**](#validmind.tests) – ValidMind Tests Module
- [**unit_metrics**](#validmind.unit_metrics) –
- [**utils**](#validmind.utils) –
- [**vm_models**](#validmind.vm_models) – Models entrypoint

**Functions:**

- [**get_test_suite**](#validmind.get_test_suite) – Gets a TestSuite object for the current project or a specific test suite
- [**init**](#validmind.init) – Initializes the API client instances and calls the /ping endpoint to ensure
- [**init_dataset**](#validmind.init_dataset) – Initializes a VM Dataset, which can then be passed to other functions
- [**init_model**](#validmind.init_model) – Initializes a VM Model, which can then be passed to other functions
- [**init_r_model**](#validmind.init_r_model) – Initializes a VM Model for an R model
- [**log_metric**](#validmind.log_metric) – Logs a unit metric
- [**preview_template**](#validmind.preview_template) – Preview the documentation template for the current project
- [**reload**](#validmind.reload) – Reconnect to the ValidMind API and reload the project configuration
- [**run_documentation_tests**](#validmind.run_documentation_tests) – Collect and run all the tests associated with a template
- [**run_test_suite**](#validmind.run_test_suite) – High Level function for running a test suite
- [**tags**](#validmind.tags) – Decorator for specifying tags for a test.
- [**tasks**](#validmind.tasks) – Decorator for specifying the task types that a test is designed for.
- [**test**](#validmind.test) – Decorator for creating and registering custom tests

### validmind.api_client

ValidMind API client

Note that this takes advantage of the fact that python modules are singletons to store and share
the configuration and session across the entire project regardless of where the client is imported.

**Functions:**

- [**aget_metadata**](#validmind.api_client.aget_metadata) – Gets a metadata object from ValidMind API.
- [**alog_figure**](#validmind.api_client.alog_figure) – Logs a figure
- [**alog_input**](#validmind.api_client.alog_input) – Logs input information - internal use for now (don't expose via public API)
- [**alog_metadata**](#validmind.api_client.alog_metadata) – Logs free-form metadata to ValidMind API.
- [**alog_metric**](#validmind.api_client.alog_metric) – See log_metric for details
- [**alog_test_result**](#validmind.api_client.alog_test_result) – Logs test results information
- [**get_ai_key**](#validmind.api_client.get_ai_key) – Calls the api to get an api key for our LLM proxy
- [**get_api_host**](#validmind.api_client.get_api_host) –
- [**get_api_model**](#validmind.api_client.get_api_model) –
- [**init**](#validmind.api_client.init) – Initializes the API client instances and calls the /ping endpoint to ensure
- [**log_input**](#validmind.api_client.log_input) –
- [**log_metric**](#validmind.api_client.log_metric) – Logs a unit metric
- [**reload**](#validmind.api_client.reload) – Reconnect to the ValidMind API and reload the project configuration

**Attributes:**

- [**logger**](#validmind.api_client.logger) –

#### validmind.api_client.aget_metadata

```python
aget_metadata(content_id)
```

Gets a metadata object from ValidMind API.

**Parameters:**

- **content_id** (<code>[str](#str)</code>) – Unique content identifier for the metadata

**Raises:**

- <code>[Exception](#Exception)</code> – If the API call fails

**Returns:**

- **dict** (<code>[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]</code>) – Metadata object

#### validmind.api_client.alog_figure

```python
alog_figure(figure)
```

Logs a figure

**Parameters:**

- **figure** (<code>[Figure](#validmind.vm_models.Figure)</code>) – The Figure object wrapper

**Raises:**

- <code>[Exception](#Exception)</code> – If the API call fails

**Returns:**

- **dict** (<code>[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]</code>) – The response from the API

#### validmind.api_client.alog_input

```python
alog_input(input_id, type, metadata)
```

Logs input information - internal use for now (don't expose via public API)

**Parameters:**

- **input_id** (<code>[str](#str)</code>) – The input_id of the input
- **type** (<code>[str](#str)</code>) – The type of the input
- **metadata** (<code>[dict](#dict)</code>) – The metadata of the input

**Raises:**

- <code>[Exception](#Exception)</code> – If the API call fails

**Returns:**

- **dict** (<code>[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]</code>) – The response from the API

#### validmind.api_client.alog_metadata

```python
alog_metadata(content_id, text=None, _json=None)
```

Logs free-form metadata to ValidMind API.

**Parameters:**

- **content_id** (<code>[str](#str)</code>) – Unique content identifier for the metadata
- **text** (<code>[str](#str)</code>) – Free-form text to assign to the metadata. Defaults to None.
- **\_json** (<code>[dict](#dict)</code>) – Free-form key-value pairs to assign to the metadata. Defaults to None.

**Raises:**

- <code>[Exception](#Exception)</code> – If the API call fails

**Returns:**

- **dict** (<code>[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]</code>) – The response from the API

#### validmind.api_client.alog_metric

```python
alog_metric(key, value, inputs=None, params=None, recorded_at=None)
```

See log_metric for details

#### validmind.api_client.alog_test_result

```python
alog_test_result(result, section_id=None, position=None)
```

Logs test results information

This method will be called automatically from any function running tests but
can also be called directly if the user wants to run tests on their own.

**Parameters:**

- **result** (<code>[dict](#dict)</code>) – A dictionary representing the test result
- **section_id** (<code>[str](#str)</code>) – The section ID add a test driven block to the documentation
- **position** (<code>[int](#int)</code>) – The position in the section to add the test driven block

**Raises:**

- <code>[Exception](#Exception)</code> – If the API call fails

**Returns:**

- **dict** (<code>[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]</code>) – The response from the API

#### validmind.api_client.get_ai_key

```python
get_ai_key()
```

Calls the api to get an api key for our LLM proxy

#### validmind.api_client.get_api_host

```python
get_api_host()
```

#### validmind.api_client.get_api_model

```python
get_api_model()
```

#### validmind.api_client.init

```python
init(
    project=None,
    api_key=None,
    api_secret=None,
    api_host=None,
    model=None,
    monitoring=False,
)
```

Initializes the API client instances and calls the /ping endpoint to ensure
the provided credentials are valid and we can connect to the ValidMind API.

If the API key and secret are not provided, the client will attempt to
retrieve them from the environment variables `VM_API_KEY` and `VM_API_SECRET`.

**Parameters:**

- **project** (<code>[str](#str)</code>) – The project CUID. Alias for model. Defaults to None. [DEPRECATED]
- **model** (<code>[str](#str)</code>) – The model CUID. Defaults to None.
- **api_key** (<code>[str](#str)</code>) – The API key. Defaults to None.
- **api_secret** (<code>[str](#str)</code>) – The API secret. Defaults to None.
- **api_host** (<code>[str](#str)</code>) – The API host. Defaults to None.
- **monitoring** (<code>[bool](#bool)</code>) – The ongoing monitoring flag. Defaults to False.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If the API key and secret are not provided

#### validmind.api_client.log_input

```python
log_input(input_id, type, metadata)
```

#### validmind.api_client.log_metric

```python
log_metric(key, value, inputs=None, params=None, recorded_at=None)
```

Logs a unit metric

Unit metrics are key-value pairs where the key is the metric name and the value is
a scalar (int or float). These key-value pairs are associated with the currently
selected model (inventory model in the ValidMind Platform) and keys can be logged
to over time to create a history of the metric. On the ValidMind Platform, these metrics
will be used to create plots/visualizations for documentation and dashboards etc.

**Parameters:**

- **key** (<code>[str](#str)</code>) – The metric key
- **value** (<code>[float](#float)</code>) – The metric value
- **inputs** (<code>[list](#list)</code>) – A list of input IDs that were used to compute the metric.
- **params** (<code>[dict](#dict)</code>) – Dictionary of parameters used to compute the metric.
- **recorded_at** (<code>[str](#str)</code>) – The timestamp of the metric. Server will use
  current time if not provided.

#### validmind.api_client.logger

```python
logger = get_logger(__name__)
```

#### validmind.api_client.reload

```python
reload()
```

Reconnect to the ValidMind API and reload the project configuration

### validmind.client

Client interface for all data and model validation functions

**Functions:**

- [**get_test_suite**](#validmind.client.get_test_suite) – Gets a TestSuite object for the current project or a specific test suite
- [**init_dataset**](#validmind.client.init_dataset) – Initializes a VM Dataset, which can then be passed to other functions
- [**init_model**](#validmind.client.init_model) – Initializes a VM Model, which can then be passed to other functions
- [**init_r_model**](#validmind.client.init_r_model) – Initializes a VM Model for an R model
- [**preview_template**](#validmind.client.preview_template) – Preview the documentation template for the current project
- [**run_documentation_tests**](#validmind.client.run_documentation_tests) – Collect and run all the tests associated with a template
- [**run_test_suite**](#validmind.client.run_test_suite) – High Level function for running a test suite

**Attributes:**

- [**logger**](#validmind.client.logger) –

#### validmind.client.get_test_suite

```python
get_test_suite(test_suite_id=None, section=None, *args, **kwargs)
```

Gets a TestSuite object for the current project or a specific test suite

This function provides an interface to retrieve the TestSuite instance for the
current project or a specific TestSuite instance identified by test_suite_id.
The project Test Suite will contain sections for every section in the project's
documentation template and these Test Suite Sections will contain all the tests
associated with that template section.

**Parameters:**

- **test_suite_id** (<code>[str](#str)</code>) – The test suite name. If not passed, then the
  project's test suite will be returned. Defaults to None.
- **section** (<code>[str](#str)</code>) – The section of the documentation template from which
  to retrieve the test suite. This only applies if test_suite_id is None.
  Defaults to None.
- **args** – Additional arguments to pass to the TestSuite
- **kwargs** – Additional keyword arguments to pass to the TestSuite

#### validmind.client.init_dataset

```python
init_dataset(
    dataset,
    model=None,
    index=None,
    index_name=None,
    date_time_index=False,
    columns=None,
    text_column=None,
    target_column=None,
    feature_columns=None,
    extra_columns=None,
    class_labels=None,
    type=None,
    input_id=None,
    __log=True,
)
```

Initializes a VM Dataset, which can then be passed to other functions
that can perform additional analysis and tests on the data. This function
also ensures we are reading a valid dataset type.

The following dataset types are supported:

- Pandas DataFrame
- Polars DataFrame
- Numpy ndarray
- Torch TensorDataset

**Parameters:**

- **dataset** – dataset from various python libraries
- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – ValidMind model object
- **targets** (<code>[DatasetTargets](#vm.vm.DatasetTargets)</code>) – A list of target variables
- **target_column** (<code>[str](#str)</code>) – The name of the target column in the dataset
- **feature_columns** (<code>[list](#list)</code>) – A list of names of feature columns in the dataset
- **extra_columns** (<code>[dictionary](#dictionary)</code>) – A dictionary containing the names of the
- **class_labels** (<code>[dict](#dict)</code>) – A list of class labels for classification problems
- **type** (<code>[str](#str)</code>) – The type of dataset (one of DATASET_TYPES)
- **input_id** (<code>[str](#str)</code>) – The input ID for the dataset (e.g. "my_dataset"). By default,
  this will be set to `dataset` but if you are passing this dataset as a
  test input using some other key than `dataset`, then you should set
  this to the same key.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If the dataset type is not supported

**Returns:**

- <code>[VMDataset](#validmind.vm_models.dataset.VMDataset)</code> – vm.vm.Dataset: A VM Dataset instance

#### validmind.client.init_model

```python
init_model(
    model=None,
    input_id="model",
    attributes=None,
    predict_fn=None,
    __log=True,
    **kwargs
)
```

Initializes a VM Model, which can then be passed to other functions
that can perform additional analysis and tests on the data. This function
also ensures we are creating a model supported libraries.

**Parameters:**

- **model** (<code>[object](#object)</code>) – A trained model or VMModel instance
- **input_id** (<code>[str](#str)</code>) – The input ID for the model (e.g. "my_model"). By default,
  this will be set to `model` but if you are passing this model as a
  test input using some other key than `model`, then you should set
  this to the same key.
- **attributes** (<code>[dict](#dict)</code>) – A dictionary of model attributes
- **predict_fn** (<code>[callable](#callable)</code>) – A function that takes an input and returns a prediction
- \*\***kwargs** – Additional arguments to pass to the model

**Raises:**

- <code>[ValueError](#ValueError)</code> – If the model type is not supported

**Returns:**

- <code>[VMModel](#validmind.vm_models.model.VMModel)</code> – vm.VMModel: A VM Model instance

#### validmind.client.init_r_model

```python
init_r_model(model_path, input_id='model')
```

Initializes a VM Model for an R model

R models must be saved to disk and the filetype depends on the model type...
Currently we support the following model types:

- LogisticRegression `glm` model in R: saved as an RDS file with `saveRDS`
- LinearRegression `lm` model in R: saved as an RDS file with `saveRDS`
- XGBClassifier: saved as a .json or .bin file with `xgb.save`
- XGBRegressor: saved as a .json or .bin file with `xgb.save`

LogisticRegression and LinearRegression models are converted to sklearn models by extracting
the coefficients and intercept from the R model. XGB models are loaded using the xgboost
since xgb models saved in .json or .bin format can be loaded directly with either Python or R

**Parameters:**

- **model_path** (<code>[str](#str)</code>) – The path to the R model saved as an RDS or XGB file
- **model_type** (<code>[str](#str)</code>) – The type of the model (one of R_MODEL_TYPES)

**Returns:**

- <code>[VMModel](#validmind.vm_models.model.VMModel)</code> – vm.vm.Model: A VM Model instance

#### validmind.client.logger

```python
logger = get_logger(__name__)
```

#### validmind.client.preview_template

```python
preview_template()
```

Preview the documentation template for the current project

This function will display the documentation template for the current project. If
the project has not been initialized, then an error will be raised.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If the project has not been initialized

#### validmind.client.run_documentation_tests

```python
run_documentation_tests(
    section=None, send=True, fail_fast=False, inputs=None, config=None, **kwargs
)
```

Collect and run all the tests associated with a template

This function will analyze the current project's documentation template and collect
all the tests associated with it into a test suite. It will then run the test
suite, log the results to the ValidMind API, and display them to the user.

**Parameters:**

- **section** (<code>[str](#str) or [list](#list)</code>) – The section(s) to preview. Defaults to None.
- **send** (<code>[bool](#bool)</code>) – Whether to send the results to the ValidMind API. Defaults to True.
- **fail_fast** (<code>[bool](#bool)</code>) – Whether to stop running tests after the first failure. Defaults to False.
- **inputs** (<code>[dict](#dict)</code>) – A dictionary of test inputs to pass to the TestSuite
- **config** – A dictionary of test parameters to override the defaults
- \*\***kwargs** – backwards compatibility for passing in test inputs using keyword arguments

**Returns:**

- – TestSuite or dict: The completed TestSuite instance or a dictionary of TestSuites if section is a list.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If the project has not been initialized

#### validmind.client.run_test_suite

```python
run_test_suite(
    test_suite_id,
    send=True,
    fail_fast=False,
    config=None,
    inputs=None,
    **kwargs
)
```

High Level function for running a test suite

This function provides a high level interface for running a test suite. A test suite is
a collection of tests. This function will automatically find the correct test suite
class based on the test_suite_id, initialize each of the tests, and run them.

**Parameters:**

- **test_suite_id** (<code>[str](#str)</code>) – The test suite name (e.g. 'classifier_full_suite')
- **config** (<code>[dict](#dict)</code>) – A dictionary of parameters to pass to the tests in the
  test suite. Defaults to None.
- **send** (<code>[bool](#bool)</code>) – Whether to post the test results to the API. send=False
  is useful for testing. Defaults to True.
- **fail_fast** (<code>[bool](#bool)</code>) – Whether to stop running tests after the first failure. Defaults to False.
- **inputs** (<code>[dict](#dict)</code>) – A dictionary of test inputs to pass to the TestSuite e.g. `model`, `dataset`
  `models` etc. These inputs will be accessible by any test in the test suite. See the test
  documentation or `vm.describe_test()` for more details on the inputs required for each.
- \*\***kwargs** – backwards compatibility for passing in test inputs using keyword arguments

**Raises:**

- <code>[ValueError](#ValueError)</code> – If the test suite name is not found or if there is an error initializing the test suite

**Returns:**

- **TestSuite** – the TestSuite instance

### validmind.client_config

Central class to track configuration of the ValidMind Library
client against the ValidMind API

**Classes:**

- [**ClientConfig**](#validmind.client_config.ClientConfig) – Configuration class for the ValidMind API client. This is instantiated

**Attributes:**

- [**client_config**](#validmind.client_config.client_config) –

#### validmind.client_config.ClientConfig

```python
ClientConfig(
    model,
    feature_flags,
    document_type,
    documentation_template,
    running_on_colab=False,
)
```

Configuration class for the ValidMind API client. This is instantiated
when initializing the API client.

**Functions:**

- [**can_generate_llm_test_descriptions**](#validmind.client_config.ClientConfig.can_generate_llm_test_descriptions) – Returns True if the client can generate LLM based test descriptions

**Attributes:**

- [**document_type**](#validmind.client_config.ClientConfig.document_type) (<code>[str](#str)</code>) –
- [**documentation_template**](#validmind.client_config.ClientConfig.documentation_template) (<code>[object](#object)</code>) –
- [**feature_flags**](#validmind.client_config.ClientConfig.feature_flags) (<code>[dict](#dict)</code>) –
- [**model**](#validmind.client_config.ClientConfig.model) (<code>[object](#object)</code>) –
- [**running_on_colab**](#validmind.client_config.ClientConfig.running_on_colab) (<code>[bool](#bool)</code>) –

##### validmind.client_config.ClientConfig.can_generate_llm_test_descriptions

```python
can_generate_llm_test_descriptions()
```

Returns True if the client can generate LLM based test descriptions

##### validmind.client_config.ClientConfig.document_type

```python
document_type: str
```

##### validmind.client_config.ClientConfig.documentation_template

```python
documentation_template: object
```

##### validmind.client_config.ClientConfig.feature_flags

```python
feature_flags: dict
```

##### validmind.client_config.ClientConfig.model

```python
model: object
```

##### validmind.client_config.ClientConfig.running_on_colab

```python
running_on_colab: bool = False
```

#### validmind.client_config.client_config

```python
client_config = ClientConfig(
    model=None,
    feature_flags={},
    document_type="model_documentation",
    documentation_template=None,
    running_on_colab=False,
)

```

### validmind.datasets

Example datasets that can be used with the ValidMind Library.

**Modules:**

- [**classification**](#validmind.datasets.classification) – Entrypoint for classification datasets.
- [**credit_risk**](#validmind.datasets.credit_risk) – Entrypoint for credit risk datasets.
- [**nlp**](#validmind.datasets.nlp) – Example datasets that can be used with the ValidMind Library.
- [**regression**](#validmind.datasets.regression) – Entrypoint for regression datasets

#### validmind.datasets.classification

Entrypoint for classification datasets.

**Modules:**

- [**customer_churn**](#validmind.datasets.classification.customer_churn) –
- [**taiwan_credit**](#validmind.datasets.classification.taiwan_credit) –

##### validmind.datasets.classification.customer_churn

**Functions:**

- [**get_demo_test_config**](#validmind.datasets.classification.customer_churn.get_demo_test_config) – Returns input configuration for the default documentation
- [**load_data**](#validmind.datasets.classification.customer_churn.load_data) –
- [**preprocess**](#validmind.datasets.classification.customer_churn.preprocess) –

**Attributes:**

- [**boolean_columns**](#validmind.datasets.classification.customer_churn.boolean_columns) –
- [**categorical_columns**](#validmind.datasets.classification.customer_churn.categorical_columns) –
- [**class_labels**](#validmind.datasets.classification.customer_churn.class_labels) –
- [**current_path**](#validmind.datasets.classification.customer_churn.current_path) –
- [**dataset_path**](#validmind.datasets.classification.customer_churn.dataset_path) –
- [**drop_columns**](#validmind.datasets.classification.customer_churn.drop_columns) –
- [**target_column**](#validmind.datasets.classification.customer_churn.target_column) –

###### validmind.datasets.classification.customer_churn.boolean_columns

```python
boolean_columns = ['Gender']
```

###### validmind.datasets.classification.customer_churn.categorical_columns

```python
categorical_columns = ['Geography']
```

###### validmind.datasets.classification.customer_churn.class_labels

```python
class_labels = {'0': 'Did not exit', '1': 'Exited'}
```

###### validmind.datasets.classification.customer_churn.current_path

```python
current_path = os.path.dirname(os.path.abspath(__file__))
```

###### validmind.datasets.classification.customer_churn.dataset_path

```python
dataset_path = os.path.join(current_path, 'datasets')
```

###### validmind.datasets.classification.customer_churn.drop_columns

```python
drop_columns = ['RowNumber', 'CustomerId', 'Surname']
```

###### validmind.datasets.classification.customer_churn.get_demo_test_config

```python
get_demo_test_config(test_suite=None)
```

Returns input configuration for the default documentation
template assigned to this demo model

The default documentation template uses the following inputs:

- raw_dataset
- train_dataset
- test_dataset
- model

We assign the following inputs depending on the input config expected
by each test:

- When a test expects a "dataset" we use the raw_dataset
- When a tets expects "datasets" we use the train_dataset and test_dataset
- When a test expects a "model" we use the model
- When a test expects "model" and "dataset" we use the model and test_dataset
- The only exception is ClassifierPerformance since that runs twice: once
  with the train_dataset (in sample) and once with the test_dataset (out of sample)

###### validmind.datasets.classification.customer_churn.load_data

```python
load_data(full_dataset=False)
```

###### validmind.datasets.classification.customer_churn.preprocess

```python
preprocess(df)
```

###### validmind.datasets.classification.customer_churn.target_column

```python
target_column = 'Exited'
```

##### validmind.datasets.classification.taiwan_credit

**Functions:**

- [**load_data**](#validmind.datasets.classification.taiwan_credit.load_data) –
- [**preprocess**](#validmind.datasets.classification.taiwan_credit.preprocess) –

**Attributes:**

- [**boolean_columns**](#validmind.datasets.classification.taiwan_credit.boolean_columns) –
- [**categorical_columns**](#validmind.datasets.classification.taiwan_credit.categorical_columns) –
- [**class_labels**](#validmind.datasets.classification.taiwan_credit.class_labels) –
- [**current_path**](#validmind.datasets.classification.taiwan_credit.current_path) –
- [**dataset_path**](#validmind.datasets.classification.taiwan_credit.dataset_path) –
- [**drop_columns**](#validmind.datasets.classification.taiwan_credit.drop_columns) –
- [**target_column**](#validmind.datasets.classification.taiwan_credit.target_column) –

###### validmind.datasets.classification.taiwan_credit.boolean_columns

```python
boolean_columns = ['SEX']
```

###### validmind.datasets.classification.taiwan_credit.categorical_columns

```python
categorical_columns = ['MARRIAGE']
```

###### validmind.datasets.classification.taiwan_credit.class_labels

```python
class_labels = {'0': 'Did not default', '1': 'Defaulted'}
```

###### validmind.datasets.classification.taiwan_credit.current_path

```python
current_path = os.path.dirname(os.path.abspath(__file__))
```

###### validmind.datasets.classification.taiwan_credit.dataset_path

```python
dataset_path = os.path.join(current_path, 'datasets')
```

###### validmind.datasets.classification.taiwan_credit.drop_columns

```python
drop_columns = ['ID']
```

###### validmind.datasets.classification.taiwan_credit.load_data

```python
load_data()
```

###### validmind.datasets.classification.taiwan_credit.preprocess

```python
preprocess(df)
```

###### validmind.datasets.classification.taiwan_credit.target_column

```python
target_column = 'DEFAULT'
```

#### validmind.datasets.credit_risk

Entrypoint for credit risk datasets.

**Modules:**

- [**lending_club**](#validmind.datasets.credit_risk.lending_club) –
- [**lending_club_bias**](#validmind.datasets.credit_risk.lending_club_bias) –

##### validmind.datasets.credit_risk.lending_club

**Functions:**

- [**compute_scores**](#validmind.datasets.credit_risk.lending_club.compute_scores) –
- [**feature_engineering**](#validmind.datasets.credit_risk.lending_club.feature_engineering) –
- [**load_data**](#validmind.datasets.credit_risk.lending_club.load_data) – Load data from either an online source or offline files, automatically dropping specified columns for offline data.
- [**preprocess**](#validmind.datasets.credit_risk.lending_club.preprocess) –
- [**split**](#validmind.datasets.credit_risk.lending_club.split) –
- [**woe_encoding**](#validmind.datasets.credit_risk.lending_club.woe_encoding) –

**Attributes:**

- [**breaks_adj**](#validmind.datasets.credit_risk.lending_club.breaks_adj) –
- [**categorical_variables**](#validmind.datasets.credit_risk.lending_club.categorical_variables) –
- [**current_path**](#validmind.datasets.credit_risk.lending_club.current_path) –
- [**dataset_path**](#validmind.datasets.credit_risk.lending_club.dataset_path) –
- [**drop_columns**](#validmind.datasets.credit_risk.lending_club.drop_columns) –
- [**drop_features**](#validmind.datasets.credit_risk.lending_club.drop_features) –
- [**offline_data_file**](#validmind.datasets.credit_risk.lending_club.offline_data_file) –
- [**online_data_file**](#validmind.datasets.credit_risk.lending_club.online_data_file) –
- [**score_params**](#validmind.datasets.credit_risk.lending_club.score_params) –
- [**target_column**](#validmind.datasets.credit_risk.lending_club.target_column) –

###### validmind.datasets.credit_risk.lending_club.breaks_adj

```python
breaks_adj = {
    "loan_amnt": [5000, 10000, 15000, 20000, 25000],
    "int_rate": [10, 15, 20],
    "annual_inc": [50000, 100000, 150000],
}

```

###### validmind.datasets.credit_risk.lending_club.categorical_variables

```python
categorical_variables = [
    "term",
    "grade",
    "sub_grade",
    "emp_length",
    "home_ownership",
    "verification_status",
    "purpose",
]

```

###### validmind.datasets.credit_risk.lending_club.compute_scores

```python
compute_scores(probabilities)
```

###### validmind.datasets.credit_risk.lending_club.current_path

```python
current_path = os.path.dirname(os.path.abspath(__file__))
```

###### validmind.datasets.credit_risk.lending_club.dataset_path

```python
dataset_path = os.path.join(current_path, 'datasets')
```

###### validmind.datasets.credit_risk.lending_club.drop_columns

```python
drop_columns = [
    "Unnamed: 0",
    "id",
    "member_id",
    "funded_amnt",
    "emp_title",
    "url",
    "desc",
    "application_type",
    "title",
    "zip_code",
    "delinq_2yrs",
    "mths_since_last_delinq",
    "mths_since_last_record",
    "mths_since_last_major_derog",
    "revol_bal",
    "total_rec_prncp",
    "total_rec_late_fee",
    "recoveries",
    "out_prncp_inv",
    "out_prncp",
    "collection_recovery_fee",
    "next_pymnt_d",
    "initial_list_status",
    "pub_rec",
    "collections_12_mths_ex_med",
    "policy_code",
    "acc_now_delinq",
    "pymnt_plan",
    "tot_coll_amt",
    "tot_cur_bal",
    "total_rev_hi_lim",
    "last_pymnt_d",
    "last_credit_pull_d",
    "earliest_cr_line",
    "issue_d",
    "addr_state",
    "dti",
    "revol_util",
    "total_pymnt_inv",
    "inq_last_6mths",
    "total_rec_int",
    "last_pymnt_amnt",
]

```

###### validmind.datasets.credit_risk.lending_club.drop_features

```python
drop_features = ['loan_amnt', 'funded_amnt_inv', 'total_pymnt']
```

###### validmind.datasets.credit_risk.lending_club.feature_engineering

```python
feature_engineering(df)
```

###### validmind.datasets.credit_risk.lending_club.load_data

```python
load_data(source='online')
```

Load data from either an online source or offline files, automatically dropping specified columns for offline data.

:param source: 'online' for online data, 'offline' for offline files. Defaults to 'online'.
:return: DataFrame containing the loaded data.

###### validmind.datasets.credit_risk.lending_club.offline_data_file

```python
offline_data_file = os.path.join(
    dataset_path, "lending_club_loan_data_2007_2014_clean.csv.gz"
)

```

###### validmind.datasets.credit_risk.lending_club.online_data_file

```python
online_data_file = "https://vmai.s3.us-west-1.amazonaws.com/datasets/lending_club_loan_data_2007_2014.csv"

```

###### validmind.datasets.credit_risk.lending_club.preprocess

```python
preprocess(df)
```

###### validmind.datasets.credit_risk.lending_club.score_params

```python
score_params = {'target_score': 600, 'target_odds': 50, 'pdo': 20}
```

###### validmind.datasets.credit_risk.lending_club.split

```python
split(df, add_constant=False)
```

###### validmind.datasets.credit_risk.lending_club.target_column

```python
target_column = 'loan_status'
```

###### validmind.datasets.credit_risk.lending_club.woe_encoding

```python
woe_encoding(df)
```

##### validmind.datasets.credit_risk.lending_club_bias

**Functions:**

- [**compute_scores**](#validmind.datasets.credit_risk.lending_club_bias.compute_scores) –
- [**load_data**](#validmind.datasets.credit_risk.lending_club_bias.load_data) – Load data from the specified CSV file.
- [**preprocess**](#validmind.datasets.credit_risk.lending_club_bias.preprocess) –
- [**split**](#validmind.datasets.credit_risk.lending_club_bias.split) –

**Attributes:**

- [**current_path**](#validmind.datasets.credit_risk.lending_club_bias.current_path) –
- [**data_file**](#validmind.datasets.credit_risk.lending_club_bias.data_file) –
- [**dataset_path**](#validmind.datasets.credit_risk.lending_club_bias.dataset_path) –
- [**drop_columns**](#validmind.datasets.credit_risk.lending_club_bias.drop_columns) –
- [**protected_classes**](#validmind.datasets.credit_risk.lending_club_bias.protected_classes) –
- [**score_params**](#validmind.datasets.credit_risk.lending_club_bias.score_params) –
- [**target_column**](#validmind.datasets.credit_risk.lending_club_bias.target_column) –

###### validmind.datasets.credit_risk.lending_club_bias.compute_scores

```python
compute_scores(probabilities)
```

###### validmind.datasets.credit_risk.lending_club_bias.current_path

```python
current_path = os.path.dirname(os.path.abspath(__file__))
```

###### validmind.datasets.credit_risk.lending_club_bias.data_file

```python
data_file = os.path.join(dataset_path, 'lending_club_biased.csv.gz')
```

###### validmind.datasets.credit_risk.lending_club_bias.dataset_path

```python
dataset_path = os.path.join(current_path, 'datasets')
```

###### validmind.datasets.credit_risk.lending_club_bias.drop_columns

```python
drop_columns = ['total_pymnt', 'id', 'verification_status', 'purpose']
```

###### validmind.datasets.credit_risk.lending_club_bias.load_data

```python
load_data()
```

Load data from the specified CSV file.

:return: DataFrame containing the loaded data.

###### validmind.datasets.credit_risk.lending_club_bias.preprocess

```python
preprocess(df)
```

###### validmind.datasets.credit_risk.lending_club_bias.protected_classes

```python
protected_classes = ['Gender', 'Race', 'Marital_Status']
```

###### validmind.datasets.credit_risk.lending_club_bias.score_params

```python
score_params = {'target_score': 600, 'target_odds': 50, 'pdo': 20}
```

###### validmind.datasets.credit_risk.lending_club_bias.split

```python
split(df, test_size=0.3)
```

###### validmind.datasets.credit_risk.lending_club_bias.target_column

```python
target_column = 'loan_status'
```

#### validmind.datasets.nlp

Example datasets that can be used with the ValidMind Library.

**Modules:**

- [**cnn_dailymail**](#validmind.datasets.nlp.cnn_dailymail) –
- [**twitter_covid_19**](#validmind.datasets.nlp.twitter_covid_19) –

##### validmind.datasets.nlp.cnn_dailymail

**Functions:**

- [**display_nice**](#validmind.datasets.nlp.cnn_dailymail.display_nice) – Primary function to format and display a DataFrame.
- [**load_data**](#validmind.datasets.nlp.cnn_dailymail.load_data) – Load data from either online source or offline files.

**Attributes:**

- [**bert_embedding_prediction_column**](#validmind.datasets.nlp.cnn_dailymail.bert_embedding_prediction_column) –
- [**current_path**](#validmind.datasets.nlp.cnn_dailymail.current_path) –
- [**dataset_path**](#validmind.datasets.nlp.cnn_dailymail.dataset_path) –
- [**gpt_35_prediction_column**](#validmind.datasets.nlp.cnn_dailymail.gpt_35_prediction_column) –
- [**t5_prediction**](#validmind.datasets.nlp.cnn_dailymail.t5_prediction) –
- [**target_column**](#validmind.datasets.nlp.cnn_dailymail.target_column) –
- [**text_column**](#validmind.datasets.nlp.cnn_dailymail.text_column) –

###### validmind.datasets.nlp.cnn_dailymail.bert_embedding_prediction_column

```python
bert_embedding_prediction_column = 'bert_embedding_model_prediction'
```

###### validmind.datasets.nlp.cnn_dailymail.current_path

```python
current_path = os.path.dirname(os.path.abspath(__file__))
```

###### validmind.datasets.nlp.cnn_dailymail.dataset_path

```python
dataset_path = os.path.join(current_path, 'datasets')
```

###### validmind.datasets.nlp.cnn_dailymail.display_nice

```python
display_nice(df, num_rows=None)
```

Primary function to format and display a DataFrame.

###### validmind.datasets.nlp.cnn_dailymail.gpt_35_prediction_column

```python
gpt_35_prediction_column = 'gpt_35_prediction'
```

###### validmind.datasets.nlp.cnn_dailymail.load_data

```python
load_data(source='online', dataset_size=None)
```

Load data from either online source or offline files.

:param source: 'online' for online data, 'offline' for offline data. Defaults to 'online'.
:param dataset_size: Applicable if source is 'offline'. '300k' or '500k' for dataset size. Defaults to None.
:return: DataFrame containing the loaded data.

###### validmind.datasets.nlp.cnn_dailymail.t5_prediction

```python
t5_prediction = 't5_prediction'
```

###### validmind.datasets.nlp.cnn_dailymail.target_column

```python
target_column = 'highlights'
```

###### validmind.datasets.nlp.cnn_dailymail.text_column

```python
text_column = 'article'
```

##### validmind.datasets.nlp.twitter_covid_19

**Functions:**

- [**load_data**](#validmind.datasets.nlp.twitter_covid_19.load_data) –

**Attributes:**

- [**current_path**](#validmind.datasets.nlp.twitter_covid_19.current_path) –
- [**dataset_path**](#validmind.datasets.nlp.twitter_covid_19.dataset_path) –
- [**drop_columns**](#validmind.datasets.nlp.twitter_covid_19.drop_columns) –
- [**target_column**](#validmind.datasets.nlp.twitter_covid_19.target_column) –

###### validmind.datasets.nlp.twitter_covid_19.current_path

```python
current_path = os.path.dirname(os.path.abspath(__file__))
```

###### validmind.datasets.nlp.twitter_covid_19.dataset_path

```python
dataset_path = os.path.join(current_path, 'datasets')
```

###### validmind.datasets.nlp.twitter_covid_19.drop_columns

```python
drop_columns = ['UserName', 'ScreenName', 'Location', 'TweetAt']
```

###### validmind.datasets.nlp.twitter_covid_19.load_data

```python
load_data(full_dataset=False)
```

###### validmind.datasets.nlp.twitter_covid_19.target_column

```python
target_column = 'Sentiment'
```

#### validmind.datasets.regression

Entrypoint for regression datasets

**Modules:**

- [**california_housing**](#validmind.datasets.regression.california_housing) –
- [**fred**](#validmind.datasets.regression.fred) –
- [**fred_timeseries**](#validmind.datasets.regression.fred_timeseries) –
- [**lending_club**](#validmind.datasets.regression.lending_club) –

##### validmind.datasets.regression.california_housing

**Functions:**

- [**load_data**](#validmind.datasets.regression.california_housing.load_data) –
- [**preprocess**](#validmind.datasets.regression.california_housing.preprocess) –

**Attributes:**

- [**current_path**](#validmind.datasets.regression.california_housing.current_path) –
- [**dataset_path**](#validmind.datasets.regression.california_housing.dataset_path) –
- [**feature_columns**](#validmind.datasets.regression.california_housing.feature_columns) –
- [**target_column**](#validmind.datasets.regression.california_housing.target_column) –

###### validmind.datasets.regression.california_housing.current_path

```python
current_path = os.path.dirname(os.path.abspath(__file__))
```

###### validmind.datasets.regression.california_housing.dataset_path

```python
dataset_path = os.path.join(current_path, 'datasets')
```

###### validmind.datasets.regression.california_housing.feature_columns

```python
feature_columns = [
    "HouseAge",
    "AveRooms",
    "AveBedrms",
    "Population",
    "AveOccup",
]

```

###### validmind.datasets.regression.california_housing.load_data

```python
load_data(full_dataset=False)
```

###### validmind.datasets.regression.california_housing.preprocess

```python
preprocess(df)
```

###### validmind.datasets.regression.california_housing.target_column

```python
target_column = 'MedHouseVal'
```

##### validmind.datasets.regression.fred

**Functions:**

- [**load_all_data**](#validmind.datasets.regression.fred.load_all_data) –
- [**load_data**](#validmind.datasets.regression.fred.load_data) –
- [**load_model**](#validmind.datasets.regression.fred.load_model) –
- [**load_processed_data**](#validmind.datasets.regression.fred.load_processed_data) –
- [**load_test_dataset**](#validmind.datasets.regression.fred.load_test_dataset) –
- [**load_train_dataset**](#validmind.datasets.regression.fred.load_train_dataset) –
- [**preprocess**](#validmind.datasets.regression.fred.preprocess) – Split a time series DataFrame into train, validation, and test sets.
- [**transform**](#validmind.datasets.regression.fred.transform) –

**Attributes:**

- [**current_path**](#validmind.datasets.regression.fred.current_path) –
- [**dataset_path**](#validmind.datasets.regression.fred.dataset_path) –
- [**feature_columns**](#validmind.datasets.regression.fred.feature_columns) –
- [**fred_files_path**](#validmind.datasets.regression.fred.fred_files_path) –
- [**frequency**](#validmind.datasets.regression.fred.frequency) –
- [**models_path**](#validmind.datasets.regression.fred.models_path) –
- [**split_option**](#validmind.datasets.regression.fred.split_option) –
- [**target_column**](#validmind.datasets.regression.fred.target_column) –
- [**transform_func**](#validmind.datasets.regression.fred.transform_func) –

###### validmind.datasets.regression.fred.current_path

```python
current_path = os.path.dirname(os.path.abspath(__file__))
```

###### validmind.datasets.regression.fred.dataset_path

```python
dataset_path = os.path.join(current_path, 'datasets')
```

###### validmind.datasets.regression.fred.feature_columns

```python
feature_columns = ['FEDFUNDS', 'GS10', 'UNRATE']
```

###### validmind.datasets.regression.fred.fred_files_path

```python
fred_files_path = os.path.join(current_path, 'datasets', 'fred')
```

###### validmind.datasets.regression.fred.frequency

```python
frequency = 'MS'
```

###### validmind.datasets.regression.fred.load_all_data

```python
load_all_data()
```

###### validmind.datasets.regression.fred.load_data

```python
load_data()
```

###### validmind.datasets.regression.fred.load_model

```python
load_model(model_name)
```

###### validmind.datasets.regression.fred.load_processed_data

```python
load_processed_data()
```

###### validmind.datasets.regression.fred.load_test_dataset

```python
load_test_dataset(model_name)
```

###### validmind.datasets.regression.fred.load_train_dataset

```python
load_train_dataset(model_path)
```

###### validmind.datasets.regression.fred.models_path

```python
models_path = os.path.join(current_path, 'models')
```

###### validmind.datasets.regression.fred.preprocess

```python
preprocess(df, split_option='train_test_val', train_size=0.6, test_size=0.2)
```

Split a time series DataFrame into train, validation, and test sets.

**Parameters:**

- **df** (<code>[DataFrame](#pandas.DataFrame)</code>) – The time series DataFrame to be split.
- **split_option** (<code>[str](#str)</code>) – The split option to choose from: 'train_test_val' (default) or 'train_test'.
- **train_size** (<code>[float](#float)</code>) – The proportion of the dataset to include in the training set. Default is 0.6.
- **test_size** (<code>[float](#float)</code>) – The proportion of the dataset to include in the test set. Default is 0.2.

**Returns:**

- **train_df** (<code>[DataFrame](#pandas.DataFrame)</code>) – The training set.
- **validation_df** (<code>[DataFrame](#pandas.DataFrame)</code>) – The validation set (only returned if split_option is 'train_test_val').
- **test_df** (<code>[DataFrame](#pandas.DataFrame)</code>) – The test set.

###### validmind.datasets.regression.fred.split_option

```python
split_option = 'train_test'
```

###### validmind.datasets.regression.fred.target_column

```python
target_column = 'MORTGAGE30US'
```

###### validmind.datasets.regression.fred.transform

```python
transform(df, transform_func='diff')
```

###### validmind.datasets.regression.fred.transform_func

```python
transform_func = 'diff'
```

##### validmind.datasets.regression.fred_timeseries

**Functions:**

- [**align_date_range**](#validmind.datasets.regression.fred_timeseries.align_date_range) –
- [**convert_to_levels**](#validmind.datasets.regression.fred_timeseries.convert_to_levels) – Convert differenced data back to original levels.
- [**get_common_date_range**](#validmind.datasets.regression.fred_timeseries.get_common_date_range) –
- [**get_demo_test_config**](#validmind.datasets.regression.fred_timeseries.get_demo_test_config) –
- [**load_data**](#validmind.datasets.regression.fred_timeseries.load_data) –

**Attributes:**

- [**current_path**](#validmind.datasets.regression.fred_timeseries.current_path) –
- [**feature_columns**](#validmind.datasets.regression.fred_timeseries.feature_columns) –
- [**fedfunds_path**](#validmind.datasets.regression.fred_timeseries.fedfunds_path) –
- [**gs10_path**](#validmind.datasets.regression.fred_timeseries.gs10_path) –
- [**mortgage30us_path**](#validmind.datasets.regression.fred_timeseries.mortgage30us_path) –
- [**target_column**](#validmind.datasets.regression.fred_timeseries.target_column) –
- [**unrate_path**](#validmind.datasets.regression.fred_timeseries.unrate_path) –

###### validmind.datasets.regression.fred_timeseries.align_date_range

```python
align_date_range(dfs, start_date, end_date)
```

###### validmind.datasets.regression.fred_timeseries.convert_to_levels

```python
convert_to_levels(diff_df, original_df, target_column)
```

Convert differenced data back to original levels.

###### validmind.datasets.regression.fred_timeseries.current_path

```python
current_path = os.path.dirname(os.path.abspath(__file__))
```

###### validmind.datasets.regression.fred_timeseries.feature_columns

```python
feature_columns = ['FEDFUNDS', 'GS10', 'UNRATE']
```

###### validmind.datasets.regression.fred_timeseries.fedfunds_path

```python
fedfunds_path = os.path.join(current_path, 'datasets', 'fred', 'FEDFUNDS.csv')
```

###### validmind.datasets.regression.fred_timeseries.get_common_date_range

```python
get_common_date_range(dfs)
```

###### validmind.datasets.regression.fred_timeseries.get_demo_test_config

```python
get_demo_test_config()
```

###### validmind.datasets.regression.fred_timeseries.gs10_path

```python
gs10_path = os.path.join(current_path, 'datasets', 'fred', 'GS10.csv')
```

###### validmind.datasets.regression.fred_timeseries.load_data

```python
load_data()
```

###### validmind.datasets.regression.fred_timeseries.mortgage30us_path

```python
mortgage30us_path = os.path.join(
    current_path, "datasets", "fred", "MORTGAGE30US.csv"
)

```

###### validmind.datasets.regression.fred_timeseries.target_column

```python
target_column = 'MORTGAGE30US'
```

###### validmind.datasets.regression.fred_timeseries.unrate_path

```python
unrate_path = os.path.join(current_path, 'datasets', 'fred', 'UNRATE.csv')
```

##### validmind.datasets.regression.lending_club

**Functions:**

- [**load_data**](#validmind.datasets.regression.lending_club.load_data) –
- [**preprocess**](#validmind.datasets.regression.lending_club.preprocess) – Split a time series DataFrame into train, validation, and test sets.
- [**transform**](#validmind.datasets.regression.lending_club.transform) –

**Attributes:**

- [**current_path**](#validmind.datasets.regression.lending_club.current_path) –
- [**dataset_path**](#validmind.datasets.regression.lending_club.dataset_path) –
- [**feature_columns**](#validmind.datasets.regression.lending_club.feature_columns) –
- [**frequency**](#validmind.datasets.regression.lending_club.frequency) –
- [**split_option**](#validmind.datasets.regression.lending_club.split_option) –
- [**target_column**](#validmind.datasets.regression.lending_club.target_column) –

###### validmind.datasets.regression.lending_club.current_path

```python
current_path = os.path.dirname(os.path.abspath(__file__))
```

###### validmind.datasets.regression.lending_club.dataset_path

```python
dataset_path = os.path.join(
    current_path, "..", "..", "..", "notebooks", "datasets", "time_series"
)

```

###### validmind.datasets.regression.lending_club.feature_columns

```python
feature_columns = ['loan_rate_B', 'loan_rate_C', 'loan_rate_D']
```

###### validmind.datasets.regression.lending_club.frequency

```python
frequency = 'MS'
```

###### validmind.datasets.regression.lending_club.load_data

```python
load_data()
```

###### validmind.datasets.regression.lending_club.preprocess

```python
preprocess(df, split_option='train_test_val', train_size=0.6, test_size=0.2)
```

Split a time series DataFrame into train, validation, and test sets.

**Parameters:**

- **df** (<code>[DataFrame](#pandas.DataFrame)</code>) – The time series DataFrame to be split.
- **split_option** (<code>[str](#str)</code>) – The split option to choose from: 'train_test_val' (default) or 'train_test'.
- **train_size** (<code>[float](#float)</code>) – The proportion of the dataset to include in the training set. Default is 0.6.
- **test_size** (<code>[float](#float)</code>) – The proportion of the dataset to include in the test set. Default is 0.2.

**Returns:**

- **train_df** (<code>[DataFrame](#pandas.DataFrame)</code>) – The training set.
- **validation_df** (<code>[DataFrame](#pandas.DataFrame)</code>) – The validation set (only returned if split_option is 'train_test_val').
- **test_df** (<code>[DataFrame](#pandas.DataFrame)</code>) – The test set.

###### validmind.datasets.regression.lending_club.split_option

```python
split_option = 'train_test'
```

###### validmind.datasets.regression.lending_club.target_column

```python
target_column = ['loan_rate_A']
```

###### validmind.datasets.regression.lending_club.transform

```python
transform(df, transform_func='diff')
```

### validmind.errors

This module contains all the custom errors that are used in the ValidMind Library.

The following base errors are defined for others:

- BaseError
- APIRequestError

**Classes:**

- [**APIRequestError**](#validmind.errors.APIRequestError) – Generic error for API request errors that are not known.
- [**BaseError**](#validmind.errors.BaseError) –
- [**GetTestSuiteError**](#validmind.errors.GetTestSuiteError) – When the test suite could not be found.
- [**InitializeTestSuiteError**](#validmind.errors.InitializeTestSuiteError) – When the test suite was found but could not be initialized.
- [**InvalidAPICredentialsError**](#validmind.errors.InvalidAPICredentialsError) –
- [**InvalidContentIdPrefixError**](#validmind.errors.InvalidContentIdPrefixError) – When an invalid text content_id is sent to the API.
- [**InvalidInputError**](#validmind.errors.InvalidInputError) – When an invalid input object.
- [**InvalidMetricResultsError**](#validmind.errors.InvalidMetricResultsError) – When an invalid metric results object is sent to the API.
- [**InvalidProjectError**](#validmind.errors.InvalidProjectError) –
- [**InvalidRequestBodyError**](#validmind.errors.InvalidRequestBodyError) – When a POST/PUT request is made with an invalid request body.
- [**InvalidTestParametersError**](#validmind.errors.InvalidTestParametersError) – When an invalid parameters for the test.
- [**InvalidTestResultsError**](#validmind.errors.InvalidTestResultsError) – When an invalid test results object is sent to the API.
- [**InvalidTextObjectError**](#validmind.errors.InvalidTextObjectError) – When an invalid Metadat (Text) object is sent to the API.
- [**InvalidValueFormatterError**](#validmind.errors.InvalidValueFormatterError) – When an invalid value formatter is provided when serializing results.
- [**InvalidXGBoostTrainedModelError**](#validmind.errors.InvalidXGBoostTrainedModelError) – When an invalid XGBoost trained model is used when calling init_r_model.
- [**LoadTestError**](#validmind.errors.LoadTestError) – Exception raised when an error occurs while loading a test
- [**MismatchingClassLabelsError**](#validmind.errors.MismatchingClassLabelsError) – When the class labels found in the dataset don't match the provided target labels.
- [**MissingAPICredentialsError**](#validmind.errors.MissingAPICredentialsError) –
- [**MissingCacheResultsArgumentsError**](#validmind.errors.MissingCacheResultsArgumentsError) – When the cache_results function is missing arguments.
- [**MissingClassLabelError**](#validmind.errors.MissingClassLabelError) – When the one or more class labels are missing from provided dataset targets.
- [**MissingDependencyError**](#validmind.errors.MissingDependencyError) – When a required dependency is missing.
- [**MissingDocumentationTemplate**](#validmind.errors.MissingDocumentationTemplate) – When the client config is missing the documentation template.
- [**MissingModelIdError**](#validmind.errors.MissingModelIdError) –
- [**MissingOrInvalidModelPredictFnError**](#validmind.errors.MissingOrInvalidModelPredictFnError) – When the pytorch model is missing a predict function or its predict
- [**MissingRExtrasError**](#validmind.errors.MissingRExtrasError) – When the R extras have not been installed.
- [**MissingRequiredTestInputError**](#validmind.errors.MissingRequiredTestInputError) – When a required test context variable is missing.
- [**MissingTextContentIdError**](#validmind.errors.MissingTextContentIdError) – When a Text object is sent to the API without a content_id.
- [**MissingTextContentsError**](#validmind.errors.MissingTextContentsError) – When a Text object is sent to the API without a "text" attribute.
- [**SkipTestError**](#validmind.errors.SkipTestError) – Useful error to throw when a test cannot be executed.
- [**TestInputInvalidDatasetError**](#validmind.errors.TestInputInvalidDatasetError) – When an invalid dataset is used in a test context.
- [**UnsupportedColumnTypeError**](#validmind.errors.UnsupportedColumnTypeError) – When an unsupported column type is found on a dataset.
- [**UnsupportedDatasetError**](#validmind.errors.UnsupportedDatasetError) – When an unsupported dataset is used.
- [**UnsupportedFigureError**](#validmind.errors.UnsupportedFigureError) – When an unsupported figure object is constructed.
- [**UnsupportedModelError**](#validmind.errors.UnsupportedModelError) – When an unsupported model is used.
- [**UnsupportedModelForSHAPError**](#validmind.errors.UnsupportedModelForSHAPError) – When an unsupported model is used for SHAP importance.
- [**UnsupportedRModelError**](#validmind.errors.UnsupportedRModelError) – When an unsupported R model is used.

**Functions:**

- [**raise_api_error**](#validmind.errors.raise_api_error) – Safely try to parse JSON from the response message in case the API
- [**should_raise_on_fail_fast**](#validmind.errors.should_raise_on_fail_fast) – Determine whether an error should be raised when fail_fast is True.

#### validmind.errors.APIRequestError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

Generic error for API request errors that are not known.

**Functions:**

- [**description**](#validmind.errors.APIRequestError.description) –

**Attributes:**

- [**message**](#validmind.errors.APIRequestError.message) –

#### validmind.errors.BaseError

```python
BaseError(message='')
```

Bases: <code>[Exception](#Exception)</code>

**Functions:**

- [**description**](#validmind.errors.BaseError.description) –

**Attributes:**

- [**message**](#validmind.errors.BaseError.message) –

##### validmind.errors.BaseError.description

```python
description(*args, **kwargs)
```

##### validmind.errors.BaseError.message

```python
message = message
```

#### validmind.errors.GetTestSuiteError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When the test suite could not be found.

**Functions:**

- [**description**](#validmind.errors.GetTestSuiteError.description) –

**Attributes:**

- [**message**](#validmind.errors.GetTestSuiteError.message) –

#### validmind.errors.InitializeTestSuiteError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When the test suite was found but could not be initialized.

**Functions:**

- [**description**](#validmind.errors.InitializeTestSuiteError.description) –

**Attributes:**

- [**message**](#validmind.errors.InitializeTestSuiteError.message) –

#### validmind.errors.InvalidAPICredentialsError

Bases: <code>[APIRequestError](#validmind.errors.APIRequestError)</code>

**Functions:**

- [**description**](#validmind.errors.InvalidAPICredentialsError.description) –

**Attributes:**

- [**message**](#validmind.errors.InvalidAPICredentialsError.message) –

##### validmind.errors.InvalidAPICredentialsError.description

```python
description(*args, **kwargs)
```

##### validmind.errors.InvalidAPICredentialsError.message

```python
message = message
```

#### validmind.errors.InvalidContentIdPrefixError

Bases: <code>[APIRequestError](#validmind.errors.APIRequestError)</code>

When an invalid text content_id is sent to the API.

**Functions:**

- [**description**](#validmind.errors.InvalidContentIdPrefixError.description) –

**Attributes:**

- [**message**](#validmind.errors.InvalidContentIdPrefixError.message) –

#### validmind.errors.InvalidInputError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When an invalid input object.

**Functions:**

- [**description**](#validmind.errors.InvalidInputError.description) –

**Attributes:**

- [**message**](#validmind.errors.InvalidInputError.message) –

#### validmind.errors.InvalidMetricResultsError

Bases: <code>[APIRequestError](#validmind.errors.APIRequestError)</code>

When an invalid metric results object is sent to the API.

**Functions:**

- [**description**](#validmind.errors.InvalidMetricResultsError.description) –

**Attributes:**

- [**message**](#validmind.errors.InvalidMetricResultsError.message) –

#### validmind.errors.InvalidProjectError

Bases: <code>[APIRequestError](#validmind.errors.APIRequestError)</code>

**Functions:**

- [**description**](#validmind.errors.InvalidProjectError.description) –

**Attributes:**

- [**message**](#validmind.errors.InvalidProjectError.message) –

##### validmind.errors.InvalidProjectError.description

```python
description(*args, **kwargs)
```

##### validmind.errors.InvalidProjectError.message

```python
message = message
```

#### validmind.errors.InvalidRequestBodyError

Bases: <code>[APIRequestError](#validmind.errors.APIRequestError)</code>

When a POST/PUT request is made with an invalid request body.

**Functions:**

- [**description**](#validmind.errors.InvalidRequestBodyError.description) –

**Attributes:**

- [**message**](#validmind.errors.InvalidRequestBodyError.message) –

#### validmind.errors.InvalidTestParametersError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When an invalid parameters for the test.

**Functions:**

- [**description**](#validmind.errors.InvalidTestParametersError.description) –

**Attributes:**

- [**message**](#validmind.errors.InvalidTestParametersError.message) –

#### validmind.errors.InvalidTestResultsError

Bases: <code>[APIRequestError](#validmind.errors.APIRequestError)</code>

When an invalid test results object is sent to the API.

**Functions:**

- [**description**](#validmind.errors.InvalidTestResultsError.description) –

**Attributes:**

- [**message**](#validmind.errors.InvalidTestResultsError.message) –

#### validmind.errors.InvalidTextObjectError

Bases: <code>[APIRequestError](#validmind.errors.APIRequestError)</code>

When an invalid Metadat (Text) object is sent to the API.

**Functions:**

- [**description**](#validmind.errors.InvalidTextObjectError.description) –

**Attributes:**

- [**message**](#validmind.errors.InvalidTextObjectError.message) –

#### validmind.errors.InvalidValueFormatterError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When an invalid value formatter is provided when serializing results.

**Functions:**

- [**description**](#validmind.errors.InvalidValueFormatterError.description) –

**Attributes:**

- [**message**](#validmind.errors.InvalidValueFormatterError.message) –

#### validmind.errors.InvalidXGBoostTrainedModelError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When an invalid XGBoost trained model is used when calling init_r_model.

**Functions:**

- [**description**](#validmind.errors.InvalidXGBoostTrainedModelError.description) –

**Attributes:**

- [**message**](#validmind.errors.InvalidXGBoostTrainedModelError.message) –

#### validmind.errors.LoadTestError

```python
LoadTestError(message, original_error=None)
```

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

Exception raised when an error occurs while loading a test

**Functions:**

- [**description**](#validmind.errors.LoadTestError.description) –

**Attributes:**

- [**message**](#validmind.errors.LoadTestError.message) –
- [**original_error**](#validmind.errors.LoadTestError.original_error) –

##### validmind.errors.LoadTestError.description

```python
description(*args, **kwargs)
```

##### validmind.errors.LoadTestError.message

```python
message = message
```

##### validmind.errors.LoadTestError.original_error

```python
original_error = original_error
```

#### validmind.errors.MismatchingClassLabelsError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When the class labels found in the dataset don't match the provided target labels.

**Functions:**

- [**description**](#validmind.errors.MismatchingClassLabelsError.description) –

**Attributes:**

- [**message**](#validmind.errors.MismatchingClassLabelsError.message) –

#### validmind.errors.MissingAPICredentialsError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

**Functions:**

- [**description**](#validmind.errors.MissingAPICredentialsError.description) –

**Attributes:**

- [**message**](#validmind.errors.MissingAPICredentialsError.message) –

##### validmind.errors.MissingAPICredentialsError.description

```python
description(*args, **kwargs)
```

##### validmind.errors.MissingAPICredentialsError.message

```python
message = message
```

#### validmind.errors.MissingCacheResultsArgumentsError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When the cache_results function is missing arguments.

**Functions:**

- [**description**](#validmind.errors.MissingCacheResultsArgumentsError.description) –

**Attributes:**

- [**message**](#validmind.errors.MissingCacheResultsArgumentsError.message) –

#### validmind.errors.MissingClassLabelError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When the one or more class labels are missing from provided dataset targets.

**Functions:**

- [**description**](#validmind.errors.MissingClassLabelError.description) –

**Attributes:**

- [**message**](#validmind.errors.MissingClassLabelError.message) –

#### validmind.errors.MissingDependencyError

```python
MissingDependencyError(message='', required_dependencies=None, extra=None)
```

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When a required dependency is missing.

**Functions:**

- [**description**](#validmind.errors.MissingDependencyError.description) –

**Attributes:**

- [**extra**](#validmind.errors.MissingDependencyError.extra) –
- [**message**](#validmind.errors.MissingDependencyError.message) –
- [**required_dependencies**](#validmind.errors.MissingDependencyError.required_dependencies) –

**Parameters:**

- **message** (<code>[str](#str)</code>) – The error message.
- **required_dependencies** (<code>[list](#list)</code>) – A list of required dependencies.
- **extra** (<code>[str](#str)</code>) – The particular validmind `extra` that will install the missing dependencies.

##### validmind.errors.MissingDependencyError.description

```python
description(*args, **kwargs)
```

##### validmind.errors.MissingDependencyError.extra

```python
extra = extra
```

##### validmind.errors.MissingDependencyError.message

```python
message = message
```

##### validmind.errors.MissingDependencyError.required_dependencies

```python
required_dependencies = required_dependencies or []
```

#### validmind.errors.MissingDocumentationTemplate

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When the client config is missing the documentation template.

**Functions:**

- [**description**](#validmind.errors.MissingDocumentationTemplate.description) –

**Attributes:**

- [**message**](#validmind.errors.MissingDocumentationTemplate.message) –

#### validmind.errors.MissingModelIdError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

**Functions:**

- [**description**](#validmind.errors.MissingModelIdError.description) –

**Attributes:**

- [**message**](#validmind.errors.MissingModelIdError.message) –

##### validmind.errors.MissingModelIdError.description

```python
description(*args, **kwargs)
```

##### validmind.errors.MissingModelIdError.message

```python
message = message
```

#### validmind.errors.MissingOrInvalidModelPredictFnError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When the pytorch model is missing a predict function or its predict
method does not have the expected arguments.

**Functions:**

- [**description**](#validmind.errors.MissingOrInvalidModelPredictFnError.description) –

**Attributes:**

- [**message**](#validmind.errors.MissingOrInvalidModelPredictFnError.message) –

#### validmind.errors.MissingRExtrasError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When the R extras have not been installed.

**Functions:**

- [**description**](#validmind.errors.MissingRExtrasError.description) –

**Attributes:**

- [**message**](#validmind.errors.MissingRExtrasError.message) –

##### validmind.errors.MissingRExtrasError.description

```python
description(*args, **kwargs)
```

##### validmind.errors.MissingRExtrasError.message

```python
message = message
```

#### validmind.errors.MissingRequiredTestInputError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When a required test context variable is missing.

**Functions:**

- [**description**](#validmind.errors.MissingRequiredTestInputError.description) –

**Attributes:**

- [**message**](#validmind.errors.MissingRequiredTestInputError.message) –

#### validmind.errors.MissingTextContentIdError

Bases: <code>[APIRequestError](#validmind.errors.APIRequestError)</code>

When a Text object is sent to the API without a content_id.

**Functions:**

- [**description**](#validmind.errors.MissingTextContentIdError.description) –

**Attributes:**

- [**message**](#validmind.errors.MissingTextContentIdError.message) –

#### validmind.errors.MissingTextContentsError

Bases: <code>[APIRequestError](#validmind.errors.APIRequestError)</code>

When a Text object is sent to the API without a "text" attribute.

**Functions:**

- [**description**](#validmind.errors.MissingTextContentsError.description) –

**Attributes:**

- [**message**](#validmind.errors.MissingTextContentsError.message) –

#### validmind.errors.SkipTestError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

Useful error to throw when a test cannot be executed.

**Functions:**

- [**description**](#validmind.errors.SkipTestError.description) –

**Attributes:**

- [**message**](#validmind.errors.SkipTestError.message) –

#### validmind.errors.TestInputInvalidDatasetError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When an invalid dataset is used in a test context.

**Functions:**

- [**description**](#validmind.errors.TestInputInvalidDatasetError.description) –

**Attributes:**

- [**message**](#validmind.errors.TestInputInvalidDatasetError.message) –

#### validmind.errors.UnsupportedColumnTypeError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When an unsupported column type is found on a dataset.

**Functions:**

- [**description**](#validmind.errors.UnsupportedColumnTypeError.description) –

**Attributes:**

- [**message**](#validmind.errors.UnsupportedColumnTypeError.message) –

#### validmind.errors.UnsupportedDatasetError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When an unsupported dataset is used.

**Functions:**

- [**description**](#validmind.errors.UnsupportedDatasetError.description) –

**Attributes:**

- [**message**](#validmind.errors.UnsupportedDatasetError.message) –

#### validmind.errors.UnsupportedFigureError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When an unsupported figure object is constructed.

**Functions:**

- [**description**](#validmind.errors.UnsupportedFigureError.description) –

**Attributes:**

- [**message**](#validmind.errors.UnsupportedFigureError.message) –

#### validmind.errors.UnsupportedModelError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When an unsupported model is used.

**Functions:**

- [**description**](#validmind.errors.UnsupportedModelError.description) –

**Attributes:**

- [**message**](#validmind.errors.UnsupportedModelError.message) –

#### validmind.errors.UnsupportedModelForSHAPError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When an unsupported model is used for SHAP importance.

**Functions:**

- [**description**](#validmind.errors.UnsupportedModelForSHAPError.description) –

**Attributes:**

- [**message**](#validmind.errors.UnsupportedModelForSHAPError.message) –

#### validmind.errors.UnsupportedRModelError

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

When an unsupported R model is used.

**Functions:**

- [**description**](#validmind.errors.UnsupportedRModelError.description) –

**Attributes:**

- [**message**](#validmind.errors.UnsupportedRModelError.message) –

#### validmind.errors.raise_api_error

```python
raise_api_error(error_string)
```

Safely try to parse JSON from the response message in case the API
returns a non-JSON string or if the API returns a non-standard error

#### validmind.errors.should_raise_on_fail_fast

```python
should_raise_on_fail_fast(error)
```

Determine whether an error should be raised when fail_fast is True.

### validmind.get_test_suite

```python
get_test_suite(test_suite_id=None, section=None, *args, **kwargs)
```

Gets a TestSuite object for the current project or a specific test suite

This function provides an interface to retrieve the TestSuite instance for the
current project or a specific TestSuite instance identified by test_suite_id.
The project Test Suite will contain sections for every section in the project's
documentation template and these Test Suite Sections will contain all the tests
associated with that template section.

**Parameters:**

- **test_suite_id** (<code>[str](#str)</code>) – The test suite name. If not passed, then the
  project's test suite will be returned. Defaults to None.
- **section** (<code>[str](#str)</code>) – The section of the documentation template from which
  to retrieve the test suite. This only applies if test_suite_id is None.
  Defaults to None.
- **args** – Additional arguments to pass to the TestSuite
- **kwargs** – Additional keyword arguments to pass to the TestSuite

### validmind.html_templates

**Modules:**

- [**content_blocks**](#validmind.html_templates.content_blocks) –

#### validmind.html_templates.content_blocks

**Attributes:**

- [**failed_content_block_html**](#validmind.html_templates.content_blocks.failed_content_block_html) –
- [**math_jax_snippet**](#validmind.html_templates.content_blocks.math_jax_snippet) –
- [**non_test_content_block_html**](#validmind.html_templates.content_blocks.non_test_content_block_html) –
- [**python_syntax_highlighting**](#validmind.html_templates.content_blocks.python_syntax_highlighting) –
- [**test_content_block_html**](#validmind.html_templates.content_blocks.test_content_block_html) –

##### validmind.html_templates.content_blocks.failed_content_block_html

```python
failed_content_block_html = '\n<div\n  class="lm-Widget p-Widget jupyter-widget-Collapse-header"\n  style="padding: 6px; padding-left: 13px; font-size: 14px;"\n>\n  <span>❌ &nbsp;&nbsp;Failed to load test: \'{test_id}\'</span>\n</div>\n'

```

##### validmind.html_templates.content_blocks.math_jax_snippet

```python
math_jax_snippet = "\n<script>\nwindow.MathJax = {\n    tex2jax: {\n        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],\n        displayMath: [['$$', '$$'], ['\\[', '\\]']],\n        processEscapes: true,\n        skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],\n        ignoreClass: \".*\",\n        processClass: \"math\"\n    }\n};\nsetTimeout(function () {\n    var script = document.createElement('script');\n    script.type = 'text/javascript';\n    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS_HTML';\n    document.head.appendChild(script);\n}, 300);\n</script>\n"

```

##### validmind.html_templates.content_blocks.non_test_content_block_html

```python
non_test_content_block_html = '\n<div\n  class="lm-Widget p-Widget jupyter-widget-Collapse-header"\n  style="padding: 6px; padding-left: 33px; font-size: 14px"\n>\n  <span>{content_type} Block: \'{content_id}\'</i></span>\n</div>\n'

```

##### validmind.html_templates.content_blocks.python_syntax_highlighting

```python
python_syntax_highlighting = "\n<script defer type=\"module\">\nimport hljs from 'https://unpkg.com/@highlightjs/cdn-assets@11.9.0/es/highlight.min.js';\nimport python from 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/es/languages/python.min.js';\n\nhljs.registerLanguage('python', python);\nhljs.highlightAll();\n</script>\n"

```

##### validmind.html_templates.content_blocks.test_content_block_html

```python
test_content_block_html = '\n<div>\n  <h2>{title}</h2>\n  <div style="border: 1px solid #ddd; border-radius: 4px; padding: 10px; margin: 10px 0;">\n    {description}\n  </div>\n</div>\n\n<h4 class="vm_required_context">\n  Required Inputs: <span style="font-size: 13px"><i>{required_inputs}</i></span>\n</h4>\n\n<div style="display: {table_display};">\n  <h4>Parameters:</h4>\n  <table class="vm_params_table" style="display: {table_display};">\n      <tr>\n          <th>Parameter</th>\n          <th>Default Value</th>\n      </tr>\n      {params_table}\n  </table>\n</div>\n\n<div class="unset">\n  <h3>How to Run:</h3>\n\n  <button\n      onclick="(() => {{e = document.getElementById(\'expandable_instructions_{uuid}\'); e.style.display === \'none\' ? e.style.display = \'block\' : e.style.display = \'none\'}})()"\n  >Show/Hide Instructions</button>\n\n  <div id="expandable_instructions_{uuid}" style="display: {instructions_display};">\n  <h4>Code:</h4>\n    <pre>\n        <code class=\'language-python\'>\nimport validmind as vm\n\n# inputs dictionary maps your inputs to the expected input names\n# keys are the expected input names and values are the actual inputs\n# values may be string input_ids or the actual VMDataset or VMModel objects\ninputs = {example_inputs}\nparams = {example_params}\n\n# to run and view the result of this test, run the following code:\nresult = vm.tests.run_test(\n  "{test_id}", inputs=inputs, params=params\n)\n\n# To see the result of the test, ensure that you have called `vm.init()` and then run:\nresult.log()</code>\n    </pre>\n  </div>\n</div>\n\n<style>\nh5.vm_required_context {{\n    margin-top: 25px;\n}}\ntable.vm_params_table {{\n  margin-top: 20px;\n  width: 350px;\n  border-collapse: collapse;\n  border-color: --jp-border-color0;\n}}\ntable.vm_params_table td, table.vm_params_table th {{\n  text-align: right;\n}}\ntable.vm_params_table td:first-child, table.vm_params_table th:first-child {{\n  text-align: left;\n}}\ntable.vm_params_table th {{\n  background-color: --jp-content-color0;\n  font-weight: bold;\n  font-size: 14px !important;\n}}\ntable.vm_params_table tr:nth-child(even) {{\n  background-color: --jp-layout-color1;\n}}\ntable.vm_params_table tr:nth-child(odd) {{\n  background-color: --jp-layout-color2;\n}}\ntable.vm_params_table tr:hover {{\n  background-color: --jp-layout-color3;\n}}\ntable.vm_params_table td, table.vm_params_table th {{\n  padding: 5px;\n  border: .8px solid --jp-border-color0;\n}}\n</style>\n'

```

### validmind.init

```python
init(
    project=None,
    api_key=None,
    api_secret=None,
    api_host=None,
    model=None,
    monitoring=False,
)
```

Initializes the API client instances and calls the /ping endpoint to ensure
the provided credentials are valid and we can connect to the ValidMind API.

If the API key and secret are not provided, the client will attempt to
retrieve them from the environment variables `VM_API_KEY` and `VM_API_SECRET`.

**Parameters:**

- **project** (<code>[str](#str)</code>) – The project CUID. Alias for model. Defaults to None. [DEPRECATED]
- **model** (<code>[str](#str)</code>) – The model CUID. Defaults to None.
- **api_key** (<code>[str](#str)</code>) – The API key. Defaults to None.
- **api_secret** (<code>[str](#str)</code>) – The API secret. Defaults to None.
- **api_host** (<code>[str](#str)</code>) – The API host. Defaults to None.
- **monitoring** (<code>[bool](#bool)</code>) – The ongoing monitoring flag. Defaults to False.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If the API key and secret are not provided

### validmind.init_dataset

```python
init_dataset(
    dataset,
    model=None,
    index=None,
    index_name=None,
    date_time_index=False,
    columns=None,
    text_column=None,
    target_column=None,
    feature_columns=None,
    extra_columns=None,
    class_labels=None,
    type=None,
    input_id=None,
    __log=True,
)
```

Initializes a VM Dataset, which can then be passed to other functions
that can perform additional analysis and tests on the data. This function
also ensures we are reading a valid dataset type.

The following dataset types are supported:

- Pandas DataFrame
- Polars DataFrame
- Numpy ndarray
- Torch TensorDataset

**Parameters:**

- **dataset** – dataset from various python libraries
- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – ValidMind model object
- **targets** (<code>[DatasetTargets](#vm.vm.DatasetTargets)</code>) – A list of target variables
- **target_column** (<code>[str](#str)</code>) – The name of the target column in the dataset
- **feature_columns** (<code>[list](#list)</code>) – A list of names of feature columns in the dataset
- **extra_columns** (<code>[dictionary](#dictionary)</code>) – A dictionary containing the names of the
- **class_labels** (<code>[dict](#dict)</code>) – A list of class labels for classification problems
- **type** (<code>[str](#str)</code>) – The type of dataset (one of DATASET_TYPES)
- **input_id** (<code>[str](#str)</code>) – The input ID for the dataset (e.g. "my_dataset"). By default,
  this will be set to `dataset` but if you are passing this dataset as a
  test input using some other key than `dataset`, then you should set
  this to the same key.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If the dataset type is not supported

**Returns:**

- <code>[VMDataset](#validmind.vm_models.dataset.VMDataset)</code> – vm.vm.Dataset: A VM Dataset instance

### validmind.init_model

```python
init_model(
    model=None,
    input_id="model",
    attributes=None,
    predict_fn=None,
    __log=True,
    **kwargs
)
```

Initializes a VM Model, which can then be passed to other functions
that can perform additional analysis and tests on the data. This function
also ensures we are creating a model supported libraries.

**Parameters:**

- **model** (<code>[object](#object)</code>) – A trained model or VMModel instance
- **input_id** (<code>[str](#str)</code>) – The input ID for the model (e.g. "my_model"). By default,
  this will be set to `model` but if you are passing this model as a
  test input using some other key than `model`, then you should set
  this to the same key.
- **attributes** (<code>[dict](#dict)</code>) – A dictionary of model attributes
- **predict_fn** (<code>[callable](#callable)</code>) – A function that takes an input and returns a prediction
- \*\***kwargs** – Additional arguments to pass to the model

**Raises:**

- <code>[ValueError](#ValueError)</code> – If the model type is not supported

**Returns:**

- <code>[VMModel](#validmind.vm_models.model.VMModel)</code> – vm.VMModel: A VM Model instance

### validmind.init_r_model

```python
init_r_model(model_path, input_id='model')
```

Initializes a VM Model for an R model

R models must be saved to disk and the filetype depends on the model type...
Currently we support the following model types:

- LogisticRegression `glm` model in R: saved as an RDS file with `saveRDS`
- LinearRegression `lm` model in R: saved as an RDS file with `saveRDS`
- XGBClassifier: saved as a .json or .bin file with `xgb.save`
- XGBRegressor: saved as a .json or .bin file with `xgb.save`

LogisticRegression and LinearRegression models are converted to sklearn models by extracting
the coefficients and intercept from the R model. XGB models are loaded using the xgboost
since xgb models saved in .json or .bin format can be loaded directly with either Python or R

**Parameters:**

- **model_path** (<code>[str](#str)</code>) – The path to the R model saved as an RDS or XGB file
- **model_type** (<code>[str](#str)</code>) – The type of the model (one of R_MODEL_TYPES)

**Returns:**

- <code>[VMModel](#validmind.vm_models.model.VMModel)</code> – vm.vm.Model: A VM Model instance

### validmind.input_registry

Central class to register inputs

**Classes:**

- [**InputRegistry**](#validmind.input_registry.InputRegistry) –

**Attributes:**

- [**input_registry**](#validmind.input_registry.input_registry) –

#### validmind.input_registry.InputRegistry

```python
InputRegistry()
```

**Functions:**

- [**add**](#validmind.input_registry.InputRegistry.add) –
- [**get**](#validmind.input_registry.InputRegistry.get) –
- [**list_input_objects**](#validmind.input_registry.InputRegistry.list_input_objects) –

**Attributes:**

- [**registry**](#validmind.input_registry.InputRegistry.registry) –

##### validmind.input_registry.InputRegistry.add

```python
add(key, obj)
```

##### validmind.input_registry.InputRegistry.get

```python
get(key)
```

##### validmind.input_registry.InputRegistry.list_input_objects

```python
list_input_objects()
```

##### validmind.input_registry.InputRegistry.registry

```python
registry = {}
```

#### validmind.input_registry.input_registry

```python
input_registry = InputRegistry()
```

### validmind.log_metric

```python
log_metric(key, value, inputs=None, params=None, recorded_at=None)
```

Logs a unit metric

Unit metrics are key-value pairs where the key is the metric name and the value is
a scalar (int or float). These key-value pairs are associated with the currently
selected model (inventory model in the ValidMind Platform) and keys can be logged
to over time to create a history of the metric. On the ValidMind Platform, these metrics
will be used to create plots/visualizations for documentation and dashboards etc.

**Parameters:**

- **key** (<code>[str](#str)</code>) – The metric key
- **value** (<code>[float](#float)</code>) – The metric value
- **inputs** (<code>[list](#list)</code>) – A list of input IDs that were used to compute the metric.
- **params** (<code>[dict](#dict)</code>) – Dictionary of parameters used to compute the metric.
- **recorded_at** (<code>[str](#str)</code>) – The timestamp of the metric. Server will use
  current time if not provided.

### validmind.logging

ValidMind logging module.

**Functions:**

- [**get_logger**](#validmind.logging.get_logger) – Get a logger for the given module name
- [**init_sentry**](#validmind.logging.init_sentry) – Initialize Sentry SDK for sending logs back to ValidMind
- [**log_performance**](#validmind.logging.log_performance) – Decorator to log the time it takes to run a function
- [**log_performance_async**](#validmind.logging.log_performance_async) – Decorator to log the time it takes to run an async function
- [**send_single_error**](#validmind.logging.send_single_error) – Send a single error to Sentry

#### validmind.logging.get_logger

```python
get_logger(name='validmind', log_level=None)
```

Get a logger for the given module name

#### validmind.logging.init_sentry

```python
init_sentry(server_config)
```

Initialize Sentry SDK for sending logs back to ValidMind

This will usually only be called by the api_client module to initialize the
sentry connection after the user calls `validmind.init()`. This is because the DSN
and other config options will be returned by the API.

**Parameters:**

- **config** (<code>[dict](#dict)</code>) – The config dictionary returned by the API
- send_logs (bool): Whether to send logs to Sentry (gets removed)
- dsn (str): The Sentry DSN
  ...: Other config options for Sentry

#### validmind.logging.log_performance

```python
log_performance(name=None, logger=None, force=False)
```

Decorator to log the time it takes to run a function

**Parameters:**

- **name** (<code>[str](#str)</code>) – The name of the function. Defaults to None.
- **logger** (<code>[Logger](#logging.Logger)</code>) – The logger to use. Defaults to None.
- **force** (<code>[bool](#bool)</code>) – Whether to force logging even if env var is off

**Returns:**

- **function** – The decorated function

#### validmind.logging.log_performance_async

```python
log_performance_async(func, name=None, logger=None, force=False)
```

Decorator to log the time it takes to run an async function

**Parameters:**

- **func** (<code>[function](#function)</code>) – The function to decorate
- **name** (<code>[str](#str)</code>) – The name of the function. Defaults to None.
- **logger** (<code>[Logger](#logging.Logger)</code>) – The logger to use. Defaults to None.
- **force** (<code>[bool](#bool)</code>) – Whether to force logging even if env var is off

**Returns:**

- **function** – The decorated function

#### validmind.logging.send_single_error

```python
send_single_error(error)
```

Send a single error to Sentry

**Parameters:**

- **error** (<code>[Exception](#Exception)</code>) – The exception to send

### validmind.models

**Modules:**

- [**foundation**](#validmind.models.foundation) –
- [**function**](#validmind.models.function) –
- [**huggingface**](#validmind.models.huggingface) –
- [**metadata**](#validmind.models.metadata) –
- [**pipeline**](#validmind.models.pipeline) –
- [**pytorch**](#validmind.models.pytorch) –
- [**r_model**](#validmind.models.r_model) –
- [**sklearn**](#validmind.models.sklearn) –

**Classes:**

- [**CatBoostModel**](#validmind.models.CatBoostModel) – Wrapper for CatBoost model
- [**FoundationModel**](#validmind.models.FoundationModel) – FoundationModel class wraps a Foundation LLM endpoint
- [**FunctionModel**](#validmind.models.FunctionModel) – FunctionModel class wraps a user-defined predict function
- [**HFModel**](#validmind.models.HFModel) –
- [**MetadataModel**](#validmind.models.MetadataModel) – MetadataModel is designed to represent a model that is not available for inference
- [**PipelineModel**](#validmind.models.PipelineModel) – An base class that wraps a trained model instance and its associated data.
- [**Prompt**](#validmind.models.Prompt) –
- [**PyTorchModel**](#validmind.models.PyTorchModel) – PyTorchModel class wraps a PyTorch model
- [**SKlearnModel**](#validmind.models.SKlearnModel) –
- [**StatsModelsModel**](#validmind.models.StatsModelsModel) – Wrapper for StatsModels model
- [**XGBoostModel**](#validmind.models.XGBoostModel) – Wrapper for XGBoost model

#### validmind.models.CatBoostModel

Bases: <code>[SKlearnModel](#validmind.models.sklearn.SKlearnModel)</code>

Wrapper for CatBoost model

**Functions:**

- [**predict**](#validmind.models.CatBoostModel.predict) – Predict method for the model. This is a wrapper around the model's
- [**predict_proba**](#validmind.models.CatBoostModel.predict_proba) – predict_proba (for classification) or predict (for regression) method
- [**serialize**](#validmind.models.CatBoostModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.CatBoostModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.CatBoostModel.attributes) –
- [**class\_**](#validmind.models.CatBoostModel.class_) –
- [**input_id**](#validmind.models.CatBoostModel.input_id) –
- [**language**](#validmind.models.CatBoostModel.language) –
- [**library**](#validmind.models.CatBoostModel.library) –
- [**library_version**](#validmind.models.CatBoostModel.library_version) –
- [**model**](#validmind.models.CatBoostModel.model) –
- [**name**](#validmind.models.CatBoostModel.name) –

#### validmind.models.FoundationModel

Bases: <code>[FunctionModel](#validmind.models.function.FunctionModel)</code>

FoundationModel class wraps a Foundation LLM endpoint

This class wraps a predict function that is user-defined and adapts it to works
with ValidMind's model interface for the purpose of model eval and documentation

**Attributes:**

- [**predict_fn**](#validmind.models.FoundationModel.predict_fn) (<code>[callable](#callable)</code>) – The predict function that should take a prompt as input
  and return the result from the model
- [**prompt**](#validmind.models.FoundationModel.prompt) (<code>[Prompt](#validmind.models.foundation.Prompt)</code>) – The prompt object that defines the prompt template and the
  variables (if any)
- [**name**](#validmind.models.FoundationModel.name) (<code>[str](#str)</code>) – The name of the model. Defaults to name of the predict_fn

**Functions:**

- [**predict**](#validmind.models.FoundationModel.predict) – Predict method for the model. This is a wrapper around the model's
- [**predict_proba**](#validmind.models.FoundationModel.predict_proba) – Predict probabilties - must be implemented by subclass if needed
- [**serialize**](#validmind.models.FoundationModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.FoundationModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.FoundationModel.attributes) –
- [**class\_**](#validmind.models.FoundationModel.class_) –
- [**input_id**](#validmind.models.FoundationModel.input_id) –
- [**language**](#validmind.models.FoundationModel.language) –
- [**library**](#validmind.models.FoundationModel.library) –
- [**library_version**](#validmind.models.FoundationModel.library_version) –
- [**model**](#validmind.models.FoundationModel.model) –
- [**name**](#validmind.models.FoundationModel.name) –

##### validmind.models.FoundationModel.attributes

```python
attributes = attributes or ModelAttributes()
```

##### validmind.models.FoundationModel.class\_

```python
class_ = self.__class__.__name__
```

##### validmind.models.FoundationModel.input_id

```python
input_id = input_id
```

##### validmind.models.FoundationModel.language

```python
language = 'Python'
```

##### validmind.models.FoundationModel.library

```python
library = self.__class__.__name__
```

##### validmind.models.FoundationModel.library_version

```python
library_version = 'N/A'
```

##### validmind.models.FoundationModel.model

```python
model = model
```

##### validmind.models.FoundationModel.name

```python
name = name or self.__class__.__name__
```

##### validmind.models.FoundationModel.predict

```python
predict(X)
```

Predict method for the model. This is a wrapper around the model's

##### validmind.models.FoundationModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

Predict probabilties - must be implemented by subclass if needed

##### validmind.models.FoundationModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

##### validmind.models.FoundationModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

#### validmind.models.FunctionModel

Bases: <code>[VMModel](#validmind.vm_models.model.VMModel)</code>

FunctionModel class wraps a user-defined predict function

**Attributes:**

- [**predict_fn**](#validmind.models.FunctionModel.predict_fn) (<code>[callable](#callable)</code>) – The predict function that should take a dictionary of
  input features and return a prediction.
- [**input_id**](#validmind.models.FunctionModel.input_id) (<code>[str](#str)</code>) – The input ID for the model. Defaults to None.
- [**name**](#validmind.models.FunctionModel.name) (<code>[str](#str)</code>) – The name of the model. Defaults to the name of the predict_fn.
- [**prompt**](#validmind.models.FunctionModel.prompt) (<code>[Prompt](#validmind.models.foundation.Prompt)</code>) – If using a prompt, the prompt object that defines the template
  and the variables (if any). Defaults to None.

**Functions:**

- [**predict**](#validmind.models.FunctionModel.predict) – Compute predictions for the input (X)
- [**predict_proba**](#validmind.models.FunctionModel.predict_proba) – Predict probabilties - must be implemented by subclass if needed
- [**serialize**](#validmind.models.FunctionModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.FunctionModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.FunctionModel.attributes) –
- [**class\_**](#validmind.models.FunctionModel.class_) –
- [**input_id**](#validmind.models.FunctionModel.input_id) –
- [**language**](#validmind.models.FunctionModel.language) –
- [**library**](#validmind.models.FunctionModel.library) –
- [**library_version**](#validmind.models.FunctionModel.library_version) –
- [**model**](#validmind.models.FunctionModel.model) –
- [**name**](#validmind.models.FunctionModel.name) –

##### validmind.models.FunctionModel.attributes

```python
attributes = attributes or ModelAttributes()
```

##### validmind.models.FunctionModel.class\_

```python
class_ = self.__class__.__name__
```

##### validmind.models.FunctionModel.input_id

```python
input_id = input_id
```

##### validmind.models.FunctionModel.language

```python
language = 'Python'
```

##### validmind.models.FunctionModel.library

```python
library = self.__class__.__name__
```

##### validmind.models.FunctionModel.library_version

```python
library_version = 'N/A'
```

##### validmind.models.FunctionModel.model

```python
model = model
```

##### validmind.models.FunctionModel.name

```python
name = name or self.__class__.__name__
```

##### validmind.models.FunctionModel.predict

```python
predict(X)
```

Compute predictions for the input (X)

**Parameters:**

- **X** (<code>[DataFrame](#pandas.DataFrame)</code>) – The input features to predict on

**Returns:**

- **list** – The predictions

##### validmind.models.FunctionModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

Predict probabilties - must be implemented by subclass if needed

##### validmind.models.FunctionModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

##### validmind.models.FunctionModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

#### validmind.models.HFModel

```python
HFModel(input_id=None, model=None, attributes=None, name=None, **kwargs)
```

Bases: <code>[VMModel](#validmind.vm_models.model.VMModel)</code>

**Functions:**

- [**predict**](#validmind.models.HFModel.predict) – Predict method for the model. This is a wrapper around the HF model's pipeline function
- [**predict_proba**](#validmind.models.HFModel.predict_proba) – Invoke predict_proba from underline model
- [**serialize**](#validmind.models.HFModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.HFModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.HFModel.attributes) –
- [**class\_**](#validmind.models.HFModel.class_) –
- [**input_id**](#validmind.models.HFModel.input_id) –
- [**language**](#validmind.models.HFModel.language) –
- [**library**](#validmind.models.HFModel.library) –
- [**library_version**](#validmind.models.HFModel.library_version) –
- [**model**](#validmind.models.HFModel.model) –
- [**name**](#validmind.models.HFModel.name) –

##### validmind.models.HFModel.attributes

```python
attributes = attributes or ModelAttributes()
```

##### validmind.models.HFModel.class\_

```python
class_ = self.__class__.__name__
```

##### validmind.models.HFModel.input_id

```python
input_id = input_id
```

##### validmind.models.HFModel.language

```python
language = 'Python'
```

##### validmind.models.HFModel.library

```python
library = self.__class__.__name__
```

##### validmind.models.HFModel.library_version

```python
library_version = 'N/A'
```

##### validmind.models.HFModel.model

```python
model = model
```

##### validmind.models.HFModel.name

```python
name = name or self.__class__.__name__
```

##### validmind.models.HFModel.predict

```python
predict(data)
```

Predict method for the model. This is a wrapper around the HF model's pipeline function

##### validmind.models.HFModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

Invoke predict_proba from underline model

##### validmind.models.HFModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

##### validmind.models.HFModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

#### validmind.models.MetadataModel

Bases: <code>[VMModel](#validmind.vm_models.model.VMModel)</code>

MetadataModel is designed to represent a model that is not available for inference
for various reasons but for which metadata and pre-computed predictions are available.

Model attributes are required since this will be the only information we can
collect and log about the model.

This class should not be instantiated directly. Instead call `vm.init_model()` and
pass in a dictionary with the required metadata as `attributes`.

**Attributes:**

- [**attributes**](#validmind.models.MetadataModel.attributes) (<code>[ModelAttributes](#ModelAttributes)</code>) – The attributes of the model. Required.
- [**input_id**](#validmind.models.MetadataModel.input_id) (<code>[str](#str)</code>) – The input ID for the model. Defaults to None.
- [**name**](#validmind.models.MetadataModel.name) (<code>[str](#str)</code>) – The name of the model. Defaults to the class name.

**Functions:**

- [**predict**](#validmind.models.MetadataModel.predict) – Not implemented for MetadataModel
- [**predict_proba**](#validmind.models.MetadataModel.predict_proba) – Not implemented for MetadataModel
- [**serialize**](#validmind.models.MetadataModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.MetadataModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.MetadataModel.attributes) –
- [**class\_**](#validmind.models.MetadataModel.class_) –
- [**input_id**](#validmind.models.MetadataModel.input_id) –
- [**language**](#validmind.models.MetadataModel.language) –
- [**library**](#validmind.models.MetadataModel.library) –
- [**library_version**](#validmind.models.MetadataModel.library_version) –
- [**model**](#validmind.models.MetadataModel.model) –
- [**name**](#validmind.models.MetadataModel.name) –

##### validmind.models.MetadataModel.attributes

```python
attributes = attributes or ModelAttributes()
```

##### validmind.models.MetadataModel.class\_

```python
class_ = self.__class__.__name__
```

##### validmind.models.MetadataModel.input_id

```python
input_id = input_id
```

##### validmind.models.MetadataModel.language

```python
language = 'Python'
```

##### validmind.models.MetadataModel.library

```python
library = self.__class__.__name__
```

##### validmind.models.MetadataModel.library_version

```python
library_version = 'N/A'
```

##### validmind.models.MetadataModel.model

```python
model = model
```

##### validmind.models.MetadataModel.name

```python
name = name or self.__class__.__name__
```

##### validmind.models.MetadataModel.predict

```python
predict(*args, **kwargs)
```

Not implemented for MetadataModel

##### validmind.models.MetadataModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

Not implemented for MetadataModel

##### validmind.models.MetadataModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

##### validmind.models.MetadataModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

#### validmind.models.PipelineModel

```python
PipelineModel(pipeline, attributes=None, input_id=None, name=None)
```

Bases: <code>[VMModel](#validmind.vm_models.model.VMModel)</code>

An base class that wraps a trained model instance and its associated data.

**Attributes:**

- [**pipeline**](#validmind.models.PipelineModel.pipeline) (<code>[ModelPipeline](#validmind.vm_models.model.ModelPipeline)</code>) – A pipeline of models to be executed. ModelPipeline
  is just a simple container class with a list that can be chained with the
  `|` operator.
- [**input_id**](#validmind.models.PipelineModel.input_id) (<code>[str](#str)</code>) – The input ID for the model. Defaults to None.
- [**attributes**](#validmind.models.PipelineModel.attributes) (<code>[ModelAttributes](#validmind.vm_models.model.ModelAttributes)</code>) – The attributes of the model. Defaults to None.
- [**name**](#validmind.models.PipelineModel.name) (<code>[str](#str)</code>) – The name of the model. Defaults to the class name.

**Functions:**

- [**predict**](#validmind.models.PipelineModel.predict) –
- [**predict_proba**](#validmind.models.PipelineModel.predict_proba) – Predict probabilties - must be implemented by subclass if needed
- [**serialize**](#validmind.models.PipelineModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.PipelineModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.PipelineModel.attributes) –
- [**class\_**](#validmind.models.PipelineModel.class_) –
- [**input_id**](#validmind.models.PipelineModel.input_id) –
- [**language**](#validmind.models.PipelineModel.language) –
- [**library**](#validmind.models.PipelineModel.library) –
- [**library_version**](#validmind.models.PipelineModel.library_version) –
- [**model**](#validmind.models.PipelineModel.model) –
- [**name**](#validmind.models.PipelineModel.name) –
- [**pipeline**](#validmind.models.PipelineModel.pipeline) –
- [**predict_col**](#validmind.models.PipelineModel.predict_col) (<code>[str](#str)</code>) –

##### validmind.models.PipelineModel.attributes

```python
attributes = attributes
```

##### validmind.models.PipelineModel.class\_

```python
class_ = self.__class__.__name__
```

##### validmind.models.PipelineModel.input_id

```python
input_id = input_id
```

##### validmind.models.PipelineModel.language

```python
language = 'Python'
```

##### validmind.models.PipelineModel.library

```python
library = self.__class__.__name__
```

##### validmind.models.PipelineModel.library_version

```python
library_version = 'N/A'
```

##### validmind.models.PipelineModel.model

```python
model = model
```

##### validmind.models.PipelineModel.name

```python
name = name or self.__class__.__name__
```

##### validmind.models.PipelineModel.pipeline

```python
pipeline = pipeline
```

##### validmind.models.PipelineModel.predict

```python
predict(X)
```

##### validmind.models.PipelineModel.predict_col

```python
predict_col: str = None
```

##### validmind.models.PipelineModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

Predict probabilties - must be implemented by subclass if needed

##### validmind.models.PipelineModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

##### validmind.models.PipelineModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

#### validmind.models.Prompt

```python
Prompt(template, variables=None)
```

**Attributes:**

- [**template**](#validmind.models.Prompt.template) (<code>[str](#str)</code>) –
- [**variables**](#validmind.models.Prompt.variables) (<code>[list](#list)</code>) –

##### validmind.models.Prompt.template

```python
template: str
```

##### validmind.models.Prompt.variables

```python
variables: list = None
```

#### validmind.models.PyTorchModel

Bases: <code>[VMModel](#validmind.vm_models.model.VMModel)</code>

PyTorchModel class wraps a PyTorch model

**Functions:**

- [**predict**](#validmind.models.PyTorchModel.predict) – Predict method for the model. This is a wrapper around the model's
- [**predict_proba**](#validmind.models.PyTorchModel.predict_proba) – Invoke predict_proba from underline model
- [**serialize**](#validmind.models.PyTorchModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.PyTorchModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.PyTorchModel.attributes) –
- [**class\_**](#validmind.models.PyTorchModel.class_) –
- [**input_id**](#validmind.models.PyTorchModel.input_id) –
- [**language**](#validmind.models.PyTorchModel.language) –
- [**library**](#validmind.models.PyTorchModel.library) –
- [**library_version**](#validmind.models.PyTorchModel.library_version) –
- [**model**](#validmind.models.PyTorchModel.model) –
- [**name**](#validmind.models.PyTorchModel.name) –

##### validmind.models.PyTorchModel.attributes

```python
attributes = attributes or ModelAttributes()
```

##### validmind.models.PyTorchModel.class\_

```python
class_ = self.__class__.__name__
```

##### validmind.models.PyTorchModel.input_id

```python
input_id = input_id
```

##### validmind.models.PyTorchModel.language

```python
language = 'Python'
```

##### validmind.models.PyTorchModel.library

```python
library = self.__class__.__name__
```

##### validmind.models.PyTorchModel.library_version

```python
library_version = 'N/A'
```

##### validmind.models.PyTorchModel.model

```python
model = model
```

##### validmind.models.PyTorchModel.name

```python
name = name or self.__class__.__name__
```

##### validmind.models.PyTorchModel.predict

```python
predict(*args, **kwargs)
```

Predict method for the model. This is a wrapper around the model's

##### validmind.models.PyTorchModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

Invoke predict_proba from underline model

##### validmind.models.PyTorchModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

##### validmind.models.PyTorchModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

#### validmind.models.SKlearnModel

Bases: <code>[VMModel](#validmind.vm_models.model.VMModel)</code>

**Functions:**

- [**predict**](#validmind.models.SKlearnModel.predict) – Predict method for the model. This is a wrapper around the model's
- [**predict_proba**](#validmind.models.SKlearnModel.predict_proba) – predict_proba (for classification) or predict (for regression) method
- [**serialize**](#validmind.models.SKlearnModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.SKlearnModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.SKlearnModel.attributes) –
- [**class\_**](#validmind.models.SKlearnModel.class_) –
- [**input_id**](#validmind.models.SKlearnModel.input_id) –
- [**language**](#validmind.models.SKlearnModel.language) –
- [**library**](#validmind.models.SKlearnModel.library) –
- [**library_version**](#validmind.models.SKlearnModel.library_version) –
- [**model**](#validmind.models.SKlearnModel.model) –
- [**name**](#validmind.models.SKlearnModel.name) –

##### validmind.models.SKlearnModel.attributes

```python
attributes = attributes or ModelAttributes()
```

##### validmind.models.SKlearnModel.class\_

```python
class_ = self.__class__.__name__
```

##### validmind.models.SKlearnModel.input_id

```python
input_id = input_id
```

##### validmind.models.SKlearnModel.language

```python
language = 'Python'
```

##### validmind.models.SKlearnModel.library

```python
library = self.__class__.__name__
```

##### validmind.models.SKlearnModel.library_version

```python
library_version = 'N/A'
```

##### validmind.models.SKlearnModel.model

```python
model = model
```

##### validmind.models.SKlearnModel.name

```python
name = name or self.__class__.__name__
```

##### validmind.models.SKlearnModel.predict

```python
predict(*args, **kwargs)
```

Predict method for the model. This is a wrapper around the model's

##### validmind.models.SKlearnModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

predict_proba (for classification) or predict (for regression) method

##### validmind.models.SKlearnModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

##### validmind.models.SKlearnModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

#### validmind.models.StatsModelsModel

Bases: <code>[SKlearnModel](#validmind.models.sklearn.SKlearnModel)</code>

Wrapper for StatsModels model

**Functions:**

- [**predict**](#validmind.models.StatsModelsModel.predict) – Predict method for the model. This is a wrapper around the model's
- [**predict_proba**](#validmind.models.StatsModelsModel.predict_proba) – predict_proba (for classification) or predict (for regression) method
- [**regression_coefficients**](#validmind.models.StatsModelsModel.regression_coefficients) – Returns the regression coefficients summary of the model
- [**serialize**](#validmind.models.StatsModelsModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.StatsModelsModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.StatsModelsModel.attributes) –
- [**class\_**](#validmind.models.StatsModelsModel.class_) –
- [**input_id**](#validmind.models.StatsModelsModel.input_id) –
- [**language**](#validmind.models.StatsModelsModel.language) –
- [**library**](#validmind.models.StatsModelsModel.library) –
- [**library_version**](#validmind.models.StatsModelsModel.library_version) –
- [**model**](#validmind.models.StatsModelsModel.model) –
- [**name**](#validmind.models.StatsModelsModel.name) –

##### validmind.models.StatsModelsModel.attributes

```python
attributes = attributes or ModelAttributes()
```

##### validmind.models.StatsModelsModel.class\_

```python
class_ = self.__class__.__name__
```

##### validmind.models.StatsModelsModel.input_id

```python
input_id = input_id
```

##### validmind.models.StatsModelsModel.language

```python
language = 'Python'
```

##### validmind.models.StatsModelsModel.library

```python
library = self.__class__.__name__
```

##### validmind.models.StatsModelsModel.library_version

```python
library_version = 'N/A'
```

##### validmind.models.StatsModelsModel.model

```python
model = model
```

##### validmind.models.StatsModelsModel.name

```python
name = name or self.__class__.__name__
```

##### validmind.models.StatsModelsModel.predict

```python
predict(*args, **kwargs)
```

Predict method for the model. This is a wrapper around the model's

##### validmind.models.StatsModelsModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

predict_proba (for classification) or predict (for regression) method

##### validmind.models.StatsModelsModel.regression_coefficients

```python
regression_coefficients()
```

Returns the regression coefficients summary of the model

##### validmind.models.StatsModelsModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

##### validmind.models.StatsModelsModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

#### validmind.models.XGBoostModel

Bases: <code>[SKlearnModel](#validmind.models.sklearn.SKlearnModel)</code>

Wrapper for XGBoost model

**Functions:**

- [**predict**](#validmind.models.XGBoostModel.predict) – Predict method for the model. This is a wrapper around the model's
- [**predict_proba**](#validmind.models.XGBoostModel.predict_proba) – predict_proba (for classification) or predict (for regression) method
- [**serialize**](#validmind.models.XGBoostModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.XGBoostModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.XGBoostModel.attributes) –
- [**class\_**](#validmind.models.XGBoostModel.class_) –
- [**input_id**](#validmind.models.XGBoostModel.input_id) –
- [**language**](#validmind.models.XGBoostModel.language) –
- [**library**](#validmind.models.XGBoostModel.library) –
- [**library_version**](#validmind.models.XGBoostModel.library_version) –
- [**model**](#validmind.models.XGBoostModel.model) –
- [**name**](#validmind.models.XGBoostModel.name) –

##### validmind.models.XGBoostModel.attributes

```python
attributes = attributes or ModelAttributes()
```

##### validmind.models.XGBoostModel.class\_

```python
class_ = self.__class__.__name__
```

##### validmind.models.XGBoostModel.input_id

```python
input_id = input_id
```

##### validmind.models.XGBoostModel.language

```python
language = 'Python'
```

##### validmind.models.XGBoostModel.library

```python
library = self.__class__.__name__
```

##### validmind.models.XGBoostModel.library_version

```python
library_version = 'N/A'
```

##### validmind.models.XGBoostModel.model

```python
model = model
```

##### validmind.models.XGBoostModel.name

```python
name = name or self.__class__.__name__
```

##### validmind.models.XGBoostModel.predict

```python
predict(*args, **kwargs)
```

Predict method for the model. This is a wrapper around the model's

##### validmind.models.XGBoostModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

predict_proba (for classification) or predict (for regression) method

##### validmind.models.XGBoostModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

##### validmind.models.XGBoostModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

#### validmind.models.foundation

**Classes:**

- [**FoundationModel**](#validmind.models.foundation.FoundationModel) – FoundationModel class wraps a Foundation LLM endpoint
- [**Prompt**](#validmind.models.foundation.Prompt) –

**Attributes:**

- [**logger**](#validmind.models.foundation.logger) –

##### validmind.models.foundation.FoundationModel

Bases: <code>[FunctionModel](#validmind.models.function.FunctionModel)</code>

FoundationModel class wraps a Foundation LLM endpoint

This class wraps a predict function that is user-defined and adapts it to works
with ValidMind's model interface for the purpose of model eval and documentation

**Attributes:**

- [**predict_fn**](#validmind.models.foundation.FoundationModel.predict_fn) (<code>[callable](#callable)</code>) – The predict function that should take a prompt as input
  and return the result from the model
- [**prompt**](#validmind.models.foundation.FoundationModel.prompt) (<code>[Prompt](#validmind.models.foundation.Prompt)</code>) – The prompt object that defines the prompt template and the
  variables (if any)
- [**name**](#validmind.models.foundation.FoundationModel.name) (<code>[str](#str)</code>) – The name of the model. Defaults to name of the predict_fn

**Functions:**

- [**predict**](#validmind.models.foundation.FoundationModel.predict) – Predict method for the model. This is a wrapper around the model's
- [**predict_proba**](#validmind.models.foundation.FoundationModel.predict_proba) – Predict probabilties - must be implemented by subclass if needed
- [**serialize**](#validmind.models.foundation.FoundationModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.foundation.FoundationModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.foundation.FoundationModel.attributes) –
- [**class\_**](#validmind.models.foundation.FoundationModel.class_) –
- [**input_id**](#validmind.models.foundation.FoundationModel.input_id) –
- [**language**](#validmind.models.foundation.FoundationModel.language) –
- [**library**](#validmind.models.foundation.FoundationModel.library) –
- [**library_version**](#validmind.models.foundation.FoundationModel.library_version) –
- [**model**](#validmind.models.foundation.FoundationModel.model) –
- [**name**](#validmind.models.foundation.FoundationModel.name) –

###### validmind.models.foundation.FoundationModel.attributes

```python
attributes = attributes or ModelAttributes()
```

###### validmind.models.foundation.FoundationModel.class\_

```python
class_ = self.__class__.__name__
```

###### validmind.models.foundation.FoundationModel.input_id

```python
input_id = input_id
```

###### validmind.models.foundation.FoundationModel.language

```python
language = 'Python'
```

###### validmind.models.foundation.FoundationModel.library

```python
library = self.__class__.__name__
```

###### validmind.models.foundation.FoundationModel.library_version

```python
library_version = 'N/A'
```

###### validmind.models.foundation.FoundationModel.model

```python
model = model
```

###### validmind.models.foundation.FoundationModel.name

```python
name = name or self.__class__.__name__
```

###### validmind.models.foundation.FoundationModel.predict

```python
predict(X)
```

Predict method for the model. This is a wrapper around the model's

###### validmind.models.foundation.FoundationModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

Predict probabilties - must be implemented by subclass if needed

###### validmind.models.foundation.FoundationModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

###### validmind.models.foundation.FoundationModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

##### validmind.models.foundation.Prompt

```python
Prompt(template, variables=None)
```

**Attributes:**

- [**template**](#validmind.models.foundation.Prompt.template) (<code>[str](#str)</code>) –
- [**variables**](#validmind.models.foundation.Prompt.variables) (<code>[list](#list)</code>) –

###### validmind.models.foundation.Prompt.template

```python
template: str
```

###### validmind.models.foundation.Prompt.variables

```python
variables: list = None
```

##### validmind.models.foundation.logger

```python
logger = get_logger(__name__)
```

#### validmind.models.function

**Classes:**

- [**FunctionModel**](#validmind.models.function.FunctionModel) – FunctionModel class wraps a user-defined predict function
- [**Input**](#validmind.models.function.Input) –

##### validmind.models.function.FunctionModel

Bases: <code>[VMModel](#validmind.vm_models.model.VMModel)</code>

FunctionModel class wraps a user-defined predict function

**Attributes:**

- [**predict_fn**](#validmind.models.function.FunctionModel.predict_fn) (<code>[callable](#callable)</code>) – The predict function that should take a dictionary of
  input features and return a prediction.
- [**input_id**](#validmind.models.function.FunctionModel.input_id) (<code>[str](#str)</code>) – The input ID for the model. Defaults to None.
- [**name**](#validmind.models.function.FunctionModel.name) (<code>[str](#str)</code>) – The name of the model. Defaults to the name of the predict_fn.
- [**prompt**](#validmind.models.function.FunctionModel.prompt) (<code>[Prompt](#validmind.models.foundation.Prompt)</code>) – If using a prompt, the prompt object that defines the template
  and the variables (if any). Defaults to None.

**Functions:**

- [**predict**](#validmind.models.function.FunctionModel.predict) – Compute predictions for the input (X)
- [**predict_proba**](#validmind.models.function.FunctionModel.predict_proba) – Predict probabilties - must be implemented by subclass if needed
- [**serialize**](#validmind.models.function.FunctionModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.function.FunctionModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.function.FunctionModel.attributes) –
- [**class\_**](#validmind.models.function.FunctionModel.class_) –
- [**input_id**](#validmind.models.function.FunctionModel.input_id) –
- [**language**](#validmind.models.function.FunctionModel.language) –
- [**library**](#validmind.models.function.FunctionModel.library) –
- [**library_version**](#validmind.models.function.FunctionModel.library_version) –
- [**model**](#validmind.models.function.FunctionModel.model) –
- [**name**](#validmind.models.function.FunctionModel.name) –

###### validmind.models.function.FunctionModel.attributes

```python
attributes = attributes or ModelAttributes()
```

###### validmind.models.function.FunctionModel.class\_

```python
class_ = self.__class__.__name__
```

###### validmind.models.function.FunctionModel.input_id

```python
input_id = input_id
```

###### validmind.models.function.FunctionModel.language

```python
language = 'Python'
```

###### validmind.models.function.FunctionModel.library

```python
library = self.__class__.__name__
```

###### validmind.models.function.FunctionModel.library_version

```python
library_version = 'N/A'
```

###### validmind.models.function.FunctionModel.model

```python
model = model
```

###### validmind.models.function.FunctionModel.name

```python
name = name or self.__class__.__name__
```

###### validmind.models.function.FunctionModel.predict

```python
predict(X)
```

Compute predictions for the input (X)

**Parameters:**

- **X** (<code>[DataFrame](#pandas.DataFrame)</code>) – The input features to predict on

**Returns:**

- **list** – The predictions

###### validmind.models.function.FunctionModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

Predict probabilties - must be implemented by subclass if needed

###### validmind.models.function.FunctionModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

###### validmind.models.function.FunctionModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

##### validmind.models.function.Input

```python
Input(*args, **kwargs)
```

Bases: <code>[dict](#dict)</code>

**Functions:**

- [**get_new**](#validmind.models.function.Input.get_new) –

###### validmind.models.function.Input.get_new

```python
get_new()
```

#### validmind.models.huggingface

**Classes:**

- [**HFModel**](#validmind.models.huggingface.HFModel) –

**Attributes:**

- [**logger**](#validmind.models.huggingface.logger) –

##### validmind.models.huggingface.HFModel

```python
HFModel(input_id=None, model=None, attributes=None, name=None, **kwargs)
```

Bases: <code>[VMModel](#validmind.vm_models.model.VMModel)</code>

**Functions:**

- [**predict**](#validmind.models.huggingface.HFModel.predict) – Predict method for the model. This is a wrapper around the HF model's pipeline function
- [**predict_proba**](#validmind.models.huggingface.HFModel.predict_proba) – Invoke predict_proba from underline model
- [**serialize**](#validmind.models.huggingface.HFModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.huggingface.HFModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.huggingface.HFModel.attributes) –
- [**class\_**](#validmind.models.huggingface.HFModel.class_) –
- [**input_id**](#validmind.models.huggingface.HFModel.input_id) –
- [**language**](#validmind.models.huggingface.HFModel.language) –
- [**library**](#validmind.models.huggingface.HFModel.library) –
- [**library_version**](#validmind.models.huggingface.HFModel.library_version) –
- [**model**](#validmind.models.huggingface.HFModel.model) –
- [**name**](#validmind.models.huggingface.HFModel.name) –

###### validmind.models.huggingface.HFModel.attributes

```python
attributes = attributes or ModelAttributes()
```

###### validmind.models.huggingface.HFModel.class\_

```python
class_ = self.__class__.__name__
```

###### validmind.models.huggingface.HFModel.input_id

```python
input_id = input_id
```

###### validmind.models.huggingface.HFModel.language

```python
language = 'Python'
```

###### validmind.models.huggingface.HFModel.library

```python
library = self.__class__.__name__
```

###### validmind.models.huggingface.HFModel.library_version

```python
library_version = 'N/A'
```

###### validmind.models.huggingface.HFModel.model

```python
model = model
```

###### validmind.models.huggingface.HFModel.name

```python
name = name or self.__class__.__name__
```

###### validmind.models.huggingface.HFModel.predict

```python
predict(data)
```

Predict method for the model. This is a wrapper around the HF model's pipeline function

###### validmind.models.huggingface.HFModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

Invoke predict_proba from underline model

###### validmind.models.huggingface.HFModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

###### validmind.models.huggingface.HFModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

##### validmind.models.huggingface.logger

```python
logger = get_logger(__name__)
```

#### validmind.models.metadata

**Classes:**

- [**MetadataModel**](#validmind.models.metadata.MetadataModel) – MetadataModel is designed to represent a model that is not available for inference

##### validmind.models.metadata.MetadataModel

Bases: <code>[VMModel](#validmind.vm_models.model.VMModel)</code>

MetadataModel is designed to represent a model that is not available for inference
for various reasons but for which metadata and pre-computed predictions are available.

Model attributes are required since this will be the only information we can
collect and log about the model.

This class should not be instantiated directly. Instead call `vm.init_model()` and
pass in a dictionary with the required metadata as `attributes`.

**Attributes:**

- [**attributes**](#validmind.models.metadata.MetadataModel.attributes) (<code>[ModelAttributes](#ModelAttributes)</code>) – The attributes of the model. Required.
- [**input_id**](#validmind.models.metadata.MetadataModel.input_id) (<code>[str](#str)</code>) – The input ID for the model. Defaults to None.
- [**name**](#validmind.models.metadata.MetadataModel.name) (<code>[str](#str)</code>) – The name of the model. Defaults to the class name.

**Functions:**

- [**predict**](#validmind.models.metadata.MetadataModel.predict) – Not implemented for MetadataModel
- [**predict_proba**](#validmind.models.metadata.MetadataModel.predict_proba) – Not implemented for MetadataModel
- [**serialize**](#validmind.models.metadata.MetadataModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.metadata.MetadataModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.metadata.MetadataModel.attributes) –
- [**class\_**](#validmind.models.metadata.MetadataModel.class_) –
- [**input_id**](#validmind.models.metadata.MetadataModel.input_id) –
- [**language**](#validmind.models.metadata.MetadataModel.language) –
- [**library**](#validmind.models.metadata.MetadataModel.library) –
- [**library_version**](#validmind.models.metadata.MetadataModel.library_version) –
- [**model**](#validmind.models.metadata.MetadataModel.model) –
- [**name**](#validmind.models.metadata.MetadataModel.name) –

###### validmind.models.metadata.MetadataModel.attributes

```python
attributes = attributes or ModelAttributes()
```

###### validmind.models.metadata.MetadataModel.class\_

```python
class_ = self.__class__.__name__
```

###### validmind.models.metadata.MetadataModel.input_id

```python
input_id = input_id
```

###### validmind.models.metadata.MetadataModel.language

```python
language = 'Python'
```

###### validmind.models.metadata.MetadataModel.library

```python
library = self.__class__.__name__
```

###### validmind.models.metadata.MetadataModel.library_version

```python
library_version = 'N/A'
```

###### validmind.models.metadata.MetadataModel.model

```python
model = model
```

###### validmind.models.metadata.MetadataModel.name

```python
name = name or self.__class__.__name__
```

###### validmind.models.metadata.MetadataModel.predict

```python
predict(*args, **kwargs)
```

Not implemented for MetadataModel

###### validmind.models.metadata.MetadataModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

Not implemented for MetadataModel

###### validmind.models.metadata.MetadataModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

###### validmind.models.metadata.MetadataModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

#### validmind.models.pipeline

**Classes:**

- [**PipelineModel**](#validmind.models.pipeline.PipelineModel) – An base class that wraps a trained model instance and its associated data.

**Attributes:**

- [**logger**](#validmind.models.pipeline.logger) –

##### validmind.models.pipeline.PipelineModel

```python
PipelineModel(pipeline, attributes=None, input_id=None, name=None)
```

Bases: <code>[VMModel](#validmind.vm_models.model.VMModel)</code>

An base class that wraps a trained model instance and its associated data.

**Attributes:**

- [**pipeline**](#validmind.models.pipeline.PipelineModel.pipeline) (<code>[ModelPipeline](#validmind.vm_models.model.ModelPipeline)</code>) – A pipeline of models to be executed. ModelPipeline
  is just a simple container class with a list that can be chained with the
  `|` operator.
- [**input_id**](#validmind.models.pipeline.PipelineModel.input_id) (<code>[str](#str)</code>) – The input ID for the model. Defaults to None.
- [**attributes**](#validmind.models.pipeline.PipelineModel.attributes) (<code>[ModelAttributes](#validmind.vm_models.model.ModelAttributes)</code>) – The attributes of the model. Defaults to None.
- [**name**](#validmind.models.pipeline.PipelineModel.name) (<code>[str](#str)</code>) – The name of the model. Defaults to the class name.

**Functions:**

- [**predict**](#validmind.models.pipeline.PipelineModel.predict) –
- [**predict_proba**](#validmind.models.pipeline.PipelineModel.predict_proba) – Predict probabilties - must be implemented by subclass if needed
- [**serialize**](#validmind.models.pipeline.PipelineModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.pipeline.PipelineModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.pipeline.PipelineModel.attributes) –
- [**class\_**](#validmind.models.pipeline.PipelineModel.class_) –
- [**input_id**](#validmind.models.pipeline.PipelineModel.input_id) –
- [**language**](#validmind.models.pipeline.PipelineModel.language) –
- [**library**](#validmind.models.pipeline.PipelineModel.library) –
- [**library_version**](#validmind.models.pipeline.PipelineModel.library_version) –
- [**model**](#validmind.models.pipeline.PipelineModel.model) –
- [**name**](#validmind.models.pipeline.PipelineModel.name) –
- [**pipeline**](#validmind.models.pipeline.PipelineModel.pipeline) –
- [**predict_col**](#validmind.models.pipeline.PipelineModel.predict_col) (<code>[str](#str)</code>) –

###### validmind.models.pipeline.PipelineModel.attributes

```python
attributes = attributes
```

###### validmind.models.pipeline.PipelineModel.class\_

```python
class_ = self.__class__.__name__
```

###### validmind.models.pipeline.PipelineModel.input_id

```python
input_id = input_id
```

###### validmind.models.pipeline.PipelineModel.language

```python
language = 'Python'
```

###### validmind.models.pipeline.PipelineModel.library

```python
library = self.__class__.__name__
```

###### validmind.models.pipeline.PipelineModel.library_version

```python
library_version = 'N/A'
```

###### validmind.models.pipeline.PipelineModel.model

```python
model = model
```

###### validmind.models.pipeline.PipelineModel.name

```python
name = name or self.__class__.__name__
```

###### validmind.models.pipeline.PipelineModel.pipeline

```python
pipeline = pipeline
```

###### validmind.models.pipeline.PipelineModel.predict

```python
predict(X)
```

###### validmind.models.pipeline.PipelineModel.predict_col

```python
predict_col: str = None
```

###### validmind.models.pipeline.PipelineModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

Predict probabilties - must be implemented by subclass if needed

###### validmind.models.pipeline.PipelineModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

###### validmind.models.pipeline.PipelineModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

##### validmind.models.pipeline.logger

```python
logger = get_logger(__name__)
```

#### validmind.models.pytorch

**Classes:**

- [**PyTorchModel**](#validmind.models.pytorch.PyTorchModel) – PyTorchModel class wraps a PyTorch model

**Attributes:**

- [**logger**](#validmind.models.pytorch.logger) –

##### validmind.models.pytorch.PyTorchModel

Bases: <code>[VMModel](#validmind.vm_models.model.VMModel)</code>

PyTorchModel class wraps a PyTorch model

**Functions:**

- [**predict**](#validmind.models.pytorch.PyTorchModel.predict) – Predict method for the model. This is a wrapper around the model's
- [**predict_proba**](#validmind.models.pytorch.PyTorchModel.predict_proba) – Invoke predict_proba from underline model
- [**serialize**](#validmind.models.pytorch.PyTorchModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.pytorch.PyTorchModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.pytorch.PyTorchModel.attributes) –
- [**class\_**](#validmind.models.pytorch.PyTorchModel.class_) –
- [**input_id**](#validmind.models.pytorch.PyTorchModel.input_id) –
- [**language**](#validmind.models.pytorch.PyTorchModel.language) –
- [**library**](#validmind.models.pytorch.PyTorchModel.library) –
- [**library_version**](#validmind.models.pytorch.PyTorchModel.library_version) –
- [**model**](#validmind.models.pytorch.PyTorchModel.model) –
- [**name**](#validmind.models.pytorch.PyTorchModel.name) –

###### validmind.models.pytorch.PyTorchModel.attributes

```python
attributes = attributes or ModelAttributes()
```

###### validmind.models.pytorch.PyTorchModel.class\_

```python
class_ = self.__class__.__name__
```

###### validmind.models.pytorch.PyTorchModel.input_id

```python
input_id = input_id
```

###### validmind.models.pytorch.PyTorchModel.language

```python
language = 'Python'
```

###### validmind.models.pytorch.PyTorchModel.library

```python
library = self.__class__.__name__
```

###### validmind.models.pytorch.PyTorchModel.library_version

```python
library_version = 'N/A'
```

###### validmind.models.pytorch.PyTorchModel.model

```python
model = model
```

###### validmind.models.pytorch.PyTorchModel.name

```python
name = name or self.__class__.__name__
```

###### validmind.models.pytorch.PyTorchModel.predict

```python
predict(*args, **kwargs)
```

Predict method for the model. This is a wrapper around the model's

###### validmind.models.pytorch.PyTorchModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

Invoke predict_proba from underline model

###### validmind.models.pytorch.PyTorchModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

###### validmind.models.pytorch.PyTorchModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

##### validmind.models.pytorch.logger

```python
logger = get_logger(__name__)
```

#### validmind.models.r_model

**Classes:**

- [**RModel**](#validmind.models.r_model.RModel) – An R model class that wraps a "fitted" R model instance and its associated data.

**Functions:**

- [**get_full_class_name**](#validmind.models.r_model.get_full_class_name) –

**Attributes:**

- [**logger**](#validmind.models.r_model.logger) –

##### validmind.models.r_model.RModel

Bases: <code>[VMModel](#validmind.vm_models.model.VMModel)</code>

An R model class that wraps a "fitted" R model instance and its associated data.

**Functions:**

- [**predict**](#validmind.models.r_model.RModel.predict) – Converts the predicted probabilities to classes
- [**predict_proba**](#validmind.models.r_model.RModel.predict_proba) – Calls the R global predict method with type="response" to get the predicted probabilities
- [**r_predict**](#validmind.models.r_model.RModel.r_predict) – Predict method for the model. This is a wrapper around R's global predict.
- [**r_xgb_predict**](#validmind.models.r_model.RModel.r_xgb_predict) – Predict method for XGBoost models. This is a wrapper around R's global predict
- [**regression_coefficients**](#validmind.models.r_model.RModel.regression_coefficients) – Returns the regression coefficients summary of the model
- [**serialize**](#validmind.models.r_model.RModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.r_model.RModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.r_model.RModel.attributes) –
- [**class\_**](#validmind.models.r_model.RModel.class_) –
- [**input_id**](#validmind.models.r_model.RModel.input_id) –
- [**language**](#validmind.models.r_model.RModel.language) –
- [**library**](#validmind.models.r_model.RModel.library) –
- [**library_version**](#validmind.models.r_model.RModel.library_version) –
- [**model**](#validmind.models.r_model.RModel.model) –
- [**name**](#validmind.models.r_model.RModel.name) –

###### validmind.models.r_model.RModel.attributes

```python
attributes = attributes or ModelAttributes()
```

###### validmind.models.r_model.RModel.class\_

```python
class_ = self.__class__.__name__
```

###### validmind.models.r_model.RModel.input_id

```python
input_id = input_id
```

###### validmind.models.r_model.RModel.language

```python
language = 'Python'
```

###### validmind.models.r_model.RModel.library

```python
library = self.__class__.__name__
```

###### validmind.models.r_model.RModel.library_version

```python
library_version = 'N/A'
```

###### validmind.models.r_model.RModel.model

```python
model = model
```

###### validmind.models.r_model.RModel.name

```python
name = name or self.__class__.__name__
```

###### validmind.models.r_model.RModel.predict

```python
predict(new_data, return_probs=False)
```

Converts the predicted probabilities to classes

###### validmind.models.r_model.RModel.predict_proba

```python
predict_proba(new_data)
```

Calls the R global predict method with type="response" to get the predicted probabilities

###### validmind.models.r_model.RModel.r_predict

```python
r_predict(new_data_r)
```

Predict method for the model. This is a wrapper around R's global predict.

An R model doesn't provide separate predict() and predict_proba() methods.
Instead, there is a global predict() method that returns the predicted
values according to the model type.

###### validmind.models.r_model.RModel.r_xgb_predict

```python
r_xgb_predict(new_data_r)
```

Predict method for XGBoost models. This is a wrapper around R's global predict

###### validmind.models.r_model.RModel.regression_coefficients

```python
regression_coefficients()
```

Returns the regression coefficients summary of the model

###### validmind.models.r_model.RModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

###### validmind.models.r_model.RModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

##### validmind.models.r_model.get_full_class_name

```python
get_full_class_name(obj)
```

##### validmind.models.r_model.logger

```python
logger = get_logger(__name__)
```

#### validmind.models.sklearn

**Classes:**

- [**CatBoostModel**](#validmind.models.sklearn.CatBoostModel) – Wrapper for CatBoost model
- [**SKlearnModel**](#validmind.models.sklearn.SKlearnModel) –
- [**StatsModelsModel**](#validmind.models.sklearn.StatsModelsModel) – Wrapper for StatsModels model
- [**XGBoostModel**](#validmind.models.sklearn.XGBoostModel) – Wrapper for XGBoost model

**Attributes:**

- [**logger**](#validmind.models.sklearn.logger) –

##### validmind.models.sklearn.CatBoostModel

Bases: <code>[SKlearnModel](#validmind.models.sklearn.SKlearnModel)</code>

Wrapper for CatBoost model

**Functions:**

- [**predict**](#validmind.models.sklearn.CatBoostModel.predict) – Predict method for the model. This is a wrapper around the model's
- [**predict_proba**](#validmind.models.sklearn.CatBoostModel.predict_proba) – predict_proba (for classification) or predict (for regression) method
- [**serialize**](#validmind.models.sklearn.CatBoostModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.sklearn.CatBoostModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.sklearn.CatBoostModel.attributes) –
- [**class\_**](#validmind.models.sklearn.CatBoostModel.class_) –
- [**input_id**](#validmind.models.sklearn.CatBoostModel.input_id) –
- [**language**](#validmind.models.sklearn.CatBoostModel.language) –
- [**library**](#validmind.models.sklearn.CatBoostModel.library) –
- [**library_version**](#validmind.models.sklearn.CatBoostModel.library_version) –
- [**model**](#validmind.models.sklearn.CatBoostModel.model) –
- [**name**](#validmind.models.sklearn.CatBoostModel.name) –

##### validmind.models.sklearn.SKlearnModel

Bases: <code>[VMModel](#validmind.vm_models.model.VMModel)</code>

**Functions:**

- [**predict**](#validmind.models.sklearn.SKlearnModel.predict) – Predict method for the model. This is a wrapper around the model's
- [**predict_proba**](#validmind.models.sklearn.SKlearnModel.predict_proba) – predict_proba (for classification) or predict (for regression) method
- [**serialize**](#validmind.models.sklearn.SKlearnModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.sklearn.SKlearnModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.sklearn.SKlearnModel.attributes) –
- [**class\_**](#validmind.models.sklearn.SKlearnModel.class_) –
- [**input_id**](#validmind.models.sklearn.SKlearnModel.input_id) –
- [**language**](#validmind.models.sklearn.SKlearnModel.language) –
- [**library**](#validmind.models.sklearn.SKlearnModel.library) –
- [**library_version**](#validmind.models.sklearn.SKlearnModel.library_version) –
- [**model**](#validmind.models.sklearn.SKlearnModel.model) –
- [**name**](#validmind.models.sklearn.SKlearnModel.name) –

###### validmind.models.sklearn.SKlearnModel.attributes

```python
attributes = attributes or ModelAttributes()
```

###### validmind.models.sklearn.SKlearnModel.class\_

```python
class_ = self.__class__.__name__
```

###### validmind.models.sklearn.SKlearnModel.input_id

```python
input_id = input_id
```

###### validmind.models.sklearn.SKlearnModel.language

```python
language = 'Python'
```

###### validmind.models.sklearn.SKlearnModel.library

```python
library = self.__class__.__name__
```

###### validmind.models.sklearn.SKlearnModel.library_version

```python
library_version = 'N/A'
```

###### validmind.models.sklearn.SKlearnModel.model

```python
model = model
```

###### validmind.models.sklearn.SKlearnModel.name

```python
name = name or self.__class__.__name__
```

###### validmind.models.sklearn.SKlearnModel.predict

```python
predict(*args, **kwargs)
```

Predict method for the model. This is a wrapper around the model's

###### validmind.models.sklearn.SKlearnModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

predict_proba (for classification) or predict (for regression) method

###### validmind.models.sklearn.SKlearnModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

###### validmind.models.sklearn.SKlearnModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

##### validmind.models.sklearn.StatsModelsModel

Bases: <code>[SKlearnModel](#validmind.models.sklearn.SKlearnModel)</code>

Wrapper for StatsModels model

**Functions:**

- [**predict**](#validmind.models.sklearn.StatsModelsModel.predict) – Predict method for the model. This is a wrapper around the model's
- [**predict_proba**](#validmind.models.sklearn.StatsModelsModel.predict_proba) – predict_proba (for classification) or predict (for regression) method
- [**regression_coefficients**](#validmind.models.sklearn.StatsModelsModel.regression_coefficients) – Returns the regression coefficients summary of the model
- [**serialize**](#validmind.models.sklearn.StatsModelsModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.sklearn.StatsModelsModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.sklearn.StatsModelsModel.attributes) –
- [**class\_**](#validmind.models.sklearn.StatsModelsModel.class_) –
- [**input_id**](#validmind.models.sklearn.StatsModelsModel.input_id) –
- [**language**](#validmind.models.sklearn.StatsModelsModel.language) –
- [**library**](#validmind.models.sklearn.StatsModelsModel.library) –
- [**library_version**](#validmind.models.sklearn.StatsModelsModel.library_version) –
- [**model**](#validmind.models.sklearn.StatsModelsModel.model) –
- [**name**](#validmind.models.sklearn.StatsModelsModel.name) –

###### validmind.models.sklearn.StatsModelsModel.attributes

```python
attributes = attributes or ModelAttributes()
```

###### validmind.models.sklearn.StatsModelsModel.class\_

```python
class_ = self.__class__.__name__
```

###### validmind.models.sklearn.StatsModelsModel.input_id

```python
input_id = input_id
```

###### validmind.models.sklearn.StatsModelsModel.language

```python
language = 'Python'
```

###### validmind.models.sklearn.StatsModelsModel.library

```python
library = self.__class__.__name__
```

###### validmind.models.sklearn.StatsModelsModel.library_version

```python
library_version = 'N/A'
```

###### validmind.models.sklearn.StatsModelsModel.model

```python
model = model
```

###### validmind.models.sklearn.StatsModelsModel.name

```python
name = name or self.__class__.__name__
```

###### validmind.models.sklearn.StatsModelsModel.predict

```python
predict(*args, **kwargs)
```

Predict method for the model. This is a wrapper around the model's

###### validmind.models.sklearn.StatsModelsModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

predict_proba (for classification) or predict (for regression) method

###### validmind.models.sklearn.StatsModelsModel.regression_coefficients

```python
regression_coefficients()
```

Returns the regression coefficients summary of the model

###### validmind.models.sklearn.StatsModelsModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

###### validmind.models.sklearn.StatsModelsModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

##### validmind.models.sklearn.XGBoostModel

Bases: <code>[SKlearnModel](#validmind.models.sklearn.SKlearnModel)</code>

Wrapper for XGBoost model

**Functions:**

- [**predict**](#validmind.models.sklearn.XGBoostModel.predict) – Predict method for the model. This is a wrapper around the model's
- [**predict_proba**](#validmind.models.sklearn.XGBoostModel.predict_proba) – predict_proba (for classification) or predict (for regression) method
- [**serialize**](#validmind.models.sklearn.XGBoostModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.models.sklearn.XGBoostModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.models.sklearn.XGBoostModel.attributes) –
- [**class\_**](#validmind.models.sklearn.XGBoostModel.class_) –
- [**input_id**](#validmind.models.sklearn.XGBoostModel.input_id) –
- [**language**](#validmind.models.sklearn.XGBoostModel.language) –
- [**library**](#validmind.models.sklearn.XGBoostModel.library) –
- [**library_version**](#validmind.models.sklearn.XGBoostModel.library_version) –
- [**model**](#validmind.models.sklearn.XGBoostModel.model) –
- [**name**](#validmind.models.sklearn.XGBoostModel.name) –

###### validmind.models.sklearn.XGBoostModel.attributes

```python
attributes = attributes or ModelAttributes()
```

###### validmind.models.sklearn.XGBoostModel.class\_

```python
class_ = self.__class__.__name__
```

###### validmind.models.sklearn.XGBoostModel.input_id

```python
input_id = input_id
```

###### validmind.models.sklearn.XGBoostModel.language

```python
language = 'Python'
```

###### validmind.models.sklearn.XGBoostModel.library

```python
library = self.__class__.__name__
```

###### validmind.models.sklearn.XGBoostModel.library_version

```python
library_version = 'N/A'
```

###### validmind.models.sklearn.XGBoostModel.model

```python
model = model
```

###### validmind.models.sklearn.XGBoostModel.name

```python
name = name or self.__class__.__name__
```

###### validmind.models.sklearn.XGBoostModel.predict

```python
predict(*args, **kwargs)
```

Predict method for the model. This is a wrapper around the model's

###### validmind.models.sklearn.XGBoostModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

predict_proba (for classification) or predict (for regression) method

###### validmind.models.sklearn.XGBoostModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

###### validmind.models.sklearn.XGBoostModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

##### validmind.models.sklearn.logger

```python
logger = get_logger(__name__)
```

### validmind.preview_template

```python
preview_template()
```

Preview the documentation template for the current project

This function will display the documentation template for the current project. If
the project has not been initialized, then an error will be raised.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If the project has not been initialized

### validmind.reload

```python
reload()
```

Reconnect to the ValidMind API and reload the project configuration

### validmind.run_documentation_tests

```python
run_documentation_tests(
    section=None, send=True, fail_fast=False, inputs=None, config=None, **kwargs
)
```

Collect and run all the tests associated with a template

This function will analyze the current project's documentation template and collect
all the tests associated with it into a test suite. It will then run the test
suite, log the results to the ValidMind API, and display them to the user.

**Parameters:**

- **section** (<code>[str](#str) or [list](#list)</code>) – The section(s) to preview. Defaults to None.
- **send** (<code>[bool](#bool)</code>) – Whether to send the results to the ValidMind API. Defaults to True.
- **fail_fast** (<code>[bool](#bool)</code>) – Whether to stop running tests after the first failure. Defaults to False.
- **inputs** (<code>[dict](#dict)</code>) – A dictionary of test inputs to pass to the TestSuite
- **config** – A dictionary of test parameters to override the defaults
- \*\***kwargs** – backwards compatibility for passing in test inputs using keyword arguments

**Returns:**

- – TestSuite or dict: The completed TestSuite instance or a dictionary of TestSuites if section is a list.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If the project has not been initialized

### validmind.run_test_suite

```python
run_test_suite(
    test_suite_id,
    send=True,
    fail_fast=False,
    config=None,
    inputs=None,
    **kwargs
)
```

High Level function for running a test suite

This function provides a high level interface for running a test suite. A test suite is
a collection of tests. This function will automatically find the correct test suite
class based on the test_suite_id, initialize each of the tests, and run them.

**Parameters:**

- **test_suite_id** (<code>[str](#str)</code>) – The test suite name (e.g. 'classifier_full_suite')
- **config** (<code>[dict](#dict)</code>) – A dictionary of parameters to pass to the tests in the
  test suite. Defaults to None.
- **send** (<code>[bool](#bool)</code>) – Whether to post the test results to the API. send=False
  is useful for testing. Defaults to True.
- **fail_fast** (<code>[bool](#bool)</code>) – Whether to stop running tests after the first failure. Defaults to False.
- **inputs** (<code>[dict](#dict)</code>) – A dictionary of test inputs to pass to the TestSuite e.g. `model`, `dataset`
  `models` etc. These inputs will be accessible by any test in the test suite. See the test
  documentation or `vm.describe_test()` for more details on the inputs required for each.
- \*\***kwargs** – backwards compatibility for passing in test inputs using keyword arguments

**Raises:**

- <code>[ValueError](#ValueError)</code> – If the test suite name is not found or if there is an error initializing the test suite

**Returns:**

- **TestSuite** – the TestSuite instance

### validmind.tags

```python
tags(*tags)
```

Decorator for specifying tags for a test.

**Parameters:**

- \***tags** – The tags to apply to the test.

### validmind.tasks

```python
tasks(*tasks)
```

Decorator for specifying the task types that a test is designed for.

**Parameters:**

- \***tasks** – The task types that the test is designed for.

### validmind.template

**Functions:**

- [**get_template_test_suite**](#validmind.template.get_template_test_suite) – Get a TestSuite instance containing all tests in a template
- [**preview_template**](#validmind.template.preview_template) – Preview a template in Jupyter Notebook

**Attributes:**

- [**CONTENT_TYPE_MAP**](#validmind.template.CONTENT_TYPE_MAP) –
- [**logger**](#validmind.template.logger) –

#### validmind.template.CONTENT_TYPE_MAP

```python
CONTENT_TYPE_MAP = {
    "test": "Threshold Test",
    "metric": "Metric",
    "unit_metric": "Unit Metric",
    "metadata_text": "Metadata Text",
    "dynamic": "Dynamic Content",
    "text": "Text",
    "risk_assessment": "Risk Assessment",
    "assessment_summary": "Assessment Summary",
    "guideline": "Guideline Assessment",
}

```

#### validmind.template.get_template_test_suite

```python
get_template_test_suite(template, section=None)
```

Get a TestSuite instance containing all tests in a template

This function will collect all tests used in a template into a dynamically-created
TestSuite object

**Parameters:**

- **template** – A valid flat template
- **section** – The section of the template to run (if not provided, run all sections)

**Returns:**

- – The TestSuite instance

#### validmind.template.logger

```python
logger = get_logger(__name__)
```

#### validmind.template.preview_template

```python
preview_template(template)
```

Preview a template in Jupyter Notebook

**Parameters:**

- **template** (<code>[dict](#dict)</code>) – The template to preview

### validmind.test

```python
test(func_or_id)
```

Decorator for creating and registering custom tests

This decorator registers the function it wraps as a test function within ValidMind
under the provided ID. Once decorated, the function can be run using the
`validmind.tests.run_test` function.

The function can take two different types of arguments:

- Inputs: ValidMind model or dataset (or list of models/datasets). These arguments
  must use the following names: `model`, `models`, `dataset`, `datasets`.
- Parameters: Any additional keyword arguments of any type (must have a default
  value) that can have any name.

The function should return one of the following types:

- Table: Either a list of dictionaries or a pandas DataFrame
- Plot: Either a matplotlib figure or a plotly figure
- Scalar: A single number (int or float)
- Boolean: A single boolean value indicating whether the test passed or failed

The function may also include a docstring. This docstring will be used and logged
as the metric's description.

**Parameters:**

- **func** – The function to decorate
- **test_id** – The identifier for the metric. If not provided, the function name is used.

**Returns:**

- – The decorated function.

### validmind.test_suites

Entrypoint for test suites.

**Modules:**

- [**classifier**](#validmind.test_suites.classifier) – Test suites for sklearn-compatible classifier models
- [**cluster**](#validmind.test_suites.cluster) – Test suites for sklearn-compatible clustering models
- [**embeddings**](#validmind.test_suites.embeddings) – Test suites for embeddings models
- [**llm**](#validmind.test_suites.llm) – Test suites for LLMs
- [**nlp**](#validmind.test_suites.nlp) – Test suites for NLP models
- [**parameters_optimization**](#validmind.test_suites.parameters_optimization) – Test suites for sklearn-compatible hyper parameters tunning
- [**regression**](#validmind.test_suites.regression) –
- [**statsmodels_timeseries**](#validmind.test_suites.statsmodels_timeseries) – Time Series Test Suites from statsmodels
- [**summarization**](#validmind.test_suites.summarization) – Test suites for llm summarization models
- [**tabular_datasets**](#validmind.test_suites.tabular_datasets) – Test suites for tabular datasets
- [**text_data**](#validmind.test_suites.text_data) – Test suites for text datasets
- [**time_series**](#validmind.test_suites.time_series) – Time Series Test Suites

**Functions:**

- [**describe_suite**](#validmind.test_suites.describe_suite) – Describes a Test Suite by ID
- [**get_by_id**](#validmind.test_suites.get_by_id) – Returns the test suite by ID
- [**list_suites**](#validmind.test_suites.list_suites) – Returns a list of all available test suites
- [**register_test_suite**](#validmind.test_suites.register_test_suite) – Registers a custom test suite

**Attributes:**

- [**core_test_suites**](#validmind.test_suites.core_test_suites) –
- [**custom_test_suites**](#validmind.test_suites.custom_test_suites) –
- [**describe_test_suite**](#validmind.test_suites.describe_test_suite) –
- [**logger**](#validmind.test_suites.logger) –

#### validmind.test_suites.classifier

Test suites for sklearn-compatible classifier models

Ideal setup is to have the API client to read a
custom test suite from the project's configuration

**Classes:**

- [**ClassifierDiagnosis**](#validmind.test_suites.classifier.ClassifierDiagnosis) – Test suite for sklearn classifier model diagnosis tests
- [**ClassifierFullSuite**](#validmind.test_suites.classifier.ClassifierFullSuite) – Full test suite for binary classification models.
- [**ClassifierMetrics**](#validmind.test_suites.classifier.ClassifierMetrics) – Test suite for sklearn classifier metrics
- [**ClassifierModelValidation**](#validmind.test_suites.classifier.ClassifierModelValidation) – Test suite for binary classification models.
- [**ClassifierPerformance**](#validmind.test_suites.classifier.ClassifierPerformance) – Test suite for sklearn classifier models

##### validmind.test_suites.classifier.ClassifierDiagnosis

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for sklearn classifier model diagnosis tests

**Attributes:**

- [**suite_id**](#validmind.test_suites.classifier.ClassifierDiagnosis.suite_id) –
- [**tests**](#validmind.test_suites.classifier.ClassifierDiagnosis.tests) –

###### validmind.test_suites.classifier.ClassifierDiagnosis.suite_id

```python
suite_id = 'classifier_model_diagnosis'
```

###### validmind.test_suites.classifier.ClassifierDiagnosis.tests

```python
tests = [
    "validmind.model_validation.sklearn.OverfitDiagnosis",
    "validmind.model_validation.sklearn.WeakspotsDiagnosis",
    "validmind.model_validation.sklearn.RobustnessDiagnosis",
]

```

##### validmind.test_suites.classifier.ClassifierFullSuite

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Full test suite for binary classification models.

**Attributes:**

- [**suite_id**](#validmind.test_suites.classifier.ClassifierFullSuite.suite_id) –
- [**tests**](#validmind.test_suites.classifier.ClassifierFullSuite.tests) –

###### validmind.test_suites.classifier.ClassifierFullSuite.suite_id

```python
suite_id = 'classifier_full_suite'
```

###### validmind.test_suites.classifier.ClassifierFullSuite.tests

```python
tests = [
    {
        "section_id": TabularDatasetDescription.suite_id,
        "section_description": TabularDatasetDescription.__doc__,
        "section_tests": TabularDatasetDescription.tests,
    },
    {
        "section_id": TabularDataQuality.suite_id,
        "section_description": TabularDataQuality.__doc__,
        "section_tests": TabularDataQuality.tests,
    },
    {
        "section_id": ClassifierMetrics.suite_id,
        "section_description": ClassifierMetrics.__doc__,
        "section_tests": ClassifierMetrics.tests,
    },
    {
        "section_id": ClassifierPerformance.suite_id,
        "section_description": ClassifierPerformance.__doc__,
        "section_tests": ClassifierPerformance.tests,
    },
    {
        "section_id": ClassifierDiagnosis.suite_id,
        "section_description": ClassifierDiagnosis.__doc__,
        "section_tests": ClassifierDiagnosis.tests,
    },
]

```

##### validmind.test_suites.classifier.ClassifierMetrics

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for sklearn classifier metrics

**Attributes:**

- [**suite_id**](#validmind.test_suites.classifier.ClassifierMetrics.suite_id) –
- [**tests**](#validmind.test_suites.classifier.ClassifierMetrics.tests) –

###### validmind.test_suites.classifier.ClassifierMetrics.suite_id

```python
suite_id = 'classifier_metrics'
```

###### validmind.test_suites.classifier.ClassifierMetrics.tests

```python
tests = [
    "validmind.model_validation.ModelMetadata",
    "validmind.data_validation.DatasetSplit",
    "validmind.model_validation.sklearn.ConfusionMatrix",
    "validmind.model_validation.sklearn.ClassifierPerformance",
    "validmind.model_validation.sklearn.PermutationFeatureImportance",
    "validmind.model_validation.sklearn.PrecisionRecallCurve",
    "validmind.model_validation.sklearn.ROCCurve",
    "validmind.model_validation.sklearn.PopulationStabilityIndex",
    "validmind.model_validation.sklearn.SHAPGlobalImportance",
]

```

##### validmind.test_suites.classifier.ClassifierModelValidation

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for binary classification models.

**Attributes:**

- [**suite_id**](#validmind.test_suites.classifier.ClassifierModelValidation.suite_id) –
- [**tests**](#validmind.test_suites.classifier.ClassifierModelValidation.tests) –

###### validmind.test_suites.classifier.ClassifierModelValidation.suite_id

```python
suite_id = 'classifier_model_validation'
```

###### validmind.test_suites.classifier.ClassifierModelValidation.tests

```python
tests = [
    {
        "section_id": ClassifierMetrics.suite_id,
        "section_description": ClassifierMetrics.__doc__,
        "section_tests": ClassifierMetrics.tests,
    },
    {
        "section_id": ClassifierPerformance.suite_id,
        "section_description": ClassifierPerformance.__doc__,
        "section_tests": ClassifierPerformance.tests,
    },
    {
        "section_id": ClassifierDiagnosis.suite_id,
        "section_description": ClassifierDiagnosis.__doc__,
        "section_tests": ClassifierDiagnosis.tests,
    },
]

```

##### validmind.test_suites.classifier.ClassifierPerformance

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for sklearn classifier models

**Attributes:**

- [**suite_id**](#validmind.test_suites.classifier.ClassifierPerformance.suite_id) –
- [**tests**](#validmind.test_suites.classifier.ClassifierPerformance.tests) –

###### validmind.test_suites.classifier.ClassifierPerformance.suite_id

```python
suite_id = 'classifier_validation'
```

###### validmind.test_suites.classifier.ClassifierPerformance.tests

```python
tests = [
    "validmind.model_validation.sklearn.MinimumAccuracy",
    "validmind.model_validation.sklearn.MinimumF1Score",
    "validmind.model_validation.sklearn.MinimumROCAUCScore",
    "validmind.model_validation.sklearn.TrainingTestDegradation",
    "validmind.model_validation.sklearn.ModelsPerformanceComparison",
]

```

#### validmind.test_suites.cluster

Test suites for sklearn-compatible clustering models

Ideal setup is to have the API client to read a
custom test suite from the project's configuration

**Classes:**

- [**ClusterFullSuite**](#validmind.test_suites.cluster.ClusterFullSuite) – Full test suite for clustering models.
- [**ClusterMetrics**](#validmind.test_suites.cluster.ClusterMetrics) – Test suite for sklearn clustering metrics
- [**ClusterPerformance**](#validmind.test_suites.cluster.ClusterPerformance) – Test suite for sklearn cluster performance

##### validmind.test_suites.cluster.ClusterFullSuite

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Full test suite for clustering models.

**Attributes:**

- [**suite_id**](#validmind.test_suites.cluster.ClusterFullSuite.suite_id) –
- [**tests**](#validmind.test_suites.cluster.ClusterFullSuite.tests) –

###### validmind.test_suites.cluster.ClusterFullSuite.suite_id

```python
suite_id = 'cluster_full_suite'
```

###### validmind.test_suites.cluster.ClusterFullSuite.tests

```python
tests = [
    {
        "section_id": ClusterMetrics.suite_id,
        "section_description": ClusterMetrics.__doc__,
        "section_tests": ClusterMetrics.tests,
    },
    {
        "section_id": ClusterPerformance.suite_id,
        "section_description": ClusterPerformance.__doc__,
        "section_tests": ClusterPerformance.tests,
    },
    {
        "section_id": KmeansParametersOptimization.suite_id,
        "section_description": KmeansParametersOptimization.__doc__,
        "section_tests": KmeansParametersOptimization.tests,
    },
]

```

##### validmind.test_suites.cluster.ClusterMetrics

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for sklearn clustering metrics

**Attributes:**

- [**suite_id**](#validmind.test_suites.cluster.ClusterMetrics.suite_id) –
- [**tests**](#validmind.test_suites.cluster.ClusterMetrics.tests) –

###### validmind.test_suites.cluster.ClusterMetrics.suite_id

```python
suite_id = 'cluster_metrics'
```

###### validmind.test_suites.cluster.ClusterMetrics.tests

```python
tests = [
    "validmind.model_validation.ModelMetadata",
    "validmind.data_validation.DatasetSplit",
    "validmind.model_validation.sklearn.HomogeneityScore",
    "validmind.model_validation.sklearn.CompletenessScore",
    "validmind.model_validation.sklearn.VMeasure",
    "validmind.model_validation.sklearn.AdjustedRandIndex",
    "validmind.model_validation.sklearn.AdjustedMutualInformation",
    "validmind.model_validation.sklearn.FowlkesMallowsScore",
    "validmind.model_validation.sklearn.ClusterPerformanceMetrics",
    "validmind.model_validation.sklearn.ClusterCosineSimilarity",
    "validmind.model_validation.sklearn.SilhouettePlot",
]

```

##### validmind.test_suites.cluster.ClusterPerformance

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for sklearn cluster performance

**Attributes:**

- [**suite_id**](#validmind.test_suites.cluster.ClusterPerformance.suite_id) –
- [**tests**](#validmind.test_suites.cluster.ClusterPerformance.tests) –

###### validmind.test_suites.cluster.ClusterPerformance.suite_id

```python
suite_id = 'cluster_performance'
```

###### validmind.test_suites.cluster.ClusterPerformance.tests

```python
tests = ['validmind.model_validation.ClusterSizeDistribution']
```

#### validmind.test_suites.core_test_suites

```python
core_test_suites = {
    ClassifierDiagnosis.suite_id: ClassifierDiagnosis,
    ClassifierFullSuite.suite_id: ClassifierFullSuite,
    ClassifierMetrics.suite_id: ClassifierMetrics,
    ClassifierModelValidation.suite_id: ClassifierModelValidation,
    ClassifierPerformance.suite_id: ClassifierPerformance,
    ClusterFullSuite.suite_id: ClusterFullSuite,
    ClusterMetrics.suite_id: ClusterMetrics,
    ClusterPerformance.suite_id: ClusterPerformance,
    EmbeddingsFullSuite.suite_id: EmbeddingsFullSuite,
    EmbeddingsMetrics.suite_id: EmbeddingsMetrics,
    EmbeddingsPerformance.suite_id: EmbeddingsPerformance,
    KmeansParametersOptimization.suite_id: KmeansParametersOptimization,
    LLMClassifierFullSuite.suite_id: LLMClassifierFullSuite,
    PromptValidation.suite_id: PromptValidation,
    NLPClassifierFullSuite.suite_id: NLPClassifierFullSuite,
    RegressionMetrics.suite_id: RegressionMetrics,
    RegressionModelDescription.suite_id: RegressionModelDescription,
    RegressionModelsEvaluation.suite_id: RegressionModelsEvaluation,
    RegressionFullSuite.suite_id: RegressionFullSuite,
    RegressionPerformance.suite_id: RegressionPerformance,
    SummarizationMetrics.suite_id: SummarizationMetrics,
    TabularDataset.suite_id: TabularDataset,
    TabularDatasetDescription.suite_id: TabularDatasetDescription,
    TabularDataQuality.suite_id: TabularDataQuality,
    TextDataQuality.suite_id: TextDataQuality,
    TimeSeriesDataQuality.suite_id: TimeSeriesDataQuality,
    TimeSeriesDataset.suite_id: TimeSeriesDataset,
    TimeSeriesModelValidation.suite_id: TimeSeriesModelValidation,
    TimeSeriesMultivariate.suite_id: TimeSeriesMultivariate,
    TimeSeriesUnivariate.suite_id: TimeSeriesUnivariate,
}

```

#### validmind.test_suites.custom_test_suites

```python
custom_test_suites = {}
```

#### validmind.test_suites.describe_suite

```python
describe_suite(test_suite_id, verbose=False)
```

Describes a Test Suite by ID

**Parameters:**

- **test_suite_id** (<code>[str](#str)</code>) – Test Suite ID
- **verbose** – If True, describe all plans and tests in the Test Suite

**Returns:**

- – pandas.DataFrame: A formatted table with the Test Suite description

#### validmind.test_suites.describe_test_suite

```python
describe_test_suite = describe_suite
```

#### validmind.test_suites.embeddings

Test suites for embeddings models

Ideal setup is to have the API client to read a
custom test suite from the project's configuration

**Classes:**

- [**EmbeddingsFullSuite**](#validmind.test_suites.embeddings.EmbeddingsFullSuite) – Full test suite for embeddings models.
- [**EmbeddingsMetrics**](#validmind.test_suites.embeddings.EmbeddingsMetrics) – Test suite for embeddings metrics
- [**EmbeddingsPerformance**](#validmind.test_suites.embeddings.EmbeddingsPerformance) – Test suite for embeddings model performance

##### validmind.test_suites.embeddings.EmbeddingsFullSuite

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Full test suite for embeddings models.

**Attributes:**

- [**suite_id**](#validmind.test_suites.embeddings.EmbeddingsFullSuite.suite_id) –
- [**tests**](#validmind.test_suites.embeddings.EmbeddingsFullSuite.tests) –

###### validmind.test_suites.embeddings.EmbeddingsFullSuite.suite_id

```python
suite_id = 'embeddings_full_suite'
```

###### validmind.test_suites.embeddings.EmbeddingsFullSuite.tests

```python
tests = [
    {
        "section_id": EmbeddingsMetrics.suite_id,
        "section_description": EmbeddingsMetrics.__doc__,
        "section_tests": EmbeddingsMetrics.tests,
    },
    {
        "section_id": EmbeddingsPerformance.suite_id,
        "section_description": EmbeddingsPerformance.__doc__,
        "section_tests": EmbeddingsPerformance.tests,
    },
]

```

##### validmind.test_suites.embeddings.EmbeddingsMetrics

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for embeddings metrics

**Attributes:**

- [**suite_id**](#validmind.test_suites.embeddings.EmbeddingsMetrics.suite_id) –
- [**tests**](#validmind.test_suites.embeddings.EmbeddingsMetrics.tests) –

###### validmind.test_suites.embeddings.EmbeddingsMetrics.suite_id

```python
suite_id = 'embeddings_metrics'
```

###### validmind.test_suites.embeddings.EmbeddingsMetrics.tests

```python
tests = [
    "validmind.model_validation.ModelMetadata",
    "validmind.data_validation.DatasetSplit",
    "validmind.model_validation.embeddings.DescriptiveAnalytics",
    "validmind.model_validation.embeddings.CosineSimilarityDistribution",
    "validmind.model_validation.embeddings.ClusterDistribution",
    "validmind.model_validation.embeddings.EmbeddingsVisualization2D",
]

```

##### validmind.test_suites.embeddings.EmbeddingsPerformance

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for embeddings model performance

**Attributes:**

- [**suite_id**](#validmind.test_suites.embeddings.EmbeddingsPerformance.suite_id) –
- [**tests**](#validmind.test_suites.embeddings.EmbeddingsPerformance.tests) –

###### validmind.test_suites.embeddings.EmbeddingsPerformance.suite_id

```python
suite_id = 'embeddings_model_performance'
```

###### validmind.test_suites.embeddings.EmbeddingsPerformance.tests

```python
tests = [
    "validmind.model_validation.embeddings.StabilityAnalysisRandomNoise",
    "validmind.model_validation.embeddings.StabilityAnalysisSynonyms",
    "validmind.model_validation.embeddings.StabilityAnalysisKeyword",
    "validmind.model_validation.embeddings.StabilityAnalysisTranslation",
]

```

#### validmind.test_suites.get_by_id

```python
get_by_id(test_suite_id)
```

Returns the test suite by ID

#### validmind.test_suites.list_suites

```python
list_suites(pretty=True)
```

Returns a list of all available test suites

#### validmind.test_suites.llm

Test suites for LLMs

**Classes:**

- [**LLMClassifierFullSuite**](#validmind.test_suites.llm.LLMClassifierFullSuite) – Full test suite for LLM classification models.
- [**PromptValidation**](#validmind.test_suites.llm.PromptValidation) – Test suite for prompt validation

##### validmind.test_suites.llm.LLMClassifierFullSuite

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Full test suite for LLM classification models.

**Attributes:**

- [**suite_id**](#validmind.test_suites.llm.LLMClassifierFullSuite.suite_id) –
- [**tests**](#validmind.test_suites.llm.LLMClassifierFullSuite.tests) –

###### validmind.test_suites.llm.LLMClassifierFullSuite.suite_id

```python
suite_id = 'llm_classifier_full_suite'
```

###### validmind.test_suites.llm.LLMClassifierFullSuite.tests

```python
tests = [
    {
        "section_id": TextDataQuality.suite_id,
        "section_description": TextDataQuality.__doc__,
        "section_tests": TextDataQuality.tests,
    },
    {
        "section_id": ClassifierMetrics.suite_id,
        "section_description": ClassifierMetrics.__doc__,
        "section_tests": ClassifierMetrics.tests,
    },
    {
        "section_id": ClassifierPerformance.suite_id,
        "section_description": ClassifierPerformance.__doc__,
        "section_tests": ClassifierPerformance.tests,
    },
    {
        "section_id": ClassifierDiagnosis.suite_id,
        "section_description": ClassifierDiagnosis.__doc__,
        "section_tests": ClassifierDiagnosis.tests,
    },
    {
        "section_id": PromptValidation.suite_id,
        "section_description": PromptValidation.__doc__,
        "section_tests": PromptValidation.tests,
    },
]

```

##### validmind.test_suites.llm.PromptValidation

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for prompt validation

**Attributes:**

- [**suite_id**](#validmind.test_suites.llm.PromptValidation.suite_id) –
- [**tests**](#validmind.test_suites.llm.PromptValidation.tests) –

###### validmind.test_suites.llm.PromptValidation.suite_id

```python
suite_id = 'prompt_validation'
```

###### validmind.test_suites.llm.PromptValidation.tests

```python
tests = [
    "validmind.prompt_validation.Bias",
    "validmind.prompt_validation.Clarity",
    "validmind.prompt_validation.Conciseness",
    "validmind.prompt_validation.Delimitation",
    "validmind.prompt_validation.NegativeInstruction",
    "validmind.prompt_validation.Robustness",
    "validmind.prompt_validation.Specificity",
]

```

#### validmind.test_suites.logger

```python
logger = get_logger(__name__)
```

#### validmind.test_suites.nlp

Test suites for NLP models

**Classes:**

- [**NLPClassifierFullSuite**](#validmind.test_suites.nlp.NLPClassifierFullSuite) – Full test suite for NLP classification models.

##### validmind.test_suites.nlp.NLPClassifierFullSuite

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Full test suite for NLP classification models.

**Attributes:**

- [**suite_id**](#validmind.test_suites.nlp.NLPClassifierFullSuite.suite_id) –
- [**tests**](#validmind.test_suites.nlp.NLPClassifierFullSuite.tests) –

###### validmind.test_suites.nlp.NLPClassifierFullSuite.suite_id

```python
suite_id = 'nlp_classifier_full_suite'
```

###### validmind.test_suites.nlp.NLPClassifierFullSuite.tests

```python
tests = [
    {
        "section_id": TextDataQuality.suite_id,
        "section_description": TextDataQuality.__doc__,
        "section_tests": TextDataQuality.tests,
    },
    {
        "section_id": ClassifierMetrics.suite_id,
        "section_description": ClassifierMetrics.__doc__,
        "section_tests": ClassifierMetrics.tests,
    },
    {
        "section_id": ClassifierPerformance.suite_id,
        "section_description": ClassifierPerformance.__doc__,
        "section_tests": ClassifierPerformance.tests,
    },
    {
        "section_id": ClassifierDiagnosis.suite_id,
        "section_description": ClassifierDiagnosis.__doc__,
        "section_tests": ClassifierDiagnosis.tests,
    },
]

```

#### validmind.test_suites.parameters_optimization

Test suites for sklearn-compatible hyper parameters tunning

Ideal setup is to have the API client to read a
custom test suite from the project's configuration

**Classes:**

- [**KmeansParametersOptimization**](#validmind.test_suites.parameters_optimization.KmeansParametersOptimization) – Test suite for sklearn hyperparameters optimization

##### validmind.test_suites.parameters_optimization.KmeansParametersOptimization

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for sklearn hyperparameters optimization

**Attributes:**

- [**suite_id**](#validmind.test_suites.parameters_optimization.KmeansParametersOptimization.suite_id) –
- [**tests**](#validmind.test_suites.parameters_optimization.KmeansParametersOptimization.tests) –

###### validmind.test_suites.parameters_optimization.KmeansParametersOptimization.suite_id

```python
suite_id = 'hyper_parameters_optimization'
```

###### validmind.test_suites.parameters_optimization.KmeansParametersOptimization.tests

```python
tests = [
    "validmind.model_validation.sklearn.HyperParametersTuning",
    "validmind.model_validation.sklearn.KMeansClustersOptimization",
]

```

#### validmind.test_suites.register_test_suite

```python
register_test_suite(suite_id, suite)
```

Registers a custom test suite

#### validmind.test_suites.regression

**Classes:**

- [**RegressionFullSuite**](#validmind.test_suites.regression.RegressionFullSuite) – Full test suite for regression models.
- [**RegressionMetrics**](#validmind.test_suites.regression.RegressionMetrics) – Test suite for performance metrics of regression metrics
- [**RegressionPerformance**](#validmind.test_suites.regression.RegressionPerformance) – Test suite for regression model performance

##### validmind.test_suites.regression.RegressionFullSuite

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Full test suite for regression models.

**Attributes:**

- [**suite_id**](#validmind.test_suites.regression.RegressionFullSuite.suite_id) –
- [**tests**](#validmind.test_suites.regression.RegressionFullSuite.tests) –

###### validmind.test_suites.regression.RegressionFullSuite.suite_id

```python
suite_id = 'regression_full_suite'
```

###### validmind.test_suites.regression.RegressionFullSuite.tests

```python
tests = [
    {
        "section_id": TabularDatasetDescription.suite_id,
        "section_description": TabularDatasetDescription.__doc__,
        "section_tests": TabularDatasetDescription.tests,
    },
    {
        "section_id": TabularDataQuality.suite_id,
        "section_description": TabularDataQuality.__doc__,
        "section_tests": TabularDataQuality.tests,
    },
    {
        "section_id": RegressionMetrics.suite_id,
        "section_description": RegressionMetrics.__doc__,
        "section_tests": RegressionMetrics.tests,
    },
    {
        "section_id": RegressionPerformance.suite_id,
        "section_description": RegressionPerformance.__doc__,
        "section_tests": RegressionPerformance.tests,
    },
]

```

##### validmind.test_suites.regression.RegressionMetrics

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for performance metrics of regression metrics

**Attributes:**

- [**suite_id**](#validmind.test_suites.regression.RegressionMetrics.suite_id) –
- [**tests**](#validmind.test_suites.regression.RegressionMetrics.tests) –

###### validmind.test_suites.regression.RegressionMetrics.suite_id

```python
suite_id = 'regression_metrics'
```

###### validmind.test_suites.regression.RegressionMetrics.tests

```python
tests = [
    "validmind.data_validation.DatasetSplit",
    "validmind.model_validation.ModelMetadata",
    "validmind.model_validation.sklearn.PermutationFeatureImportance",
]

```

##### validmind.test_suites.regression.RegressionPerformance

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for regression model performance

**Attributes:**

- [**suite_id**](#validmind.test_suites.regression.RegressionPerformance.suite_id) –
- [**tests**](#validmind.test_suites.regression.RegressionPerformance.tests) –

###### validmind.test_suites.regression.RegressionPerformance.suite_id

```python
suite_id = 'regression_performance'
```

###### validmind.test_suites.regression.RegressionPerformance.tests

```python
tests = [
    "validmind.model_validation.sklearn.RegressionErrors",
    "validmind.model_validation.sklearn.RegressionR2Square",
]

```

#### validmind.test_suites.statsmodels_timeseries

Time Series Test Suites from statsmodels

**Classes:**

- [**RegressionModelDescription**](#validmind.test_suites.statsmodels_timeseries.RegressionModelDescription) – Test suite for performance metric of regression model of statsmodels library
- [**RegressionModelsEvaluation**](#validmind.test_suites.statsmodels_timeseries.RegressionModelsEvaluation) – Test suite for metrics comparison of regression model of statsmodels library

##### validmind.test_suites.statsmodels_timeseries.RegressionModelDescription

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for performance metric of regression model of statsmodels library

**Attributes:**

- [**suite_id**](#validmind.test_suites.statsmodels_timeseries.RegressionModelDescription.suite_id) –
- [**tests**](#validmind.test_suites.statsmodels_timeseries.RegressionModelDescription.tests) –

###### validmind.test_suites.statsmodels_timeseries.RegressionModelDescription.suite_id

```python
suite_id = 'regression_model_description'
```

###### validmind.test_suites.statsmodels_timeseries.RegressionModelDescription.tests

```python
tests = [
    "validmind.data_validation.DatasetSplit",
    "validmind.model_validation.ModelMetadata",
]

```

##### validmind.test_suites.statsmodels_timeseries.RegressionModelsEvaluation

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for metrics comparison of regression model of statsmodels library

**Attributes:**

- [**suite_id**](#validmind.test_suites.statsmodels_timeseries.RegressionModelsEvaluation.suite_id) –
- [**tests**](#validmind.test_suites.statsmodels_timeseries.RegressionModelsEvaluation.tests) –

###### validmind.test_suites.statsmodels_timeseries.RegressionModelsEvaluation.suite_id

```python
suite_id = 'regression_models_evaluation'
```

###### validmind.test_suites.statsmodels_timeseries.RegressionModelsEvaluation.tests

```python
tests = [
    "validmind.model_validation.statsmodels.RegressionModelCoeffs",
    "validmind.model_validation.sklearn.RegressionModelsPerformanceComparison",
]

```

#### validmind.test_suites.summarization

Test suites for llm summarization models

**Classes:**

- [**SummarizationMetrics**](#validmind.test_suites.summarization.SummarizationMetrics) – Test suite for Summarization metrics

##### validmind.test_suites.summarization.SummarizationMetrics

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for Summarization metrics

**Attributes:**

- [**suite_id**](#validmind.test_suites.summarization.SummarizationMetrics.suite_id) –
- [**tests**](#validmind.test_suites.summarization.SummarizationMetrics.tests) –

###### validmind.test_suites.summarization.SummarizationMetrics.suite_id

```python
suite_id = 'summarization_metrics'
```

###### validmind.test_suites.summarization.SummarizationMetrics.tests

```python
tests = [
    "validmind.model_validation.TokenDisparity",
    "validmind.model_validation.BleuScore",
    "validmind.model_validation.BertScore",
    "validmind.model_validation.ContextualRecall",
]

```

#### validmind.test_suites.tabular_datasets

Test suites for tabular datasets

**Classes:**

- [**TabularDataQuality**](#validmind.test_suites.tabular_datasets.TabularDataQuality) – Test suite for data quality on tabular datasets
- [**TabularDataset**](#validmind.test_suites.tabular_datasets.TabularDataset) – Test suite for tabular datasets.
- [**TabularDatasetDescription**](#validmind.test_suites.tabular_datasets.TabularDatasetDescription) – Test suite to extract metadata and descriptive

##### validmind.test_suites.tabular_datasets.TabularDataQuality

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for data quality on tabular datasets

**Attributes:**

- [**suite_id**](#validmind.test_suites.tabular_datasets.TabularDataQuality.suite_id) –
- [**tests**](#validmind.test_suites.tabular_datasets.TabularDataQuality.tests) –

###### validmind.test_suites.tabular_datasets.TabularDataQuality.suite_id

```python
suite_id = 'tabular_data_quality'
```

###### validmind.test_suites.tabular_datasets.TabularDataQuality.tests

```python
tests = [
    "validmind.data_validation.ClassImbalance",
    "validmind.data_validation.Duplicates",
    "validmind.data_validation.HighCardinality",
    "validmind.data_validation.HighPearsonCorrelation",
    "validmind.data_validation.MissingValues",
    "validmind.data_validation.Skewness",
    "validmind.data_validation.UniqueRows",
    "validmind.data_validation.TooManyZeroValues",
]

```

##### validmind.test_suites.tabular_datasets.TabularDataset

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for tabular datasets.

**Attributes:**

- [**suite_id**](#validmind.test_suites.tabular_datasets.TabularDataset.suite_id) –
- [**tests**](#validmind.test_suites.tabular_datasets.TabularDataset.tests) –

###### validmind.test_suites.tabular_datasets.TabularDataset.suite_id

```python
suite_id = 'tabular_dataset'
```

###### validmind.test_suites.tabular_datasets.TabularDataset.tests

```python
tests = [
    {
        "section_id": TabularDatasetDescription.suite_id,
        "section_description": TabularDatasetDescription.__doc__,
        "section_tests": TabularDatasetDescription.tests,
    },
    {
        "section_id": TabularDataQuality.suite_id,
        "section_description": TabularDataQuality.__doc__,
        "section_tests": TabularDataQuality.tests,
    },
]

```

##### validmind.test_suites.tabular_datasets.TabularDatasetDescription

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite to extract metadata and descriptive
statistics from a tabular dataset

**Attributes:**

- [**suite_id**](#validmind.test_suites.tabular_datasets.TabularDatasetDescription.suite_id) –
- [**tests**](#validmind.test_suites.tabular_datasets.TabularDatasetDescription.tests) –

###### validmind.test_suites.tabular_datasets.TabularDatasetDescription.suite_id

```python
suite_id = 'tabular_dataset_description'
```

###### validmind.test_suites.tabular_datasets.TabularDatasetDescription.tests

```python
tests = [
    "validmind.data_validation.DatasetDescription",
    "validmind.data_validation.DescriptiveStatistics",
    "validmind.data_validation.PearsonCorrelationMatrix",
]

```

#### validmind.test_suites.text_data

Test suites for text datasets

**Classes:**

- [**TextDataQuality**](#validmind.test_suites.text_data.TextDataQuality) – Test suite for data quality on text data

##### validmind.test_suites.text_data.TextDataQuality

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for data quality on text data

**Attributes:**

- [**suite_id**](#validmind.test_suites.text_data.TextDataQuality.suite_id) –
- [**tests**](#validmind.test_suites.text_data.TextDataQuality.tests) –

###### validmind.test_suites.text_data.TextDataQuality.suite_id

```python
suite_id = 'text_data_quality'
```

###### validmind.test_suites.text_data.TextDataQuality.tests

```python
tests = [
    "validmind.data_validation.ClassImbalance",
    "validmind.data_validation.Duplicates",
    "validmind.data_validation.nlp.StopWords",
    "validmind.data_validation.nlp.Punctuations",
    "validmind.data_validation.nlp.CommonWords",
    "validmind.data_validation.nlp.TextDescription",
]

```

#### validmind.test_suites.time_series

Time Series Test Suites

**Classes:**

- [**TimeSeriesDataQuality**](#validmind.test_suites.time_series.TimeSeriesDataQuality) – Test suite for data quality on time series datasets
- [**TimeSeriesDataset**](#validmind.test_suites.time_series.TimeSeriesDataset) – Test suite for time series datasets.
- [**TimeSeriesModelValidation**](#validmind.test_suites.time_series.TimeSeriesModelValidation) – Test suite for time series model validation.
- [**TimeSeriesMultivariate**](#validmind.test_suites.time_series.TimeSeriesMultivariate) – This test suite provides a preliminary understanding of the features
- [**TimeSeriesUnivariate**](#validmind.test_suites.time_series.TimeSeriesUnivariate) – This test suite provides a preliminary understanding of the target variable(s)

##### validmind.test_suites.time_series.TimeSeriesDataQuality

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for data quality on time series datasets

**Attributes:**

- [**suite_id**](#validmind.test_suites.time_series.TimeSeriesDataQuality.suite_id) –
- [**tests**](#validmind.test_suites.time_series.TimeSeriesDataQuality.tests) –

###### validmind.test_suites.time_series.TimeSeriesDataQuality.suite_id

```python
suite_id = 'time_series_data_quality'
```

###### validmind.test_suites.time_series.TimeSeriesDataQuality.tests

```python
tests = [
    "validmind.data_validation.TimeSeriesOutliers",
    "validmind.data_validation.TimeSeriesMissingValues",
    "validmind.data_validation.TimeSeriesFrequency",
]

```

##### validmind.test_suites.time_series.TimeSeriesDataset

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for time series datasets.

**Attributes:**

- [**suite_id**](#validmind.test_suites.time_series.TimeSeriesDataset.suite_id) –
- [**tests**](#validmind.test_suites.time_series.TimeSeriesDataset.tests) –

###### validmind.test_suites.time_series.TimeSeriesDataset.suite_id

```python
suite_id = 'time_series_dataset'
```

###### validmind.test_suites.time_series.TimeSeriesDataset.tests

```python
tests = [
    {
        "section_id": TimeSeriesDataQuality.suite_id,
        "section_description": TimeSeriesDataQuality.__doc__,
        "section_tests": TimeSeriesDataQuality.tests,
    },
    {
        "section_id": TimeSeriesUnivariate.suite_id,
        "section_description": TimeSeriesUnivariate.__doc__,
        "section_tests": TimeSeriesUnivariate.tests,
    },
    {
        "section_id": TimeSeriesMultivariate.suite_id,
        "section_description": TimeSeriesMultivariate.__doc__,
        "section_tests": TimeSeriesMultivariate.tests,
    },
]

```

##### validmind.test_suites.time_series.TimeSeriesModelValidation

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

Test suite for time series model validation.

**Attributes:**

- [**suite_id**](#validmind.test_suites.time_series.TimeSeriesModelValidation.suite_id) –
- [**tests**](#validmind.test_suites.time_series.TimeSeriesModelValidation.tests) –

###### validmind.test_suites.time_series.TimeSeriesModelValidation.suite_id

```python
suite_id = 'time_series_model_validation'
```

###### validmind.test_suites.time_series.TimeSeriesModelValidation.tests

```python
tests = [
    {
        "section_id": RegressionModelDescription.suite_id,
        "section_description": RegressionModelDescription.__doc__,
        "section_tests": RegressionModelDescription.tests,
    },
    {
        "section_id": RegressionModelsEvaluation.suite_id,
        "section_description": RegressionModelsEvaluation.__doc__,
        "section_tests": RegressionModelsEvaluation.tests,
    },
]

```

##### validmind.test_suites.time_series.TimeSeriesMultivariate

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

This test suite provides a preliminary understanding of the features
and relationship in multivariate dataset. It presents various
multivariate visualizations that can help identify patterns, trends,
and relationships between pairs of variables. The visualizations are
designed to explore the relationships between multiple features
simultaneously. They allow you to quickly identify any patterns or
trends in the data, as well as any potential outliers or anomalies.
The individual feature distribution can also be explored to provide
insight into the range and frequency of values observed in the data.
This multivariate analysis test suite aims to provide an overview of
the data structure and guide further exploration and modeling.

**Attributes:**

- [**suite_id**](#validmind.test_suites.time_series.TimeSeriesMultivariate.suite_id) –
- [**tests**](#validmind.test_suites.time_series.TimeSeriesMultivariate.tests) –

###### validmind.test_suites.time_series.TimeSeriesMultivariate.suite_id

```python
suite_id = 'time_series_multivariate'
```

###### validmind.test_suites.time_series.TimeSeriesMultivariate.tests

```python
tests = [
    "validmind.data_validation.ScatterPlot",
    "validmind.data_validation.LaggedCorrelationHeatmap",
    "validmind.data_validation.EngleGrangerCoint",
    "validmind.data_validation.SpreadPlot",
]

```

##### validmind.test_suites.time_series.TimeSeriesUnivariate

Bases: <code>[TestSuite](#validmind.vm_models.TestSuite)</code>

This test suite provides a preliminary understanding of the target variable(s)
used in the time series dataset. It visualizations that present the raw time
series data and a histogram of the target variable(s).

The raw time series data provides a visual inspection of the target variable's
behavior over time. This helps to identify any patterns or trends in the data,
as well as any potential outliers or anomalies. The histogram of the target
variable displays the distribution of values, providing insight into the range
and frequency of values observed in the data.

**Attributes:**

- [**suite_id**](#validmind.test_suites.time_series.TimeSeriesUnivariate.suite_id) –
- [**tests**](#validmind.test_suites.time_series.TimeSeriesUnivariate.tests) –

###### validmind.test_suites.time_series.TimeSeriesUnivariate.suite_id

```python
suite_id = 'time_series_univariate'
```

###### validmind.test_suites.time_series.TimeSeriesUnivariate.tests

```python
tests = [
    "validmind.data_validation.TimeSeriesLinePlot",
    "validmind.data_validation.TimeSeriesHistogram",
    "validmind.data_validation.ACFandPACFPlot",
    "validmind.data_validation.SeasonalDecompose",
    "validmind.data_validation.AutoSeasonality",
    "validmind.data_validation.AutoStationarity",
    "validmind.data_validation.RollingStatsPlot",
    "validmind.data_validation.AutoAR",
    "validmind.data_validation.AutoMA",
]

```

### validmind.tests

ValidMind Tests Module

**Modules:**

- [**comparison**](#validmind.tests.comparison) –
- [**data_validation**](#validmind.tests.data_validation) –
- [**decorator**](#validmind.tests.decorator) – Decorators for creating and registering tests with the ValidMind Library.
- [**load**](#validmind.tests.load) – Module for listing and loading tests.
- [**model_validation**](#validmind.tests.model_validation) –
- [**output**](#validmind.tests.output) –
- [**prompt_validation**](#validmind.tests.prompt_validation) –
- [**run**](#validmind.tests.run) –
- [**test_providers**](#validmind.tests.test_providers) –

**Classes:**

- [**LoadTestError**](#validmind.tests.LoadTestError) – Exception raised when an error occurs while loading a test
- [**LocalTestProvider**](#validmind.tests.LocalTestProvider) – Test providers in ValidMind are responsible for loading tests from different sources,
- [**TestProvider**](#validmind.tests.TestProvider) – Protocol for user-defined test providers

**Functions:**

- [**describe_test**](#validmind.tests.describe_test) – Get or show details about the test
- [**list_tags**](#validmind.tests.list_tags) – List unique tags from all test classes.
- [**list_tasks**](#validmind.tests.list_tasks) – List unique tasks from all test classes.
- [**list_tasks_and_tags**](#validmind.tests.list_tasks_and_tags) – List all task types and their associated tags, with one row per task type and
- [**list_tests**](#validmind.tests.list_tests) – List all tests in the tests directory.
- [**load_test**](#validmind.tests.load_test) – Load a test by test ID
- [**register_test_provider**](#validmind.tests.register_test_provider) – Register an external test provider
- [**run_test**](#validmind.tests.run_test) – Run a ValidMind or custom test
- [**tags**](#validmind.tests.tags) – Decorator for specifying tags for a test.
- [**tasks**](#validmind.tests.tasks) – Decorator for specifying the task types that a test is designed for.
- [**test**](#validmind.tests.test) – Decorator for creating and registering custom tests

#### validmind.tests.LoadTestError

```python
LoadTestError(message, original_error=None)
```

Bases: <code>[BaseError](#validmind.errors.BaseError)</code>

Exception raised when an error occurs while loading a test

**Functions:**

- [**description**](#validmind.tests.LoadTestError.description) –

**Attributes:**

- [**message**](#validmind.tests.LoadTestError.message) –
- [**original_error**](#validmind.tests.LoadTestError.original_error) –

##### validmind.tests.LoadTestError.description

```python
description(*args, **kwargs)
```

##### validmind.tests.LoadTestError.message

```python
message = message
```

##### validmind.tests.LoadTestError.original_error

```python
original_error = original_error
```

#### validmind.tests.LocalTestProvider

```python
LocalTestProvider(root_folder)
```

Test providers in ValidMind are responsible for loading tests from different sources,
such as local files, databases, or remote services. The LocalTestProvider specifically
loads tests from the local file system.

To use the LocalTestProvider, you need to provide the root_folder, which is the
root directory for local tests. The test_id is a combination of the namespace (set
when registering the test provider) and the path to the test class module, where
slashes are replaced by dots and the .py extension is left out.

Example usage:

```
# Create an instance of LocalTestProvider with the root folder
test_provider = LocalTestProvider("/path/to/tests/folder")

# Register the test provider with a namespace
register_test_provider("my_namespace", test_provider)

# List all tests in the namespace (returns a list of test IDs)
test_provider.list_tests()
# this is used by the validmind.tests.list_tests() function to aggregate all tests
# from all test providers

# Load a test using the test_id (namespace + path to test class module)
test = test_provider.load_test("my_namespace.my_test_class")
# full path to the test class module is /path/to/tests/folder/my_test_class.py
```

**Attributes:**

- [**root_folder**](#validmind.tests.LocalTestProvider.root_folder) (<code>[str](#str)</code>) – The root directory for local tests.

**Functions:**

- [**list_tests**](#validmind.tests.LocalTestProvider.list_tests) – List all tests in the given namespace
- [**load_test**](#validmind.tests.LocalTestProvider.load_test) – Load the test identified by the given test_id.

**Attributes:**

- [**root_folder**](#validmind.tests.LocalTestProvider.root_folder) –

Initialize the LocalTestProvider with the given root_folder
(see class docstring for details)

**Parameters:**

- **root_folder** (<code>[str](#str)</code>) – The root directory for local tests.

##### validmind.tests.LocalTestProvider.list_tests

```python
list_tests()
```

List all tests in the given namespace

**Returns:**

- **list** – A list of test IDs

##### validmind.tests.LocalTestProvider.load_test

```python
load_test(test_id)
```

Load the test identified by the given test_id.

**Parameters:**

- **test_id** (<code>[str](#str)</code>) – The identifier of the test. This corresponds to the relative

**Returns:**

- – The test class that matches the last part of the test_id.

**Raises:**

- <code>[LocalTestProviderLoadModuleError](#LocalTestProviderLoadModuleError)</code> – If the test module cannot be imported
- <code>[LocalTestProviderLoadTestError](#LocalTestProviderLoadTestError)</code> – If the test class cannot be found in the module

##### validmind.tests.LocalTestProvider.root_folder

```python
root_folder = os.path.abspath(root_folder)
```

#### validmind.tests.TestProvider

Bases: <code>[Protocol](#typing.Protocol)</code>

Protocol for user-defined test providers

**Functions:**

- [**list_tests**](#validmind.tests.TestProvider.list_tests) – List all tests in the given namespace
- [**load_test**](#validmind.tests.TestProvider.load_test) – Load the test function identified by the given test_id

##### validmind.tests.TestProvider.list_tests

```python
list_tests()
```

List all tests in the given namespace

**Returns:**

- **list** (<code>[List](#typing.List)\[[str](#str)\]</code>) – A list of test IDs

##### validmind.tests.TestProvider.load_test

```python
load_test(test_id)
```

Load the test function identified by the given test_id

**Parameters:**

- **test_id** (<code>[str](#str)</code>) – The test ID (does not contain the namespace under which
  the test is registered)

**Returns:**

- **callable** (<code>[callable](#callable)</code>) – The test function

**Raises:**

- <code>[FileNotFoundError](#FileNotFoundError)</code> – If the test is not found

#### validmind.tests.comparison

**Functions:**

- [**combine_results**](#validmind.tests.comparison.combine_results) – Combine multiple test results into a single set of outputs.
- [**get_comparison_test_configs**](#validmind.tests.comparison.get_comparison_test_configs) – Generate test configurations based on input and parameter grids.

**Attributes:**

- [**logger**](#validmind.tests.comparison.logger) –

##### validmind.tests.comparison.combine_results

```python
combine_results(results)
```

Combine multiple test results into a single set of outputs.

**Parameters:**

- **results** (<code>[List](#typing.List)\[[TestResult](#validmind.vm_models.result.TestResult)\]</code>) – A list of TestResult objects to combine.

**Returns:**

- <code>[Tuple](#typing.Tuple)\[[List](#typing.List)\[[Any](#typing.Any)\], [Dict](#typing.Dict)\[[str](#str), [List](#typing.List)\[[Any](#typing.Any)\]\], [Dict](#typing.Dict)\[[str](#str), [List](#typing.List)\[[Any](#typing.Any)\]\]\]</code> – A tuple containing:
- A list of combined outputs (tables and figures).
- A dictionary of inputs with lists of all values.
- A dictionary of parameters with lists of all values.

##### validmind.tests.comparison.get_comparison_test_configs

```python
get_comparison_test_configs(
    input_grid=None, param_grid=None, inputs=None, params=None
)
```

Generate test configurations based on input and parameter grids.

Function inputs should be validated before calling this.

**Parameters:**

- **input_grid** (<code>[Union](#typing.Union)\[[Dict](#typing.Dict)\[[str](#str), [List](#typing.List)\[[Any](#typing.Any)\]\], [List](#typing.List)\[[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]\], None\]</code>) – A dictionary or list defining the grid of inputs.
- **param_grid** (<code>[Union](#typing.Union)\[[Dict](#typing.Dict)\[[str](#str), [List](#typing.List)\[[Any](#typing.Any)\]\], [List](#typing.List)\[[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]\], None\]</code>) – A dictionary or list defining the grid of parameters.
- **inputs** (<code>[Union](#typing.Union)\[[Dict](#typing.Dict)\[[str](#str), [Union](#typing.Union)\[[VMInput](#validmind.vm_models.input.VMInput), [List](#typing.List)\[[VMInput](#validmind.vm_models.input.VMInput)\]\]\], None\]</code>) – A dictionary of inputs.
- **params** (<code>[Union](#typing.Union)\[[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\], None\]</code>) – A dictionary of parameters.

**Returns:**

- <code>[List](#typing.List)\[[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]\]</code> – A list of test configurations.

##### validmind.tests.comparison.logger

```python
logger = get_logger(__name__)
```

#### validmind.tests.data_validation

**Modules:**

- [**ACFandPACFPlot**](#validmind.tests.data_validation.ACFandPACFPlot) –
- [**ADF**](#validmind.tests.data_validation.ADF) –
- [**AutoAR**](#validmind.tests.data_validation.AutoAR) –
- [**AutoMA**](#validmind.tests.data_validation.AutoMA) –
- [**AutoSeasonality**](#validmind.tests.data_validation.AutoSeasonality) –
- [**AutoStationarity**](#validmind.tests.data_validation.AutoStationarity) –
- [**BivariateScatterPlots**](#validmind.tests.data_validation.BivariateScatterPlots) –
- [**BoxPierce**](#validmind.tests.data_validation.BoxPierce) –
- [**ChiSquaredFeaturesTable**](#validmind.tests.data_validation.ChiSquaredFeaturesTable) –
- [**ClassImbalance**](#validmind.tests.data_validation.ClassImbalance) – Threshold based tests
- [**DatasetDescription**](#validmind.tests.data_validation.DatasetDescription) –
- [**DatasetSplit**](#validmind.tests.data_validation.DatasetSplit) –
- [**DescriptiveStatistics**](#validmind.tests.data_validation.DescriptiveStatistics) –
- [**DickeyFullerGLS**](#validmind.tests.data_validation.DickeyFullerGLS) –
- [**Duplicates**](#validmind.tests.data_validation.Duplicates) –
- [**EngleGrangerCoint**](#validmind.tests.data_validation.EngleGrangerCoint) –
- [**FeatureTargetCorrelationPlot**](#validmind.tests.data_validation.FeatureTargetCorrelationPlot) –
- [**HighCardinality**](#validmind.tests.data_validation.HighCardinality) –
- [**HighPearsonCorrelation**](#validmind.tests.data_validation.HighPearsonCorrelation) –
- [**IQROutliersBarPlot**](#validmind.tests.data_validation.IQROutliersBarPlot) –
- [**IQROutliersTable**](#validmind.tests.data_validation.IQROutliersTable) –
- [**IsolationForestOutliers**](#validmind.tests.data_validation.IsolationForestOutliers) –
- [**JarqueBera**](#validmind.tests.data_validation.JarqueBera) –
- [**KPSS**](#validmind.tests.data_validation.KPSS) –
- [**LJungBox**](#validmind.tests.data_validation.LJungBox) –
- [**LaggedCorrelationHeatmap**](#validmind.tests.data_validation.LaggedCorrelationHeatmap) –
- [**MissingValues**](#validmind.tests.data_validation.MissingValues) –
- [**MissingValuesBarPlot**](#validmind.tests.data_validation.MissingValuesBarPlot) –
- [**PearsonCorrelationMatrix**](#validmind.tests.data_validation.PearsonCorrelationMatrix) –
- [**PhillipsPerronArch**](#validmind.tests.data_validation.PhillipsPerronArch) –
- [**ProtectedClassesCombination**](#validmind.tests.data_validation.ProtectedClassesCombination) –
- [**ProtectedClassesDescription**](#validmind.tests.data_validation.ProtectedClassesDescription) –
- [**ProtectedClassesDisparity**](#validmind.tests.data_validation.ProtectedClassesDisparity) –
- [**ProtectedClassesThresholdOptimizer**](#validmind.tests.data_validation.ProtectedClassesThresholdOptimizer) –
- [**RollingStatsPlot**](#validmind.tests.data_validation.RollingStatsPlot) –
- [**RunsTest**](#validmind.tests.data_validation.RunsTest) –
- [**ScatterPlot**](#validmind.tests.data_validation.ScatterPlot) –
- [**SeasonalDecompose**](#validmind.tests.data_validation.SeasonalDecompose) –
- [**ShapiroWilk**](#validmind.tests.data_validation.ShapiroWilk) –
- [**Skewness**](#validmind.tests.data_validation.Skewness) –
- [**SpreadPlot**](#validmind.tests.data_validation.SpreadPlot) –
- [**TabularCategoricalBarPlots**](#validmind.tests.data_validation.TabularCategoricalBarPlots) –
- [**TabularDateTimeHistograms**](#validmind.tests.data_validation.TabularDateTimeHistograms) –
- [**TabularDescriptionTables**](#validmind.tests.data_validation.TabularDescriptionTables) –
- [**TabularNumericalHistograms**](#validmind.tests.data_validation.TabularNumericalHistograms) –
- [**TargetRateBarPlots**](#validmind.tests.data_validation.TargetRateBarPlots) –
- [**TimeSeriesDescription**](#validmind.tests.data_validation.TimeSeriesDescription) –
- [**TimeSeriesDescriptiveStatistics**](#validmind.tests.data_validation.TimeSeriesDescriptiveStatistics) –
- [**TimeSeriesFrequency**](#validmind.tests.data_validation.TimeSeriesFrequency) –
- [**TimeSeriesHistogram**](#validmind.tests.data_validation.TimeSeriesHistogram) –
- [**TimeSeriesLinePlot**](#validmind.tests.data_validation.TimeSeriesLinePlot) –
- [**TimeSeriesMissingValues**](#validmind.tests.data_validation.TimeSeriesMissingValues) –
- [**TimeSeriesOutliers**](#validmind.tests.data_validation.TimeSeriesOutliers) –
- [**TooManyZeroValues**](#validmind.tests.data_validation.TooManyZeroValues) –
- [**UniqueRows**](#validmind.tests.data_validation.UniqueRows) –
- [**WOEBinPlots**](#validmind.tests.data_validation.WOEBinPlots) –
- [**WOEBinTable**](#validmind.tests.data_validation.WOEBinTable) –
- [**ZivotAndrewsArch**](#validmind.tests.data_validation.ZivotAndrewsArch) –
- [**nlp**](#validmind.tests.data_validation.nlp) –

##### validmind.tests.data_validation.ACFandPACFPlot

**Functions:**

- [**ACFandPACFPlot**](#validmind.tests.data_validation.ACFandPACFPlot.ACFandPACFPlot) – Analyzes time series data using Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) plots to

###### validmind.tests.data_validation.ACFandPACFPlot.ACFandPACFPlot

```python
ACFandPACFPlot(dataset)
```

Analyzes time series data using Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) plots to
reveal trends and correlations.

### Purpose

The ACF (Autocorrelation Function) and PACF (Partial Autocorrelation Function) plot test is employed to analyze
time series data in machine learning models. It illuminates the correlation of the data over time by plotting the
correlation of the series with its own lags (ACF), and the correlations after removing effects already accounted
for by earlier lags (PACF). This information can identify trends, such as seasonality, degrees of autocorrelation,
and inform the selection of order parameters for AutoRegressive Integrated Moving Average (ARIMA) models.

### Test Mechanism

The `ACFandPACFPlot` test accepts a dataset with a time-based index. It first confirms the index is of a datetime
type, then handles any NaN values. The test subsequently generates ACF and PACF plots for each column in the
dataset, producing a subplot for each. If the dataset doesn't include key columns, an error is returned.

### Signs of High Risk

- Sudden drops in the correlation at a specific lag might signal a model at high risk.
- Consistent high correlation across multiple lags could also indicate non-stationarity in the data, which may
  suggest that a model estimated on this data won't generalize well to future, unknown data.

### Strengths

- ACF and PACF plots offer clear graphical representations of the correlations in time series data.
- These plots are effective at revealing important data characteristics such as seasonality, trends, and
  correlation patterns.
- The insights from these plots aid in better model configuration, particularly in the selection of ARIMA model
  parameters.

### Limitations

- ACF and PACF plots are exclusively for time series data and hence, can't be applied to all ML models.
- These plots require large, consistent datasets as gaps could lead to misleading results.
- The plots can only represent linear correlations and fail to capture any non-linear relationships within the data.
- The plots might be difficult for non-experts to interpret and should not replace more advanced analyses.

##### validmind.tests.data_validation.ADF

**Functions:**

- [**ADF**](#validmind.tests.data_validation.ADF.ADF) – Assesses the stationarity of a time series dataset using the Augmented Dickey-Fuller (ADF) test.

**Attributes:**

- [**logger**](#validmind.tests.data_validation.ADF.logger) –

###### validmind.tests.data_validation.ADF.ADF

```python
ADF(dataset)
```

Assesses the stationarity of a time series dataset using the Augmented Dickey-Fuller (ADF) test.

### Purpose

The Augmented Dickey-Fuller (ADF) test metric is used to determine the order of integration, i.e., the stationarity
of a given time series dataset. The stationary property of data is pivotal in many machine learning models as it
impacts the reliability and effectiveness of predictions and forecasts.

### Test Mechanism

The ADF test is executed using the `adfuller` function from the `statsmodels` library on each feature of the
dataset. Multiple outputs are generated for each run, including the ADF test statistic and p-value, count of lags
used, the number of observations considered in the test, critical values at various confidence levels, and the
information criterion. These results are stored for each feature for subsequent analysis.

### Signs of High Risk

- An inflated ADF statistic and high p-value (generally above 0.05) indicate a high risk to the model's performance
  due to the presence of a unit root indicating non-stationarity.
- Non-stationarity might result in untrustworthy or insufficient forecasts.

### Strengths

- The ADF test is robust to sophisticated correlations within the data, making it suitable for settings where data
  displays complex stochastic behavior.
- It provides explicit outputs like test statistics, critical values, and information criterion, enhancing
  understanding and transparency in the model validation process.

### Limitations

- The ADF test might demonstrate low statistical power, making it challenging to differentiate between a unit root
  and near-unit-root processes, potentially causing false negatives.
- It assumes the data follows an autoregressive process, which might not always be the case.
- The test struggles with time series data that have structural breaks.

###### validmind.tests.data_validation.ADF.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.data_validation.AutoAR

**Functions:**

- [**AutoAR**](#validmind.tests.data_validation.AutoAR.AutoAR) – Automatically identifies the optimal Autoregressive (AR) order for a time series using BIC and AIC criteria.

**Attributes:**

- [**logger**](#validmind.tests.data_validation.AutoAR.logger) –

###### validmind.tests.data_validation.AutoAR.AutoAR

```python
AutoAR(dataset, max_ar_order=3)
```

Automatically identifies the optimal Autoregressive (AR) order for a time series using BIC and AIC criteria.

### Purpose

The AutoAR test is intended to automatically identify the Autoregressive (AR) order of a time series by utilizing
the Bayesian Information Criterion (BIC) and Akaike Information Criterion (AIC). AR order is crucial in forecasting
tasks as it dictates the quantity of prior terms in the sequence to use for predicting the current term. The
objective is to select the most fitting AR model that encapsulates the trend and seasonality in the time series
data.

### Test Mechanism

The test mechanism operates by iterating through a possible range of AR orders up to a defined maximum. An AR model
is fitted for each order, and the corresponding BIC and AIC are computed. BIC and AIC statistical measures are
designed to penalize models for complexity, preferring simpler models that fit the data proficiently. To verify the
stationarity of the time series, the Augmented Dickey-Fuller test is executed. The AR order, BIC, and AIC findings
are compiled into a dataframe for effortless comparison. Then, the AR order with the smallest BIC is established as
the desirable order for each variable.

### Signs of High Risk

- An augmented Dickey Fuller test p-value > 0.05, indicating the time series isn't stationary, may lead to
  inaccurate results.
- Problems with the model fitting procedure, such as computational or convergence issues.
- Continuous selection of the maximum specified AR order may suggest an insufficient set limit.

### Strengths

- The test independently pinpoints the optimal AR order, thereby reducing potential human bias.
- It strikes a balance between model simplicity and goodness-of-fit to avoid overfitting.
- Has the capability to account for stationarity in a time series, an essential aspect for dependable AR modeling.
- The results are aggregated into a comprehensive table, enabling an easy interpretation.

### Limitations

- The tests need a stationary time series input.
- They presume a linear relationship between the series and its lags.
- The search for the best model is constrained by the maximum AR order supplied in the parameters. Therefore, a low
  max_ar_order could result in subpar outcomes.
- AIC and BIC may not always agree on the selection of the best model. This potentially requires the user to juggle
  interpretational choices.

###### validmind.tests.data_validation.AutoAR.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.data_validation.AutoMA

**Functions:**

- [**AutoMA**](#validmind.tests.data_validation.AutoMA.AutoMA) – Automatically selects the optimal Moving Average (MA) order for each variable in a time series dataset based on

**Attributes:**

- [**logger**](#validmind.tests.data_validation.AutoMA.logger) –

###### validmind.tests.data_validation.AutoMA.AutoMA

```python
AutoMA(dataset, max_ma_order=3)
```

Automatically selects the optimal Moving Average (MA) order for each variable in a time series dataset based on
minimal BIC and AIC values.

### Purpose

The `AutoMA` metric serves an essential role of automated decision-making for selecting the optimal Moving Average
(MA) order for every variable in a given time series dataset. The selection is dependent on the minimalization of
BIC (Bayesian Information Criterion) and AIC (Akaike Information Criterion); these are established statistical
tools used for model selection. Furthermore, prior to the commencement of the model fitting process, the algorithm
conducts a stationarity test (Augmented Dickey-Fuller test) on each series.

### Test Mechanism

Starting off, the `AutoMA` algorithm checks whether the `max_ma_order` parameter has been provided. It consequently
loops through all variables in the dataset, carrying out the Dickey-Fuller test for stationarity. For each
stationary variable, it fits an ARIMA model for orders running from 0 to `max_ma_order`. The result is a list
showcasing the BIC and AIC values of the ARIMA models based on different orders. The MA order, which yields the
smallest BIC, is chosen as the 'best MA order' for every single variable. The final results include a table
summarizing the auto MA analysis and another table listing the best MA order for each variable.

### Signs of High Risk

- When a series is non-stationary (p-value>0.05 in the Dickey-Fuller test), the produced result could be inaccurate.
- Any error that arises in the process of fitting the ARIMA models, especially with a higher MA order, can
  potentially indicate risks and might need further investigation.

### Strengths

- The metric facilitates automation in the process of selecting the MA order for time series forecasting. This
  significantly saves time and reduces efforts conventionally necessary for manual hyperparameter tuning.
- The use of both BIC and AIC enhances the likelihood of selecting the most suitable model.
- The metric ascertains the stationarity of the series prior to model fitting, thus ensuring that the underlying
  assumptions of the MA model are fulfilled.

### Limitations

- If the time series fails to be stationary, the metric may yield inaccurate results. Consequently, it necessitates
  pre-processing steps to stabilize the series before fitting the ARIMA model.
- The metric adopts a rudimentary model selection process based on BIC and doesn't consider other potential model
  selection strategies. Depending on the specific dataset, other strategies could be more appropriate.
- The 'max_ma_order' parameter must be manually input which doesn't always guarantee optimal performance,
  especially when configured too low.
- The computation time increases with the rise in `max_ma_order`, hence, the metric may become computationally
  costly for larger values.

###### validmind.tests.data_validation.AutoMA.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.data_validation.AutoSeasonality

**Functions:**

- [**AutoSeasonality**](#validmind.tests.data_validation.AutoSeasonality.AutoSeasonality) – Automatically identifies and quantifies optimal seasonality in time series data to improve forecasting model
- [**evaluate_seasonal_periods**](#validmind.tests.data_validation.AutoSeasonality.evaluate_seasonal_periods) –

**Attributes:**

- [**logger**](#validmind.tests.data_validation.AutoSeasonality.logger) –

###### validmind.tests.data_validation.AutoSeasonality.AutoSeasonality

```python
AutoSeasonality(dataset, min_period=1, max_period=4)
```

Automatically identifies and quantifies optimal seasonality in time series data to improve forecasting model
performance.

### Purpose

The AutoSeasonality test aims to automatically detect and identify the best seasonal order or period for each
variable in a time series dataset. This detection helps to quantify periodic patterns and seasonality that reoccur
at fixed intervals in the data. Understanding the seasonality component can drastically improve prediction
accuracy, which is especially significant for forecasting-based models.

### Test Mechanism

This test uses the seasonal decomposition method from the Statsmodels Python library. The function takes the
'additive' model type for each variable and applies it within the prescribed range of 'min_period' and
'max_period'. It decomposes the seasonality for each period in the range and calculates the mean residual error for
each period. The seasonal period that results in the minimum residuals is marked as the 'Best Period'. The test
results include the 'Best Period', the calculated residual errors, and a determination of 'Seasonality' or 'No
Seasonality'.

### Signs of High Risk

- If the optimal seasonal period (or 'Best Period') is consistently at the maximum or minimum limit of the offered
  range for a majority of variables, it may suggest that the range set does not adequately capture the true seasonal
  pattern in the series.
- A high average 'Residual Error' for the selected 'Best Period' could indicate issues with the model's performance.

### Strengths

- The metric offers an automatic approach to identifying and quantifying the optimal seasonality, providing a
  robust method for analyzing time series datasets.
- It is applicable to multiple variables in a dataset, providing a comprehensive evaluation of each variable's
  seasonality.
- The use of concrete and measurable statistical methods improves the objectivity and reproducibility of the model.

### Limitations

- This AutoSeasonality metric may not be suitable if the time series data exhibits random walk behavior or lacks
  clear seasonality, as the seasonal decomposition model may not be appropriate.
- The defined range for the seasonal period (min_period and max_period) can influence the outcomes. If the actual
  seasonality period lies outside this range, this method will not be able to identify the true seasonal order.
- This metric may not be able to fully interpret complex patterns that go beyond the simple additive model for
  seasonal decomposition.
- The tool may incorrectly infer seasonality if random fluctuations in the data match the predefined seasonal
  period range.

###### validmind.tests.data_validation.AutoSeasonality.evaluate_seasonal_periods

```python
evaluate_seasonal_periods(series, min_period, max_period)
```

###### validmind.tests.data_validation.AutoSeasonality.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.data_validation.AutoStationarity

**Functions:**

- [**AutoStationarity**](#validmind.tests.data_validation.AutoStationarity.AutoStationarity) – Automates Augmented Dickey-Fuller test to assess stationarity across multiple time series in a DataFrame.

###### validmind.tests.data_validation.AutoStationarity.AutoStationarity

```python
AutoStationarity(dataset, max_order=5, threshold=0.05)
```

Automates Augmented Dickey-Fuller test to assess stationarity across multiple time series in a DataFrame.

### Purpose

The AutoStationarity metric is intended to automatically detect and evaluate the stationary nature of each time
series in a DataFrame. It incorporates the Augmented Dickey-Fuller (ADF) test, a statistical approach used to
assess stationarity. Stationarity is a fundamental property suggesting that statistic features like mean and
variance remain unchanged over time. This is necessary for many time-series models.

### Test Mechanism

The mechanism for the AutoStationarity test involves applying the Augmented Dicky-Fuller test to each time series
within the given dataframe to assess if they are stationary. Every series in the dataframe is looped, using the ADF
test up to a defined maximum order (configurable and by default set to 5). The p-value resulting from the ADF test
is compared against a predetermined threshold (also configurable and by default set to 0.05). The time series is
deemed stationary at its current differencing order if the p-value is less than the threshold.

### Signs of High Risk

- A significant number of series not achieving stationarity even at the maximum order of differencing can indicate
  high risk or potential failure in the model.
- This could suggest the series may not be appropriately modeled by a stationary process, hence other modeling
  approaches might be required.

### Strengths

- The key strength in this metric lies in the automation of the ADF test, enabling mass stationarity analysis
  across various time series and boosting the efficiency and credibility of the analysis.
- The utilization of the ADF test, a widely accepted method for testing stationarity, lends authenticity to the
  results derived.
- The introduction of the max order and threshold parameters give users the autonomy to determine their preferred
  levels of stringency in the tests.

### Limitations

- The Augmented Dickey-Fuller test and the stationarity test are not without their limitations. These tests are
  premised on the assumption that the series can be modeled by an autoregressive process, which may not always hold
  true.
- The stationarity check is highly sensitive to the choice of threshold for the significance level; an extremely
  high or low threshold could lead to incorrect results regarding the stationarity properties.
- There's also a risk of over-differencing if the maximum order is set too high, which could induce unnecessary
  cycles.

##### validmind.tests.data_validation.BivariateScatterPlots

**Functions:**

- [**BivariateScatterPlots**](#validmind.tests.data_validation.BivariateScatterPlots.BivariateScatterPlots) – Generates bivariate scatterplots to visually inspect relationships between pairs of numerical predictor variables

###### validmind.tests.data_validation.BivariateScatterPlots.BivariateScatterPlots

```python
BivariateScatterPlots(dataset)
```

Generates bivariate scatterplots to visually inspect relationships between pairs of numerical predictor variables
in machine learning classification tasks.

### Purpose

This function is intended for visual inspection and monitoring of relationships between pairs of numerical
variables in a machine learning model targeting classification tasks. It helps in understanding how predictor
variables (features) interact with each other, which can inform feature selection, model-building strategies, and
identify potential biases or irregularities in the data.

### Test Mechanism

The function creates scatter plots for each pair of numerical features in the dataset. It first filters out
non-numerical and binary features, ensuring the plots focus on meaningful numerical relationships. The resulting
scatterplots are color-coded uniformly to avoid visual distraction, and the function returns a tuple of Plotly
figure objects, each representing a scatter plot for a pair of features.

### Signs of High Risk

- Visual patterns suggesting non-linear relationships, multicollinearity, clustering, or outlier points in the
  scatter plots.
- Such issues could affect the assumptions and performance of certain models, especially those assuming linearity,
  like logistic regression.

### Strengths

- Scatterplots provide an intuitive and visual tool to explore relationships between two variables.
- They are useful for identifying outliers, variable associations, and trends, including non-linear patterns.
- Supports visualization of binary or multi-class classification datasets, focusing on numerical features.

### Limitations

- Scatterplots are limited to bivariate analysis, showing relationships between only two variables at a time.
- Not ideal for very large datasets where overlapping points can reduce the clarity of the visualization.
- Scatterplots are exploratory tools and do not provide quantitative measures of model quality or performance.
- Interpretation is subjective and relies on the domain knowledge and judgment of the viewer.

##### validmind.tests.data_validation.BoxPierce

**Functions:**

- [**BoxPierce**](#validmind.tests.data_validation.BoxPierce.BoxPierce) – Detects autocorrelation in time-series data through the Box-Pierce test to validate model performance.

###### validmind.tests.data_validation.BoxPierce.BoxPierce

```python
BoxPierce(dataset)
```

Detects autocorrelation in time-series data through the Box-Pierce test to validate model performance.

### Purpose

The Box-Pierce test is utilized to detect the presence of autocorrelation in a time-series dataset.
Autocorrelation, or serial correlation, refers to the degree of similarity between observations based on the
temporal spacing between them. This test is essential for affirming the quality of a time-series model by ensuring
that the error terms in the model are random and do not adhere to a specific pattern.

### Test Mechanism

The implementation of the Box-Pierce test involves calculating a test statistic along with a corresponding p-value
derived from the dataset features. These quantities are used to test the null hypothesis that posits the data to be
independently distributed. This is achieved by iterating over every feature column in the time-series data and
applying the `acorr_ljungbox` function of the statsmodels library. The function yields the Box-Pierce test
statistic as well as the respective p-value, all of which are cached as test results.

### Signs of High Risk

- A low p-value, typically under 0.05 as per statistical convention, throws the null hypothesis of independence
  into question. This implies that the dataset potentially houses autocorrelations, thus indicating a high-risk
  scenario concerning model performance.
- Large Box-Pierce test statistic values may indicate the presence of autocorrelation.

### Strengths

- Detects patterns in data that are supposed to be random, thereby ensuring no underlying autocorrelation.
- Can be computed efficiently given its low computational complexity.
- Can be widely applied to most regression problems, making it very versatile.

### Limitations

- Assumes homoscedasticity (constant variance) and normality of residuals, which may not always be the case in
  real-world datasets.
- May exhibit reduced power for detecting complex autocorrelation schemes such as higher-order or negative
  correlations.
- It only provides a general indication of the existence of autocorrelation, without providing specific insights
  into the nature or patterns of the detected autocorrelation.
- In the presence of trends or seasonal patterns, the Box-Pierce test may yield misleading results.
- Applicability is limited to time-series data, which limits its overall utility.

##### validmind.tests.data_validation.ChiSquaredFeaturesTable

**Functions:**

- [**ChiSquaredFeaturesTable**](#validmind.tests.data_validation.ChiSquaredFeaturesTable.ChiSquaredFeaturesTable) – Assesses the statistical association between categorical features and a target variable using the Chi-Squared test.

###### validmind.tests.data_validation.ChiSquaredFeaturesTable.ChiSquaredFeaturesTable

```python
ChiSquaredFeaturesTable(dataset, p_threshold=0.05)
```

Assesses the statistical association between categorical features and a target variable using the Chi-Squared test.

### Purpose

The `ChiSquaredFeaturesTable` function is designed to evaluate the relationship between categorical features and a
target variable in a dataset. It performs a Chi-Squared test of independence for each categorical feature to
determine whether a statistically significant association exists with the target variable. This is particularly
useful in Model Risk Management for understanding the relevance of features and identifying potential biases in a
classification model.

### Test Mechanism

The function creates a contingency table for each categorical feature and the target variable, then applies the
Chi-Squared test to compute the Chi-squared statistic and the p-value. The results for each feature include the
variable name, Chi-squared statistic, p-value, p-value threshold, and a pass/fail status based on whether the
p-value is below the specified threshold. The output is a DataFrame summarizing these results, sorted by p-value to
highlight the most statistically significant associations.

### Signs of High Risk

- High p-values (greater than the set threshold) indicate a lack of significant association between a feature and
  the target variable, resulting in a 'Fail' status.
- Features with a 'Fail' status might not be relevant for the model, which could negatively impact model
  performance.

### Strengths

- Provides a clear, statistical assessment of the relationship between categorical features and the target variable.
- Produces an easily interpretable summary with a 'Pass/Fail' outcome for each feature, helping in feature
  selection.
- The p-value threshold is adjustable, allowing for flexibility in statistical rigor.

### Limitations

- Assumes the dataset is tabular and consists of categorical variables, which may not be suitable for all datasets.
- The test is designed for classification tasks and is not applicable to regression problems.
- As with all hypothesis tests, the Chi-Squared test can only detect associations, not causal relationships.
- The choice of p-value threshold can affect the interpretation of feature relevance, and different thresholds may
  lead to different conclusions.

##### validmind.tests.data_validation.ClassImbalance

Threshold based tests

**Functions:**

- [**ClassImbalance**](#validmind.tests.data_validation.ClassImbalance.ClassImbalance) – Evaluates and quantifies class distribution imbalance in a dataset used by a machine learning model.

###### validmind.tests.data_validation.ClassImbalance.ClassImbalance

```python
ClassImbalance(dataset, min_percent_threshold=10)
```

Evaluates and quantifies class distribution imbalance in a dataset used by a machine learning model.

### Purpose

The Class Imbalance test is designed to evaluate the distribution of target classes in a dataset that's utilized by
a machine learning model. Specifically, it aims to ensure that the classes aren't overly skewed, which could lead
to bias in the model's predictions. It's crucial to have a balanced training dataset to avoid creating a model
that's biased with high accuracy for the majority class and low accuracy for the minority class.

### Test Mechanism

This Class Imbalance test operates by calculating the frequency (expressed as a percentage) of each class in the
target column of the dataset. It then checks whether each class appears in at least a set minimum percentage of the
total records. This minimum percentage is a modifiable parameter, but the default value is set to 10%.

### Signs of High Risk

- Any class that represents less than the pre-set minimum percentage threshold is marked as high risk, implying a
  potential class imbalance.
- The function provides a pass/fail outcome for each class based on this criterion.
- Fundamentally, if any class fails this test, it's highly likely that the dataset possesses imbalanced class
  distribution.

### Strengths

- The test can spot under-represented classes that could affect the efficiency of a machine learning model.
- The calculation is straightforward and swift.
- The test is highly informative because it not only spots imbalance, but it also quantifies the degree of
  imbalance.
- The adjustable threshold enables flexibility and adaptation to differing use-cases or domain-specific needs.
- The test creates a visually insightful plot showing the classes and their corresponding proportions, enhancing
  interpretability and comprehension of the data.

### Limitations

- The test might struggle to perform well or provide vital insights for datasets with a high number of classes. In
  such cases, the imbalance could be inevitable due to the inherent class distribution.
- Sensitivity to the threshold value might result in faulty detection of imbalance if the threshold is set
  excessively high.
- Regardless of the percentage threshold, it doesn't account for varying costs or impacts of misclassifying
  different classes, which might fluctuate based on specific applications or domains.
- While it can identify imbalances in class distribution, it doesn't provide direct methods to address or correct
  these imbalances.
- The test is only applicable for classification operations and unsuitable for regression or clustering tasks.

##### validmind.tests.data_validation.DatasetDescription

**Functions:**

- [**DatasetDescription**](#validmind.tests.data_validation.DatasetDescription.DatasetDescription) – Provides comprehensive analysis and statistical summaries of each column in a machine learning model's dataset.
- [**describe_column**](#validmind.tests.data_validation.DatasetDescription.describe_column) – Gets descriptive statistics for a single column in a Pandas DataFrame.
- [**get_column_histograms**](#validmind.tests.data_validation.DatasetDescription.get_column_histograms) – Returns a collection of histograms for a numerical or categorical column.
- [**get_numerical_histograms**](#validmind.tests.data_validation.DatasetDescription.get_numerical_histograms) – Returns a collection of histograms for a numerical column, each one
- [**infer_datatypes**](#validmind.tests.data_validation.DatasetDescription.infer_datatypes) –

**Attributes:**

- [**DEFAULT_HISTOGRAM_BINS**](#validmind.tests.data_validation.DatasetDescription.DEFAULT_HISTOGRAM_BINS) –
- [**DEFAULT_HISTOGRAM_BIN_SIZES**](#validmind.tests.data_validation.DatasetDescription.DEFAULT_HISTOGRAM_BIN_SIZES) –
- [**logger**](#validmind.tests.data_validation.DatasetDescription.logger) –

###### validmind.tests.data_validation.DatasetDescription.DEFAULT_HISTOGRAM_BINS

```python
DEFAULT_HISTOGRAM_BINS = 10
```

###### validmind.tests.data_validation.DatasetDescription.DEFAULT_HISTOGRAM_BIN_SIZES

```python
DEFAULT_HISTOGRAM_BIN_SIZES = [5, 10, 20, 50]
```

###### validmind.tests.data_validation.DatasetDescription.DatasetDescription

```python
DatasetDescription(dataset)
```

Provides comprehensive analysis and statistical summaries of each column in a machine learning model's dataset.

### Purpose

The test depicted in the script is meant to run a comprehensive analysis on a Machine Learning model's datasets.
The test or metric is implemented to obtain a complete summary of the columns in the dataset, including vital
statistics of each column such as count, distinct values, missing values, histograms for numerical, categorical,
boolean, and text columns. This summary gives a comprehensive overview of the dataset to better understand the
characteristics of the data that the model is trained on or evaluates.

### Test Mechanism

The DatasetDescription class accomplishes the purpose as follows: firstly, the test method "run" infers the data
type of each column in the dataset and stores the details (id, column type). For each column, the
"describe_column" method is invoked to collect statistical information about the column, including count,
missing value count and its proportion to the total, unique value count, and its proportion to the total. Depending
on the data type of a column, histograms are generated that reflect the distribution of data within the column.
Numerical columns use the "get_numerical_histograms" method to calculate histogram distribution, whereas for
categorical, boolean and text columns, a histogram is computed with frequencies of each unique value in the
datasets. For unsupported types, an error is raised. Lastly, a summary table is built to aggregate all the
statistical insights and histograms of the columns in a dataset.

### Signs of High Risk

- High ratio of missing values to total values in one or more columns which may impact the quality of the
  predictions.
- Unsupported data types in dataset columns.
- Large number of unique values in the dataset's columns which might make it harder for the model to establish
  patterns.
- Extreme skewness or irregular distribution of data as reflected in the histograms.

### Strengths

- Provides a detailed analysis of the dataset with versatile summaries like count, unique values, histograms, etc.
- Flexibility in handling different types of data: numerical, categorical, boolean, and text.
- Useful in detecting problems in the dataset like missing values, unsupported data types, irregular data
  distribution, etc.
- The summary gives a comprehensive understanding of dataset features allowing developers to make informed
  decisions.

### Limitations

- The computation can be expensive from a resource standpoint, particularly for large datasets with numerous columns.
- The histograms use an arbitrary number of bins which may not be the optimal number of bins for specific data
  distribution.
- Unsupported data types for columns will raise an error which may limit evaluating the dataset.
- Columns with all null or missing values are not included in histogram computation.
- This test only validates the quality of the dataset but doesn't address the model's performance directly.

###### validmind.tests.data_validation.DatasetDescription.describe_column

```python
describe_column(df, column)
```

Gets descriptive statistics for a single column in a Pandas DataFrame.

###### validmind.tests.data_validation.DatasetDescription.get_column_histograms

```python
get_column_histograms(df, column, type_)
```

Returns a collection of histograms for a numerical or categorical column.
We store different combinations of bin sizes to allow analyzing the data better

Will be used in favor of \_get_histogram in the future

###### validmind.tests.data_validation.DatasetDescription.get_numerical_histograms

```python
get_numerical_histograms(df, column)
```

Returns a collection of histograms for a numerical column, each one
with a different bin size

###### validmind.tests.data_validation.DatasetDescription.infer_datatypes

```python
infer_datatypes(df)
```

###### validmind.tests.data_validation.DatasetDescription.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.data_validation.DatasetSplit

**Functions:**

- [**DatasetSplit**](#validmind.tests.data_validation.DatasetSplit.DatasetSplit) – Evaluates and visualizes the distribution proportions among training, testing, and validation datasets of an ML

**Attributes:**

- [**DATASET_LABELS**](#validmind.tests.data_validation.DatasetSplit.DATASET_LABELS) –

###### validmind.tests.data_validation.DatasetSplit.DATASET_LABELS

```python
DATASET_LABELS = {
    "train_ds": "Training",
    "test_ds": "Test",
    "validation_ds": "Validation",
    "total": "Total",
}

```

###### validmind.tests.data_validation.DatasetSplit.DatasetSplit

```python
DatasetSplit(datasets)
```

Evaluates and visualizes the distribution proportions among training, testing, and validation datasets of an ML
model.

### Purpose

The DatasetSplit test is designed to evaluate and visualize the distribution of data among training, testing, and
validation datasets, if available, within a given machine learning model. The main purpose is to assess whether the
model's datasets are split appropriately, as an imbalanced split might affect the model's ability to learn from the
data and generalize to unseen data.

### Test Mechanism

The DatasetSplit test first calculates the total size of all available datasets in the model. Then, for each
individual dataset, the methodology involves determining the size of the dataset and its proportion relative to the
total size. The results are then conveniently summarized in a table that shows dataset names, sizes, and
proportions. Absolute size and proportion of the total dataset size are displayed for each individual dataset.

### Signs of High Risk

- A very small training dataset, which may result in the model not learning enough from the data.
- A very large training dataset and a small test dataset, which may lead to model overfitting and poor
  generalization to unseen data.
- A small or non-existent validation dataset, which might complicate the model's performance assessment.

### Strengths

- The DatasetSplit test provides a clear, understandable visualization of dataset split proportions, which can
  highlight any potential imbalance in dataset splits quickly.
- It covers a wide range of task types including classification, regression, and text-related tasks.
- The metric is not tied to any specific data type and is applicable to tabular data, time series data, or text
  data.

### Limitations

- The DatasetSplit test does not provide any insight into the quality or diversity of the data within each split,
  just the size and proportion.
- The test does not give any recommendations or adjustments for imbalanced datasets.
- Potential lack of compatibility with more complex modes of data splitting (for example, stratified or time-based
  splits) could limit the applicability of this test.

##### validmind.tests.data_validation.DescriptiveStatistics

**Functions:**

- [**DescriptiveStatistics**](#validmind.tests.data_validation.DescriptiveStatistics.DescriptiveStatistics) – Performs a detailed descriptive statistical analysis of both numerical and categorical data within a model's
- [**get_summary_statistics_categorical**](#validmind.tests.data_validation.DescriptiveStatistics.get_summary_statistics_categorical) –
- [**get_summary_statistics_numerical**](#validmind.tests.data_validation.DescriptiveStatistics.get_summary_statistics_numerical) –

###### validmind.tests.data_validation.DescriptiveStatistics.DescriptiveStatistics

```python
DescriptiveStatistics(dataset)
```

Performs a detailed descriptive statistical analysis of both numerical and categorical data within a model's
dataset.

### Purpose

The purpose of the Descriptive Statistics metric is to provide a comprehensive summary of both numerical and
categorical data within a dataset. This involves statistics such as count, mean, standard deviation, minimum and
maximum values for numerical data. For categorical data, it calculates the count, number of unique values, most
common value and its frequency, and the proportion of the most frequent value relative to the total. The goal is to
visualize the overall distribution of the variables in the dataset, aiding in understanding the model's behavior
and predicting its performance.

### Test Mechanism

The testing mechanism utilizes two in-built functions of pandas dataframes: `describe()` for numerical fields and
`value_counts()` for categorical fields. The `describe()` function pulls out several summary statistics, while
`value_counts()` accounts for unique values. The resulting data is formatted into two distinct tables, one for
numerical and another for categorical variable summaries. These tables provide a clear summary of the main
characteristics of the variables, which can be instrumental in assessing the model's performance.

### Signs of High Risk

- Skewed data or significant outliers can represent high risk. For numerical data, this may be reflected via a
  significant difference between the mean and median (50% percentile).
- For categorical data, a lack of diversity (low count of unique values), or overdominance of a single category
  (high frequency of the top value) can indicate high risk.

### Strengths

- Provides a comprehensive summary of the dataset, shedding light on the distribution and characteristics of the
  variables under consideration.
- It is a versatile and robust method, applicable to both numerical and categorical data.
- Helps highlight crucial anomalies such as outliers, extreme skewness, or lack of diversity, which are vital in
  understanding model behavior during testing and validation.

### Limitations

- While this metric offers a high-level overview of the data, it may fail to detect subtle correlations or complex
  patterns.
- Does not offer any insights on the relationship between variables.
- Alone, descriptive statistics cannot be used to infer properties about future unseen data.
- Should be used in conjunction with other statistical tests to provide a comprehensive understanding of the
  model's data.

###### validmind.tests.data_validation.DescriptiveStatistics.get_summary_statistics_categorical

```python
get_summary_statistics_categorical(df, categorical_fields)
```

###### validmind.tests.data_validation.DescriptiveStatistics.get_summary_statistics_numerical

```python
get_summary_statistics_numerical(df, numerical_fields)
```

##### validmind.tests.data_validation.DickeyFullerGLS

**Functions:**

- [**DickeyFullerGLS**](#validmind.tests.data_validation.DickeyFullerGLS.DickeyFullerGLS) – Assesses stationarity in time series data using the Dickey-Fuller GLS test to determine the order of integration.

**Attributes:**

- [**logger**](#validmind.tests.data_validation.DickeyFullerGLS.logger) –

###### validmind.tests.data_validation.DickeyFullerGLS.DickeyFullerGLS

```python
DickeyFullerGLS(dataset)
```

Assesses stationarity in time series data using the Dickey-Fuller GLS test to determine the order of integration.

### Purpose

The Dickey-Fuller GLS (DFGLS) test is utilized to determine the order of integration in time series data. For
machine learning models dealing with time series and forecasting, this metric evaluates the existence of a unit
root, thereby checking whether a time series is non-stationary. This analysis is a crucial initial step when
dealing with time series data.

### Test Mechanism

This code implements the Dickey-Fuller GLS unit root test on each attribute of the dataset. This process involves
iterating through every column of the dataset and applying the DFGLS test to assess the presence of a unit root.
The resulting information, including the test statistic ('stat'), the p-value ('pvalue'), the quantity of lagged
differences utilized in the regression ('usedlag'), and the number of observations ('nobs'), is subsequently stored.

### Signs of High Risk

- A high p-value for the DFGLS test represents a high risk. Specifically, a p-value above a typical threshold of
  0.05 suggests that the time series data is quite likely to be non-stationary, thus presenting a high risk for
  generating unreliable forecasts.

### Strengths

- The Dickey-Fuller GLS test is a potent tool for checking the stationarity of time series data.
- It helps to verify the assumptions of the models before the actual construction of the machine learning models
  proceeds.
- The results produced by this metric offer a clear insight into whether the data is appropriate for specific
  machine learning models, especially those demanding the stationarity of time series data.

### Limitations

- Despite its benefits, the DFGLS test does present some drawbacks. It can potentially lead to inaccurate
  conclusions if the time series data incorporates a structural break.
- If the time series tends to follow a trend while still being stationary, the test might misinterpret it,
  necessitating further detrending.
- The test also presents challenges when dealing with shorter time series data or volatile data, not producing
  reliable results in these cases.

###### validmind.tests.data_validation.DickeyFullerGLS.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.data_validation.Duplicates

**Functions:**

- [**Duplicates**](#validmind.tests.data_validation.Duplicates.Duplicates) – Tests dataset for duplicate entries, ensuring model reliability via data quality verification.

###### validmind.tests.data_validation.Duplicates.Duplicates

```python
Duplicates(dataset, min_threshold=1)
```

Tests dataset for duplicate entries, ensuring model reliability via data quality verification.

### Purpose

The 'Duplicates' test is designed to check for duplicate rows within the dataset provided to the model. It serves
as a measure of data quality, ensuring that the model isn't merely memorizing duplicate entries or being swayed by
redundant information. This is an important step in the pre-processing of data for both classification and
regression tasks.

### Test Mechanism

This test operates by checking each row for duplicates in the dataset. If a text column is specified in the
dataset, the test is conducted on this column; if not, the test is run on all feature columns. The number and
percentage of duplicates are calculated and returned in a DataFrame. Additionally, a test is passed if the total
count of duplicates falls below a specified minimum threshold.

### Signs of High Risk

- A high number of duplicate rows in the dataset, which can lead to overfitting where the model performs well on
  the training data but poorly on unseen data.
- A high percentage of duplicate rows in the dataset, indicating potential problems with data collection or
  processing.

### Strengths

- Assists in improving the reliability of the model's training process by ensuring the training data is not
  contaminated with duplicate entries, which can distort statistical analyses.
- Provides both absolute numbers and percentage values of duplicate rows, giving a thorough overview of data
  quality.
- Highly customizable as it allows for setting a user-defined minimum threshold to determine if the test has been
  passed.

### Limitations

- Does not distinguish between benign duplicates (i.e., coincidental identical entries in different rows) and
  problematic duplicates originating from data collection or processing errors.
- The test becomes more computationally intensive as the size of the dataset increases, which might not be suitable
  for very large datasets.
- Can only check for exact duplicates and may miss semantically similar information packaged differently.

##### validmind.tests.data_validation.EngleGrangerCoint

**Functions:**

- [**EngleGrangerCoint**](#validmind.tests.data_validation.EngleGrangerCoint.EngleGrangerCoint) – Assesses the degree of co-movement between pairs of time series data using the Engle-Granger cointegration test.

###### validmind.tests.data_validation.EngleGrangerCoint.EngleGrangerCoint

```python
EngleGrangerCoint(dataset, threshold=0.05)
```

Assesses the degree of co-movement between pairs of time series data using the Engle-Granger cointegration test.

### Purpose

The intent of this Engle-Granger cointegration test is to explore and quantify the degree of co-movement between
pairs of time series variables in a dataset. This is particularly useful in enhancing the accuracy of predictive
regressions whenever the underlying variables are co-integrated, i.e., they move together over time.

### Test Mechanism

The test first drops any non-applicable values from the input dataset and then iterates over each pair of variables
to apply the Engle-Granger cointegration test. The test generates a 'p' value, which is then compared against a
pre-specified threshold (0.05 by default). The pair is labeled as 'Cointegrated' if the 'p' value is less than or
equal to the threshold or 'Not cointegrated' otherwise. A summary table is returned by the metric showing
cointegration results for each variable pair.

### Signs of High Risk

- A significant number of hypothesized cointegrated variables do not pass the test.
- A considerable number of 'p' values are close to the threshold, indicating minor data fluctuations can switch the
  decision between 'Cointegrated' and 'Not cointegrated'.

### Strengths

- Provides an effective way to analyze relationships between time series, particularly in contexts where it's
  essential to check if variables move together in a statistically significant manner.
- Useful in various domains, especially finance or economics, where predictive models often hinge on understanding
  how different variables move together over time.

### Limitations

- Assumes that the time series are integrated of the same order, which isn't always true in multivariate time
  series datasets.
- The presence of non-stationary characteristics in the series or structural breaks can result in falsely positive
  or negative cointegration results.
- May not perform well for small sample sizes due to lack of statistical power and should be supplemented with
  other predictive indicators for a more robust model evaluation.

##### validmind.tests.data_validation.FeatureTargetCorrelationPlot

**Functions:**

- [**FeatureTargetCorrelationPlot**](#validmind.tests.data_validation.FeatureTargetCorrelationPlot.FeatureTargetCorrelationPlot) – Visualizes the correlation between input features and the model's target output in a color-coded horizontal bar

###### validmind.tests.data_validation.FeatureTargetCorrelationPlot.FeatureTargetCorrelationPlot

```python
FeatureTargetCorrelationPlot(dataset, fig_height=600)
```

Visualizes the correlation between input features and the model's target output in a color-coded horizontal bar
plot.

### Purpose

This test is designed to graphically illustrate the correlations between distinct input features and the target
output of a Machine Learning model. Understanding how each feature influences the model's predictions is crucial—a
higher correlation indicates a stronger influence of the feature on the target variable. This correlation study is
especially advantageous during feature selection and for comprehending the model's operation.

### Test Mechanism

This FeatureTargetCorrelationPlot test computes and presents the correlations between the features and the target
variable using a specific dataset. These correlations are calculated and are then graphically represented in a
horizontal bar plot, color-coded based on the strength of the correlation. A hovering template can also be utilized
for informative tooltips. It is possible to specify the features to be analyzed and adjust the graph's height
according to need.

### Signs of High Risk

- There are no strong correlations (either positive or negative) between features and the target variable. This
  could suggest high risk as the supplied features do not appear to significantly impact the prediction output.
- The presence of duplicated correlation values might hint at redundancy in the feature set.

### Strengths

- Provides visual assistance to interpreting correlations more effectively.
- Gives a clear and simple tour of how each feature affects the model's target variable.
- Beneficial for feature selection and grasping the model's prediction nature.
- Precise correlation values for each feature are offered by the hover template, contributing to a granular-level
  comprehension.

### Limitations

- The test only accepts numerical data, meaning variables of other types need to be prepared beforehand.
- The plot assumes all correlations to be linear, thus non-linear relationships might not be captured effectively.
- Not apt for models that employ complex feature interactions, like Decision Trees or Neural Networks, as the test
  may not accurately reflect their importance.

##### validmind.tests.data_validation.HighCardinality

**Functions:**

- [**HighCardinality**](#validmind.tests.data_validation.HighCardinality.HighCardinality) – Assesses the number of unique values in categorical columns to detect high cardinality and potential overfitting.

###### validmind.tests.data_validation.HighCardinality.HighCardinality

```python
HighCardinality(
    dataset, num_threshold=100, percent_threshold=0.1, threshold_type="percent"
)
```

Assesses the number of unique values in categorical columns to detect high cardinality and potential overfitting.

### Purpose

The “High Cardinality” test is used to evaluate the number of unique values present in the categorical columns of a
dataset. In this context, high cardinality implies the presence of a large number of unique, non-repetitive values
in the dataset.

### Test Mechanism

The test first infers the dataset's type and then calculates an initial numeric threshold based on the test
parameters. It only considers columns classified as "Categorical". For each of these columns, the number of
distinct values (n_distinct) and the percentage of distinct values (p_distinct) are calculated. The test will pass
if n_distinct is less than the calculated numeric threshold. Lastly, the results, which include details such as
column name, number of distinct values, and pass/fail status, are compiled into a table.

### Signs of High Risk

- A large number of distinct values (high cardinality) in one or more categorical columns implies a high risk.
- A column failing the test (n_distinct >= num_threshold) is another indicator of high risk.

### Strengths

- The High Cardinality test is effective in early detection of potential overfitting and unwanted noise.
- It aids in identifying potential outliers and inconsistencies, thereby improving data quality.
- The test can be applied to both classification and regression task types, demonstrating its versatility.

### Limitations

- The test is restricted to only "Categorical" data types and is thus not suitable for numerical or continuous
  features, limiting its scope.
- The test does not consider the relevance or importance of unique values in categorical features, potentially
  causing it to overlook critical data points.
- The threshold (both number and percent) used for the test is static and may not be optimal for diverse datasets
  and varied applications. Further mechanisms to adjust and refine this threshold could enhance its effectiveness.

##### validmind.tests.data_validation.HighPearsonCorrelation

**Functions:**

- [**HighPearsonCorrelation**](#validmind.tests.data_validation.HighPearsonCorrelation.HighPearsonCorrelation) – Identifies highly correlated feature pairs in a dataset suggesting feature redundancy or multicollinearity.

###### validmind.tests.data_validation.HighPearsonCorrelation.HighPearsonCorrelation

```python
HighPearsonCorrelation(dataset, max_threshold=0.3, top_n_correlations=10)
```

Identifies highly correlated feature pairs in a dataset suggesting feature redundancy or multicollinearity.

### Purpose

The High Pearson Correlation test measures the linear relationship between features in a dataset, with the main
goal of identifying high correlations that might indicate feature redundancy or multicollinearity. Identification
of such issues allows developers and risk management teams to properly deal with potential impacts on the machine
learning model's performance and interpretability.

### Test Mechanism

The test works by generating pairwise Pearson correlations for all features in the dataset, then sorting and
eliminating duplicate and self-correlations. It assigns a Pass or Fail based on whether the absolute value of the
correlation coefficient surpasses a pre-set threshold (defaulted at 0.3). It lastly returns the top n strongest
correlations regardless of passing or failing status (where n is 10 by default but can be configured by passing the
`top_n_correlations` parameter).

### Signs of High Risk

- A high risk indication would be the presence of correlation coefficients exceeding the threshold.
- If the features share a strong linear relationship, this could lead to potential multicollinearity and model
  overfitting.
- Redundancy of variables can undermine the interpretability of the model due to uncertainty over the authenticity
  of individual variable's predictive power.

### Strengths

- Provides a quick and simple means of identifying relationships between feature pairs.
- Generates a transparent output that displays pairs of correlated variables, the Pearson correlation coefficient,
  and a Pass or Fail status for each.
- Aids in early identification of potential multicollinearity issues that may disrupt model training.

### Limitations

- Can only delineate linear relationships, failing to shed light on nonlinear relationships or dependencies.
- Sensitive to outliers where a few outliers could notably affect the correlation coefficient.
- Limited to identifying redundancy only within feature pairs; may fail to spot more complex relationships among
  three or more variables.

##### validmind.tests.data_validation.IQROutliersBarPlot

**Functions:**

- [**IQROutliersBarPlot**](#validmind.tests.data_validation.IQROutliersBarPlot.IQROutliersBarPlot) – Visualizes outlier distribution across percentiles in numerical data using the Interquartile Range (IQR) method.
- [**compute_outliers**](#validmind.tests.data_validation.IQROutliersBarPlot.compute_outliers) –

###### validmind.tests.data_validation.IQROutliersBarPlot.IQROutliersBarPlot

```python
IQROutliersBarPlot(dataset, threshold=1.5, fig_width=800)
```

Visualizes outlier distribution across percentiles in numerical data using the Interquartile Range (IQR) method.

### Purpose

The InterQuartile Range Outliers Bar Plot (IQROutliersBarPlot) metric aims to visually analyze and evaluate the
extent of outliers in numeric variables based on percentiles. Its primary purpose is to clarify the dataset's
distribution, flag possible abnormalities in it, and gauge potential risks associated with processing potentially
skewed data, which can affect the machine learning model's predictive prowess.

### Test Mechanism

The examination invokes a series of steps:

1. For every numeric feature in the dataset, the 25th percentile (Q1) and 75th percentile (Q3) are calculated
   before deriving the Interquartile Range (IQR), the difference between Q1 and Q3.
1. Subsequently, the metric calculates the lower and upper thresholds by subtracting Q1 from the `threshold` times
   IQR and adding Q3 to `threshold` times IQR, respectively. The default `threshold` is set at 1.5.
1. Any value in the feature that falls below the lower threshold or exceeds the upper threshold is labeled as an
   outlier.
1. The number of outliers are tallied for different percentiles, such as [0-25], [25-50], [50-75], and [75-100].
1. These counts are employed to construct a bar plot for the feature, showcasing the distribution of outliers
   across different percentiles.

### Signs of High Risk

- A prevalence of outliers in the data, potentially skewing its distribution.
- Outliers dominating higher percentiles (75-100) which implies the presence of extreme values, capable of severely
  influencing the model's performance.
- Certain features harboring most of their values as outliers, which signifies that these features might not
  contribute positively to the model's forecasting ability.

### Strengths

- Effectively identifies outliers in the data through visual means, facilitating easier comprehension and offering
  insights into the outliers' possible impact on the model.
- Provides flexibility by accommodating all numeric features or a chosen subset.
- Task-agnostic in nature; it is viable for both classification and regression tasks.
- Can handle large datasets as its operation does not hinge on computationally heavy operations.

### Limitations

- Its application is limited to numerical variables and does not extend to categorical ones.
- Only reveals the presence and distribution of outliers and does not provide insights into how these outliers
  might affect the model's predictive performance.
- The assumption that data is unimodal and symmetric may not always hold true. In cases with non-normal
  distributions, the results can be misleading.

###### validmind.tests.data_validation.IQROutliersBarPlot.compute_outliers

```python
compute_outliers(series, threshold)
```

##### validmind.tests.data_validation.IQROutliersTable

**Functions:**

- [**IQROutliersTable**](#validmind.tests.data_validation.IQROutliersTable.IQROutliersTable) – Determines and summarizes outliers in numerical features using the Interquartile Range method.
- [**compute_outliers**](#validmind.tests.data_validation.IQROutliersTable.compute_outliers) –

###### validmind.tests.data_validation.IQROutliersTable.IQROutliersTable

```python
IQROutliersTable(dataset, threshold=1.5)
```

Determines and summarizes outliers in numerical features using the Interquartile Range method.

### Purpose

The "Interquartile Range Outliers Table" (IQROutliersTable) metric is designed to identify and summarize outliers
within numerical features of a dataset using the Interquartile Range (IQR) method. This exercise is crucial in the
pre-processing of data because outliers can substantially distort statistical analysis and impact the performance
of machine learning models.

### Test Mechanism

The IQR, which is the range separating the first quartile (25th percentile) from the third quartile (75th
percentile), is calculated for each numerical feature within the dataset. An outlier is defined as a data point
falling below the "Q1 - 1.5 * IQR" or above "Q3 + 1.5 * IQR" range. The test computes the number of outliers and
their summary statistics (minimum, 25th percentile, median, 75th percentile, and maximum values) for each numerical
feature. If no specific features are chosen, the test applies to all numerical features in the dataset. The default
outlier threshold is set to 1.5 but can be customized by the user.

### Signs of High Risk

- A large number of outliers in multiple features.
- Outliers significantly distanced from the mean value of variables.
- Extremely high or low outlier values indicative of data entry errors or other data quality issues.

### Strengths

- Provides a comprehensive summary of outliers for each numerical feature, helping pinpoint features with potential
  quality issues.
- The IQR method is robust to extremely high or low outlier values as it is based on quartile calculations.
- Can be customized to work on selected features and set thresholds for outliers.

### Limitations

- Might cause false positives if the variable deviates from a normal or near-normal distribution, especially for
  skewed distributions.
- Does not provide interpretation or recommendations for addressing outliers, relying on further analysis by users
  or data scientists.
- Only applicable to numerical features, not categorical data.
- Default thresholds may not be optimal for data with heavy pre-processing, manipulation, or inherently high
  kurtosis (heavy tails).

###### validmind.tests.data_validation.IQROutliersTable.compute_outliers

```python
compute_outliers(series, threshold=1.5)
```

##### validmind.tests.data_validation.IsolationForestOutliers

**Functions:**

- [**IsolationForestOutliers**](#validmind.tests.data_validation.IsolationForestOutliers.IsolationForestOutliers) – Detects outliers in a dataset using the Isolation Forest algorithm and visualizes results through scatter plots.

###### validmind.tests.data_validation.IsolationForestOutliers.IsolationForestOutliers

```python
IsolationForestOutliers(
    dataset, random_state=0, contamination=0.1, feature_columns=None
)
```

Detects outliers in a dataset using the Isolation Forest algorithm and visualizes results through scatter plots.

### Purpose

The IsolationForestOutliers test is designed to identify anomalies or outliers in the model's dataset using the
isolation forest algorithm. This algorithm assumes that anomalous data points can be isolated more quickly due to
their distinctive properties. By creating isolation trees and identifying instances with shorter average path
lengths, the test is able to pick out data points that differ from the majority.

### Test Mechanism

The test uses the isolation forest algorithm, which builds an ensemble of isolation trees by randomly selecting
features and splitting the data based on random thresholds. It isolates anomalies rather than focusing on normal
data points. For each pair of variables, a scatter plot is generated which distinguishes the identified outliers
from the inliers. The results of the test can be visualized using these scatter plots, illustrating the distinction
between outliers and inliers.

### Signs of High Risk

- The presence of high contamination, indicating a large number of anomalies
- Inability to detect clusters of anomalies that are close in the feature space
- Misclassifying normal instances as anomalies
- Failure to detect actual anomalies

### Strengths

- Ability to handle large, high-dimensional datasets
- Efficiency in isolating anomalies instead of normal instances
- Insensitivity to the underlying distribution of data
- Ability to recognize anomalies even when they are not separated from the main data cloud through identifying
  distinctive properties
- Visually presents the test results for better understanding and interpretability

### Limitations

- Difficult to detect anomalies that are close to each other or prevalent in datasets
- Dependency on the contamination parameter which may need fine-tuning to be effective
- Potential failure in detecting collective anomalies if they behave similarly to normal data
- Potential lack of precision in identifying which features contribute most to the anomalous behavior

##### validmind.tests.data_validation.JarqueBera

**Functions:**

- [**JarqueBera**](#validmind.tests.data_validation.JarqueBera.JarqueBera) – Assesses normality of dataset features in an ML model using the Jarque-Bera test.

###### validmind.tests.data_validation.JarqueBera.JarqueBera

```python
JarqueBera(dataset)
```

Assesses normality of dataset features in an ML model using the Jarque-Bera test.

### Purpose

The purpose of the Jarque-Bera test as implemented in this metric is to determine if the features in the dataset of
a given Machine Learning model follow a normal distribution. This is crucial for understanding the distribution and
behavior of the model's features, as numerous statistical methods assume normal distribution of the data.

### Test Mechanism

The test mechanism involves computing the Jarque-Bera statistic, p-value, skew, and kurtosis for each feature in
the dataset. It utilizes the 'jarque_bera' function from the 'statsmodels' library in Python, storing the results
in a dictionary. The test evaluates the skewness and kurtosis to ascertain whether the dataset follows a normal
distribution. A significant p-value (typically less than 0.05) implies that the data does not possess normal
distribution.

### Signs of High Risk

- A high Jarque-Bera statistic and a low p-value (usually less than 0.05) indicate high-risk conditions.
- Such results suggest the data significantly deviates from a normal distribution. If a machine learning model
  expects feature data to be normally distributed, these findings imply that it may not function as intended.

### Strengths

- Provides insights into the shape of the data distribution, helping determine whether a given set of data follows
  a normal distribution.
- Particularly useful for risk assessment for models that assume a normal distribution of data.
- By measuring skewness and kurtosis, it provides additional insights into the nature and magnitude of a
  distribution's deviation.

### Limitations

- Only checks for normality in the data distribution. It cannot provide insights into other types of distributions.
- Datasets that aren't normally distributed but follow some other distribution might lead to inaccurate risk
  assessments.
- Highly sensitive to large sample sizes, often rejecting the null hypothesis (that data is normally distributed)
  even for minor deviations in larger datasets.

##### validmind.tests.data_validation.KPSS

**Functions:**

- [**KPSS**](#validmind.tests.data_validation.KPSS.KPSS) – Assesses the stationarity of time-series data in a machine learning model using the KPSS unit root test.

**Attributes:**

- [**logger**](#validmind.tests.data_validation.KPSS.logger) –

###### validmind.tests.data_validation.KPSS.KPSS

```python
KPSS(dataset)
```

Assesses the stationarity of time-series data in a machine learning model using the KPSS unit root test.

### Purpose

The KPSS (Kwiatkowski-Phillips-Schmidt-Shin) unit root test is utilized to ensure the stationarity of data within a
machine learning model. It specifically works on time-series data to establish the order of integration, which is
essential for accurate forecasting. A fundamental requirement for any time series model is that the series should
be stationary.

### Test Mechanism

This test calculates the KPSS score for each feature in the dataset. The KPSS score includes a statistic, a
p-value, a used lag, and critical values. The core principle behind the KPSS test is to evaluate the hypothesis
that an observable time series is stationary around a deterministic trend. If the computed statistic exceeds the
critical value, the null hypothesis (that the series is stationary) is rejected, indicating that the series is
non-stationary.

### Signs of High Risk

- High KPSS score, particularly if the calculated statistic is higher than the critical value.
- Rejection of the null hypothesis, indicating that the series is recognized as non-stationary, can severely affect
  the model's forecasting capability.

### Strengths

- Directly measures the stationarity of a series, fulfilling a key prerequisite for many time-series models.
- The underlying logic of the test is intuitive and simple, making it easy to understand and accessible for both
  developers and risk management teams.

### Limitations

- Assumes the absence of a unit root in the series and doesn't differentiate between series that are stationary and
  those border-lining stationarity.
- The test may have restricted power against certain alternatives.
- The reliability of the test is contingent on the number of lags selected, which introduces potential bias in the
  measurement.

###### validmind.tests.data_validation.KPSS.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.data_validation.LJungBox

**Functions:**

- [**LJungBox**](#validmind.tests.data_validation.LJungBox.LJungBox) – Assesses autocorrelations in dataset features by performing a Ljung-Box test on each feature.

###### validmind.tests.data_validation.LJungBox.LJungBox

```python
LJungBox(dataset)
```

Assesses autocorrelations in dataset features by performing a Ljung-Box test on each feature.

### Purpose

The Ljung-Box test is a type of statistical test utilized to ascertain whether there are autocorrelations within a
given dataset that differ significantly from zero. In the context of a machine learning model, this test is
primarily used to evaluate data utilized in regression tasks, especially those involving time series and
forecasting.

### Test Mechanism

The test operates by iterating over each feature within the dataset and applying the `acorr_ljungbox`
function from the `statsmodels.stats.diagnostic` library. This function calculates the Ljung-Box statistic and
p-value for each feature. These results are then stored in a pandas DataFrame where the columns are the feature names,
statistic, and p-value respectively. Generally, a lower p-value indicates a higher likelihood of significant
autocorrelations within the feature.

### Signs of High Risk

- High Ljung-Box statistic values or low p-values.
- Presence of significant autocorrelations in the respective features.
- Potential for negative impact on model performance or bias if autocorrelations are not properly handled.

### Strengths

- Powerful tool for detecting autocorrelations within datasets, especially in time series data.
- Provides quantitative measures (statistic and p-value) for precise evaluation.
- Helps avoid issues related to autoregressive residuals and other challenges in regression models.

### Limitations

- Cannot detect all types of non-linearity or complex interrelationships among variables.
- Testing individual features may not fully encapsulate the dynamics of the data if features interact with each other.
- Designed more for traditional statistical models and may not be fully compatible with certain types of complex
  machine learning models.

##### validmind.tests.data_validation.LaggedCorrelationHeatmap

**Functions:**

- [**LaggedCorrelationHeatmap**](#validmind.tests.data_validation.LaggedCorrelationHeatmap.LaggedCorrelationHeatmap) – Assesses and visualizes correlation between target variable and lagged independent variables in a time-series

**Attributes:**

- [**COOLWARM**](#validmind.tests.data_validation.LaggedCorrelationHeatmap.COOLWARM) –

###### validmind.tests.data_validation.LaggedCorrelationHeatmap.COOLWARM

```python
COOLWARM = [
    [0, "rgb(95,5,255)"],
    [0.5, "rgb(255,255,255)"],
    [1, "rgb(255,5,0)"],
]

```

###### validmind.tests.data_validation.LaggedCorrelationHeatmap.LaggedCorrelationHeatmap

```python
LaggedCorrelationHeatmap(dataset, num_lags=10)
```

Assesses and visualizes correlation between target variable and lagged independent variables in a time-series
dataset.

### Purpose

The LaggedCorrelationHeatmap metric is utilized to appraise and illustrate the correlation between the target
variable and delayed copies (lags) of independent variables in a time-series dataset. It assists in revealing
relationships in time-series data where the influence of an independent variable on the dependent variable is not
immediate but occurs after a period (lags).

### Test Mechanism

To execute this test, Python's Pandas library pairs with Plotly to perform computations and present the
visualization in the form of a heatmap. The test begins by extracting the target variable and corresponding
independent variables from the dataset. Then, generation of lags of independent variables takes place, followed by
the calculation of correlation between these lagged variables and the target variable. The outcome is a correlation
matrix that gets recorded and illustrated as a heatmap, where different color intensities represent the strength of
the correlation, making patterns easier to identify.

### Signs of High Risk

- Insignificant correlations across the heatmap, indicating a lack of noteworthy relationships between variables.
- Correlations that break intuition or previous understanding, suggesting potential issues with the dataset or the
  model.

### Strengths

- This metric serves as an exceptional tool for exploring and visualizing time-dependent relationships between
  features and the target variable in a time-series dataset.
- It aids in identifying delayed effects that might go unnoticed with other correlation measures.
- The heatmap offers an intuitive visual representation of time-dependent correlations and influences.

### Limitations

- The metric presumes linear relationships between variables, potentially ignoring non-linear relationships.
- The correlation considered is linear; therefore, intricate non-linear interactions might be overlooked.
- The metric is only applicable for time-series data, limiting its utility outside of this context.
- The number of lags chosen can significantly influence the results; too many lags can render the heatmap difficult
  to interpret, while too few might overlook delayed effects.
- This metric does not take into account any causal relationships, but merely demonstrates correlation.

##### validmind.tests.data_validation.MissingValues

**Functions:**

- [**MissingValues**](#validmind.tests.data_validation.MissingValues.MissingValues) – Evaluates dataset quality by ensuring missing value ratio across all features does not exceed a set threshold.

###### validmind.tests.data_validation.MissingValues.MissingValues

```python
MissingValues(dataset, min_threshold=1)
```

Evaluates dataset quality by ensuring missing value ratio across all features does not exceed a set threshold.

### Purpose

The Missing Values test is designed to evaluate the quality of a dataset by measuring the number of missing values
across all features. The objective is to ensure that the ratio of missing data to total data is less than a
predefined threshold, defaulting to 1, in order to maintain the data quality necessary for reliable predictive
strength in a machine learning model.

### Test Mechanism

The mechanism for this test involves iterating through each column of the dataset, counting missing values
(represented as NaNs), and calculating the percentage they represent against the total number of rows. The test
then checks if these missing value counts are less than the predefined `min_threshold`. The results are shown in a
table summarizing each column, the number of missing values, the percentage of missing values in each column, and a
Pass/Fail status based on the threshold comparison.

### Signs of High Risk

- When the number of missing values in any column exceeds the `min_threshold` value.
- Presence of missing values across many columns, leading to multiple instances of failing the threshold.

### Strengths

- Quick and granular identification of missing data across each feature in the dataset.
- Provides an effective and straightforward means of maintaining data quality, essential for constructing efficient
  machine learning models.

### Limitations

- Does not suggest the root causes of the missing values or recommend ways to impute or handle them.
- May overlook features with significant missing data but still less than the `min_threshold`, potentially
  impacting the model.
- Does not account for data encoded as values like "-999" or "None," which might not technically classify as
  missing but could bear similar implications.

##### validmind.tests.data_validation.MissingValuesBarPlot

**Functions:**

- [**MissingValuesBarPlot**](#validmind.tests.data_validation.MissingValuesBarPlot.MissingValuesBarPlot) – Assesses the percentage and distribution of missing values in the dataset via a bar plot, with emphasis on

###### validmind.tests.data_validation.MissingValuesBarPlot.MissingValuesBarPlot

```python
MissingValuesBarPlot(dataset, threshold=80, fig_height=600)
```

Assesses the percentage and distribution of missing values in the dataset via a bar plot, with emphasis on
identifying high-risk columns based on a user-defined threshold.

### Purpose

The 'MissingValuesBarPlot' metric provides a color-coded visual representation of the percentage of missing values
for each column in an ML model's dataset. The primary purpose of this metric is to easily identify and quantify
missing data, which are essential steps in data preprocessing. The presence of missing data can potentially skew
the model's predictions and decrease its accuracy. Additionally, this metric uses a pre-set threshold to categorize
various columns into ones that contain missing data above the threshold (high risk) and below the threshold (less
risky).

### Test Mechanism

The test mechanism involves scanning each column in the input dataset and calculating the percentage of missing
values. It then compares each column's missing data percentage with the predefined threshold, categorizing columns
with missing data above the threshold as high-risk. The test generates a bar plot in which columns with missing
data are represented on the y-axis and their corresponding missing data percentages are displayed on the x-axis.
The color of each bar reflects the missing data percentage in relation to the threshold: grey for values below the
threshold and light coral for those exceeding it. The user-defined threshold is represented by a red dashed line on
the plot.

### Signs of High Risk

- Columns with higher percentages of missing values beyond the threshold are high-risk. These are visually
  represented by light coral bars on the bar plot.

### Strengths

- Helps in quickly identifying and quantifying missing data across all columns of the dataset.
- Facilitates pattern recognition through visual representation.
- Enables customization of the level of risk tolerance via a user-defined threshold.
- Supports both classification and regression tasks, sharing its versatility.

### Limitations

- It only considers the quantity of missing values, not differentiating between different types of missingness
  (Missing completely at random - MCAR, Missing at random - MAR, Not Missing at random - NMAR).
- It doesn't offer insights into potential approaches for handling missing entries, such as various imputation
  strategies.
- The metric does not consider possible impacts of the missing data on the model's accuracy or precision.
- Interpretation of the findings and the next steps might require an expert understanding of the field.

##### validmind.tests.data_validation.PearsonCorrelationMatrix

**Functions:**

- [**PearsonCorrelationMatrix**](#validmind.tests.data_validation.PearsonCorrelationMatrix.PearsonCorrelationMatrix) – Evaluates linear dependency between numerical variables in a dataset via a Pearson Correlation coefficient heat map.

###### validmind.tests.data_validation.PearsonCorrelationMatrix.PearsonCorrelationMatrix

```python
PearsonCorrelationMatrix(dataset)
```

Evaluates linear dependency between numerical variables in a dataset via a Pearson Correlation coefficient heat map.

### Purpose

This test is intended to evaluate the extent of linear dependency between all pairs of numerical variables in the
given dataset. It provides the Pearson Correlation coefficient, which reveals any high correlations present. The
purpose of doing this is to identify potential redundancy, as variables that are highly correlated can often be
removed to reduce the dimensionality of the dataset without significantly impacting the model's performance.

### Test Mechanism

This metric test generates a correlation matrix for all numerical variables in the dataset using the Pearson
correlation formula. A heat map is subsequently created to visualize this matrix effectively. The color of each
point on the heat map corresponds to the magnitude and direction (positive or negative) of the correlation, with a
range from -1 (perfect negative correlation) to 1 (perfect positive correlation). Any correlation coefficients
higher than 0.7 (in absolute terms) are indicated in white in the heat map, suggesting a high degree of correlation.

### Signs of High Risk

- A large number of variables in the dataset showing a high degree of correlation (coefficients approaching ±1).
  This indicates redundancy within the dataset, suggesting that some variables may not be contributing new
  information to the model.
- Potential risk of overfitting.

### Strengths

- Detects and quantifies the linearity of relationships between variables, aiding in identifying redundant
  variables to simplify models and potentially improve performance.
- The heatmap visualization provides an easy-to-understand overview of correlations, beneficial for users not
  comfortable with numerical matrices.

### Limitations

- Limited to detecting linear relationships, potentially missing non-linear relationships which impede
  opportunities for dimensionality reduction.
- Measures only the degree of linear relationship, not the strength of one variable's effect on another.
- The 0.7 correlation threshold is arbitrary and might exclude valid dependencies with lower coefficients.

##### validmind.tests.data_validation.PhillipsPerronArch

**Functions:**

- [**PhillipsPerronArch**](#validmind.tests.data_validation.PhillipsPerronArch.PhillipsPerronArch) – Assesses the stationarity of time series data in each feature of the ML model using the Phillips-Perron test.

**Attributes:**

- [**logger**](#validmind.tests.data_validation.PhillipsPerronArch.logger) –

###### validmind.tests.data_validation.PhillipsPerronArch.PhillipsPerronArch

```python
PhillipsPerronArch(dataset)
```

Assesses the stationarity of time series data in each feature of the ML model using the Phillips-Perron test.

### Purpose

The Phillips-Perron (PP) test is used to determine the stationarity of time series data for each feature in a
dataset, which is crucial for forecasting tasks. It tests the null hypothesis that a time series is unit-root
non-stationary. This is vital for understanding the stochastic behavior of the data and ensuring the robustness and
validity of predictions generated by regression analysis models.

### Test Mechanism

The PP test is conducted for each feature in the dataset as follows:

- A data frame is created from the dataset.
- For each column, the Phillips-Perron method calculates the test statistic, p-value, lags used, and number of
  observations.
- The results are then stored for each feature, providing a metric that indicates the stationarity of the time
  series data.

### Signs of High Risk

- A high p-value, indicating that the series has a unit root and is non-stationary.
- Test statistic values exceeding critical values, suggesting non-stationarity.
- High 'usedlag' value, pointing towards autocorrelation issues that may degrade model performance.

### Strengths

- Resilience against heteroskedasticity in the error term.
- Effective for long time series data.
- Helps in determining whether the time series is stationary, aiding in the selection of suitable forecasting
  models.

### Limitations

- Applicable only within a univariate time series framework.
- Relies on asymptotic theory, which may reduce the test’s power for small sample sizes.
- Non-stationary time series must be converted to stationary series through differencing, potentially leading to
  loss of important data points.

###### validmind.tests.data_validation.PhillipsPerronArch.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.data_validation.ProtectedClassesCombination

**Functions:**

- [**ProtectedClassesCombination**](#validmind.tests.data_validation.ProtectedClassesCombination.ProtectedClassesCombination) – Visualizes combinations of protected classes and their corresponding error metric differences.

**Attributes:**

- [**logger**](#validmind.tests.data_validation.ProtectedClassesCombination.logger) –

###### validmind.tests.data_validation.ProtectedClassesCombination.ProtectedClassesCombination

```python
ProtectedClassesCombination(dataset, model, protected_classes=None)
```

Visualizes combinations of protected classes and their corresponding error metric differences.

### Purpose

This test aims to provide insights into how different combinations of protected classes affect various error metrics,
particularly the false negative rate (FNR) and false positive rate (FPR). By visualizing these combinations,
it helps identify potential biases or disparities in model performance across different intersectional groups.

### Test Mechanism

The test performs the following steps:

1. Combines the specified protected class columns to create a single multi-class category.
1. Calculates error metrics (FNR, FPR, etc.) for each combination of protected classes.
1. Generates visualizations showing the distribution of these metrics across all class combinations.

### Signs of High Risk

- Large disparities in FNR or FPR across different protected class combinations.
- Consistent patterns of higher error rates for specific combinations of protected attributes.
- Unexpected or unexplainable variations in error metrics between similar group combinations.

### Strengths

- Provides a comprehensive view of intersectional fairness across multiple protected attributes.
- Allows for easy identification of potentially problematic combinations of protected classes.
- Visualizations make it easier to spot patterns or outliers in model performance across groups.

### Limitations

- May become complex and difficult to interpret with a large number of protected classes or combinations.
- Does not provide statistical significance of observed differences.
- Visualization alone may not capture all nuances of intersectional fairness.

###### validmind.tests.data_validation.ProtectedClassesCombination.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.data_validation.ProtectedClassesDescription

**Functions:**

- [**ProtectedClassesDescription**](#validmind.tests.data_validation.ProtectedClassesDescription.ProtectedClassesDescription) – Visualizes the distribution of protected classes in the dataset relative to the target variable

**Attributes:**

- [**logger**](#validmind.tests.data_validation.ProtectedClassesDescription.logger) –

###### validmind.tests.data_validation.ProtectedClassesDescription.ProtectedClassesDescription

```python
ProtectedClassesDescription(dataset, protected_classes=None)
```

Visualizes the distribution of protected classes in the dataset relative to the target variable
and provides descriptive statistics.

### Purpose

The ProtectedClassesDescription test aims to identify potential biases or significant differences in the
distribution of target outcomes across different protected classes. This visualization and statistical summary
help in understanding the relationship between protected attributes and the target variable, which is crucial
for assessing fairness in machine learning models.

### Test Mechanism

The function creates interactive stacked bar charts for each specified protected class using Plotly.
Additionally, it generates a single table of descriptive statistics for all protected classes, including:

- Protected class and category
- Count and percentage of each category within the protected class
- Mean, median, and mode of the target variable for each category
- Standard deviation of the target variable for each category
- Minimum and maximum values of the target variable for each category

### Signs of High Risk

- Significant imbalances in the distribution of target outcomes across different categories of a protected class.
- Large disparities in mean, median, or mode of the target variable across categories.
- Underrepresentation or overrepresentation of certain groups within protected classes.
- High standard deviations in certain categories, indicating potential volatility or outliers.

### Strengths

- Provides both visual and statistical representation of potential biases in the dataset.
- Allows for easy identification of imbalances in target variable distribution across protected classes.
- Interactive plots enable detailed exploration of the data.
- Consolidated statistical summary provides quantitative measures to complement visual analysis.
- Applicable to both classification and regression tasks.

### Limitations

- Does not provide advanced statistical measures of bias or fairness.
- May become cluttered if there are many categories within a protected class or many unique target values.
- Interpretation may require domain expertise to understand the implications of observed disparities.
- Does not account for intersectionality or complex interactions between multiple protected attributes.

###### validmind.tests.data_validation.ProtectedClassesDescription.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.data_validation.ProtectedClassesDisparity

**Functions:**

- [**ProtectedClassesDisparity**](#validmind.tests.data_validation.ProtectedClassesDisparity.ProtectedClassesDisparity) – Investigates disparities in model performance across different protected class segments.

**Attributes:**

- [**logger**](#validmind.tests.data_validation.ProtectedClassesDisparity.logger) –

###### validmind.tests.data_validation.ProtectedClassesDisparity.ProtectedClassesDisparity

```python
ProtectedClassesDisparity(
    dataset,
    model,
    protected_classes=None,
    disparity_tolerance=1.25,
    metrics=["fnr", "fpr", "tpr"],
)
```

Investigates disparities in model performance across different protected class segments.

### Purpose

This test aims to identify and quantify potential biases in model outcomes by comparing various performance metrics
across different segments of protected classes. It helps in assessing whether the model produces discriminatory
outcomes for certain groups, which is crucial for ensuring fairness in machine learning models.

### Test Mechanism

The test performs the following steps:

1. Calculates performance metrics (e.g., false negative rate, false positive rate, true positive rate) for each segment
   of the specified protected classes.
1. Computes disparity ratios by comparing these metrics between different segments and a reference group.
1. Generates visualizations showing the disparities and their relation to a user-defined disparity tolerance threshold.
1. Produces a comprehensive table with various disparity metrics for detailed analysis.

### Signs of High Risk

- Disparity ratios exceeding the specified disparity tolerance threshold.
- Consistent patterns of higher error rates or lower performance for specific protected class segments.
- Statistically significant differences in performance metrics across segments.

### Strengths

- Provides a comprehensive view of model fairness across multiple protected attributes and metrics.
- Allows for easy identification of problematic disparities through visual and tabular representations.
- Customizable disparity tolerance threshold to align with specific use-case requirements.
- Applicable to various performance metrics, offering a multi-faceted analysis of model fairness.

### Limitations

- Relies on a predefined reference group for each protected class, which may not always be the most appropriate choice.
- Does not account for intersectionality between different protected attributes.
- The interpretation of results may require domain expertise to understand the implications of observed disparities.

###### validmind.tests.data_validation.ProtectedClassesDisparity.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.data_validation.ProtectedClassesThresholdOptimizer

**Functions:**

- [**ProtectedClassesThresholdOptimizer**](#validmind.tests.data_validation.ProtectedClassesThresholdOptimizer.ProtectedClassesThresholdOptimizer) – Obtains a classifier by applying group-specific thresholds to the provided estimator.
- [**calculate_fairness_metrics**](#validmind.tests.data_validation.ProtectedClassesThresholdOptimizer.calculate_fairness_metrics) –
- [**calculate_group_metrics**](#validmind.tests.data_validation.ProtectedClassesThresholdOptimizer.calculate_group_metrics) –
- [**get_thresholds_by_group**](#validmind.tests.data_validation.ProtectedClassesThresholdOptimizer.get_thresholds_by_group) –
- [**initialize_and_fit_optimizer**](#validmind.tests.data_validation.ProtectedClassesThresholdOptimizer.initialize_and_fit_optimizer) –
- [**make_predictions**](#validmind.tests.data_validation.ProtectedClassesThresholdOptimizer.make_predictions) –
- [**plot_thresholds**](#validmind.tests.data_validation.ProtectedClassesThresholdOptimizer.plot_thresholds) –

**Attributes:**

- [**logger**](#validmind.tests.data_validation.ProtectedClassesThresholdOptimizer.logger) –

###### validmind.tests.data_validation.ProtectedClassesThresholdOptimizer.ProtectedClassesThresholdOptimizer

```python
ProtectedClassesThresholdOptimizer(
    dataset, pipeline=None, protected_classes=None, X_train=None, y_train=None
)
```

Obtains a classifier by applying group-specific thresholds to the provided estimator.

### Purpose

This test aims to optimize the fairness of a machine learning model by applying different
classification thresholds for different protected groups. It helps in mitigating bias and
achieving more equitable outcomes across different demographic groups.

### Test Mechanism

The test uses Fairlearn's ThresholdOptimizer to:

1. Fit an optimizer on the training data, considering protected classes.
1. Apply optimized thresholds to make predictions on the test data.
1. Calculate and report various fairness metrics.
1. Visualize the optimized thresholds.

### Signs of High Risk

- Large disparities in fairness metrics (e.g., Demographic Parity Ratio, Equalized Odds Ratio)
  across different protected groups.
- Significant differences in False Positive Rates (FPR) or True Positive Rates (TPR) between groups.
- Thresholds that vary widely across different protected groups.

### Strengths

- Provides a post-processing method to improve model fairness without modifying the original model.
- Allows for balancing multiple fairness criteria simultaneously.
- Offers visual insights into the threshold optimization process.

### Limitations

- May lead to a decrease in overall model performance while improving fairness.
- Requires access to protected attribute information at prediction time.
- The effectiveness can vary depending on the chosen fairness constraint and objective.

###### validmind.tests.data_validation.ProtectedClassesThresholdOptimizer.calculate_fairness_metrics

```python
calculate_fairness_metrics(test_df, target, y_pred_opt, protected_classes)
```

###### validmind.tests.data_validation.ProtectedClassesThresholdOptimizer.calculate_group_metrics

```python
calculate_group_metrics(test_df, target, y_pred_opt, protected_classes)
```

###### validmind.tests.data_validation.ProtectedClassesThresholdOptimizer.get_thresholds_by_group

```python
get_thresholds_by_group(threshold_optimizer)
```

###### validmind.tests.data_validation.ProtectedClassesThresholdOptimizer.initialize_and_fit_optimizer

```python
initialize_and_fit_optimizer(pipeline, X_train, y_train, protected_classes_df)
```

###### validmind.tests.data_validation.ProtectedClassesThresholdOptimizer.logger

```python
logger = get_logger(__name__)
```

###### validmind.tests.data_validation.ProtectedClassesThresholdOptimizer.make_predictions

```python
make_predictions(threshold_optimizer, test_df, protected_classes)
```

###### validmind.tests.data_validation.ProtectedClassesThresholdOptimizer.plot_thresholds

```python
plot_thresholds(threshold_optimizer)
```

##### validmind.tests.data_validation.RollingStatsPlot

**Functions:**

- [**RollingStatsPlot**](#validmind.tests.data_validation.RollingStatsPlot.RollingStatsPlot) – Evaluates the stationarity of time series data by plotting its rolling mean and standard deviation over a specified
- [**plot_rolling_statistics**](#validmind.tests.data_validation.RollingStatsPlot.plot_rolling_statistics) –

###### validmind.tests.data_validation.RollingStatsPlot.RollingStatsPlot

```python
RollingStatsPlot(dataset, window_size=12)
```

Evaluates the stationarity of time series data by plotting its rolling mean and standard deviation over a specified
window.

### Purpose

The `RollingStatsPlot` metric is employed to gauge the stationarity of time series data in a given dataset. This
metric specifically evaluates the rolling mean and rolling standard deviation of the dataset over a pre-specified
window size. The rolling mean provides an understanding of the average trend in the data, while the rolling
standard deviation gauges the volatility of the data within the window. It is critical in preparing time series
data for modeling as it reveals key insights into data behavior across time.

### Test Mechanism

This mechanism is comprised of two steps. Initially, the rolling mean and standard deviation for each of the
dataset's columns are calculated over a window size, which can be user-specified or by default set to 12 data
points. Then, the calculated rolling mean and standard deviation are visualized via separate plots, illustrating
the trends and volatility in the dataset. A straightforward check is conducted to ensure the existence of columns
in the dataset, and to verify that the given dataset has been indexed by its date and time—a necessary prerequisite
for time series analysis.

### Signs of High Risk

- The presence of non-stationary patterns in either the rolling mean or the rolling standard deviation plots, which
  could indicate trends or seasonality in the data that may affect the performance of time series models.
- Missing columns in the dataset, which would prevent the execution of this metric correctly.
- The detection of NaN values in the dataset, which may need to be addressed before the metric can proceed
  successfully.

### Strengths

- Offers visualizations of trending behavior and volatility within the data, facilitating a broader understanding
  of the dataset's inherent characteristics.
- Checks of the dataset's integrity, such as the existence of all required columns and the availability of a
  datetime index.
- Adjusts to accommodate various window sizes, thus allowing accurate analysis of data with differing temporal
  granularities.
- Considers each column of the data individually, thereby accommodating multi-feature datasets.

### Limitations

- For all columns, a fixed-size window is utilized. This may not accurately capture patterns in datasets where
  different features may require different optimal window sizes.
- Requires the dataset to be indexed by date and time, hence it may not be usable for datasets without a timestamp
  index.
- Primarily serves for data visualization as it does not facilitate any quantitative measures for stationarity,
  such as through statistical tests. Therefore, the interpretation is subjective and depends heavily on modeler
  discretion.

###### validmind.tests.data_validation.RollingStatsPlot.plot_rolling_statistics

```python
plot_rolling_statistics(df, col, window_size)
```

##### validmind.tests.data_validation.RunsTest

**Functions:**

- [**RunsTest**](#validmind.tests.data_validation.RunsTest.RunsTest) – Executes Runs Test on ML model to detect non-random patterns in output data sequence.

###### validmind.tests.data_validation.RunsTest.RunsTest

```python
RunsTest(dataset)
```

Executes Runs Test on ML model to detect non-random patterns in output data sequence.

### Purpose

The Runs Test is a statistical procedure used to determine whether the sequence of data extracted from the ML model
behaves randomly or not. Specifically, it analyzes runs, sequences of consecutive positives or negatives, in the
data to check if there are more or fewer runs than expected under the assumption of randomness. This can be an
indication of some pattern, trend, or cycle in the model's output which may need attention.

### Test Mechanism

The testing mechanism applies the Runs Test from the statsmodels module on each column of the training dataset. For
every feature in the dataset, a Runs Test is executed, whose output includes a Runs Statistic and P-value. A low
P-value suggests that data arrangement in the feature is not likely to be random. The results are stored in a
dictionary where the keys are the feature names, and the values are another dictionary storing the test statistic
and the P-value for each feature.

### Signs of High Risk

- High risk is indicated when the P-value is close to zero.
- If the P-value is less than a predefined significance level (like 0.05), it suggests that the runs (series of
  positive or negative values) in the model's output are not random and are longer or shorter than what is expected
  under a random scenario.
- This would mean there's a high risk of non-random distribution of errors or model outcomes, suggesting potential
  issues with the model.

### Strengths

- Straightforward and fast for detecting non-random patterns in data sequence.
- Validates assumptions of randomness, which is valuable for checking error distributions in regression models,
  trendless time series data, and ensuring a classifier doesn't favor one class over another.
- Can be applied to both classification and regression tasks, making it versatile.

### Limitations

- Assumes that the data is independently and identically distributed (i.i.d.), which might not be the case for many
  real-world datasets.
- The conclusion drawn from the low P-value indicating non-randomness does not provide information about the type
  or the source of the detected pattern.
- Sensitive to extreme values (outliers), and overly large or small run sequences can influence the results.
- Does not provide model performance evaluation; it is used to detect patterns in the sequence of outputs only.

##### validmind.tests.data_validation.ScatterPlot

**Functions:**

- [**ScatterPlot**](#validmind.tests.data_validation.ScatterPlot.ScatterPlot) – Assesses visual relationships, patterns, and outliers among features in a dataset through scatter plot matrices.

###### validmind.tests.data_validation.ScatterPlot.ScatterPlot

```python
ScatterPlot(dataset)
```

Assesses visual relationships, patterns, and outliers among features in a dataset through scatter plot matrices.

### Purpose

The ScatterPlot test aims to visually analyze a given dataset by constructing a scatter plot matrix of its
numerical features. The primary goal is to uncover relationships, patterns, and outliers across different features
to provide both quantitative and qualitative insights into multidimensional relationships within the dataset. This
visual assessment aids in understanding the efficacy of the chosen features for model training and their
suitability.

### Test Mechanism

Using the Seaborn library, the ScatterPlot function creates the scatter plot matrix. The process involves
retrieving all numerical columns from the dataset and generating a scatter matrix for these columns. The resulting
scatter plot provides visual representations of feature relationships. The function also adjusts axis labels for
readability and returns the final plot as a Matplotlib Figure object for further analysis and visualization.

### Signs of High Risk

- The emergence of non-linear or random patterns across different feature pairs, suggesting complex relationships
  unsuitable for linear assumptions.
- Lack of clear patterns or clusters, indicating weak or non-existent correlations among features, which could
  challenge certain model types.
- Presence of outliers, as visual outliers can adversely influence the model's performance.

### Strengths

- Provides insight into the multidimensional relationships among multiple features.
- Assists in identifying trends, correlations, and outliers that could affect model performance.
- Validates assumptions made during model creation, such as linearity.
- Versatile for application in both regression and classification tasks.
- Using Seaborn facilitates an intuitive and detailed visual exploration of data.

### Limitations

- Scatter plot matrices may become cluttered and hard to decipher as the number of features increases.
- Primarily reveals pairwise relationships and may fail to illuminate complex interactions involving three or more
  features.
- Being a visual tool, precision in quantitative analysis might be compromised.
- Outliers not clearly visible in plots can be missed, affecting model performance.
- Assumes that the dataset can fit into the computer's memory, which might not be valid for extremely large
  datasets.

##### validmind.tests.data_validation.SeasonalDecompose

**Functions:**

- [**SeasonalDecompose**](#validmind.tests.data_validation.SeasonalDecompose.SeasonalDecompose) – Assesses patterns and seasonality in a time series dataset by decomposing its features into foundational components.

**Attributes:**

- [**logger**](#validmind.tests.data_validation.SeasonalDecompose.logger) –

###### validmind.tests.data_validation.SeasonalDecompose.SeasonalDecompose

```python
SeasonalDecompose(dataset, seasonal_model='additive')
```

Assesses patterns and seasonality in a time series dataset by decomposing its features into foundational components.

### Purpose

The Seasonal Decompose test aims to decompose the features of a time series dataset into their fundamental
components: observed, trend, seasonal, and residuals. By utilizing the Seasonal Decomposition of Time Series by
Loess (STL) method, the test identifies underlying patterns, predominantly seasonality, in the dataset's features.
This aids in developing a more comprehensive understanding of the dataset, which in turn facilitates more effective
model validation.

### Test Mechanism

The testing process leverages the `seasonal_decompose` function from the `statsmodels.tsa.seasonal` library to
evaluate each feature in the dataset. It isolates each feature into four components—observed, trend, seasonal, and
residuals—and generates six subplot graphs per feature for visual interpretation. Prior to decomposition, the test
scrutinizes and removes any non-finite values, ensuring the reliability of the analysis.

### Signs of High Risk

- **Non-Finiteness**: Datasets with a high number of non-finite values may flag as high risk since these values are
  omitted before conducting the seasonal decomposition.
- **Frequent Warnings**: Chronic failure to infer the frequency for a scrutinized feature indicates high risk.
- **High Seasonality**: A significant seasonal component could potentially render forecasts unreliable due to
  overwhelming seasonal variation.

### Strengths

- **Seasonality Detection**: Accurately discerns hidden seasonality patterns in dataset features.
- **Visualization**: Facilitates interpretation and comprehension through graphical representations.
- **Unrestricted Usage**: Not confined to any specific regression model, promoting wide-ranging applicability.

### Limitations

- **Dependence on Assumptions**: Assumes that dataset features are periodically distributed. Features with no
  inferable frequency are excluded from the test.
- **Handling Non-Finite Values**: Disregards non-finite values during analysis, potentially resulting in an
  incomplete understanding of the dataset.
- **Unreliability with Noisy Datasets**: Produces unreliable results when used with datasets that contain heavy
  noise.

###### validmind.tests.data_validation.SeasonalDecompose.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.data_validation.ShapiroWilk

**Functions:**

- [**ShapiroWilk**](#validmind.tests.data_validation.ShapiroWilk.ShapiroWilk) – Evaluates feature-wise normality of training data using the Shapiro-Wilk test.

###### validmind.tests.data_validation.ShapiroWilk.ShapiroWilk

```python
ShapiroWilk(dataset)
```

Evaluates feature-wise normality of training data using the Shapiro-Wilk test.

### Purpose

The Shapiro-Wilk test is utilized to investigate whether a particular dataset conforms to the standard normal
distribution. This analysis is crucial in machine learning modeling because the normality of the data can
profoundly impact the performance of the model. This metric is especially useful in evaluating various features of
the dataset in both classification and regression tasks.

### Test Mechanism

The Shapiro-Wilk test is conducted on each feature column of the training dataset to determine if the data
contained fall within the normal distribution. The test presents a statistic and a p-value, with the p-value
serving to validate or repudiate the null hypothesis, which is that the tested data is normally distributed.

### Signs of High Risk

- A p-value that falls below 0.05 signifies a high risk as it discards the null hypothesis, indicating that the
  data does not adhere to the normal distribution.
- For machine learning models built on the presumption of data normality, such an outcome could result in subpar
  performance or incorrect predictions.

### Strengths

- The Shapiro-Wilk test is esteemed for its level of accuracy, thereby making it particularly well-suited to
  datasets of small to moderate sizes.
- It proves its versatility through its efficient functioning in both classification and regression tasks.
- By separately testing each feature column, the Shapiro-Wilk test can raise an alarm if a specific feature does
  not comply with the normality.

### Limitations

- The Shapiro-Wilk test's sensitivity can be a disadvantage as it often rejects the null hypothesis (i.e., data is
  normally distributed), even for minor deviations, especially in large datasets. This may lead to unwarranted 'false
  alarms' of high risk by deeming the data as not normally distributed even if it approximates normal distribution.
- Exceptional care must be taken in managing missing data or outliers prior to testing as these can greatly skew
  the results.
- Lastly, the Shapiro-Wilk test is not optimally suited for processing data with pronounced skewness or kurtosis.

##### validmind.tests.data_validation.Skewness

**Functions:**

- [**Skewness**](#validmind.tests.data_validation.Skewness.Skewness) – Evaluates the skewness of numerical data in a dataset to check against a defined threshold, aiming to ensure data

###### validmind.tests.data_validation.Skewness.Skewness

```python
Skewness(dataset, max_threshold=1)
```

Evaluates the skewness of numerical data in a dataset to check against a defined threshold, aiming to ensure data
quality and optimize model performance.

### Purpose

The purpose of the Skewness test is to measure the asymmetry in the distribution of data within a predictive
machine learning model. Specifically, it evaluates the divergence of said distribution from a normal distribution.
Understanding the level of skewness helps identify data quality issues, which are crucial for optimizing the
performance of traditional machine learning models in both classification and regression settings.

### Test Mechanism

This test calculates the skewness of numerical columns in the dataset, focusing specifically on numerical data
types. The calculated skewness value is then compared against a predetermined maximum threshold, which is set by
default to 1. If the skewness value is less than this maximum threshold, the test passes; otherwise, it fails. The
test results, along with the skewness values and column names, are then recorded for further analysis.

### Signs of High Risk

- Substantial skewness levels that significantly exceed the maximum threshold.
- Persistent skewness in the data, indicating potential issues with the foundational assumptions of the machine
  learning model.
- Subpar model performance, erroneous predictions, or biased inferences due to skewed data distributions.

### Strengths

- Fast and efficient identification of unequal data distributions within a machine learning model.
- Adjustable maximum threshold parameter, allowing for customization based on user needs.
- Provides a clear quantitative measure to mitigate model risks related to data skewness.

### Limitations

- Only evaluates numeric columns, potentially missing skewness or bias in non-numeric data.
- Assumes that data should follow a normal distribution, which may not always be applicable to real-world data.
- Subjective threshold for risk grading, requiring expert input and recurrent iterations for refinement.

##### validmind.tests.data_validation.SpreadPlot

**Functions:**

- [**SpreadPlot**](#validmind.tests.data_validation.SpreadPlot.SpreadPlot) – Assesses potential correlations between pairs of time series variables through visualization to enhance

###### validmind.tests.data_validation.SpreadPlot.SpreadPlot

```python
SpreadPlot(dataset)
```

Assesses potential correlations between pairs of time series variables through visualization to enhance
understanding of their relationships.

### Purpose

The SpreadPlot test aims to graphically illustrate and analyze the relationships between pairs of time series
variables within a given dataset. This facilitated understanding helps in identifying and assessing potential time
series correlations, such as cointegration, between the variables.

### Test Mechanism

The SpreadPlot test computes and represents the spread between each pair of time series variables in the dataset.
Specifically, the difference between two variables is calculated and presented as a line graph. This process is
iterated for each unique pair of variables in the dataset, allowing for comprehensive visualization of their
relationships.

### Signs of High Risk

- Large fluctuations in the spread over a given timespan.
- Unexpected patterns or trends that may signal potential risks in the underlying correlations between the
  variables.
- Presence of significant missing data or extreme outlier values, which could potentially skew the spread and
  indicate high risk.

### Strengths

- Allows for thorough visual examination and interpretation of the correlations between time-series pairs.
- Aids in revealing complex relationships like cointegration.
- Enhances interpretability by visualizing the relationships, thereby helping in spotting outliers and trends.
- Capable of handling numerous variable pairs from the dataset through a versatile and adaptable process.

### Limitations

- Primarily serves as a visualization tool and does not offer quantitative measurements or statistics to
  objectively determine relationships.
- Heavily relies on the quality and granularity of the data—missing data or outliers can notably disturb the
  interpretation of relationships.
- Can become inefficient or difficult to interpret with a high number of variables due to the profuse number of
  plots.
- Might not completely capture intricate non-linear relationships between the variables.

##### validmind.tests.data_validation.TabularCategoricalBarPlots

**Functions:**

- [**TabularCategoricalBarPlots**](#validmind.tests.data_validation.TabularCategoricalBarPlots.TabularCategoricalBarPlots) – Generates and visualizes bar plots for each category in categorical features to evaluate the dataset's composition.

###### validmind.tests.data_validation.TabularCategoricalBarPlots.TabularCategoricalBarPlots

```python
TabularCategoricalBarPlots(dataset)
```

Generates and visualizes bar plots for each category in categorical features to evaluate the dataset's composition.

### Purpose

The purpose of this metric is to visually analyze categorical data using bar plots. It is intended to evaluate the
dataset's composition by displaying the counts of each category in each categorical feature.

### Test Mechanism

The provided dataset is first checked to determine if it contains any categorical variables. If no categorical
columns are found, the tool raises a ValueError. For each categorical variable in the dataset, a separate bar plot
is generated. The number of occurrences for each category is calculated and displayed on the plot. If a dataset
contains multiple categorical columns, multiple bar plots are produced.

### Signs of High Risk

- High risk could occur if the categorical variables exhibit an extreme imbalance, with categories having very few
  instances possibly being underrepresented in the model, which could affect the model's performance and its ability
  to generalize.
- Another sign of risk is if there are too many categories in a single variable, which could lead to overfitting
  and make the model complex.

### Strengths

- Provides a visual and intuitively understandable representation of categorical data.
- Aids in the analysis of variable distributions.
- Helps in easily identifying imbalances or rare categories that could affect the model's performance.

### Limitations

- This method only works with categorical data and won't apply to numerical variables.
- It does not provide informative value when there are too many categories, as the bar chart could become cluttered
  and hard to interpret.
- Offers no insights into the model's performance or precision, but rather provides a descriptive analysis of the
  input.

##### validmind.tests.data_validation.TabularDateTimeHistograms

**Functions:**

- [**TabularDateTimeHistograms**](#validmind.tests.data_validation.TabularDateTimeHistograms.TabularDateTimeHistograms) – Generates histograms to provide graphical insight into the distribution of time intervals in a model's datetime

###### validmind.tests.data_validation.TabularDateTimeHistograms.TabularDateTimeHistograms

```python
TabularDateTimeHistograms(dataset)
```

Generates histograms to provide graphical insight into the distribution of time intervals in a model's datetime
data.

### Purpose

The `TabularDateTimeHistograms` metric is designed to provide graphical insight into the distribution of time
intervals in a machine learning model's datetime data. By plotting histograms of differences between consecutive
date entries in all datetime variables, it enables an examination of the underlying pattern of time series data and
identification of anomalies.

### Test Mechanism

This test operates by first identifying all datetime columns and extracting them from the dataset. For each
datetime column, it next computes the differences (in days) between consecutive dates, excluding zero values, and
visualizes these differences in a histogram. The Plotly library's histogram function is used to generate
histograms, which are labeled appropriately and provide a graphical representation of the frequency of different
day intervals in the dataset.

### Signs of High Risk

- If no datetime columns are detected in the dataset, this would lead to a ValueError. Hence, the absence of
  datetime columns signifies a high risk.
- A severely skewed or irregular distribution depicted in the histogram may indicate possible complications with
  the data, such as faulty timestamps or abnormalities.

### Strengths

- The metric offers a visual overview of time interval frequencies within the dataset, supporting the recognition
  of inherent patterns.
- Histogram plots can aid in the detection of potential outliers and data anomalies, contributing to an assessment
  of data quality.
- The metric is versatile, compatible with a range of task types, including classification and regression, and can
  work with multiple datetime variables if present.

### Limitations

- A major weakness of this metric is its dependence on the visual examination of data, as it does not provide a
  measurable evaluation of the model.
- The metric might overlook complex or multi-dimensional trends in the data.
- The test is only applicable to datasets containing datetime columns and will fail if such columns are unavailable.
- The interpretation of the histograms relies heavily on the domain expertise and experience of the reviewer.

##### validmind.tests.data_validation.TabularDescriptionTables

**Functions:**

- [**TabularDescriptionTables**](#validmind.tests.data_validation.TabularDescriptionTables.TabularDescriptionTables) – Summarizes key descriptive statistics for numerical, categorical, and datetime variables in a dataset.
- [**get_categorical_columns**](#validmind.tests.data_validation.TabularDescriptionTables.get_categorical_columns) –
- [**get_datetime_columns**](#validmind.tests.data_validation.TabularDescriptionTables.get_datetime_columns) –
- [**get_numerical_columns**](#validmind.tests.data_validation.TabularDescriptionTables.get_numerical_columns) –
- [**get_summary_statistics_categorical**](#validmind.tests.data_validation.TabularDescriptionTables.get_summary_statistics_categorical) –
- [**get_summary_statistics_datetime**](#validmind.tests.data_validation.TabularDescriptionTables.get_summary_statistics_datetime) –
- [**get_summary_statistics_numerical**](#validmind.tests.data_validation.TabularDescriptionTables.get_summary_statistics_numerical) –

###### validmind.tests.data_validation.TabularDescriptionTables.TabularDescriptionTables

```python
TabularDescriptionTables(dataset)
```

Summarizes key descriptive statistics for numerical, categorical, and datetime variables in a dataset.

### Purpose

The main purpose of this metric is to gather and present the descriptive statistics of numerical, categorical, and
datetime variables present in a dataset. The attributes it measures include the count, mean, minimum and maximum
values, percentage of missing values, data types of fields, and unique values for categorical fields, among others.

### Test Mechanism

The test first segregates the variables in the dataset according to their data types (numerical, categorical, or
datetime). Then, it compiles summary statistics for each type of variable. The specifics of these statistics vary
depending on the type of variable:

- For numerical variables, the metric extracts descriptors like count, mean, minimum and maximum values, count of
  missing values, and data types.
- For categorical variables, it counts the number of unique values, displays unique values, counts missing values,
  and identifies data types.
- For datetime variables, it counts the number of unique values, identifies the earliest and latest dates, counts
  missing values, and identifies data types.

### Signs of High Risk

- Masses of missing values in the descriptive statistics results could hint at high risk or failure, indicating
  potential data collection, integrity, and quality issues.
- Detection of inappropriate distributions for numerical variables, like having negative values for variables that
  are always supposed to be positive.
- Identifying inappropriate data types, like a continuous variable being encoded as a categorical type.

### Strengths

- Provides a comprehensive overview of the dataset.
- Gives a snapshot into the essence of the numerical, categorical, and datetime fields.
- Identifies potential data quality issues such as missing values or inconsistencies crucial for building credible
  machine learning models.
- The metadata, including the data type and missing value information, are vital for anyone including data
  scientists dealing with the dataset before the modeling process.

### Limitations

- It does not perform any deeper statistical analysis or tests on the data.
- It does not handle issues such as outliers, or relationships between variables.
- It offers no insights into potential correlations or possible interactions between variables.
- It does not investigate the potential impact of missing values on the performance of the machine learning models.
- It does not explore potential transformation requirements that may be necessary to enhance the performance of the
  chosen algorithm.

###### validmind.tests.data_validation.TabularDescriptionTables.get_categorical_columns

```python
get_categorical_columns(dataset)
```

###### validmind.tests.data_validation.TabularDescriptionTables.get_datetime_columns

```python
get_datetime_columns(dataset)
```

###### validmind.tests.data_validation.TabularDescriptionTables.get_numerical_columns

```python
get_numerical_columns(dataset)
```

###### validmind.tests.data_validation.TabularDescriptionTables.get_summary_statistics_categorical

```python
get_summary_statistics_categorical(dataset, categorical_fields)
```

###### validmind.tests.data_validation.TabularDescriptionTables.get_summary_statistics_datetime

```python
get_summary_statistics_datetime(dataset, datetime_fields)
```

###### validmind.tests.data_validation.TabularDescriptionTables.get_summary_statistics_numerical

```python
get_summary_statistics_numerical(dataset, numerical_fields)
```

##### validmind.tests.data_validation.TabularNumericalHistograms

**Functions:**

- [**TabularNumericalHistograms**](#validmind.tests.data_validation.TabularNumericalHistograms.TabularNumericalHistograms) – Generates histograms for each numerical feature in a dataset to provide visual insights into data distribution and

###### validmind.tests.data_validation.TabularNumericalHistograms.TabularNumericalHistograms

```python
TabularNumericalHistograms(dataset)
```

Generates histograms for each numerical feature in a dataset to provide visual insights into data distribution and
detect potential issues.

### Purpose

The purpose of this test is to provide visual analysis of numerical data through the generation of histograms for
each numerical feature in the dataset. Histograms aid in the exploratory analysis of data, offering insight into
the distribution of the data, skewness, presence of outliers, and central tendencies. It helps in understanding if
the inputs to the model are normally distributed, which is a common assumption in many machine learning algorithms.

### Test Mechanism

This test scans the provided dataset and extracts all the numerical columns. For each numerical column, it
constructs a histogram using plotly, with 50 bins. The deployment of histograms offers a robust visual aid,
ensuring unruffled identification and understanding of numerical data distribution patterns.

### Signs of High Risk

- A high degree of skewness
- Unexpected data distributions
- Existence of extreme outliers in the histograms

These may indicate issues with the data that the model is receiving. If data for a numerical feature is expected to
follow a certain distribution (like a normal distribution) but does not, it could lead to sub-par performance by
the model. As such these instances should be treated as high-risk indicators.

### Strengths

- Provides a simple, easy-to-interpret visualization of how data for each numerical attribute is distributed.
- Helps detect skewed values and outliers that could potentially harm the AI model's performance.
- Can be applied to large datasets and multiple numerical variables conveniently.

### Limitations

- Only works with numerical data, thus ignoring non-numerical or categorical data.
- Does not analyze relationships between different features, only the individual feature distributions.
- Is a univariate analysis and may miss patterns or anomalies that only appear when considering multiple variables
  together.
- Does not provide any insight into how these features affect the output of the model; it is purely an input
  analysis tool.

##### validmind.tests.data_validation.TargetRateBarPlots

**Functions:**

- [**TargetRateBarPlots**](#validmind.tests.data_validation.TargetRateBarPlots.TargetRateBarPlots) – Generates bar plots visualizing the default rates of categorical features for a classification machine learning

###### validmind.tests.data_validation.TargetRateBarPlots.TargetRateBarPlots

```python
TargetRateBarPlots(dataset)
```

Generates bar plots visualizing the default rates of categorical features for a classification machine learning
model.

### Purpose

This test, implemented as a metric, is designed to provide an intuitive, graphical summary of the decision-making
patterns exhibited by a categorical classification machine learning model. The model's performance is evaluated
using bar plots depicting the ratio of target rates—meaning the proportion of positive classes—for different
categorical inputs. This allows for an easy, at-a-glance understanding of the model's accuracy.

### Test Mechanism

The test involves creating a pair of bar plots for each categorical feature in the dataset. The first plot depicts
the frequency of each category in the dataset, with each category visually distinguished by its unique color. The
second plot shows the mean target rate of each category (sourced from the "default_column"). Plotly, a Python
library, is used to generate these plots, with distinct plots created for each feature. If no specific columns are
selected, the test will generate plots for each categorical column in the dataset.

### Signs of High Risk

- Inconsistent or non-binary values in the "default_column" could complicate or render impossible the calculation
  of average target rates.
- Particularly low or high target rates for a specific category might suggest that the model is misclassifying
  instances of that category.

### Strengths

- This test offers a visually interpretable breakdown of the model's decisions, providing an easy way to spot
  irregularities, inconsistencies, or patterns.
- Its flexibility allows for the inspection of one or multiple columns, as needed.

### Limitations

- The readability of the bar plots drops as the number of distinct categories increases in the dataset, which can
  make them harder to understand and less useful.

##### validmind.tests.data_validation.TimeSeriesDescription

**Functions:**

- [**TimeSeriesDescription**](#validmind.tests.data_validation.TimeSeriesDescription.TimeSeriesDescription) – Generates a detailed analysis for the provided time series dataset, summarizing key statistics to identify trends,

###### validmind.tests.data_validation.TimeSeriesDescription.TimeSeriesDescription

```python
TimeSeriesDescription(dataset)
```

Generates a detailed analysis for the provided time series dataset, summarizing key statistics to identify trends,
patterns, and data quality issues.

### Purpose

The TimeSeriesDescription function aims to analyze an individual time series by providing a summary of key
statistics. This helps in understanding trends, patterns, and data quality issues within the time series.

### Test Mechanism

The function extracts the time series data and provides a summary of key statistics. The dataset is expected to
have a datetime index. The function checks this and raises an error if the index is not in datetime format. For
each variable (column) in the dataset, appropriate statistics including start date, end date, frequency, number of
missing values, count, min, and max values are calculated.

### Signs of High Risk

- If the index of the dataset is not in datetime format, it could lead to errors in time-series analysis.
- Inconsistent or missing data within the dataset might affect the analysis of trends and patterns.

### Strengths

- Provides a comprehensive summary of key statistics for each variable, helping to identify data quality issues
  such as missing values.
- Helps in understanding the distribution and range of the data by including min and max values.

### Limitations

- Assumes that the dataset is provided as a DataFrameDataset object with a .df attribute to access the pandas
  DataFrame.
- Only analyzes datasets with a datetime index and will raise an error for other types of indices.
- Does not handle large datasets efficiently; performance may degrade with very large datasets.

##### validmind.tests.data_validation.TimeSeriesDescriptiveStatistics

**Functions:**

- [**TimeSeriesDescriptiveStatistics**](#validmind.tests.data_validation.TimeSeriesDescriptiveStatistics.TimeSeriesDescriptiveStatistics) – Evaluates the descriptive statistics of a time series dataset to identify trends, patterns, and data quality issues.

###### validmind.tests.data_validation.TimeSeriesDescriptiveStatistics.TimeSeriesDescriptiveStatistics

```python
TimeSeriesDescriptiveStatistics(dataset)
```

Evaluates the descriptive statistics of a time series dataset to identify trends, patterns, and data quality issues.

### Purpose

The purpose of the TimeSeriesDescriptiveStatistics function is to analyze an individual time series by providing a
summary of key descriptive statistics. This analysis helps in understanding trends, patterns, and data quality
issues within the time series dataset.

### Test Mechanism

The function extracts the time series data and provides a summary of key descriptive statistics. The dataset is
expected to have a datetime index, and the function will check this and raise an error if the index is not in a
datetime format. For each variable (column) in the dataset, appropriate statistics, including start date, end date,
min, mean, max, skewness, kurtosis, and count, are calculated.

### Signs of High Risk

- If the index of the dataset is not in datetime format, it could lead to errors in time-series analysis.
- Inconsistent or missing data within the dataset might affect the analysis of trends and patterns.

### Strengths

- Provides a comprehensive summary of key descriptive statistics for each variable.
- Helps identify data quality issues and understand the distribution of the data.

### Limitations

- Assumes the dataset is provided as a DataFrameDataset object with a .df attribute to access the pandas DataFrame.
- Only analyzes datasets with a datetime index and will raise an error for other types of indices.
- Does not handle large datasets efficiently, and performance may degrade with very large datasets.

##### validmind.tests.data_validation.TimeSeriesFrequency

**Functions:**

- [**TimeSeriesFrequency**](#validmind.tests.data_validation.TimeSeriesFrequency.TimeSeriesFrequency) – Evaluates consistency of time series data frequency and generates a frequency plot.

###### validmind.tests.data_validation.TimeSeriesFrequency.TimeSeriesFrequency

```python
TimeSeriesFrequency(dataset)
```

Evaluates consistency of time series data frequency and generates a frequency plot.

### Purpose

The purpose of the TimeSeriesFrequency test is to evaluate the consistency in the frequency of data points in a
time-series dataset. This test inspects the intervals or duration between each data point to determine if a fixed
pattern (such as daily, weekly, or monthly) exists. The identification of such patterns is crucial to time-series
analysis as any irregularities could lead to erroneous results and hinder the model's capacity for identifying
trends and patterns.

### Test Mechanism

Initially, the test checks if the dataframe index is in datetime format. Subsequently, it utilizes pandas'
`infer_freq` method to identify the frequency of each data series within the dataframe. The `infer_freq` method
attempts to establish the frequency of a time series and returns both the frequency string and a dictionary
relating these strings to their respective labels. The test compares the frequencies of all datasets. If they share
a common frequency, the test passes, but it fails if they do not. Additionally, Plotly is used to create a
frequency plot, offering a visual depiction of the time differences between consecutive entries in the dataframe
index.

### Signs of High Risk

- The test fails, indicating multiple unique frequencies within the dataset. This failure could suggest irregular
  intervals between observations, potentially interrupting pattern recognition or trend analysis.
- The presence of missing or null frequencies could be an indication of inconsistencies in data or gaps within the
  data collection process.

### Strengths

- This test uses a systematic approach to checking the consistency of data frequency within a time-series dataset.
- It increases the model's reliability by asserting the consistency of observations over time, an essential factor
  in time-series analysis.
- The test generates a visual plot, providing an intuitive representation of the dataset's frequency distribution,
  which caters to visual learners and aids in interpretation and explanation.

### Limitations

- This test is only applicable to time-series datasets and hence not suitable for other types of datasets.
- The `infer_freq` method might not always correctly infer frequency when faced with missing or irregular data
  points.
- Depending on context or the model under development, mixed frequencies might sometimes be acceptable, but this
  test considers them a failing condition.

##### validmind.tests.data_validation.TimeSeriesHistogram

**Functions:**

- [**TimeSeriesHistogram**](#validmind.tests.data_validation.TimeSeriesHistogram.TimeSeriesHistogram) – Visualizes distribution of time-series data using histograms and Kernel Density Estimation (KDE) lines.

###### validmind.tests.data_validation.TimeSeriesHistogram.TimeSeriesHistogram

```python
TimeSeriesHistogram(dataset, nbins=30)
```

Visualizes distribution of time-series data using histograms and Kernel Density Estimation (KDE) lines.

### Purpose

The TimeSeriesHistogram test aims to perform a histogram analysis on time-series data to assess the distribution of
values within a dataset over time. This test is useful for regression tasks and can be applied to various types of
data, such as internet traffic, stock prices, and weather data, providing insights into the probability
distribution, skewness, and kurtosis of the dataset.

### Test Mechanism

This test operates on a specific column within the dataset that must have a datetime type index. For each column in
the dataset, a histogram is created using Plotly's histplot function. If the dataset includes more than one
time-series, a distinct histogram is plotted for each series. Additionally, a Kernel Density Estimate (KDE) line is
drawn for each histogram, visualizing the data's underlying probability distribution. The x and y-axis labels are
hidden to focus solely on the data distribution.

### Signs of High Risk

- The dataset lacks a column with a datetime type index.
- The specified columns do not exist within the dataset.
- High skewness or kurtosis in the data distribution, indicating potential bias.
- Presence of significant outliers in the data distribution.

### Strengths

- Serves as a visual diagnostic tool for understanding data behavior and distribution trends.
- Effective for analyzing both single and multiple time-series data.
- KDE line provides a smooth estimate of the overall trend in data distribution.

### Limitations

- Provides a high-level view without specific numeric measures such as skewness or kurtosis.
- The histogram loses some detail due to binning of data values.
- Cannot handle non-numeric data columns.
- Histogram shape may be sensitive to the number of bins used.

##### validmind.tests.data_validation.TimeSeriesLinePlot

**Functions:**

- [**TimeSeriesLinePlot**](#validmind.tests.data_validation.TimeSeriesLinePlot.TimeSeriesLinePlot) – Generates and analyses time-series data through line plots revealing trends, patterns, anomalies over time.

###### validmind.tests.data_validation.TimeSeriesLinePlot.TimeSeriesLinePlot

```python
TimeSeriesLinePlot(dataset)
```

Generates and analyses time-series data through line plots revealing trends, patterns, anomalies over time.

### Purpose

The TimeSeriesLinePlot metric is designed to generate and analyze time series data through the creation of line
plots. This assists in the initial inspection of the data by providing a visual representation of patterns, trends,
seasonality, irregularity, and anomalies that may be present in the dataset over a period of time.

### Test Mechanism

The mechanism for this Python class involves extracting the column names from the provided dataset and subsequently
generating line plots for each column using the Plotly Python library. For every column in the dataset, a
time-series line plot is created where the values are plotted against the dataset's datetime index. It is important
to note that indexes that are not of datetime type will result in a ValueError.

### Signs of High Risk

- Presence of time-series data that does not have datetime indices.
- Provided columns do not exist in the provided dataset.
- The detection of anomalous patterns or irregularities in the time-series plots, indicating potential high model
  instability or probable predictive error.

### Strengths

- The visual representation of complex time series data, which simplifies understanding and helps in recognizing
  temporal trends, patterns, and anomalies.
- The adaptability of the metric, which allows it to effectively work with multiple time series within the same
  dataset.
- Enables the identification of anomalies and irregular patterns through visual inspection, assisting in spotting
  potential data or model performance problems.

### Limitations

- The effectiveness of the metric is heavily reliant on the quality and patterns of the provided time series data.
- Exclusively a visual tool, it lacks the capability to provide quantitative measurements, making it less effective
  for comparing and ranking multiple models or when specific numerical diagnostics are needed.
- The metric necessitates that the time-specific data has been transformed into a datetime index, with the data
  formatted correctly.
- The metric has an inherent limitation in that it cannot extract deeper statistical insights from the time series
  data, which can limit its efficacy with complex data structures and phenomena.

##### validmind.tests.data_validation.TimeSeriesMissingValues

**Functions:**

- [**TimeSeriesMissingValues**](#validmind.tests.data_validation.TimeSeriesMissingValues.TimeSeriesMissingValues) – Validates time-series data quality by confirming the count of missing values is below a certain threshold.

###### validmind.tests.data_validation.TimeSeriesMissingValues.TimeSeriesMissingValues

```python
TimeSeriesMissingValues(dataset, min_threshold=1)
```

Validates time-series data quality by confirming the count of missing values is below a certain threshold.

### Purpose

This test is designed to validate the quality of a historical time-series dataset by verifying that the number of
missing values is below a specified threshold. As time-series models greatly depend on the continuity and
temporality of data points, missing values could compromise the model's performance. Consequently, this test aims
to ensure data quality and readiness for the machine learning model, safeguarding its predictive capacity.

### Test Mechanism

The test method commences by validating if the dataset has a datetime index; if not, an error is raised. It
establishes a lower limit threshold for missing values and performs a missing values check on each column of the
dataset. An object for the test result is created stating whether the number of missing values is within the
specified threshold. Additionally, the test calculates the percentage of missing values alongside the raw count.

### Signs of High Risk

- The number of missing values in any column of the dataset surpasses the threshold, marking a failure and a
  high-risk scenario. The reasons could range from incomplete data collection, faulty sensors to data preprocessing
  errors.

### Strengths

- Effectively identifies missing values which could adversely affect the model’s performance.
- Applicable and customizable through the threshold parameter across different data sets.
- Goes beyond raw numbers by calculating the percentage of missing values, offering a more relative understanding
  of data scarcity.

### Limitations

- Although it identifies missing values, the test does not provide solutions to handle them.
- The test demands that the dataset should have a datetime index, hence limiting its use only to time series
  analysis.
- The test's sensitivity to the 'min_threshold' parameter may raise false alarms if set too strictly or may
  overlook problematic data if set too loosely.
- Solely focuses on the 'missingness' of the data and might fall short in addressing other aspects of data quality.

##### validmind.tests.data_validation.TimeSeriesOutliers

**Functions:**

- [**TimeSeriesOutliers**](#validmind.tests.data_validation.TimeSeriesOutliers.TimeSeriesOutliers) – Identifies and visualizes outliers in time-series data using the z-score method.

###### validmind.tests.data_validation.TimeSeriesOutliers.TimeSeriesOutliers

```python
TimeSeriesOutliers(dataset, zscore_threshold=3)
```

Identifies and visualizes outliers in time-series data using the z-score method.

### Purpose

This test is designed to identify outliers in time-series data using the z-score method. It's vital for ensuring
data quality before modeling, as outliers can skew predictive models and significantly impact their overall
performance.

### Test Mechanism

The test processes a given dataset which must have datetime indexing, checks if a 'zscore_threshold' parameter has
been supplied, and identifies columns with numeric data types. After finding numeric columns, the implementer then
applies the z-score method to each numeric column, identifying outliers based on the threshold provided. Each
outlier is listed together with their variable name, z-score, timestamp, and relative threshold in a dictionary and
converted to a DataFrame for convenient output. Additionally, it produces visual plots for each time series
illustrating outliers in the context of the broader dataset. The 'zscore_threshold' parameter sets the limit beyond
which a data point will be labeled as an outlier. The default threshold is set at 3, indicating that any data point
that falls 3 standard deviations away from the mean will be marked as an outlier.

### Signs of High Risk

- Many or substantial outliers are present within the dataset, indicating significant anomalies.
- Data points with z-scores higher than the set threshold.
- Potential impact on the performance of machine learning models if outliers are not properly addressed.

### Strengths

- The z-score method is a popular and robust method for identifying outliers in a dataset.
- Simplifies time series maintenance by requiring a datetime index.
- Identifies outliers for each numeric feature individually.
- Provides an elaborate report showing variables, dates, z-scores, and pass/fail tests.
- Offers visual inspection for detected outliers through plots.

### Limitations

- The test only identifies outliers in numeric columns, not in categorical variables.
- The utility and accuracy of z-scores can be limited if the data doesn't follow a normal distribution.
- The method relies on a subjective z-score threshold for deciding what constitutes an outlier, which might not
  always be suitable depending on the dataset and use case.
- It does not address possible ways to handle identified outliers in the data.
- The requirement for a datetime index could limit its application.

##### validmind.tests.data_validation.TooManyZeroValues

**Functions:**

- [**TooManyZeroValues**](#validmind.tests.data_validation.TooManyZeroValues.TooManyZeroValues) – Identifies numerical columns in a dataset that contain an excessive number of zero values, defined by a threshold

###### validmind.tests.data_validation.TooManyZeroValues.TooManyZeroValues

```python
TooManyZeroValues(dataset, max_percent_threshold=0.03)
```

Identifies numerical columns in a dataset that contain an excessive number of zero values, defined by a threshold
percentage.

### Purpose

The 'TooManyZeroValues' test is utilized to identify numerical columns in the dataset that may present a quantity
of zero values considered excessive. The aim is to detect situations where these may implicate data sparsity or a
lack of variation, limiting their effectiveness within a machine learning model. The definition of 'too many' is
quantified as a percentage of total values, with a default set to 3%.

### Test Mechanism

This test is conducted by looping through each column in the dataset and categorizing those that pertain to
numerical data. On identifying a numerical column, the function computes the total quantity of zero values and
their ratio to the total row count. Should the proportion exceed a pre-set threshold parameter, set by default at
0.03 or 3%, the column is considered to have failed the test. The results for each column are summarized and
reported, indicating the count and percentage of zero values for each numerical column, alongside a status
indicating whether the column has passed or failed the test.

### Signs of High Risk

- Numerical columns showing a high ratio of zero values when compared to the total count of rows (exceeding the
  predetermined threshold).
- Columns characterized by zero values across the board suggest a complete lack of data variation, signifying high
  risk.

### Strengths

- Assists in highlighting columns featuring an excess of zero values that could otherwise go unnoticed within a
  large dataset.
- Provides the flexibility to alter the threshold that determines when the quantity of zero values becomes 'too
  many', thus catering to specific needs of a particular analysis or model.
- Offers feedback in the form of both counts and percentages of zero values, which allows a closer inspection of
  the distribution and proportion of zeros within a column.
- Targets specifically numerical data, thereby avoiding inappropriate application to non-numerical columns and
  mitigating the risk of false test failures.

### Limitations

- Is exclusively designed to check for zero values and doesn’t assess the potential impact of other values that
  could affect the dataset, such as extremely high or low figures, missing values, or outliers.
- Lacks the ability to detect a repetitive pattern of zeros, which could be significant in time-series or
  longitudinal data.
- Zero values can actually be meaningful in some contexts; therefore, tagging them as 'too many' could potentially
  misinterpret the data to some extent.
- This test does not take into consideration the context of the dataset, and fails to recognize that within certain
  columns, a high number of zero values could be quite normal and not necessarily an indicator of poor data quality.
- Cannot evaluate non-numerical or categorical columns, which might bring with them different types of concerns or
  issues.

##### validmind.tests.data_validation.UniqueRows

**Functions:**

- [**UniqueRows**](#validmind.tests.data_validation.UniqueRows.UniqueRows) – Verifies the diversity of the dataset by ensuring that the count of unique rows exceeds a prescribed threshold.

###### validmind.tests.data_validation.UniqueRows.UniqueRows

```python
UniqueRows(dataset, min_percent_threshold=1)
```

Verifies the diversity of the dataset by ensuring that the count of unique rows exceeds a prescribed threshold.

### Purpose

The UniqueRows test is designed to gauge the quality of the data supplied to the machine learning model by
verifying that the count of distinct rows in the dataset exceeds a specific threshold, thereby ensuring a varied
collection of data. Diversity in data is essential for training an unbiased and robust model that excels when faced
with novel data.

### Test Mechanism

The testing process starts with calculating the total number of rows in the dataset. Subsequently, the count of
unique rows is determined for each column in the dataset. If the percentage of unique rows (calculated as the ratio
of unique rows to the overall row count) is less than the prescribed minimum percentage threshold given as a
function parameter, the test passes. The results are cached and a final pass or fail verdict is given based on
whether all columns have successfully passed the test.

### Signs of High Risk

- A lack of diversity in data columns, demonstrated by a count of unique rows that falls short of the preset
  minimum percentage threshold, is indicative of high risk.
- This lack of variety in the data signals potential issues with data quality, possibly leading to overfitting in
  the model and issues with generalization, thus posing a significant risk.

### Strengths

- The UniqueRows test is efficient in evaluating the data's diversity across each information column in the dataset.
- This test provides a quick, systematic method to assess data quality based on uniqueness, which can be pivotal in
  developing effective and unbiased machine learning models.

### Limitations

- A limitation of the UniqueRows test is its assumption that the data's quality is directly proportionate to its
  uniqueness, which may not always hold true. There might be contexts where certain non-unique rows are essential and
  should not be overlooked.
- The test does not consider the relative 'importance' of each column in predicting the output, treating all
  columns equally.
- This test may not be suitable or useful for categorical variables, where the count of unique categories is
  inherently limited.

##### validmind.tests.data_validation.WOEBinPlots

**Functions:**

- [**WOEBinPlots**](#validmind.tests.data_validation.WOEBinPlots.WOEBinPlots) – Generates visualizations of Weight of Evidence (WoE) and Information Value (IV) for understanding predictive power

**Attributes:**

- [**logger**](#validmind.tests.data_validation.WOEBinPlots.logger) –

###### validmind.tests.data_validation.WOEBinPlots.WOEBinPlots

```python
WOEBinPlots(dataset, breaks_adj=None, fig_height=600, fig_width=500)
```

Generates visualizations of Weight of Evidence (WoE) and Information Value (IV) for understanding predictive power
of categorical variables in a data set.

### Purpose

This test is designed to visualize the Weight of Evidence (WoE) and Information Value (IV) for categorical
variables in a provided dataset. By showcasing the data distribution across different categories of each feature,
it aids in understanding each variable's predictive power in the context of a classification-based machine learning
model. Commonly used in credit scoring models, WoE and IV are robust statistical methods for evaluating a
variable's predictive power.

### Test Mechanism

The test implementation follows defined steps. Initially, it selects non-numeric columns from the dataset and
changes them to string type, paving the way for accurate binning. It then performs an automated WoE binning
operation on these selected features, effectively categorizing the potential values of a variable into distinct
bins. After the binning process, the function generates two separate visualizations (a scatter chart for WoE values
and a bar chart for IV) for each variable. These visual presentations are formed according to the spread of each
metric across various categories of each feature.

### Signs of High Risk

- Errors occurring during the binning process.
- Challenges in converting non-numeric columns into string data type.
- Misbalance in the distribution of WoE and IV, with certain bins overtaking others conspicuously. This could
  denote that the model is disproportionately dependent on certain variables or categories for predictions, an
  indication of potential risks to its robustness and generalizability.

### Strengths

- Provides a detailed visual representation of the relationship between feature categories and the target variable.
  This grants an intuitive understanding of each feature's contribution to the model.
- Allows for easy identification of features with high impact, facilitating feature selection and enhancing
  comprehension of the model's decision logic.
- WoE conversions are monotonic, upholding the rank ordering of the original data points, which simplifies analysis.

### Limitations

- The method is largely reliant on the binning process, and an inappropriate binning threshold or bin number choice
  might result in a misrepresentation of the variable's distribution.
- While excellent for categorical data, the encoding of continuous variables into categorical can sometimes lead to
  information loss.
- Extreme or outlier values can dramatically affect the computation of WoE and IV, skewing results.
- The method requires a sufficient number of events per bin to generate a reliable information value and weight of
  evidence.

###### validmind.tests.data_validation.WOEBinPlots.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.data_validation.WOEBinTable

**Functions:**

- [**WOEBinTable**](#validmind.tests.data_validation.WOEBinTable.WOEBinTable) – Assesses the Weight of Evidence (WoE) and Information Value (IV) of each feature to evaluate its predictive power

###### validmind.tests.data_validation.WOEBinTable.WOEBinTable

```python
WOEBinTable(dataset, breaks_adj=None)
```

Assesses the Weight of Evidence (WoE) and Information Value (IV) of each feature to evaluate its predictive power
in a binary classification model.

### Purpose

The Weight of Evidence (WoE) and Information Value (IV) test is designed to evaluate the predictive power of each
feature in a machine learning model. This test generates binned groups of values from each feature, computes the
WoE and IV for each bin, and provides insights into the relationship between each feature and the target variable,
illustrating their contribution to the model's predictive capabilities.

### Test Mechanism

The test uses the `scorecardpy.woebin` method to perform automatic binning of the dataset based on WoE. The method
accepts a list of break points for binning numeric variables through the parameter `breaks_adj`. If no breaks are
provided, it uses default binning. The bins are then used to calculate the WoE and IV values, effectively creating
a dataframe that includes the bin boundaries, WoE, and IV values for each feature. A target variable is required
in the dataset to perform this analysis.

### Signs of High Risk

- High IV values, indicating variables with excessive predictive power which might lead to overfitting.
- Errors during the binning process, potentially due to inappropriate data types or poorly defined bins.

### Strengths

- Highly effective for feature selection in binary classification problems, as it quantifies the predictive
  information within each feature concerning the binary outcome.
- The WoE transformation creates a monotonic relationship between the target and independent variables.

### Limitations

- Primarily designed for binary classification tasks, making it less applicable or reliable for multi-class
  classification or regression tasks.
- Potential difficulties if the dataset has many features, non-binnable features, or non-numeric features.
- The metric does not help in distinguishing whether the observed predictive factor is due to data randomness or a
  true phenomenon.

##### validmind.tests.data_validation.ZivotAndrewsArch

**Functions:**

- [**ZivotAndrewsArch**](#validmind.tests.data_validation.ZivotAndrewsArch.ZivotAndrewsArch) – Evaluates the order of integration and stationarity of time series data using the Zivot-Andrews unit root test.

**Attributes:**

- [**logger**](#validmind.tests.data_validation.ZivotAndrewsArch.logger) –

###### validmind.tests.data_validation.ZivotAndrewsArch.ZivotAndrewsArch

```python
ZivotAndrewsArch(dataset)
```

Evaluates the order of integration and stationarity of time series data using the Zivot-Andrews unit root test.

### Purpose

The Zivot-Andrews Arch metric is used to evaluate the order of integration for time series data in a machine
learning model. It's designed to test for stationarity, a crucial aspect of time series analysis, where data points
are independent of time. Stationarity means that the statistical properties such as mean, variance, and
autocorrelation are constant over time.

### Test Mechanism

The Zivot-Andrews unit root test is performed on each feature in the dataset using the `ZivotAndrews` function from
the `arch.unitroot` module. This function returns several metrics for each feature, including the statistical
value, p-value (probability value), the number of lags used, and the number of observations. The p-value is used to
decide on the null hypothesis (the time series has a unit root and is non-stationary) based on a chosen level of
significance.

### Signs of High Risk

- A high p-value suggests high risk, indicating insufficient evidence to reject the null hypothesis, implying that
  the time series has a unit root and is non-stationary.
- Non-stationary time series data can lead to misleading statistics and unreliable machine learning models.

### Strengths

- Dynamically tests for stationarity against structural breaks in time series data, offering robust evaluation of
  stationarity in features.
- Especially beneficial with financial, economic, or other time-series data where data observations lack a
  consistent pattern and structural breaks may occur.

### Limitations

- Assumes data is derived from a single-equation, autoregressive model, making it less appropriate for multivariate
  time series data or data not aligning with this model.
- May not account for unexpected shocks or changes in the series trend, both of which can significantly impact data
  stationarity.

###### validmind.tests.data_validation.ZivotAndrewsArch.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.data_validation.nlp

**Modules:**

- [**CommonWords**](#validmind.tests.data_validation.nlp.CommonWords) –
- [**Hashtags**](#validmind.tests.data_validation.nlp.Hashtags) –
- [**LanguageDetection**](#validmind.tests.data_validation.nlp.LanguageDetection) –
- [**Mentions**](#validmind.tests.data_validation.nlp.Mentions) –
- [**PolarityAndSubjectivity**](#validmind.tests.data_validation.nlp.PolarityAndSubjectivity) –
- [**Punctuations**](#validmind.tests.data_validation.nlp.Punctuations) – Metrics functions for any Pandas-compatible datasets
- [**Sentiment**](#validmind.tests.data_validation.nlp.Sentiment) –
- [**StopWords**](#validmind.tests.data_validation.nlp.StopWords) – Threshold based tests
- [**TextDescription**](#validmind.tests.data_validation.nlp.TextDescription) –
- [**Toxicity**](#validmind.tests.data_validation.nlp.Toxicity) –

###### validmind.tests.data_validation.nlp.CommonWords

**Functions:**

- [**CommonWords**](#validmind.tests.data_validation.nlp.CommonWords.CommonWords) – Assesses the most frequent non-stopwords in a text column for identifying prevalent language patterns.

####### validmind.tests.data_validation.nlp.CommonWords.CommonWords

```python
CommonWords(dataset)
```

Assesses the most frequent non-stopwords in a text column for identifying prevalent language patterns.

### Purpose

The CommonWords metric is used to identify and visualize the most prevalent words within a specified text column of
a dataset. This provides insights into the prevalent language patterns and vocabulary, especially useful in Natural
Language Processing (NLP) tasks such as text classification and text summarization.

### Test Mechanism

The test methodology involves splitting the specified text column's entries into words, collating them into a
corpus, and then counting the frequency of each word using the Counter. The forty most frequently occurring
non-stopwords are then visualized in an interactive bar chart using Plotly, where the x-axis represents the words,
and the y-axis indicates their frequency of occurrence.

### Signs of High Risk

- A lack of distinct words within the list, or the most common words being stopwords.
- Frequent occurrence of irrelevant or inappropriate words could point out a poorly curated or noisy dataset.
- An error returned due to the absence of a valid Dataset object, indicating high risk as the metric cannot be
  effectively implemented without it.

### Strengths

- The metric provides clear insights into the language features – specifically word frequency – of unstructured
  text data.
- It can reveal prominent vocabulary and language patterns, which prove vital for feature extraction in NLP tasks.
- The interactive visualization helps in quickly capturing the patterns and understanding the data intuitively.

### Limitations

- The test disregards semantic or context-related information as it solely focuses on word frequency.
- It intentionally ignores stopwords, which might carry necessary significance in certain scenarios.
- The applicability is limited to English-language text data as English stopwords are used for filtering, hence
  cannot account for data in other languages.
- The metric requires a valid Dataset object, indicating a dependency condition that limits its broader
  applicability.

###### validmind.tests.data_validation.nlp.Hashtags

**Functions:**

- [**Hashtags**](#validmind.tests.data_validation.nlp.Hashtags.Hashtags) – Assesses hashtag frequency in a text column, highlighting usage trends and potential dataset bias or spam.

####### validmind.tests.data_validation.nlp.Hashtags.Hashtags

```python
Hashtags(dataset, top_hashtags=25)
```

Assesses hashtag frequency in a text column, highlighting usage trends and potential dataset bias or spam.

### Purpose

The Hashtags test is designed to measure the frequency of hashtags used within a given text column in a dataset. It
is particularly useful for natural language processing tasks such as text classification and text summarization.
The goal is to identify common trends and patterns in the use of hashtags, which can serve as critical indicators
or features within a machine learning model.

### Test Mechanism

The test implements a regular expression (regex) to extract all hashtags from the specified text column. For each
hashtag found, it makes a tally of its occurrences. It then outputs a list of the top N hashtags (default is 25,
but customizable), sorted by their counts in descending order. The results are also visualized in a bar plot, with
frequency counts on the y-axis and the corresponding hashtags on the x-axis.

### Signs of High Risk

- A low diversity in the usage of hashtags, as indicated by a few hashtags being used disproportionately more than
  others.
- Repeated usage of one or few hashtags can be indicative of spam or a biased dataset.
- If there are no or extremely few hashtags found in the dataset, it perhaps signifies that the text data does not
  contain structured social media data.

### Strengths

- Provides a concise visual representation of the frequency of hashtags, which can be critical for understanding
  trends about a particular topic in text data.
- Instrumental in tasks specifically related to social media text analytics, such as opinion analysis and trend
  discovery.
- Adaptable, allowing the flexibility to determine the number of top hashtags to be analyzed.

### Limitations

- Assumes the presence of hashtags and therefore may not be applicable for text datasets that do not contain
  hashtags (e.g., formal documents, scientific literature).
- Language-specific limitations of hashtag formulations are not taken into account.
- Does not account for typographical errors, variations, or synonyms in hashtags.
- Does not provide context or sentiment associated with the hashtags, so the information provided may have limited
  utility on its own.

###### validmind.tests.data_validation.nlp.LanguageDetection

**Functions:**

- [**LanguageDetection**](#validmind.tests.data_validation.nlp.LanguageDetection.LanguageDetection) – Assesses the diversity of languages in a textual dataset by detecting and visualizing the distribution of languages.

####### validmind.tests.data_validation.nlp.LanguageDetection.LanguageDetection

```python
LanguageDetection(dataset)
```

Assesses the diversity of languages in a textual dataset by detecting and visualizing the distribution of languages.

### Purpose

The Language Detection test aims to identify and visualize the distribution of languages present within a textual
dataset. This test helps in understanding the diversity of languages in the data, which is crucial for developing
and validating multilingual models.

### Test Mechanism

This test operates by:

- Checking if the dataset has a specified text column.
- Using a language detection library to determine the language of each text entry in the dataset.
- Generating a histogram plot of the language distribution, with language codes on the x-axis and their frequencies
  on the y-axis.

If the text column is not specified, a ValueError is raised to ensure proper dataset configuration.

### Signs of High Risk

- A high proportion of entries returning "Unknown" language codes.
- Detection of unexpectedly diverse or incorrect language codes, indicating potential data quality issues.
- Significant imbalance in language distribution, which might indicate potential biases in the dataset.

### Strengths

- Provides a visual representation of language diversity within the dataset.
- Helps identify data quality issues related to incorrect or unknown language detection.
- Useful for ensuring that multilingual models have adequate and appropriate representation from various languages.

### Limitations

- Dependency on the accuracy of the language detection library, which may not be perfect.
- Languages with similar structures or limited text length may be incorrectly classified.
- The test returns "Unknown" for entries where language detection fails, which might mask underlying issues with
  certain languages or text formats.

###### validmind.tests.data_validation.nlp.Mentions

**Functions:**

- [**Mentions**](#validmind.tests.data_validation.nlp.Mentions.Mentions) – Calculates and visualizes frequencies of '@' prefixed mentions in a text-based dataset for NLP model analysis.

####### validmind.tests.data_validation.nlp.Mentions.Mentions

```python
Mentions(dataset, top_mentions=25)
```

Calculates and visualizes frequencies of '@' prefixed mentions in a text-based dataset for NLP model analysis.

### Purpose

The "Mentions" test is designed to gauge the quality of data in a Natural Language Processing (NLP) or text-focused
Machine Learning model. The primary objective is to identify and calculate the frequency of 'mentions' within a
chosen text column of a dataset. A 'mention' in this context refers to individual text elements that are prefixed
by '@'. The output of this test reveals the most frequently mentioned entities or usernames, which can be integral
for applications such as social media analyses or customer sentiment analyses.

### Test Mechanism

The test first verifies the existence of a text column in the provided dataset. It then employs a regular
expression pattern to extract mentions from the text. Subsequently, the frequency of each unique mention is
calculated. The test selects the most frequent mentions based on default or user-defined parameters, the default
being the top 25, for representation. This process of thresholding forms the core of the test. A treemap plot
visualizes the test results, where the size of each rectangle corresponds to the frequency of a particular mention.

### Signs of High Risk

- The lack of a valid text column in the dataset, which would result in the failure of the test execution.
- The absence of any mentions within the text data, indicating that there might not be any text associated with
  '@'. This situation could point toward sparse or poor-quality data, thereby hampering the model's generalization or
  learning capabilities.

### Strengths

- The test is specifically optimized for text-based datasets which gives it distinct power in the context of NLP.
- It enables quick identification and visually appealing representation of the predominant elements or mentions.
- It can provide crucial insights about the most frequently mentioned entities or usernames.

### Limitations

- The test only recognizes mentions that are prefixed by '@', hence useful textual aspects not preceded by '@'
  might be ignored.
- This test isn't suited for datasets devoid of textual data.
- It does not provide insights on less frequently occurring data or outliers, which means potentially significant
  patterns could be overlooked.

###### validmind.tests.data_validation.nlp.PolarityAndSubjectivity

**Functions:**

- [**PolarityAndSubjectivity**](#validmind.tests.data_validation.nlp.PolarityAndSubjectivity.PolarityAndSubjectivity) – Analyzes the polarity and subjectivity of text data within a given dataset to visualize the sentiment distribution.

####### validmind.tests.data_validation.nlp.PolarityAndSubjectivity.PolarityAndSubjectivity

```python
PolarityAndSubjectivity(
    dataset, threshold_subjectivity=0.5, threshold_polarity=0
)
```

Analyzes the polarity and subjectivity of text data within a given dataset to visualize the sentiment distribution.

### Purpose

The Polarity and Subjectivity test is designed to evaluate the sentiment expressed in textual data. By analyzing
these aspects, it helps to identify the emotional tone and subjectivity of the dataset, which could be crucial in
understanding customer feedback, social media sentiments, or other text-related data.

### Test Mechanism

This test uses TextBlob to compute the polarity and subjectivity scores of textual data in a given dataset. The
mechanism includes:

- Iterating through each text entry in the specified column of the dataset.
- Applying the TextBlob library to compute the polarity (ranging from -1 for negative sentiment to +1 for positive
  sentiment) and subjectivity (ranging from 0 for objective to 1 for subjective) for each entry.
- Creating a scatter plot using Plotly to visualize the relationship between polarity and subjectivity.

### Signs of High Risk

- High concentration of negative polarity values indicating prevalent negative sentiments.
- High subjectivity scores suggesting the text data is largely opinion-based rather than factual.
- Disproportionate clusters of extreme scores (e.g., many points near -1 or +1 polarity).

### Strengths

- Quantifies sentiment and subjectivity which can provide actionable insights.
- Visualizes sentiment distribution, aiding in easy interpretation.
- Utilizes well-established TextBlob library for sentiment analysis.

### Limitations

- Polarity and subjectivity calculations may oversimplify nuanced text sentiments.
- Reliance on TextBlob which may not be accurate for all domains or contexts.
- Visualization could become cluttered with very large datasets, making interpretation difficult.

###### validmind.tests.data_validation.nlp.Punctuations

Metrics functions for any Pandas-compatible datasets

**Functions:**

- [**Punctuations**](#validmind.tests.data_validation.nlp.Punctuations.Punctuations) – Analyzes and visualizes the frequency distribution of punctuation usage in a given text dataset.

####### validmind.tests.data_validation.nlp.Punctuations.Punctuations

```python
Punctuations(dataset, count_mode='token')
```

Analyzes and visualizes the frequency distribution of punctuation usage in a given text dataset.

### Purpose

The Punctuations Metric's primary purpose is to analyze the frequency of punctuation usage within a given text
dataset. This is often used in Natural Language Processing tasks, such as text classification and text
summarization.

### Test Mechanism

The test begins by verifying that the input "dataset" is of the type VMDataset. The count_mode parameter must be
either "token" (counts punctuation marks as individual tokens) or "word" (counts punctuation marks within words).
Following that, a corpus is created from the dataset by splitting its text on spaces. Each unique punctuation
character in the text corpus is then tallied. The frequency distribution of each punctuation symbol is visualized
as a bar graph, with these results being stored as Figures and associated with the main Punctuations object.

### Signs of High Risk

- Excessive or unusual frequency of specific punctuation marks, potentially denoting dubious quality, data
  corruption, or skewed data.

### Strengths

- Provides valuable insights into the distribution of punctuation usage in a text dataset.
- Important in validating the quality, consistency, and nature of the data.
- Can provide hints about the style or tonality of the text corpus, such as informal and emotional context
  indicated by frequent exclamation marks.

### Limitations

- Focuses solely on punctuation usage, potentially missing other important textual characteristics.
- General cultural or tonality assumptions based on punctuation distribution can be misguiding, as these vary
  across different languages and contexts.
- Less effective with languages that use non-standard or different punctuation.
- Visualization may lack interpretability when there are many unique punctuation marks in the dataset.

###### validmind.tests.data_validation.nlp.Sentiment

**Functions:**

- [**Sentiment**](#validmind.tests.data_validation.nlp.Sentiment.Sentiment) – Analyzes the sentiment of text data within a dataset using the VADER sentiment analysis tool.

####### validmind.tests.data_validation.nlp.Sentiment.Sentiment

```python
Sentiment(dataset)
```

Analyzes the sentiment of text data within a dataset using the VADER sentiment analysis tool.

### Purpose

The Sentiment test evaluates the overall sentiment of text data within a dataset. By analyzing sentiment scores, it
aims to ensure that the model is interpreting text data accurately and is not biased towards a particular sentiment.

### Test Mechanism

This test uses the VADER (Valence Aware Dictionary and sEntiment Reasoner) SentimentIntensityAnalyzer. It processes
each text entry in a specified column of the dataset to calculate the compound sentiment score, which represents
the overall sentiment polarity. The distribution of these sentiment scores is then visualized using a KDE (Kernel
Density Estimation) plot, highlighting any skewness or concentration in sentiment.

### Signs of High Risk

- Extreme polarity in sentiment scores, indicating potential bias.
- Unusual concentration of sentiment scores in a specific range.
- Significant deviation from expected sentiment distribution for the given text data.

### Strengths

- Provides a clear visual representation of sentiment distribution.
- Uses a well-established sentiment analysis tool (VADER).
- Can handle a wide range of text data, making it flexible for various applications.

### Limitations

- May not capture nuanced or context-specific sentiments.
- Relies heavily on the accuracy of the VADER sentiment analysis tool.
- Visualization alone may not provide comprehensive insights into underlying causes of sentiment distribution.

###### validmind.tests.data_validation.nlp.StopWords

Threshold based tests

**Functions:**

- [**StopWords**](#validmind.tests.data_validation.nlp.StopWords.StopWords) – Evaluates and visualizes the frequency of English stop words in a text dataset against a defined threshold.

####### validmind.tests.data_validation.nlp.StopWords.StopWords

```python
StopWords(dataset, min_percent_threshold=0.5, num_words=25)
```

Evaluates and visualizes the frequency of English stop words in a text dataset against a defined threshold.

### Purpose

The StopWords threshold test is a tool designed for assessing the quality of text data in an ML model. It focuses
on the identification and analysis of "stop words" in a given dataset. Stop words are frequent, common, yet
semantically insignificant words (for example: "the", "and", "is") in a language. This test evaluates the
proportion of stop words to the total word count in the dataset, in essence, scrutinizing the frequency of stop
word usage. The core objective is to highlight the prevalent stop words based on their usage frequency, which can
be instrumental in cleaning the data from noise and improving ML model performance.

### Test Mechanism

The StopWords test initiates on receiving an input of a 'VMDataset' object. Absence of such an object will trigger
an error. The methodology involves inspection of the text column of the VMDataset to create a 'corpus' (a
collection of written texts). Leveraging the Natural Language Toolkit's (NLTK) stop word repository, the test
screens the corpus for any stop words and documents their frequency. It further calculates the percentage usage of
each stop word compared to the total word count in the corpus. This percentage is evaluated against a predefined
'min_percent_threshold'. If this threshold is breached, the test returns a failed output. Top prevailing stop words
along with their usage percentages are returned, facilitated by a bar chart visualization of these stop words and
their frequency.

### Signs of High Risk

- A percentage of any stop words exceeding the predefined 'min_percent_threshold'.
- High frequency of stop words in the dataset which may adversely affect the application's analytical performance
  due to noise creation.

### Strengths

- The ability to scrutinize and quantify the usage of stop words.
- Provides insights into potential noise in the text data due to stop words.
- Directly aids in enhancing model training efficiency.
- Includes a bar chart visualization feature to easily interpret and action upon the stop words frequency
  information.

### Limitations

- The test only supports English stop words, making it less effective with datasets of other languages.
- The 'min_percent_threshold' parameter may require fine-tuning for different datasets, impacting the overall
  effectiveness of the test.
- Contextual use of the stop words within the dataset is not considered, potentially overlooking their significance
  in certain contexts.
- The test focuses specifically on the frequency of stop words, not providing direct measures of model performance
  or predictive accuracy.

###### validmind.tests.data_validation.nlp.TextDescription

**Functions:**

- [**TextDescription**](#validmind.tests.data_validation.nlp.TextDescription.TextDescription) – Conducts comprehensive textual analysis on a dataset using NLTK to evaluate various parameters and generate
- [**create_metrics_df**](#validmind.tests.data_validation.nlp.TextDescription.create_metrics_df) –

####### validmind.tests.data_validation.nlp.TextDescription.TextDescription

```python
TextDescription(
    dataset,
    unwanted_tokens={
        "s",
        "s'",
        "mr",
        "ms",
        "mrs",
        "dr",
        "'s",
        " ",
        "''",
        "dollar",
        "us",
        "``",
    },
    lang="english",
)
```

Conducts comprehensive textual analysis on a dataset using NLTK to evaluate various parameters and generate
visualizations.

### Purpose

The TextDescription test aims to conduct a thorough textual analysis of a dataset using the NLTK (Natural Language
Toolkit) library. It evaluates various metrics such as total words, total sentences, average sentence length, total
paragraphs, total unique words, most common words, total punctuations, and lexical diversity. The goal is to
understand the nature of the text and anticipate challenges machine learning models might face in text processing,
language understanding, or summarization tasks.

### Test Mechanism

The test works by:

- Parsing the dataset and tokenizing the text into words, sentences, and paragraphs using NLTK.
- Removing stopwords and unwanted tokens.
- Calculating parameters like total words, total sentences, average sentence length, total paragraphs, total unique
  words, total punctuations, and lexical diversity.
- Generating scatter plots to visualize correlations between various metrics (e.g., Total Words vs Total Sentences).

### Signs of High Risk

- Anomalies or increased complexity in lexical diversity.
- Longer sentences and paragraphs.
- High uniqueness of words.
- Large number of unwanted tokens.
- Missing or erroneous visualizations.

### Strengths

- Essential for pre-processing text data in machine learning models.
- Provides a comprehensive breakdown of text data, aiding in understanding its complexity.
- Generates visualizations to help comprehend text structure and complexity.

### Limitations

- Highly dependent on the NLTK library, limiting the test to supported languages.
- Limited customization for removing undesirable tokens and stop words.
- Does not consider semantic or grammatical complexities.
- Assumes well-structured documents, which may result in inaccuracies with poorly formatted text.

####### validmind.tests.data_validation.nlp.TextDescription.create_metrics_df

```python
create_metrics_df(df, text_column, unwanted_tokens, lang)
```

###### validmind.tests.data_validation.nlp.Toxicity

**Functions:**

- [**Toxicity**](#validmind.tests.data_validation.nlp.Toxicity.Toxicity) – Assesses the toxicity of text data within a dataset to visualize the distribution of toxicity scores.

####### validmind.tests.data_validation.nlp.Toxicity.Toxicity

```python
Toxicity(dataset)
```

Assesses the toxicity of text data within a dataset to visualize the distribution of toxicity scores.

### Purpose

The Toxicity test aims to evaluate the level of toxic content present in a text dataset by leveraging a pre-trained
toxicity model. It helps in identifying potentially harmful or offensive language that may negatively impact users
or stakeholders.

### Test Mechanism

This test uses a pre-trained toxicity evaluation model and applies it to each text entry in the specified column of
a dataset’s dataframe. The procedure involves:

- Loading a pre-trained toxicity model.
- Extracting the text from the specified column in the dataset.
- Computing toxicity scores for each text entry.
- Generating a KDE (Kernel Density Estimate) plot to visualize the distribution of these toxicity scores.

### Signs of High Risk

- High concentration of high toxicity scores in the KDE plot.
- A significant proportion of text entries with toxicity scores above a predefined threshold.
- Wide distribution of toxicity scores, indicating inconsistency in content quality.

### Strengths

- Provides a visual representation of toxicity distribution, making it easier to identify outliers.
- Uses a robust pre-trained model for toxicity evaluation.
- Can process large text datasets efficiently.

### Limitations

- Depends on the accuracy and bias of the pre-trained toxicity model.
- Does not provide context-specific insights, which may be necessary for nuanced understanding.
- May not capture all forms of subtle or indirect toxic language.

#### validmind.tests.decorator

Decorators for creating and registering tests with the ValidMind Library.

**Functions:**

- [**tags**](#validmind.tests.decorator.tags) – Decorator for specifying tags for a test.
- [**tasks**](#validmind.tests.decorator.tasks) – Decorator for specifying the task types that a test is designed for.
- [**test**](#validmind.tests.decorator.test) – Decorator for creating and registering custom tests

**Attributes:**

- [**logger**](#validmind.tests.decorator.logger) –

##### validmind.tests.decorator.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.decorator.tags

```python
tags(*tags)
```

Decorator for specifying tags for a test.

**Parameters:**

- \***tags** – The tags to apply to the test.

##### validmind.tests.decorator.tasks

```python
tasks(*tasks)
```

Decorator for specifying the task types that a test is designed for.

**Parameters:**

- \***tasks** – The task types that the test is designed for.

##### validmind.tests.decorator.test

```python
test(func_or_id)
```

Decorator for creating and registering custom tests

This decorator registers the function it wraps as a test function within ValidMind
under the provided ID. Once decorated, the function can be run using the
`validmind.tests.run_test` function.

The function can take two different types of arguments:

- Inputs: ValidMind model or dataset (or list of models/datasets). These arguments
  must use the following names: `model`, `models`, `dataset`, `datasets`.
- Parameters: Any additional keyword arguments of any type (must have a default
  value) that can have any name.

The function should return one of the following types:

- Table: Either a list of dictionaries or a pandas DataFrame
- Plot: Either a matplotlib figure or a plotly figure
- Scalar: A single number (int or float)
- Boolean: A single boolean value indicating whether the test passed or failed

The function may also include a docstring. This docstring will be used and logged
as the metric's description.

**Parameters:**

- **func** – The function to decorate
- **test_id** – The identifier for the metric. If not provided, the function name is used.

**Returns:**

- – The decorated function.

#### validmind.tests.describe_test

```python
describe_test(test_id=None, raw=False, show=True)
```

Get or show details about the test

This function can be used to see test details including the test name, description,
required inputs and default params. It can also be used to get a dictionary of the
above information for programmatic use.

**Parameters:**

- **test_id** (<code>[str](#str)</code>) – The test ID. Defaults to None.
- **raw** (<code>[bool](#bool)</code>) – If True, returns a dictionary with the test details.
  Defaults to False.

#### validmind.tests.list_tags

```python
list_tags()
```

List unique tags from all test classes.

#### validmind.tests.list_tasks

```python
list_tasks()
```

List unique tasks from all test classes.

#### validmind.tests.list_tasks_and_tags

```python
list_tasks_and_tags()
```

List all task types and their associated tags, with one row per task type and
all tags for a task type in one row.

**Returns:**

- – pandas.DataFrame: A DataFrame with 'Task Type' and concatenated 'Tags'.

#### validmind.tests.list_tests

```python
list_tests(filter=None, task=None, tags=None, pretty=True, truncate=True)
```

List all tests in the tests directory.

**Parameters:**

- **filter** (<code>[str](#str)</code>) – Find tests where the ID, tasks or tags match the
  filter string. Defaults to None.
- **task** (<code>[str](#str)</code>) – Find tests that match the task. Can be used to
  narrow down matches from the filter string. Defaults to None.
- **tags** (<code>[list](#list)</code>) – Find tests that match list of tags. Can be used to
  narrow down matches from the filter string. Defaults to None.
- **pretty** (<code>[bool](#bool)</code>) – If True, returns a pandas DataFrame with a
  formatted table. Defaults to True.
- **truncate** (<code>[bool](#bool)</code>) – If True, truncates the test description to the first
  line. Defaults to True. (only used if pretty=True)

**Returns:**

- – list or pandas.DataFrame: A list of all tests or a formatted table.

#### validmind.tests.load

Module for listing and loading tests.

**Functions:**

- [**describe_test**](#validmind.tests.load.describe_test) – Get or show details about the test
- [**list_tags**](#validmind.tests.load.list_tags) – List unique tags from all test classes.
- [**list_tasks**](#validmind.tests.load.list_tasks) – List unique tasks from all test classes.
- [**list_tasks_and_tags**](#validmind.tests.load.list_tasks_and_tags) – List all task types and their associated tags, with one row per task type and
- [**list_tests**](#validmind.tests.load.list_tests) – List all tests in the tests directory.
- [**load_test**](#validmind.tests.load.load_test) – Load a test by test ID

**Attributes:**

- [**INPUT_TYPE_MAP**](#validmind.tests.load.INPUT_TYPE_MAP) –
- [**logger**](#validmind.tests.load.logger) –

##### validmind.tests.load.INPUT_TYPE_MAP

```python
INPUT_TYPE_MAP = {
    "dataset": VMDataset,
    "datasets": List[VMDataset],
    "model": VMModel,
    "models": List[VMModel],
}

```

##### validmind.tests.load.describe_test

```python
describe_test(test_id=None, raw=False, show=True)
```

Get or show details about the test

This function can be used to see test details including the test name, description,
required inputs and default params. It can also be used to get a dictionary of the
above information for programmatic use.

**Parameters:**

- **test_id** (<code>[str](#str)</code>) – The test ID. Defaults to None.
- **raw** (<code>[bool](#bool)</code>) – If True, returns a dictionary with the test details.
  Defaults to False.

##### validmind.tests.load.list_tags

```python
list_tags()
```

List unique tags from all test classes.

##### validmind.tests.load.list_tasks

```python
list_tasks()
```

List unique tasks from all test classes.

##### validmind.tests.load.list_tasks_and_tags

```python
list_tasks_and_tags()
```

List all task types and their associated tags, with one row per task type and
all tags for a task type in one row.

**Returns:**

- – pandas.DataFrame: A DataFrame with 'Task Type' and concatenated 'Tags'.

##### validmind.tests.load.list_tests

```python
list_tests(filter=None, task=None, tags=None, pretty=True, truncate=True)
```

List all tests in the tests directory.

**Parameters:**

- **filter** (<code>[str](#str)</code>) – Find tests where the ID, tasks or tags match the
  filter string. Defaults to None.
- **task** (<code>[str](#str)</code>) – Find tests that match the task. Can be used to
  narrow down matches from the filter string. Defaults to None.
- **tags** (<code>[list](#list)</code>) – Find tests that match list of tags. Can be used to
  narrow down matches from the filter string. Defaults to None.
- **pretty** (<code>[bool](#bool)</code>) – If True, returns a pandas DataFrame with a
  formatted table. Defaults to True.
- **truncate** (<code>[bool](#bool)</code>) – If True, truncates the test description to the first
  line. Defaults to True. (only used if pretty=True)

**Returns:**

- – list or pandas.DataFrame: A list of all tests or a formatted table.

##### validmind.tests.load.load_test

```python
load_test(test_id, test_func=None, reload=False)
```

Load a test by test ID

Test IDs are in the format `namespace.path_to_module.TestClassOrFuncName[:tag]`.
The tag is optional and is used to distinguish between multiple results from the
same test.

**Parameters:**

- **test_id** (<code>[str](#str)</code>) – The test ID in the format `namespace.path_to_module.TestName[:tag]`
- **test_func** (<code>[callable](#callable)</code>) – The test function to load. If not provided, the
  test will be loaded from the test provider. Defaults to None.

##### validmind.tests.load.logger

```python
logger = get_logger(__name__)
```

#### validmind.tests.load_test

```python
load_test(test_id, test_func=None, reload=False)
```

Load a test by test ID

Test IDs are in the format `namespace.path_to_module.TestClassOrFuncName[:tag]`.
The tag is optional and is used to distinguish between multiple results from the
same test.

**Parameters:**

- **test_id** (<code>[str](#str)</code>) – The test ID in the format `namespace.path_to_module.TestName[:tag]`
- **test_func** (<code>[callable](#callable)</code>) – The test function to load. If not provided, the
  test will be loaded from the test provider. Defaults to None.

#### validmind.tests.model_validation

**Modules:**

- [**BertScore**](#validmind.tests.model_validation.BertScore) –
- [**BleuScore**](#validmind.tests.model_validation.BleuScore) –
- [**ClusterSizeDistribution**](#validmind.tests.model_validation.ClusterSizeDistribution) –
- [**ContextualRecall**](#validmind.tests.model_validation.ContextualRecall) –
- [**FeaturesAUC**](#validmind.tests.model_validation.FeaturesAUC) –
- [**MeteorScore**](#validmind.tests.model_validation.MeteorScore) –
- [**ModelMetadata**](#validmind.tests.model_validation.ModelMetadata) –
- [**ModelPredictionResiduals**](#validmind.tests.model_validation.ModelPredictionResiduals) –
- [**RegardScore**](#validmind.tests.model_validation.RegardScore) –
- [**RegressionResidualsPlot**](#validmind.tests.model_validation.RegressionResidualsPlot) –
- [**RougeScore**](#validmind.tests.model_validation.RougeScore) –
- [**TimeSeriesPredictionWithCI**](#validmind.tests.model_validation.TimeSeriesPredictionWithCI) –
- [**TimeSeriesPredictionsPlot**](#validmind.tests.model_validation.TimeSeriesPredictionsPlot) –
- [**TimeSeriesR2SquareBySegments**](#validmind.tests.model_validation.TimeSeriesR2SquareBySegments) –
- [**TokenDisparity**](#validmind.tests.model_validation.TokenDisparity) –
- [**ToxicityScore**](#validmind.tests.model_validation.ToxicityScore) –
- [**sklearn**](#validmind.tests.model_validation.sklearn) –
- [**statsmodels**](#validmind.tests.model_validation.statsmodels) –

##### validmind.tests.model_validation.BertScore

**Functions:**

- [**BertScore**](#validmind.tests.model_validation.BertScore.BertScore) – Assesses the quality of machine-generated text using BERTScore metrics and visualizes results through histograms

###### validmind.tests.model_validation.BertScore.BertScore

```python
BertScore(dataset, model, evaluation_model='distilbert-base-uncased')
```

Assesses the quality of machine-generated text using BERTScore metrics and visualizes results through histograms
and bar charts, alongside compiling a comprehensive table of descriptive statistics.

### Purpose

This function is designed to assess the quality of text generated by machine learning models using BERTScore
metrics. BERTScore evaluates text generation models' performance by calculating precision, recall, and F1 score
based on BERT contextual embeddings.

### Test Mechanism

The function starts by extracting the true and predicted values from the provided dataset and model. It then
initializes the BERTScore evaluator. For each pair of true and predicted texts, the function calculates the
BERTScore metrics and compiles them into a dataframe. Histograms and bar charts are generated for each BERTScore
metric (Precision, Recall, and F1 Score) to visualize their distribution. Additionally, a table of descriptive
statistics (mean, median, standard deviation, minimum, and maximum) is compiled for each metric, providing a
comprehensive summary of the model's performance. The test uses the `evaluation_model` param to specify the
huggingface model to use for evaluation. `microsoft/deberta-xlarge-mnli` is the best-performing model but is
very large and may be slow without a GPU. `microsoft/deberta-large-mnli` is a smaller model that is faster to
run and `distilbert-base-uncased` is much lighter and can run on a CPU but is less accurate.

### Signs of High Risk

- Consistently low scores across BERTScore metrics could indicate poor quality in the generated text, suggesting
  that the model fails to capture the essential content of the reference texts.
- Low precision scores might suggest that the generated text contains a lot of redundant or irrelevant information.
- Low recall scores may indicate that important information from the reference text is being omitted.
- An imbalanced performance between precision and recall, reflected by a low F1 Score, could signal issues in the
  model's ability to balance informativeness and conciseness.

### Strengths

- Provides a multifaceted evaluation of text quality through different BERTScore metrics, offering a detailed view
  of model performance.
- Visual representations (histograms and bar charts) make it easier to interpret the distribution and trends of the
  scores.
- Descriptive statistics offer a concise summary of the model's strengths and weaknesses in generating text.

### Limitations

- BERTScore relies on the contextual embeddings from BERT models, which may not fully capture all nuances of text
  similarity.
- The evaluation relies on the availability of high-quality reference texts, which may not always be obtainable.
- While useful for comparison, BERTScore metrics alone do not provide a complete assessment of a model's
  performance and should be supplemented with other metrics and qualitative analysis.

##### validmind.tests.model_validation.BleuScore

**Functions:**

- [**BleuScore**](#validmind.tests.model_validation.BleuScore.BleuScore) – Evaluates the quality of machine-generated text using BLEU metrics and visualizes the results through histograms

###### validmind.tests.model_validation.BleuScore.BleuScore

```python
BleuScore(dataset, model)
```

Evaluates the quality of machine-generated text using BLEU metrics and visualizes the results through histograms
and bar charts, alongside compiling a comprehensive table of descriptive statistics for BLEU scores.

### Purpose

This function is designed to assess the quality of text generated by machine learning models using the BLEU metric.
BLEU, which stands for Bilingual Evaluation Understudy, is a metric used to evaluate the overlap of n-grams between
the machine-generated text and reference texts. This evaluation is crucial for tasks such as text summarization,
machine translation, and text generation, where the goal is to produce text that accurately reflects the content
and meaning of human-crafted references.

### Test Mechanism

The function starts by extracting the true and predicted values from the provided dataset and model. It then
initializes the BLEU evaluator. For each pair of true and predicted texts, the function calculates the BLEU scores
and compiles them into a dataframe. Histograms and bar charts are generated for the BLEU scores to visualize their
distribution. Additionally, a table of descriptive statistics (mean, median, standard deviation, minimum, and
maximum) is compiled for the BLEU scores, providing a comprehensive summary of the model's performance.

### Signs of High Risk

- Consistently low BLEU scores could indicate poor quality in the generated text, suggesting that the model fails
  to capture the essential content of the reference texts.
- Low precision scores might suggest that the generated text contains a lot of redundant or irrelevant information.
- Low recall scores may indicate that important information from the reference text is being omitted.
- An imbalanced performance between precision and recall, reflected by a low BLEU score, could signal issues in the
  model's ability to balance informativeness and conciseness.

### Strengths

- Provides a straightforward and widely-used evaluation of text quality through BLEU scores.
- Visual representations (histograms and bar charts) make it easier to interpret the distribution and trends of the
  scores.
- Descriptive statistics offer a concise summary of the model's strengths and weaknesses in generating text.

### Limitations

- BLEU metrics primarily focus on n-gram overlap and may not fully capture semantic coherence, fluency, or
  grammatical quality of the text.
- The evaluation relies on the availability of high-quality reference texts, which may not always be obtainable.
- While useful for comparison, BLEU scores alone do not provide a complete assessment of a model's performance and
  should be supplemented with other metrics and qualitative analysis.

##### validmind.tests.model_validation.ClusterSizeDistribution

**Functions:**

- [**ClusterSizeDistribution**](#validmind.tests.model_validation.ClusterSizeDistribution.ClusterSizeDistribution) – Assesses the performance of clustering models by comparing the distribution of cluster sizes in model predictions

###### validmind.tests.model_validation.ClusterSizeDistribution.ClusterSizeDistribution

```python
ClusterSizeDistribution(dataset, model)
```

Assesses the performance of clustering models by comparing the distribution of cluster sizes in model predictions
with the actual data.

### Purpose

The Cluster Size Distribution test aims to assess the performance of clustering models by comparing the
distribution of cluster sizes in the model's predictions with the actual data. This comparison helps determine if
the clustering model's output aligns well with the true cluster distribution, providing insights into the model's
accuracy and performance.

### Test Mechanism

The test mechanism involves the following steps:

- Run the clustering model on the provided dataset to obtain predictions.
- Convert both the actual and predicted outputs into pandas dataframes.
- Use pandas built-in functions to derive the cluster size distributions from these dataframes.
- Construct two histograms: one for the actual cluster size distribution and one for the predicted distribution.
- Plot the histograms side-by-side for visual comparison.

### Signs of High Risk

- Discrepancies between the actual cluster size distribution and the predicted cluster size distribution.
- Irregular distribution of data across clusters in the predicted outcomes.
- High number of outlier clusters suggesting the model struggles to correctly group data.

### Strengths

- Provides a visual and intuitive way to compare the clustering model's performance against actual data.
- Effectively reveals where the model may be over- or underestimating cluster sizes.
- Versatile as it works well with any clustering model.

### Limitations

- Assumes that the actual cluster distribution is optimal, which may not always be the case.
- Relies heavily on visual comparison, which could be subjective and may not offer a precise numerical measure of
  performance.
- May not fully capture other important aspects of clustering, such as cluster density, distances between clusters,
  and the shape of clusters.

##### validmind.tests.model_validation.ContextualRecall

**Functions:**

- [**ContextualRecall**](#validmind.tests.model_validation.ContextualRecall.ContextualRecall) – Evaluates a Natural Language Generation model's ability to generate contextually relevant and factually correct

###### validmind.tests.model_validation.ContextualRecall.ContextualRecall

```python
ContextualRecall(dataset, model)
```

Evaluates a Natural Language Generation model's ability to generate contextually relevant and factually correct
text, visualizing the results through histograms and bar charts, alongside compiling a comprehensive table of
descriptive statistics for contextual recall scores.

### Purpose

The Contextual Recall metric is used to evaluate the ability of a natural language generation (NLG) model to
generate text that appropriately reflects the given context or prompt. It measures the model's capability to
remember and reproduce the main context in its resulting output. This metric is critical in natural language
processing tasks, as the coherency and contextuality of the generated text are essential.

### Test Mechanism

The function starts by extracting the true and predicted values from the provided dataset and model. It then
tokenizes the reference and candidate texts into discernible words or tokens using NLTK. The token overlap between
the reference and candidate texts is identified, and the Contextual Recall score is computed by dividing the number
of overlapping tokens by the total number of tokens in the reference text. Scores are calculated for each test
dataset instance, resulting in an array of scores. These scores are visualized using a histogram and a bar chart to
show score variations across different rows. Additionally, a table of descriptive statistics (mean, median,
standard deviation, minimum, and maximum) is compiled for the contextual recall scores, providing a comprehensive
summary of the model's performance.

### Signs of High Risk

- Low contextual recall scores could indicate that the model is not effectively reflecting the original context in
  its output, leading to incoherent or contextually misaligned text.
- A consistent trend of low recall scores could suggest underperformance of the model.

### Strengths

- Provides a quantifiable measure of a model's adherence to the context and factual elements of the generated
  narrative.
- Visual representations (histograms and bar charts) make it easier to interpret the distribution and trends of
  contextual recall scores.
- Descriptive statistics offer a concise summary of the model's performance in generating contextually relevant
  texts.

### Limitations

- The focus on word overlap could result in high scores for texts that use many common words, even when these texts
  lack coherence or meaningful context.
- This metric does not consider the order of words, which could lead to overestimated scores for scrambled outputs.
- Models that effectively use infrequent words might be undervalued, as these words might not overlap as often.

##### validmind.tests.model_validation.FeaturesAUC

**Functions:**

- [**FeaturesAUC**](#validmind.tests.model_validation.FeaturesAUC.FeaturesAUC) – Evaluates the discriminatory power of each individual feature within a binary classification model by calculating

**Attributes:**

- [**logger**](#validmind.tests.model_validation.FeaturesAUC.logger) –

###### validmind.tests.model_validation.FeaturesAUC.FeaturesAUC

```python
FeaturesAUC(dataset, fontsize=12, figure_height=500)
```

Evaluates the discriminatory power of each individual feature within a binary classification model by calculating
the Area Under the Curve (AUC) for each feature separately.

### Purpose

The central objective of this metric is to quantify how well each feature on its own can differentiate between the
two classes in a binary classification problem. It serves as a univariate analysis tool that can help in
pre-modeling feature selection or post-modeling interpretation.

### Test Mechanism

For each feature, the metric treats the feature values as raw scores to compute the AUC against the actual binary
outcomes. It provides an AUC value for each feature, offering a simple yet powerful indication of each feature's
univariate classification strength.

### Signs of High Risk

- A feature with a low AUC score may not be contributing significantly to the differentiation between the two
  classes, which could be a concern if it is expected to be predictive.
- Conversely, a surprisingly high AUC for a feature not believed to be informative may suggest data leakage or
  other issues with the data.

### Strengths

- By isolating each feature, it highlights the individual contribution of features to the classification task
  without the influence of other variables.
- Useful for both initial feature evaluation and for providing insights into the model's reliance on individual
  features after model training.

### Limitations

- Does not reflect the combined effects of features or any interaction between them, which can be critical in
  certain models.
- The AUC values are calculated without considering the model's use of the features, which could lead to different
  interpretations of feature importance when considering the model holistically.
- This metric is applicable only to binary classification tasks and cannot be directly extended to multiclass
  classification or regression without modifications.

###### validmind.tests.model_validation.FeaturesAUC.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.model_validation.MeteorScore

**Functions:**

- [**MeteorScore**](#validmind.tests.model_validation.MeteorScore.MeteorScore) – Assesses the quality of machine-generated translations by comparing them to human-produced references using the

###### validmind.tests.model_validation.MeteorScore.MeteorScore

```python
MeteorScore(dataset, model)
```

Assesses the quality of machine-generated translations by comparing them to human-produced references using the
METEOR score, which evaluates precision, recall, and word order.

### Purpose

The METEOR (Metric for Evaluation of Translation with Explicit ORdering) score is designed to evaluate the quality
of machine translations by comparing them against reference translations. It emphasizes both the accuracy and
fluency of translations, incorporating precision, recall, and word order into its assessment.

### Test Mechanism

The function starts by extracting the true and predicted values from the provided dataset and model. The METEOR
score is computed for each pair of machine-generated translation (prediction) and its corresponding human-produced
reference. This is done by considering unigram matches between the translations, including matches based on surface
forms, stemmed forms, and synonyms. The score is a combination of unigram precision and recall, adjusted for word
order through a fragmentation penalty. Scores are compiled into a dataframe, and histograms and bar charts are
generated to visualize the distribution of METEOR scores. Additionally, a table of descriptive statistics (mean,
median, standard deviation, minimum, and maximum) is compiled for the METEOR scores, providing a comprehensive
summary of the model's performance.

### Signs of High Risk

- Lower METEOR scores can indicate a lack of alignment between the machine-generated translations and their
  human-produced references, highlighting potential deficiencies in both the accuracy and fluency of translations.
- Significant discrepancies in word order or an excessive fragmentation penalty could signal issues with how the
  translation model processes and reconstructs sentence structures, potentially compromising the natural flow of
  translated text.
- Persistent underperformance across a variety of text types or linguistic contexts might suggest a broader
  inability of the model to adapt to the nuances of different languages or dialects, pointing towards gaps in its
  training or inherent limitations.

### Strengths

- Incorporates a balanced consideration of precision and recall, weighted towards recall to reflect the importance
  of content coverage in translations.
- Directly accounts for word order, offering a nuanced evaluation of translation fluency beyond simple lexical
  matching.
- Adapts to various forms of lexical similarity, including synonyms and stemmed forms, allowing for flexible
  matching.

### Limitations

- While comprehensive, the complexity of METEOR's calculation can make it computationally intensive, especially for
  large datasets.
- The use of external resources for synonym and stemming matching may introduce variability based on the resources'
  quality and relevance to the specific translation task.

##### validmind.tests.model_validation.ModelMetadata

**Functions:**

- [**ModelMetadata**](#validmind.tests.model_validation.ModelMetadata.ModelMetadata) – Compare metadata of different models and generate a summary table with the results.

###### validmind.tests.model_validation.ModelMetadata.ModelMetadata

```python
ModelMetadata(model)
```

Compare metadata of different models and generate a summary table with the results.

**Purpose**: The purpose of this function is to compare the metadata of different models, including information about their architecture, framework, framework version, and programming language.

**Test Mechanism**: The function retrieves the metadata for each model using `get_model_info`, renames columns according to a predefined set of labels, and compiles this information into a summary table.

**Signs of High Risk**:

- Inconsistent or missing metadata across models can indicate potential issues in model documentation or management.
- Significant differences in framework versions or programming languages might pose challenges in model integration and deployment.

**Strengths**:

- Provides a clear comparison of essential model metadata.
- Standardizes metadata labels for easier interpretation and comparison.
- Helps identify potential compatibility or consistency issues across models.

**Limitations**:

- Assumes that the `get_model_info` function returns all necessary metadata fields.
- Relies on the correctness and completeness of the metadata provided by each model.
- Does not include detailed parameter information, focusing instead on high-level metadata.

##### validmind.tests.model_validation.ModelPredictionResiduals

**Functions:**

- [**ModelPredictionResiduals**](#validmind.tests.model_validation.ModelPredictionResiduals.ModelPredictionResiduals) – Assesses normality and behavior of residuals in regression models through visualization and statistical tests.

###### validmind.tests.model_validation.ModelPredictionResiduals.ModelPredictionResiduals

```python
ModelPredictionResiduals(
    dataset,
    model,
    nbins=100,
    p_value_threshold=0.05,
    start_date=None,
    end_date=None,
)
```

Assesses normality and behavior of residuals in regression models through visualization and statistical tests.

### Purpose

The Model Prediction Residuals test aims to visualize the residuals of model predictions and assess their normality
using the Kolmogorov-Smirnov (KS) test. It helps to identify potential issues related to model assumptions and
effectiveness.

### Test Mechanism

The function calculates residuals and generates
two figures: one for the time series of residuals and one for the histogram of residuals.
It also calculates the KS test for normality and summarizes the results in a table.

### Signs of High Risk

- Residuals are not normally distributed, indicating potential issues with model assumptions.
- High skewness or kurtosis in the residuals, which may suggest model misspecification.

### Strengths

- Provides clear visualizations of residuals over time and their distribution.
- Includes statistical tests to assess the normality of residuals.
- Helps in identifying potential model misspecifications and assumption violations.

### Limitations

- Assumes that the dataset is provided as a DataFrameDataset object with a .df attribute to access the pandas
  DataFrame.
- Only generates plots for datasets with a datetime index, resulting in errors for other types of indices.

##### validmind.tests.model_validation.RegardScore

**Functions:**

- [**RegardScore**](#validmind.tests.model_validation.RegardScore.RegardScore) – Assesses the sentiment and potential biases in text generated by NLP models by computing and visualizing regard

###### validmind.tests.model_validation.RegardScore.RegardScore

```python
RegardScore(dataset, model)
```

Assesses the sentiment and potential biases in text generated by NLP models by computing and visualizing regard
scores.

### Purpose

The `RegardScore` test aims to evaluate the levels of regard (positive, negative, neutral, or other) in texts
generated by NLP models. It helps in understanding the sentiment and bias present in the generated content.

### Test Mechanism

This test extracts the true and predicted values from the provided dataset and model. It then computes the regard
scores for each text instance using a preloaded `regard` evaluation tool. The scores are compiled into dataframes,
and visualizations such as histograms and bar charts are generated to display the distribution of regard scores.
Additionally, descriptive statistics (mean, median, standard deviation, minimum, and maximum) are calculated for
the regard scores, providing a comprehensive overview of the model's performance.

### Signs of High Risk

- Noticeable skewness in the histogram, especially when comparing the predicted regard scores with the target
  regard scores, can indicate biases or inconsistencies in the model.
- Lack of neutral scores in the model's predictions, despite a balanced distribution in the target data, might
  signal an issue.

### Strengths

- Provides a clear evaluation of regard levels in generated texts, aiding in ensuring content appropriateness.
- Visual representations (histograms and bar charts) make it easier to interpret the distribution and trends of
  regard scores.
- Descriptive statistics offer a concise summary of the model's performance in generating texts with balanced
  sentiments.

### Limitations

- The accuracy of the regard scores is contingent upon the underlying `regard` tool.
- The scores provide a broad overview but do not specify which portions or tokens of the text are responsible for
  high regard.
- Supplementary, in-depth analysis might be needed for granular insights.

##### validmind.tests.model_validation.RegressionResidualsPlot

**Functions:**

- [**RegressionResidualsPlot**](#validmind.tests.model_validation.RegressionResidualsPlot.RegressionResidualsPlot) – Evaluates regression model performance using residual distribution and actual vs. predicted plots.

###### validmind.tests.model_validation.RegressionResidualsPlot.RegressionResidualsPlot

```python
RegressionResidualsPlot(model, dataset, bin_size=0.1)
```

Evaluates regression model performance using residual distribution and actual vs. predicted plots.

### Purpose

The `RegressionResidualsPlot` metric aims to evaluate the performance of regression models. By generating and
analyzing two plots – a distribution of residuals and a scatter plot of actual versus predicted values – this tool
helps to visually appraise how well the model predicts and the nature of errors it makes.

### Test Mechanism

The process begins by extracting the true output values (`y_true`) and the model's predicted values (`y_pred`).
Residuals are computed by subtracting predicted from true values. These residuals are then visualized using a
histogram to display their distribution. Additionally, a scatter plot is derived to compare true values against
predicted values, together with a "Perfect Fit" line, which represents an ideal match (predicted values equal
actual values), facilitating the assessment of the model's predictive accuracy.

### Signs of High Risk

- Residuals showing a non-normal distribution, especially those with frequent extreme values.
- Significant deviations of predicted values from actual values in the scatter plot.
- Sparse density of data points near the "Perfect Fit" line in the scatter plot, indicating poor prediction
  accuracy.
- Visible patterns or trends in the residuals plot, suggesting the model's failure to capture the underlying data
  structure adequately.

### Strengths

- Provides a direct, visually intuitive assessment of a regression model’s accuracy and handling of data.
- Visual plots can highlight issues of underfitting or overfitting.
- Can reveal systematic deviations or trends that purely numerical metrics might miss.
- Applicable across various regression model types.

### Limitations

- Relies on visual interpretation, which can be subjective and less precise than numerical evaluations.
- May be difficult to interpret in cases with multi-dimensional outputs due to the plots’ two-dimensional nature.
- Overlapping data points in the residuals plot can complicate interpretation efforts.
- Does not summarize model performance into a single quantifiable metric, which might be needed for comparative or
  summary analyses.

##### validmind.tests.model_validation.RougeScore

**Functions:**

- [**RougeScore**](#validmind.tests.model_validation.RougeScore.RougeScore) – Assesses the quality of machine-generated text using ROUGE metrics and visualizes the results to provide

###### validmind.tests.model_validation.RougeScore.RougeScore

```python
RougeScore(dataset, model, metric='rouge-1')
```

Assesses the quality of machine-generated text using ROUGE metrics and visualizes the results to provide
comprehensive performance insights.

### Purpose

The ROUGE Score test is designed to evaluate the quality of text generated by machine learning models using various
ROUGE metrics. ROUGE, which stands for Recall-Oriented Understudy for Gisting Evaluation, measures the overlap of
n-grams, word sequences, and word pairs between machine-generated text and reference texts. This evaluation is
crucial for tasks like text summarization, machine translation, and text generation, where the goal is to produce
text that accurately reflects the content and meaning of human-crafted references.

### Test Mechanism

The test extracts the true and predicted values from the provided dataset and model. It initializes the ROUGE
evaluator with the specified metric (e.g., ROUGE-1). For each pair of true and predicted texts, it calculates the
ROUGE scores and compiles them into a dataframe. Histograms and bar charts are generated for each ROUGE metric
(Precision, Recall, and F1 Score) to visualize their distribution. Additionally, a table of descriptive statistics
(mean, median, standard deviation, minimum, and maximum) is compiled for each metric, providing a comprehensive
summary of the model's performance.

### Signs of High Risk

- Consistently low scores across ROUGE metrics could indicate poor quality in the generated text, suggesting that
  the model fails to capture the essential content of the reference texts.
- Low precision scores might suggest that the generated text contains a lot of redundant or irrelevant information.
- Low recall scores may indicate that important information from the reference text is being omitted.
- An imbalanced performance between precision and recall, reflected by a low F1 Score, could signal issues in the
  model's ability to balance informativeness and conciseness.

### Strengths

- Provides a multifaceted evaluation of text quality through different ROUGE metrics, offering a detailed view of
  model performance.
- Visual representations (histograms and bar charts) make it easier to interpret the distribution and trends of the
  scores.
- Descriptive statistics offer a concise summary of the model's strengths and weaknesses in generating text.

### Limitations

- ROUGE metrics primarily focus on n-gram overlap and may not fully capture semantic coherence, fluency, or
  grammatical quality of the text.
- The evaluation relies on the availability of high-quality reference texts, which may not always be obtainable.
- While useful for comparison, ROUGE scores alone do not provide a complete assessment of a model's performance and
  should be supplemented with other metrics and qualitative analysis.

##### validmind.tests.model_validation.TimeSeriesPredictionWithCI

**Functions:**

- [**TimeSeriesPredictionWithCI**](#validmind.tests.model_validation.TimeSeriesPredictionWithCI.TimeSeriesPredictionWithCI) – Assesses predictive accuracy and uncertainty in time series models, highlighting breaches beyond confidence

###### validmind.tests.model_validation.TimeSeriesPredictionWithCI.TimeSeriesPredictionWithCI

```python
TimeSeriesPredictionWithCI(dataset, model, confidence=0.95)
```

Assesses predictive accuracy and uncertainty in time series models, highlighting breaches beyond confidence
intervals.

### Purpose

The purpose of the Time Series Prediction with Confidence Intervals (CI) test is to visualize the actual versus
predicted values for time series data, including confidence intervals, and to compute and report the number of
breaches beyond these intervals. This helps in evaluating the reliability and accuracy of the model's predictions.

### Test Mechanism

The function performs the following steps:

- Calculates the standard deviation of prediction errors.
- Determines the confidence intervals using a specified confidence level, typically 95%.
- Counts the number of actual values that fall outside the confidence intervals, referred to as breaches.
- Generates a plot visualizing the actual values, predicted values, and confidence intervals.
- Returns a DataFrame summarizing the breach information, including the total breaches, upper breaches, and lower
  breaches.

### Signs of High Risk

- A high number of breaches indicates that the model's predictions are not reliable within the specified confidence
  level.
- Significant deviations between actual and predicted values may highlight model inadequacies or issues with data
  quality.

### Strengths

- Provides a visual representation of prediction accuracy and the uncertainty around predictions.
- Includes a statistical measure of prediction reliability through confidence intervals.
- Computes and reports breaches, offering a quantitative assessment of prediction performance.

### Limitations

- Assumes that the dataset is provided as a DataFrameDataset object with a datetime index.
- Requires that `dataset.y_pred(model)` returns the predicted values for the model.
- The calculation of confidence intervals assumes normally distributed errors, which may not hold for all datasets.

##### validmind.tests.model_validation.TimeSeriesPredictionsPlot

**Functions:**

- [**TimeSeriesPredictionsPlot**](#validmind.tests.model_validation.TimeSeriesPredictionsPlot.TimeSeriesPredictionsPlot) – Plot actual vs predicted values for time series data and generate a visual comparison for the model.

###### validmind.tests.model_validation.TimeSeriesPredictionsPlot.TimeSeriesPredictionsPlot

```python
TimeSeriesPredictionsPlot(dataset, model)
```

Plot actual vs predicted values for time series data and generate a visual comparison for the model.

### Purpose

The purpose of this function is to visualize the actual versus predicted values for time
series data for a single model.

### Test Mechanism

The function plots the actual values from the dataset and overlays the predicted
values from the model using Plotly for interactive visualization.

- Large discrepancies between actual and predicted values indicate poor model performance.
- Systematic deviations in predicted values can highlight model bias or issues with data patterns.

### Strengths

- Provides a clear visual comparison of model predictions against actual values.
- Uses Plotly for interactive and visually appealing plots.

### Limitations

- Assumes that the dataset is provided as a DataFrameDataset object with a datetime index.
- Requires that `dataset.y_pred(model)` returns the predicted values for the model.

##### validmind.tests.model_validation.TimeSeriesR2SquareBySegments

**Functions:**

- [**TimeSeriesR2SquareBySegments**](#validmind.tests.model_validation.TimeSeriesR2SquareBySegments.TimeSeriesR2SquareBySegments) – Evaluates the R-Squared values of regression models over specified time segments in time series data to assess

###### validmind.tests.model_validation.TimeSeriesR2SquareBySegments.TimeSeriesR2SquareBySegments

```python
TimeSeriesR2SquareBySegments(dataset, model, segments=None)
```

Evaluates the R-Squared values of regression models over specified time segments in time series data to assess
segment-wise model performance.

### Purpose

The TimeSeriesR2SquareBySegments test aims to evaluate the R-Squared values for several regression models across
different segments of time series data. This helps in determining how well the models explain the variability in
the data within each specific time segment.

### Test Mechanism

- Provides a visual representation of model performance across different time segments.
- Allows for identification of segments where the model performs poorly.
- Calculating the R-Squared values for each segment.
- Generating a bar chart to visually represent the R-Squared values across different models and segments.

### Signs of High Risk

- Significantly low R-Squared values for certain time segments, indicating poor model performance in those periods.
- Large variability in R-Squared values across different segments for the same model, suggesting inconsistent
  performance.

### Strengths

- Provides a visual representation of how well models perform over different time periods.
- Helps identify time segments where models may need improvement or retraining.
- Facilitates comparison between multiple models in a straightforward manner.

### Limitations

- Assumes datasets are provided as DataFrameDataset objects with the attributes `y`, `y_pred`, and
  `feature_columns`.
- Requires that `dataset.y_pred(model)` returns predicted values for the model.
- Assumes that both `y_true` and `y_pred` are pandas Series with datetime indices, which may not always be the case.
- May not account for more nuanced temporal dependencies within the segments.

##### validmind.tests.model_validation.TokenDisparity

**Functions:**

- [**TokenDisparity**](#validmind.tests.model_validation.TokenDisparity.TokenDisparity) – Evaluates the token disparity between reference and generated texts, visualizing the results through histograms and

###### validmind.tests.model_validation.TokenDisparity.TokenDisparity

```python
TokenDisparity(dataset, model)
```

Evaluates the token disparity between reference and generated texts, visualizing the results through histograms and
bar charts, alongside compiling a comprehensive table of descriptive statistics for token counts.

### Purpose

The Token Disparity test aims to assess the difference in the number of tokens between reference texts and texts
generated by the model. Understanding token disparity is essential for evaluating how well the generated content
matches the expected length and richness of the reference texts.

### Test Mechanism

The test extracts true and predicted values from the dataset and model. It computes the number of tokens in each
reference and generated text. The results are visualized using histograms and bar charts to display the
distribution of token counts. Additionally, a table of descriptive statistics, including the mean, median, standard
deviation, minimum, and maximum token counts, is compiled to provide a detailed summary of token usage.

### Signs of High Risk

- Significant disparity in token counts between reference and generated texts could indicate issues with text
  generation quality, such as verbosity or lack of detail.
- Consistently low token counts in generated texts compared to references might suggest that the model is producing
  incomplete or overly concise outputs.

### Strengths

- Provides a simple yet effective evaluation of text length and token usage.
- Visual representations (histograms and bar charts) make it easier to interpret the distribution and trends of
  token counts.
- Descriptive statistics offer a concise summary of the model's performance in generating texts of appropriate
  length.

### Limitations

- Token counts alone do not provide a complete assessment of text quality and should be supplemented with other
  metrics and qualitative analysis.

##### validmind.tests.model_validation.ToxicityScore

**Functions:**

- [**ToxicityScore**](#validmind.tests.model_validation.ToxicityScore.ToxicityScore) – Assesses the toxicity levels of texts generated by NLP models to identify and mitigate harmful or offensive content.

###### validmind.tests.model_validation.ToxicityScore.ToxicityScore

```python
ToxicityScore(dataset, model)
```

Assesses the toxicity levels of texts generated by NLP models to identify and mitigate harmful or offensive content.

### Purpose

The ToxicityScore metric is designed to evaluate the toxicity levels of texts generated by models. This is crucial
for identifying and mitigating harmful or offensive content in machine-generated texts.

### Test Mechanism

The function starts by extracting the input, true, and predicted values from the provided dataset and model. The
toxicity score is computed for each text using a preloaded `toxicity` evaluation tool. The scores are compiled into
dataframes, and histograms and bar charts are generated to visualize the distribution of toxicity scores.
Additionally, a table of descriptive statistics (mean, median, standard deviation, minimum, and maximum) is
compiled for the toxicity scores, providing a comprehensive summary of the model's performance.

### Signs of High Risk

- Drastic spikes in toxicity scores indicate potentially toxic content within the associated text segment.
- Persistent high toxicity scores across multiple texts may suggest systemic issues in the model's text generation
  process.

### Strengths

- Provides a clear evaluation of toxicity levels in generated texts, helping to ensure content safety and
  appropriateness.
- Visual representations (histograms and bar charts) make it easier to interpret the distribution and trends of
  toxicity scores.
- Descriptive statistics offer a concise summary of the model's performance in generating non-toxic texts.

### Limitations

- The accuracy of the toxicity scores is contingent upon the underlying `toxicity` tool.
- The scores provide a broad overview but do not specify which portions or tokens of the text are responsible for
  high toxicity.
- Supplementary, in-depth analysis might be needed for granular insights.

##### validmind.tests.model_validation.sklearn

**Modules:**

- [**AdjustedMutualInformation**](#validmind.tests.model_validation.sklearn.AdjustedMutualInformation) –
- [**AdjustedRandIndex**](#validmind.tests.model_validation.sklearn.AdjustedRandIndex) –
- [**ClassifierPerformance**](#validmind.tests.model_validation.sklearn.ClassifierPerformance) –
- [**ClusterCosineSimilarity**](#validmind.tests.model_validation.sklearn.ClusterCosineSimilarity) –
- [**ClusterPerformanceMetrics**](#validmind.tests.model_validation.sklearn.ClusterPerformanceMetrics) –
- [**CompletenessScore**](#validmind.tests.model_validation.sklearn.CompletenessScore) –
- [**ConfusionMatrix**](#validmind.tests.model_validation.sklearn.ConfusionMatrix) –
- [**FeatureImportance**](#validmind.tests.model_validation.sklearn.FeatureImportance) –
- [**FowlkesMallowsScore**](#validmind.tests.model_validation.sklearn.FowlkesMallowsScore) –
- [**HomogeneityScore**](#validmind.tests.model_validation.sklearn.HomogeneityScore) –
- [**HyperParametersTuning**](#validmind.tests.model_validation.sklearn.HyperParametersTuning) –
- [**KMeansClustersOptimization**](#validmind.tests.model_validation.sklearn.KMeansClustersOptimization) –
- [**MinimumAccuracy**](#validmind.tests.model_validation.sklearn.MinimumAccuracy) –
- [**MinimumF1Score**](#validmind.tests.model_validation.sklearn.MinimumF1Score) –
- [**MinimumROCAUCScore**](#validmind.tests.model_validation.sklearn.MinimumROCAUCScore) –
- [**ModelsPerformanceComparison**](#validmind.tests.model_validation.sklearn.ModelsPerformanceComparison) –
- [**OverfitDiagnosis**](#validmind.tests.model_validation.sklearn.OverfitDiagnosis) –
- [**PermutationFeatureImportance**](#validmind.tests.model_validation.sklearn.PermutationFeatureImportance) –
- [**PopulationStabilityIndex**](#validmind.tests.model_validation.sklearn.PopulationStabilityIndex) –
- [**PrecisionRecallCurve**](#validmind.tests.model_validation.sklearn.PrecisionRecallCurve) –
- [**ROCCurve**](#validmind.tests.model_validation.sklearn.ROCCurve) –
- [**RegressionErrors**](#validmind.tests.model_validation.sklearn.RegressionErrors) –
- [**RegressionErrorsComparison**](#validmind.tests.model_validation.sklearn.RegressionErrorsComparison) –
- [**RegressionPerformance**](#validmind.tests.model_validation.sklearn.RegressionPerformance) –
- [**RegressionR2Square**](#validmind.tests.model_validation.sklearn.RegressionR2Square) –
- [**RegressionR2SquareComparison**](#validmind.tests.model_validation.sklearn.RegressionR2SquareComparison) –
- [**RobustnessDiagnosis**](#validmind.tests.model_validation.sklearn.RobustnessDiagnosis) –
- [**SHAPGlobalImportance**](#validmind.tests.model_validation.sklearn.SHAPGlobalImportance) –
- [**SilhouettePlot**](#validmind.tests.model_validation.sklearn.SilhouettePlot) –
- [**TrainingTestDegradation**](#validmind.tests.model_validation.sklearn.TrainingTestDegradation) –
- [**VMeasure**](#validmind.tests.model_validation.sklearn.VMeasure) –
- [**WeakspotsDiagnosis**](#validmind.tests.model_validation.sklearn.WeakspotsDiagnosis) –

###### validmind.tests.model_validation.sklearn.AdjustedMutualInformation

**Functions:**

- [**AdjustedMutualInformation**](#validmind.tests.model_validation.sklearn.AdjustedMutualInformation.AdjustedMutualInformation) – Evaluates clustering model performance by measuring mutual information between true and predicted labels, adjusting

####### validmind.tests.model_validation.sklearn.AdjustedMutualInformation.AdjustedMutualInformation

```python
AdjustedMutualInformation(model, dataset)
```

Evaluates clustering model performance by measuring mutual information between true and predicted labels, adjusting
for chance.

### Purpose

The purpose of this metric (Adjusted Mutual Information) is to evaluate the performance of a machine learning
model, more specifically, a clustering model. It measures the mutual information between the true labels and the
ones predicted by the model, adjusting for chance.

### Test Mechanism

The Adjusted Mutual Information (AMI) uses sklearn's `adjusted_mutual_info_score` function. This function
calculates the mutual information between the true labels and the ones predicted while correcting for the chance
correlation expected due to random label assignments. This test requires the model, the training dataset, and the
test dataset as inputs.

### Signs of High Risk

- Low Adjusted Mutual Information Score: This score ranges between 0 and 1. A low score (closer to 0) can indicate
  poor model performance as the predicted labels do not align well with the true labels.
- In case of high-dimensional data, if the algorithm shows high scores, this could also be a potential risk as AMI
  may not perform reliably.

### Strengths

- The AMI metric takes into account the randomness of the predicted labels, which makes it more robust than the
  simple Mutual Information.
- The scale of AMI is not dependent on the sizes of the clustering, allowing for comparability between different
  datasets or models.
- Good for comparing the output of clustering algorithms where the number of clusters is not known a priori.

### Limitations

- Adjusted Mutual Information does not take into account the continuous nature of some data. As a result, it may
  not be the best choice for regression or other continuous types of tasks.
- AMI has the drawback of being biased towards clusterings with a higher number of clusters.
- In comparison to other metrics, AMI can be slower to compute.
- The interpretability of the score can be complex as it depends on the understanding of information theory
  concepts.

###### validmind.tests.model_validation.sklearn.AdjustedRandIndex

**Functions:**

- [**AdjustedRandIndex**](#validmind.tests.model_validation.sklearn.AdjustedRandIndex.AdjustedRandIndex) – Measures the similarity between two data clusters using the Adjusted Rand Index (ARI) metric in clustering machine

####### validmind.tests.model_validation.sklearn.AdjustedRandIndex.AdjustedRandIndex

```python
AdjustedRandIndex(model, dataset)
```

Measures the similarity between two data clusters using the Adjusted Rand Index (ARI) metric in clustering machine
learning models.

### Purpose

The Adjusted Rand Index (ARI) metric is intended to measure the similarity between two data clusters. This metric
is specifically used for clustering machine learning models to quantify how well the model is clustering and
producing data groups. It involves comparing the model's produced clusters against the actual (true) clusters found
in the dataset.

### Test Mechanism

The Adjusted Rand Index (ARI) is calculated using the `adjusted_rand_score` method from the `sklearn.metrics`
module in Python. The test requires inputs including the model itself and the model's training and test datasets.
The model's computed clusters and the true clusters are compared, and the similarities are measured to compute the
ARI.

### Signs of High Risk

- If the ARI is close to zero, it signifies that the model's cluster assignments are random and do not match the
  actual dataset clusters, indicating a high risk.
- An ARI of less than zero indicates that the model's clustering performance is worse than random.

### Strengths

- ARI is normalized and provides a consistent metric between -1 and +1, irrespective of raw cluster sizes or
  dataset size variations.
- It does not require a ground truth for computation, making it ideal for unsupervised learning model evaluations.
- It penalizes for false positives and false negatives, providing a robust measure of clustering quality.

### Limitations

- In real-world situations, true clustering is often unknown, which can hinder the practical application of the ARI.
- The ARI requires all individual data instances to be independent, which may not always hold true.
- It may be difficult to interpret the implications of an ARI score without context or a benchmark, as it is
  heavily dependent on the characteristics of the dataset used.

###### validmind.tests.model_validation.sklearn.ClassifierPerformance

**Functions:**

- [**ClassifierPerformance**](#validmind.tests.model_validation.sklearn.ClassifierPerformance.ClassifierPerformance) – Evaluates performance of binary or multiclass classification models using precision, recall, F1-Score, accuracy,
- [**multiclass_roc_auc_score**](#validmind.tests.model_validation.sklearn.ClassifierPerformance.multiclass_roc_auc_score) –

####### validmind.tests.model_validation.sklearn.ClassifierPerformance.ClassifierPerformance

```python
ClassifierPerformance(dataset, model, average='macro')
```

Evaluates performance of binary or multiclass classification models using precision, recall, F1-Score, accuracy,
and ROC AUC scores.

### Purpose

The Classifier Performance test is designed to evaluate the performance of Machine Learning classification models.
It accomplishes this by computing precision, recall, F1-Score, and accuracy, as well as the ROC AUC (Receiver
operating characteristic - Area under the curve) scores, thereby providing a comprehensive analytic view of the
models' performance. The test is adaptable, handling binary and multiclass models equally effectively.

### Test Mechanism

The test produces a report that includes precision, recall, F1-Score, and accuracy, by leveraging the
`classification_report` from scikit-learn's metrics module. For multiclass models, macro and weighted averages for
these scores are also calculated. Additionally, the ROC AUC scores are calculated and included in the report using
the `multiclass_roc_auc_score` function. The outcome of the test (report format) differs based on whether the model
is binary or multiclass.

### Signs of High Risk

- Low values for precision, recall, F1-Score, accuracy, and ROC AUC, indicating poor performance.
- Imbalance in precision and recall scores.
- A low ROC AUC score, especially scores close to 0.5 or lower, suggesting a failing model.

### Strengths

- Versatile, capable of assessing both binary and multiclass models.
- Utilizes a variety of commonly employed performance metrics, offering a comprehensive view of model performance.
- The use of ROC-AUC as a metric is beneficial for evaluating unbalanced datasets.

### Limitations

- Assumes correctly identified labels for binary classification models.
- Specifically designed for classification models and not suitable for regression models.
- May provide limited insights if the test dataset does not represent real-world scenarios adequately.

####### validmind.tests.model_validation.sklearn.ClassifierPerformance.multiclass_roc_auc_score

```python
multiclass_roc_auc_score(y_test, y_pred, average='macro')
```

###### validmind.tests.model_validation.sklearn.ClusterCosineSimilarity

**Functions:**

- [**ClusterCosineSimilarity**](#validmind.tests.model_validation.sklearn.ClusterCosineSimilarity.ClusterCosineSimilarity) – Measures the intra-cluster similarity of a clustering model using cosine similarity.

####### validmind.tests.model_validation.sklearn.ClusterCosineSimilarity.ClusterCosineSimilarity

```python
ClusterCosineSimilarity(model, dataset)
```

Measures the intra-cluster similarity of a clustering model using cosine similarity.

### Purpose

The purpose of this metric is to measure how similar the data points within each cluster of a clustering model are.
This is done using cosine similarity, which compares the multi-dimensional direction (but not magnitude) of data
vectors. From a Model Risk Management perspective, this metric is used to quantitatively validate that clusters
formed by a model have high intra-cluster similarity.

### Test Mechanism

This test works by first extracting the true and predicted clusters of the model's training data. Then, it computes
the centroid (average data point) of each cluster. Next, it calculates the cosine similarity between each data
point within a cluster and its respective centroid. Finally, it outputs the mean cosine similarity of each cluster,
highlighting how similar, on average, data points in a cluster are to the cluster's centroid.

### Signs of High Risk

- Low mean cosine similarity for one or more clusters: If the mean cosine similarity is low, the data points within
  the respective cluster have high variance in their directions. This can be indicative of poor clustering,
  suggesting that the model might not be suitably separating the data into distinct patterns.
- High disparity between mean cosine similarity values across clusters: If there's a significant difference in mean
  cosine similarity across different clusters, this could indicate imbalance in how the model forms clusters.

### Strengths

- Cosine similarity operates in a multi-dimensional space, making it effective for measuring similarity in high
  dimensional datasets, typical for many machine learning problems.
- It provides an agnostic view of the cluster performance by only considering the direction (and not the magnitude)
  of each vector.
- This metric is not dependent on the scale of the variables, making it equally effective on different scales.

### Limitations

- Cosine similarity does not consider magnitudes (i.e. lengths) of vectors, only their direction. This means it may
  overlook instances where clusters have been adequately separated in terms of magnitude.
- This method summarily assumes that centroids represent the average behavior of data points in each cluster. This
  might not always be true, especially in clusters with high amounts of variance or non-spherical shapes.
- It primarily works with continuous variables and is not suitable for binary or categorical variables.
- Lastly, although rare, perfect perpendicular vectors (cosine similarity = 0) could be within the same cluster,
  which may give an inaccurate representation of a 'bad' cluster due to low cosine similarity score.

###### validmind.tests.model_validation.sklearn.ClusterPerformanceMetrics

**Functions:**

- [**ClusterPerformanceMetrics**](#validmind.tests.model_validation.sklearn.ClusterPerformanceMetrics.ClusterPerformanceMetrics) – Evaluates the performance of clustering machine learning models using multiple established metrics.

**Attributes:**

- [**ADJUSTED_MUTUAL_INFORMATION**](#validmind.tests.model_validation.sklearn.ClusterPerformanceMetrics.ADJUSTED_MUTUAL_INFORMATION) –
- [**ADJUSTED_RAND_INDEX**](#validmind.tests.model_validation.sklearn.ClusterPerformanceMetrics.ADJUSTED_RAND_INDEX) –
- [**COMPLETENESS**](#validmind.tests.model_validation.sklearn.ClusterPerformanceMetrics.COMPLETENESS) –
- [**FOULKES_MALLOWS_SCORE**](#validmind.tests.model_validation.sklearn.ClusterPerformanceMetrics.FOULKES_MALLOWS_SCORE) –
- [**HOMOGENEITY**](#validmind.tests.model_validation.sklearn.ClusterPerformanceMetrics.HOMOGENEITY) –
- [**V_MEASURE**](#validmind.tests.model_validation.sklearn.ClusterPerformanceMetrics.V_MEASURE) –

####### validmind.tests.model_validation.sklearn.ClusterPerformanceMetrics.ADJUSTED_MUTUAL_INFORMATION

```python
ADJUSTED_MUTUAL_INFORMATION = "\nThe Adjusted Mutual Information (AMI) is a clustering evaluation metric used to quantify the degree of\nagreement between a clustering solution and the true class labels. It provides a score that ranges from 0 to 1,\nwith a higher score indicating a better clustering result. A score of 1 signifies perfect agreement,\nwhile a score of 0 suggests that the clustering is random with respect to the true labels. AMI takes into account the\npotential randomness in the assignments and adjusts for chance, making it a robust measure that considers both the\nextent of agreement and the potential for random clustering.\n"

```

####### validmind.tests.model_validation.sklearn.ClusterPerformanceMetrics.ADJUSTED_RAND_INDEX

```python
ADJUSTED_RAND_INDEX = "\nThe Adjusted Rand Index (ARI) is a clustering evaluation metric used to measure the\nsimilarity between the cluster assignments in a clustering solution and the true class labels. It calculates a\nscore that ranges from -1 to 1, with a higher score indicating a better clustering result. A score of 1 signifies\nperfect agreement between the clustering and the ground truth, while a score near 0 implies that the clustering\nis random with respect to the true labels, and negative values indicate disagreement. ARI accounts for chance\nclustering, making it a robust measure for assessing the quality of clustering solutions by considering both the\nextent of agreement and potential randomness in the assignments.\n"

```

####### validmind.tests.model_validation.sklearn.ClusterPerformanceMetrics.COMPLETENESS

```python
COMPLETENESS = "\nThe completeness score is a clustering evaluation metric used to assess how well a clustering solution captures all data points\nthat belong to a single true class or category. It quantifies the extent to which the data points of a given class are\ngrouped into a single cluster. The completeness score ranges from 0 to 1, with a higher score indicating that the clustering\nsolution effectively accounts for all data points within their actual class, emphasizing the comprehensiveness of the\nclustering results with respect to the ground truth labels.\n"

```

####### validmind.tests.model_validation.sklearn.ClusterPerformanceMetrics.ClusterPerformanceMetrics

```python
ClusterPerformanceMetrics(model, dataset)
```

Evaluates the performance of clustering machine learning models using multiple established metrics.

### Purpose

The `ClusterPerformanceMetrics` test is used to assess the performance and validity of clustering machine learning
models. It evaluates homogeneity, completeness, V measure score, the Adjusted Rand Index, the Adjusted Mutual
Information, and the Fowlkes-Mallows score of the model. These metrics provide a holistic understanding of the
model's ability to accurately form clusters of the given dataset.

### Test Mechanism

The `ClusterPerformanceMetrics` test runs a clustering ML model over a given dataset and then calculates six
metrics using the Scikit-learn metrics computation functions: Homogeneity Score, Completeness Score, V Measure,
Adjusted Rand Index (ARI), Adjusted Mutual Information (AMI), and Fowlkes-Mallows Score. It then returns the result
as a summary, presenting the metric values for both training and testing datasets.

### Signs of High Risk

- Low Homogeneity Score: Indicates that the clusters formed contain a variety of classes, resulting in less pure
  clusters.
- Low Completeness Score: Suggests that class instances are scattered across multiple clusters rather than being
  gathered in a single cluster.
- Low V Measure: Reports a low overall clustering performance.
- ARI close to 0 or Negative: Implies that clustering results are random or disagree with the true labels.
- AMI close to 0: Means that clustering labels are random compared with the true labels.
- Low Fowlkes-Mallows score: Signifies less precise and poor clustering performance in terms of precision and
  recall.

### Strengths

- Provides a comprehensive view of clustering model performance by examining multiple clustering metrics.
- Uses established and widely accepted metrics from scikit-learn, providing reliability in the results.
- Able to provide performance metrics for both training and testing datasets.
- Clearly defined and human-readable descriptions of each score make it easy to understand what each score
  represents.

### Limitations

- Only applies to clustering models; not suitable for other types of machine learning models.
- Does not test for overfitting or underfitting in the clustering model.
- All the scores rely on ground truth labels, the absence or inaccuracy of which can lead to misleading results.
- Does not consider aspects like computational efficiency of the model or its capability to handle high dimensional
  data.

####### validmind.tests.model_validation.sklearn.ClusterPerformanceMetrics.FOULKES_MALLOWS_SCORE

```python
FOULKES_MALLOWS_SCORE = "\nThe Fowlkes-Mallows score is a clustering evaluation metric used to assess the quality of\na clustering solution by measuring the geometric mean of two fundamental clustering metrics: precision and recall. It\nprovides a score that ranges from 0 to 1, where a higher score indicates a better clustering result. A score of 1 signifies\nperfect agreement with the true class labels, while lower scores suggest less precise and recall clustering performance.\nThe Fowlkes-Mallows score offers a balanced evaluation of clustering quality by considering both the ability to correctly\nidentify members of the same class (precision) and the ability to capture all members of the same class (recall).\n"

```

####### validmind.tests.model_validation.sklearn.ClusterPerformanceMetrics.HOMOGENEITY

```python
HOMOGENEITY = "\nThe homogeneity score is a clustering evaluation metric that quantifies the degree to which each cluster within a\nclustering solution contains only data points that belong to a single true class or category. It provides a score\nwithin the range of 0 to 1, where a higher homogeneity score indicates that the clusters are more pure and internally\nconsistent with respect to the ground truth labels, meaning that the data points within each cluster are closely related\nin terms of their actual class membership.\n"

```

####### validmind.tests.model_validation.sklearn.ClusterPerformanceMetrics.V_MEASURE

```python
V_MEASURE = "\nThe V-Measure score is a clustering evaluation metric that combines both homogeneity and completeness to provide a\nsingle measure of the overall quality of a clustering solution. It takes into account how well clusters are internally\ncoherent (homogeneity) and how well they capture all data points from the true classes (completeness). The V-Measure\nscore ranges from 0 to 1, where a higher score indicates a better clustering result. It balances the trade-off between\ncluster purity and the extent to which all data points from true classes are captured, offering a comprehensive evaluation\nof the clustering performance.\n"

```

###### validmind.tests.model_validation.sklearn.CompletenessScore

**Functions:**

- [**CompletenessScore**](#validmind.tests.model_validation.sklearn.CompletenessScore.CompletenessScore) – Evaluates a clustering model's capacity to categorize instances from a single class into the same cluster.

####### validmind.tests.model_validation.sklearn.CompletenessScore.CompletenessScore

```python
CompletenessScore(model, dataset)
```

Evaluates a clustering model's capacity to categorize instances from a single class into the same cluster.

### Purpose

The Completeness Score metric is used to assess the performance of clustering models. It measures the extent to
which all the data points that are members of a given class are elements of the same cluster. The aim is to
determine the capability of the model to categorize all instances from a single class into the same cluster.

### Test Mechanism

This test takes three inputs, a model and its associated training and testing datasets. It invokes the
`completeness_score` function from the sklearn library on the labels predicted by the model. High scores indicate
that data points from the same class generally appear in the same cluster, while low scores suggest the opposite.

### Signs of High Risk

- Low completeness score: This suggests that the model struggles to group instances from the same class into one
  cluster, indicating poor clustering performance.

### Strengths

- The Completeness Score provides an effective method for assessing the performance of a clustering model,
  specifically its ability to group class instances together.
- This test metric conveniently relies on the capabilities provided by the sklearn library, ensuring consistent and
  reliable test results.

### Limitations

- This metric only evaluates a specific aspect of clustering, meaning it may not provide a holistic or complete
  view of the model's performance.
- It cannot assess the effectiveness of the model in differentiating between separate classes, as it is solely
  focused on how well data points from the same class are grouped.
- The Completeness Score only applies to clustering models; it cannot be used for other types of machine learning
  models.

###### validmind.tests.model_validation.sklearn.ConfusionMatrix

**Functions:**

- [**ConfusionMatrix**](#validmind.tests.model_validation.sklearn.ConfusionMatrix.ConfusionMatrix) – Evaluates and visually represents the classification ML model's predictive performance using a Confusion Matrix

####### validmind.tests.model_validation.sklearn.ConfusionMatrix.ConfusionMatrix

```python
ConfusionMatrix(dataset, model)
```

Evaluates and visually represents the classification ML model's predictive performance using a Confusion Matrix
heatmap.

### Purpose

The Confusion Matrix tester is designed to assess the performance of a classification Machine Learning model. This
performance is evaluated based on how well the model is able to correctly classify True Positives, True Negatives,
False Positives, and False Negatives - fundamental aspects of model accuracy.

### Test Mechanism

The mechanism used involves taking the predicted results (`y_test_predict`) from the classification model and
comparing them against the actual values (`y_test_true`). A confusion matrix is built using the unique labels
extracted from `y_test_true`, employing scikit-learn's metrics. The matrix is then visually rendered with the help
of Plotly's `create_annotated_heatmap` function. A heatmap is created which provides a two-dimensional graphical
representation of the model's performance, showcasing distributions of True Positives (TP), True Negatives (TN),
False Positives (FP), and False Negatives (FN).

### Signs of High Risk

- High numbers of False Positives (FP) and False Negatives (FN), depicting that the model is not effectively
  classifying the values.
- Low numbers of True Positives (TP) and True Negatives (TN), implying that the model is struggling with correctly
  identifying class labels.

### Strengths

- It provides a simplified yet comprehensive visual snapshot of the classification model's predictive performance.
- It distinctly brings out True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives
  (FN), thus making it easier to focus on potential areas of improvement.
- The matrix is beneficial in dealing with multi-class classification problems as it can provide a simple view of
  complex model performances.
- It aids in understanding the different types of errors that the model could potentially make, as it provides
  in-depth insights into Type-I and Type-II errors.

### Limitations

- In cases of unbalanced classes, the effectiveness of the confusion matrix might be lessened. It may wrongly
  interpret the accuracy of a model that is essentially just predicting the majority class.
- It does not provide a single unified statistic that could evaluate the overall performance of the model.
  Different aspects of the model's performance are evaluated separately instead.
- It mainly serves as a descriptive tool and does not offer the capability for statistical hypothesis testing.
- Risks of misinterpretation exist because the matrix doesn't directly provide precision, recall, or F1-score data.
  These metrics have to be computed separately.

###### validmind.tests.model_validation.sklearn.FeatureImportance

**Functions:**

- [**FeatureImportance**](#validmind.tests.model_validation.sklearn.FeatureImportance.FeatureImportance) – Compute feature importance scores for a given model and generate a summary table

####### validmind.tests.model_validation.sklearn.FeatureImportance.FeatureImportance

```python
FeatureImportance(dataset, model, num_features=3)
```

Compute feature importance scores for a given model and generate a summary table
with the top important features.

### Purpose

The Feature Importance Comparison test is designed to compare the feature importance scores for different models
when applied to various datasets. By doing so, it aims to identify the most impactful features and assess the
consistency of feature importance across models.

### Test Mechanism

This test works by iterating through each dataset-model pair and calculating permutation feature importance (PFI)
scores. It then generates a summary table containing the top `num_features` important features for each model. The
process involves:

- Extracting features and target data from each dataset.
- Computing PFI scores using `sklearn.inspection.permutation_importance`.
- Sorting and selecting the top features based on their importance scores.
- Compiling these features into a summary table for comparison.

### Signs of High Risk

- Key features expected to be important are ranked low, indicating potential issues with model training or data
  quality.
- High variance in feature importance scores across different models, suggesting instability in feature selection.

### Strengths

- Provides a clear comparison of the most important features for each model.
- Uses permutation importance, which is a model-agnostic method and can be applied to any estimator.

### Limitations

- Assumes that the dataset is provided as a DataFrameDataset object with `x_df` and `y_df` methods to access
  feature and target data.
- Requires that `model.model` is compatible with `sklearn.inspection.permutation_importance`.
- The function's output is dependent on the number of features specified by `num_features`, which defaults to 3 but
  can be adjusted.

###### validmind.tests.model_validation.sklearn.FowlkesMallowsScore

**Functions:**

- [**FowlkesMallowsScore**](#validmind.tests.model_validation.sklearn.FowlkesMallowsScore.FowlkesMallowsScore) – Evaluates the similarity between predicted and actual cluster assignments in a model using the Fowlkes-Mallows

####### validmind.tests.model_validation.sklearn.FowlkesMallowsScore.FowlkesMallowsScore

```python
FowlkesMallowsScore(dataset, model)
```

Evaluates the similarity between predicted and actual cluster assignments in a model using the Fowlkes-Mallows
score.

### Purpose

The FowlkesMallowsScore is a performance metric used to validate clustering algorithms within machine learning
models. The score intends to evaluate the matching grade between two clusters. It measures the similarity between
the predicted and actual cluster assignments, thus gauging the accuracy of the model's clustering capability.

### Test Mechanism

The FowlkesMallowsScore method applies the `fowlkes_mallows_score` function from the `sklearn` library to evaluate
the model's accuracy in clustering different types of data. The test fetches the datasets from the model's training
and testing datasets as inputs then compares the resulting clusters against the previously known clusters to obtain
a score. A high score indicates a better clustering performance by the model.

### Signs of High Risk

- A low Fowlkes-Mallows score (near zero): This indicates that the model's clustering capability is poor and the
  algorithm isn't properly grouping data.
- Inconsistently low scores across different datasets: This may indicate that the model's clustering performance is
  not robust and the model may fail when applied to unseen data.

### Strengths

- The Fowlkes-Mallows score is a simple and effective method for evaluating the performance of clustering
  algorithms.
- This metric takes into account both precision and recall in its calculation, therefore providing a balanced and
  comprehensive measure of model performance.
- The Fowlkes-Mallows score is non-biased meaning it treats False Positives and False Negatives equally.

### Limitations

- As a pairwise-based method, this score can be computationally intensive for large datasets and can become
  unfeasible as the size of the dataset increases.
- The Fowlkes-Mallows score works best with balanced distribution of samples across clusters. If this condition is
  not met, the score can be skewed.
- It does not handle mismatching numbers of clusters between the true and predicted labels. As such, it may return
  misleading results if the predicted labels suggest a different number of clusters than what is in the true labels.

###### validmind.tests.model_validation.sklearn.HomogeneityScore

**Functions:**

- [**HomogeneityScore**](#validmind.tests.model_validation.sklearn.HomogeneityScore.HomogeneityScore) – Assesses clustering homogeneity by comparing true and predicted labels, scoring from 0 (heterogeneous) to 1

####### validmind.tests.model_validation.sklearn.HomogeneityScore.HomogeneityScore

```python
HomogeneityScore(dataset, model)
```

Assesses clustering homogeneity by comparing true and predicted labels, scoring from 0 (heterogeneous) to 1
(homogeneous).

### Purpose

The Homogeneity Score encapsulated in this performance test is used to measure the homogeneity of the clusters
formed by a machine learning model. In simple terms, a clustering result satisfies homogeneity if all of its
clusters contain only points which are members of a single class.

### Test Mechanism

This test uses the `homogeneity_score` function from the `sklearn.metrics` library to compare the ground truth
class labels of the training and testing sets with the labels predicted by the given model. The returned score is a
metric of the clustering accuracy, and ranges from 0.0 to 1.0, with 1.0 denoting the highest possible degree of
homogeneity.

### Signs of High Risk

- A score close to 0: This denotes that clusters are highly heterogenous and points within the same cluster might
  not belong to the same class.
- A significantly lower score for testing data compared to the score for training data: This can indicate
  overfitting, where the model has learned to perfectly match the training data but fails to perform well on unseen
  data.

### Strengths

- It provides a simple quantitative measure of the degree to which clusters contain points from only one class.
- Useful for validating clustering solutions where the ground truth — class membership of points — is known.
- It's agnostic to the absolute labels, and cares only that the points within the same cluster have the same class
  label.

### Limitations

- The Homogeneity Score is not useful for clustering solutions where the ground truth labels are not known.
- It doesn’t work well with differently sized clusters since it gives predominance to larger clusters.
- The score does not address the actual number of clusters formed, or the evenness of cluster sizes. It only checks
  the homogeneity within the given clusters created by the model.

###### validmind.tests.model_validation.sklearn.HyperParametersTuning

**Functions:**

- [**HyperParametersTuning**](#validmind.tests.model_validation.sklearn.HyperParametersTuning.HyperParametersTuning) – Exerts exhaustive grid search to identify optimal hyperparameters for the model, improving performance.

####### validmind.tests.model_validation.sklearn.HyperParametersTuning.HyperParametersTuning

```python
HyperParametersTuning(model, dataset, param_grid=None, scoring=None)
```

Exerts exhaustive grid search to identify optimal hyperparameters for the model, improving performance.

### Purpose:

The "HyperParametersTuning" metric aims to find the optimal set of hyperparameters for a given model. The test is
designed to enhance the performance of the model by determining the best configuration of hyperparameters. The
parameters that are being optimized are defined by the parameter grid provided to the metric.

### Test Mechanism:

The HyperParametersTuning test employs a grid search mechanism using the GridSearchCV function from the
scikit-learn library. The grid search algorithm systematically works through multiple combinations of parameter
values, cross-validating to determine which combination gives the best model performance. The chosen model and the
parameter grid passed for tuning are necessary inputs. Once the grid search is complete, the test caches and
returns details of the best model and its associated parameters.

### Signs of High Risk:

- The test raises a SkipTestError if the param_grid is not supplied, indicating a lack of specific parameters to
  optimize, which can be risky for certain model types reliant on parameter tuning.
- Poorly chosen scoring metrics that do not align well with the specific model or problem at hand could reflect
  potential risks or failures in achieving optimal performance.

### Strengths:

- Provides a comprehensive exploration mechanism to identify the best set of hyperparameters for the supplied
  model, thereby enhancing its performance.
- Implements GridSearchCV, simplifying and automating the time-consuming task of hyperparameter tuning.

### Limitations:

- The grid search algorithm can be computationally expensive, especially with large datasets or complex models, and
  can be time-consuming as it tests all possible combinations within the specified parameter grid.
- The effectiveness of the tuning is heavily dependent on the quality of data and only accepts datasets with
  numerical or ordered categories.
- Assumes that the same set of hyperparameters is optimal for all problem sets, which may not be true in every
  scenario.
- There's a potential risk of overfitting the model if the training set is not representative of the data that the
  model will be applied to.

###### validmind.tests.model_validation.sklearn.KMeansClustersOptimization

**Functions:**

- [**KMeansClustersOptimization**](#validmind.tests.model_validation.sklearn.KMeansClustersOptimization.KMeansClustersOptimization) – Optimizes the number of clusters in K-means models using Elbow and Silhouette methods.

####### validmind.tests.model_validation.sklearn.KMeansClustersOptimization.KMeansClustersOptimization

```python
KMeansClustersOptimization(model, dataset, n_clusters=None)
```

Optimizes the number of clusters in K-means models using Elbow and Silhouette methods.

### Purpose

This metric is used to optimize the number of clusters used in K-means clustering models. It intends to measure and
evaluate the optimal number of clusters by leveraging two methodologies, namely the Elbow method and the Silhouette
method. This is crucial as an inappropriate number of clusters can either overly simplify or overcomplicate the
structure of the data, thereby undermining the effectiveness of the model.

### Test Mechanism

The test mechanism involves iterating over a predefined range of cluster numbers and applying both the Elbow method
and the Silhouette method. The Elbow method computes the sum of the minimum euclidean distances between data points
and their respective cluster centers (distortion). This value decreases as the number of clusters increases; the
optimal number is typically at the 'elbow' point where the decrease in distortion becomes less pronounced.
Meanwhile, the Silhouette method calculates the average silhouette score for each data point in the dataset,
providing a measure of how similar each item is to its own cluster compared to other clusters. The optimal number
of clusters under this method is the one that maximizes the average silhouette score. The results of both methods
are plotted for visual inspection.

### Signs of High Risk

- A high distortion value or a low silhouette average score for the optimal number of clusters.
- No clear 'elbow' point or plateau observed in the distortion plot, or a uniformly low silhouette average score
  across different numbers of clusters, suggesting the data is not amenable to clustering.
- An optimal cluster number that is unreasonably high or low, suggestive of overfitting or underfitting,
  respectively.

### Strengths

- Provides both a visual and quantitative method to determine the optimal number of clusters.
- Leverages two different methods (Elbow and Silhouette), thereby affording robustness and versatility in assessing
  the data's clusterability.
- Facilitates improved model performance by allowing for an informed selection of the number of clusters.

### Limitations

- Assumes that a suitable number of clusters exists in the data, which may not always be true, especially for
  complex or noisy data.
- Both methods may fail to provide definitive answers when the data lacks clear cluster structures.
- Might not be straightforward to determine the 'elbow' point or maximize the silhouette average score, especially
  in larger and complicated datasets.
- Assumes spherical clusters (due to using the Euclidean distance in the Elbow method), which might not align with
  the actual structure of the data.

###### validmind.tests.model_validation.sklearn.MinimumAccuracy

**Functions:**

- [**MinimumAccuracy**](#validmind.tests.model_validation.sklearn.MinimumAccuracy.MinimumAccuracy) – Checks if the model's prediction accuracy meets or surpasses a specified threshold.

####### validmind.tests.model_validation.sklearn.MinimumAccuracy.MinimumAccuracy

```python
MinimumAccuracy(dataset, model, min_threshold=0.7)
```

Checks if the model's prediction accuracy meets or surpasses a specified threshold.

### Purpose

The Minimum Accuracy test’s objective is to verify whether the model's prediction accuracy on a specific dataset
meets or surpasses a predetermined minimum threshold. Accuracy, which is simply the ratio of correct predictions to
total predictions, is a key metric for evaluating the model's performance. Considering binary as well as multiclass
classifications, accurate labeling becomes indispensable.

### Test Mechanism

The test mechanism involves contrasting the model's accuracy score with a preset minimum threshold value, with the
default being 0.7. The accuracy score is computed utilizing sklearn’s `accuracy_score` method, where the true
labels `y_true` and predicted labels `class_pred` are compared. If the accuracy score is above the threshold, the
test receives a passing mark. The test returns the result along with the accuracy score and threshold used for the
test.

### Signs of High Risk

- Model fails to achieve or surpass the predefined score threshold.
- Persistent scores below the threshold, indicating a high risk of inaccurate predictions.

### Strengths

- Simplicity, presenting a straightforward measure of holistic model performance across all classes.
- Particularly advantageous when classes are balanced.
- Versatile, as it can be implemented on both binary and multiclass classification tasks.

### Limitations

- Misleading accuracy scores when classes in the dataset are highly imbalanced.
- Favoritism towards the majority class, giving an inaccurate perception of model performance.
- Inability to measure the model's precision, recall, or capacity to manage false positives or false negatives.
- Focused on overall correctness and may not be sufficient for all types of model analytics.

###### validmind.tests.model_validation.sklearn.MinimumF1Score

**Functions:**

- [**MinimumF1Score**](#validmind.tests.model_validation.sklearn.MinimumF1Score.MinimumF1Score) – Assesses if the model's F1 score on the validation set meets a predefined minimum threshold, ensuring balanced

####### validmind.tests.model_validation.sklearn.MinimumF1Score.MinimumF1Score

```python
MinimumF1Score(dataset, model, min_threshold=0.5)
```

Assesses if the model's F1 score on the validation set meets a predefined minimum threshold, ensuring balanced
performance between precision and recall.

### Purpose

The main objective of this test is to ensure that the F1 score, a balanced measure of precision and recall, of the
model meets or surpasses a predefined threshold on the validation dataset. The F1 score is highly useful for
gauging model performance in classification tasks, especially in cases where the distribution of positive and
negative classes is skewed.

### Test Mechanism

The F1 score for the validation dataset is computed through scikit-learn's metrics in Python. The scoring mechanism
differs based on the classification problem: for multi-class problems, macro averaging is used, and for binary
classification, the built-in `f1_score` calculation is used. The obtained F1 score is then assessed against the
predefined minimum F1 score that is expected from the model.

### Signs of High Risk

- If a model returns an F1 score that is less than the established threshold, it is regarded as high risk.
- A low F1 score might suggest that the model is not finding an optimal balance between precision and recall,
  failing to effectively identify positive classes while minimizing false positives.

### Strengths

- Provides a balanced measure of a model's performance by accounting for both false positives and false negatives.
- Particularly advantageous in scenarios with imbalanced class distribution, where accuracy can be misleading.
- Flexibility in setting the threshold value allows tailored minimum acceptable performance standards.

### Limitations

- May not be suitable for all types of models and machine learning tasks.
- The F1 score assumes an equal cost for false positives and false negatives, which may not be true in some
  real-world scenarios.
- Practitioners might need to rely on other metrics such as precision, recall, or the ROC-AUC score that align more
  closely with specific requirements.

###### validmind.tests.model_validation.sklearn.MinimumROCAUCScore

**Functions:**

- [**MinimumROCAUCScore**](#validmind.tests.model_validation.sklearn.MinimumROCAUCScore.MinimumROCAUCScore) – Validates model by checking if the ROC AUC score meets or surpasses a specified threshold.

####### validmind.tests.model_validation.sklearn.MinimumROCAUCScore.MinimumROCAUCScore

```python
MinimumROCAUCScore(dataset, model, min_threshold=0.5)
```

Validates model by checking if the ROC AUC score meets or surpasses a specified threshold.

### Purpose

The Minimum ROC AUC Score test is used to determine the model's performance by ensuring that the Receiver Operating
Characteristic Area Under the Curve (ROC AUC) score on the validation dataset meets or exceeds a predefined
threshold. The ROC AUC score indicates how well the model can distinguish between different classes, making it a
crucial measure in binary and multiclass classification tasks.

### Test Mechanism

This test implementation calculates the multiclass ROC AUC score on the true target values and the model's
predictions. The test converts the multi-class target variables into binary format using `LabelBinarizer` before
computing the score. If this ROC AUC score is higher than the predefined threshold (defaulted to 0.5), the test
passes; otherwise, it fails. The results, including the ROC AUC score, the threshold, and whether the test passed
or failed, are then stored in a `ThresholdTestResult` object.

### Signs of High Risk

- A high risk or failure in the model's performance as related to this metric would be represented by a low ROC AUC
  score, specifically any score lower than the predefined minimum threshold. This suggests that the model is
  struggling to distinguish between different classes effectively.

### Strengths

- The test considers both the true positive rate and false positive rate, providing a comprehensive performance
  measure.
- ROC AUC score is threshold-independent meaning it measures the model's quality across various classification
  thresholds.
- Works robustly with binary as well as multi-class classification problems.

### Limitations

- ROC AUC may not be useful if the class distribution is highly imbalanced; it could perform well in terms of AUC
  but still fail to predict the minority class.
- The test does not provide insight into what specific aspects of the model are causing poor performance if the ROC
  AUC score is unsatisfactory.
- The use of macro average for multiclass ROC AUC score implies equal weightage to each class, which might not be
  appropriate if the classes are imbalanced.

###### validmind.tests.model_validation.sklearn.ModelsPerformanceComparison

**Functions:**

- [**ModelsPerformanceComparison**](#validmind.tests.model_validation.sklearn.ModelsPerformanceComparison.ModelsPerformanceComparison) – Evaluates and compares the performance of multiple Machine Learning models using various metrics like accuracy,

####### validmind.tests.model_validation.sklearn.ModelsPerformanceComparison.ModelsPerformanceComparison

```python
ModelsPerformanceComparison(dataset, models)
```

Evaluates and compares the performance of multiple Machine Learning models using various metrics like accuracy,
precision, recall, and F1 score.

### Purpose

The Models Performance Comparison test aims to evaluate and compare the performance of various Machine Learning
models using test data. It employs multiple metrics such as accuracy, precision, recall, and the F1 score, among
others, to assess model performance and assist in selecting the most effective model for the designated task.

### Test Mechanism

The test employs Scikit-learn’s performance metrics to evaluate each model's performance for both binary and
multiclass classification tasks. To compare performances, the test runs each model against the test dataset, then
produces a comprehensive classification report. This report includes metrics such as accuracy, precision, recall,
and the F1 score. Based on whether the task at hand is binary or multiclass classification, it calculates metrics
for all the classes and their weighted averages, macro averages, and per-class metrics. The test will be skipped if
no models are supplied.

### Signs of High Risk

- Low scores in accuracy, precision, recall, and F1 metrics indicate a potentially high risk.
- A low area under the Receiver Operating Characteristic (ROC) curve (roc_auc score) is another possible indicator
  of high risk.
- If the metrics scores are significantly lower than alternative models, this might suggest a high risk of failure.

### Strengths

- Provides a simple way to compare the performance of multiple models, accommodating both binary and multiclass
  classification tasks.
- Offers a holistic view of model performance through a comprehensive report of key performance metrics.
- The inclusion of the ROC AUC score is advantageous, as this robust performance metric can effectively handle
  class imbalance issues.

### Limitations

- May not be suitable for more complex performance evaluations that consider factors such as prediction speed,
  computational cost, or business-specific constraints.
- The test's reliability depends on the provided test dataset; hence, the selected models' performance could vary
  with unseen data or changes in the data distribution.
- The ROC AUC score might not be as meaningful or easily interpretable for multilabel/multiclass tasks.

###### validmind.tests.model_validation.sklearn.OverfitDiagnosis

**Functions:**

- [**OverfitDiagnosis**](#validmind.tests.model_validation.sklearn.OverfitDiagnosis.OverfitDiagnosis) – Assesses potential overfitting in a model's predictions, identifying regions where performance between training and

**Attributes:**

- [**DEFAULT_CLASSIFICATION_METRIC**](#validmind.tests.model_validation.sklearn.OverfitDiagnosis.DEFAULT_CLASSIFICATION_METRIC) –
- [**DEFAULT_REGRESSION_METRIC**](#validmind.tests.model_validation.sklearn.OverfitDiagnosis.DEFAULT_REGRESSION_METRIC) –
- [**DEFAULT_THRESHOLD**](#validmind.tests.model_validation.sklearn.OverfitDiagnosis.DEFAULT_THRESHOLD) –
- [**PERFORMANCE_METRICS**](#validmind.tests.model_validation.sklearn.OverfitDiagnosis.PERFORMANCE_METRICS) –
- [**logger**](#validmind.tests.model_validation.sklearn.OverfitDiagnosis.logger) –

####### validmind.tests.model_validation.sklearn.OverfitDiagnosis.DEFAULT_CLASSIFICATION_METRIC

```python
DEFAULT_CLASSIFICATION_METRIC = 'auc'
```

####### validmind.tests.model_validation.sklearn.OverfitDiagnosis.DEFAULT_REGRESSION_METRIC

```python
DEFAULT_REGRESSION_METRIC = 'mse'
```

####### validmind.tests.model_validation.sklearn.OverfitDiagnosis.DEFAULT_THRESHOLD

```python
DEFAULT_THRESHOLD = 0.04
```

####### validmind.tests.model_validation.sklearn.OverfitDiagnosis.OverfitDiagnosis

```python
OverfitDiagnosis(
    model, datasets, metric=None, cut_off_threshold=DEFAULT_THRESHOLD
)
```

Assesses potential overfitting in a model's predictions, identifying regions where performance between training and
testing sets deviates significantly.

### Purpose

The Overfit Diagnosis test aims to identify areas in a model's predictions where there is a significant difference
in performance between the training and testing sets. This test helps to pinpoint specific regions or feature
segments where the model may be overfitting.

### Test Mechanism

This test compares the model's performance on training versus test data, grouped by feature columns. It calculates
the difference between the training and test performance for each group and identifies regions where this
difference exceeds a specified threshold:

- The test works for both classification and regression models.
- It defaults to using the AUC metric for classification models and the MSE metric for regression models.
- The threshold for identifying overfitting regions is set to 0.04 by default.
- The test calculates the performance metrics for each feature segment and plots regions where the performance gap
  exceeds the threshold.

### Signs of High Risk

- Significant gaps between training and test performance metrics for specific feature segments.
- Multiple regions with performance gaps exceeding the defined threshold.
- Higher than expected differences in predicted versus actual values in the test set compared to the training set.

### Strengths

- Identifies specific areas where overfitting occurs.
- Supports multiple performance metrics, providing flexibility.
- Applicable to both classification and regression models.
- Visualization of overfitting segments aids in better understanding and debugging.

### Limitations

- The default threshold may not be suitable for all use cases and requires tuning.
- May not capture more subtle forms of overfitting that do not exceed the threshold.
- Assumes that the binning of features adequately represents the data segments.

####### validmind.tests.model_validation.sklearn.OverfitDiagnosis.PERFORMANCE_METRICS

```python
PERFORMANCE_METRICS = {
    "accuracy": {"function": metrics.accuracy_score, "is_lower_better": False},
    "auc": {"function": metrics.roc_auc_score, "is_lower_better": False},
    "f1": {"function": metrics.f1_score, "is_lower_better": False},
    "precision": {
        "function": metrics.precision_score,
        "is_lower_better": False,
    },
    "recall": {"function": metrics.recall_score, "is_lower_better": False},
    "mse": {"function": metrics.mean_squared_error, "is_lower_better": True},
    "mae": {"function": metrics.mean_absolute_error, "is_lower_better": True},
    "r2": {"function": metrics.r2_score, "is_lower_better": False},
    "mape": {
        "function": metrics.mean_absolute_percentage_error,
        "is_lower_better": True,
    },
}

```

####### validmind.tests.model_validation.sklearn.OverfitDiagnosis.logger

```python
logger = get_logger(__name__)
```

###### validmind.tests.model_validation.sklearn.PermutationFeatureImportance

**Functions:**

- [**PermutationFeatureImportance**](#validmind.tests.model_validation.sklearn.PermutationFeatureImportance.PermutationFeatureImportance) – Assesses the significance of each feature in a model by evaluating the impact on model performance when feature

**Attributes:**

- [**logger**](#validmind.tests.model_validation.sklearn.PermutationFeatureImportance.logger) –

####### validmind.tests.model_validation.sklearn.PermutationFeatureImportance.PermutationFeatureImportance

```python
PermutationFeatureImportance(model, dataset, fontsize=None, figure_height=None)
```

Assesses the significance of each feature in a model by evaluating the impact on model performance when feature
values are randomly rearranged.

### Purpose

The Permutation Feature Importance (PFI) metric aims to assess the importance of each feature used by the Machine
Learning model. The significance is measured by evaluating the decrease in the model's performance when the
feature's values are randomly arranged.

### Test Mechanism

PFI is calculated via the `permutation_importance` method from the `sklearn.inspection` module. This method
shuffles the columns of the feature dataset and measures the impact on the model's performance. A significant
decrease in performance after permutating a feature's values deems the feature as important. On the other hand, if
performance remains the same, the feature is likely not important. The output of the PFI metric is a figure
illustrating the importance of each feature.

### Signs of High Risk

- The model heavily relies on a feature with highly variable or easily permutable values, indicating instability.
- A feature deemed unimportant by the model but expected to have a significant effect on the outcome based on
  domain knowledge is not influencing the model's predictions.

### Strengths

- Provides insights into the importance of different features and may reveal underlying data structure.
- Can indicate overfitting if a particular feature or set of features overly impacts the model's predictions.
- Model-agnostic and can be used with any classifier that provides a measure of prediction accuracy before and
  after feature permutation.

### Limitations

- Does not imply causality; it only presents the amount of information that a feature provides for the prediction
  task.
- Does not account for interactions between features. If features are correlated, the permutation importance may
  allocate importance to one and not the other.
- Cannot interact with certain libraries like statsmodels, pytorch, catboost, etc., thus limiting its applicability.

####### validmind.tests.model_validation.sklearn.PermutationFeatureImportance.logger

```python
logger = get_logger(__name__)
```

###### validmind.tests.model_validation.sklearn.PopulationStabilityIndex

**Functions:**

- [**PopulationStabilityIndex**](#validmind.tests.model_validation.sklearn.PopulationStabilityIndex.PopulationStabilityIndex) – Assesses the Population Stability Index (PSI) to quantify the stability of an ML model's predictions across
- [**calculate_psi**](#validmind.tests.model_validation.sklearn.PopulationStabilityIndex.calculate_psi) – Taken from:

**Attributes:**

- [**logger**](#validmind.tests.model_validation.sklearn.PopulationStabilityIndex.logger) –

####### validmind.tests.model_validation.sklearn.PopulationStabilityIndex.PopulationStabilityIndex

```python
PopulationStabilityIndex(datasets, model, num_bins=10, mode='fixed')
```

Assesses the Population Stability Index (PSI) to quantify the stability of an ML model's predictions across
different datasets.

### Purpose

The Population Stability Index (PSI) serves as a quantitative assessment for evaluating the stability of a machine
learning model's output distributions when comparing two different datasets. Typically, these would be a
development and a validation dataset or two datasets collected at different periods. The PSI provides a measurable
indication of any significant shift in the model's performance over time or noticeable changes in the
characteristics of the population the model is making predictions for.

### Test Mechanism

The implementation of the PSI in this script involves calculating the PSI for each feature between the training and
test datasets. Data from both datasets is sorted and placed into either a predetermined number of bins or
quantiles. The boundaries for these bins are initially determined based on the distribution of the training data.
The contents of each bin are calculated and their respective proportions determined. Subsequently, the PSI is
derived for each bin through a logarithmic transformation of the ratio of the proportions of data for each feature
in the training and test datasets. The PSI, along with the proportions of data in each bin for both datasets, are
displayed in a summary table, a grouped bar chart, and a scatter plot.

### Signs of High Risk

- A high PSI value is a clear indicator of high risk. Such a value suggests a significant shift in the model
  predictions or severe changes in the characteristics of the underlying population.
- This ultimately suggests that the model may not be performing as well as expected and that it may be less
  reliable for making future predictions.

### Strengths

- The PSI provides a quantitative measure of the stability of a model over time or across different samples, making
  it an invaluable tool for evaluating changes in a model's performance.
- It allows for direct comparisons across different features based on the PSI value.
- The calculation and interpretation of the PSI are straightforward, facilitating its use in model risk management.
- The use of visual aids such as tables and charts further simplifies the comprehension and interpretation of the
  PSI.

### Limitations

- The PSI test does not account for the interdependence between features: features that are dependent on one
  another may show similar shifts in their distributions, which in turn may result in similar PSI values.
- The PSI test does not inherently provide insights into why there are differences in distributions or why the PSI
  values may have changed.
- The test may not handle features with significant outliers adequately.
- Additionally, the PSI test is performed on model predictions, not on the underlying data distributions which can
  lead to misinterpretations. Any changes in PSI could be due to shifts in the model (model drift), changes in the
  relationships between features and the target variable (concept drift), or both. However, distinguishing between
  these causes is non-trivial.

####### validmind.tests.model_validation.sklearn.PopulationStabilityIndex.calculate_psi

```python
calculate_psi(score_initial, score_new, num_bins=10, mode='fixed')
```

Taken from:
https://towardsdatascience.com/checking-model-stability-and-population-shift-with-psi-and-csi-6d12af008783

####### validmind.tests.model_validation.sklearn.PopulationStabilityIndex.logger

```python
logger = get_logger(__name__)
```

###### validmind.tests.model_validation.sklearn.PrecisionRecallCurve

**Functions:**

- [**PrecisionRecallCurve**](#validmind.tests.model_validation.sklearn.PrecisionRecallCurve.PrecisionRecallCurve) – Evaluates the precision-recall trade-off for binary classification models and visualizes the Precision-Recall curve.

####### validmind.tests.model_validation.sklearn.PrecisionRecallCurve.PrecisionRecallCurve

```python
PrecisionRecallCurve(model, dataset)
```

Evaluates the precision-recall trade-off for binary classification models and visualizes the Precision-Recall curve.

### Purpose

The Precision Recall Curve metric is intended to evaluate the trade-off between precision and recall in
classification models, particularly binary classification models. It assesses the model's capacity to produce
accurate results (high precision), as well as its ability to capture a majority of all positive instances (high
recall).

### Test Mechanism

The test extracts ground truth labels and prediction probabilities from the model's test dataset. It applies the
`precision_recall_curve` method from the sklearn metrics module to these extracted labels and predictions, which
computes a precision-recall pair for each possible threshold. This calculation results in an array of precision and
recall scores that can be plotted against each other to form the Precision-Recall Curve. This curve is then
visually represented by using Plotly's scatter plot.

### Signs of High Risk

- A lower area under the Precision-Recall Curve signifies high risk.
- This corresponds to a model yielding a high amount of false positives (low precision) and/or false negatives (low
  recall).
- If the curve is closer to the bottom left of the plot, rather than being closer to the top right corner, it can
  be a sign of high risk.

### Strengths

- This metric aptly represents the balance between precision (minimizing false positives) and recall (minimizing
  false negatives), which is especially critical in scenarios where both values are significant.
- Through the graphic representation, it enables an intuitive understanding of the model's performance across
  different threshold levels.

### Limitations

- This metric is only applicable to binary classification models - it raises errors for multiclass classification
  models or Foundation models.
- It may not fully represent the overall accuracy of the model if the cost of false positives and false negatives
  are extremely different, or if the dataset is heavily imbalanced.

###### validmind.tests.model_validation.sklearn.ROCCurve

**Functions:**

- [**ROCCurve**](#validmind.tests.model_validation.sklearn.ROCCurve.ROCCurve) – Evaluates binary classification model performance by generating and plotting the Receiver Operating Characteristic

####### validmind.tests.model_validation.sklearn.ROCCurve.ROCCurve

```python
ROCCurve(model, dataset)
```

Evaluates binary classification model performance by generating and plotting the Receiver Operating Characteristic
(ROC) curve and calculating the Area Under Curve (AUC) score.

### Purpose

The Receiver Operating Characteristic (ROC) curve is designed to evaluate the performance of binary classification
models. This curve illustrates the balance between the True Positive Rate (TPR) and False Positive Rate (FPR)
across various threshold levels. In combination with the Area Under the Curve (AUC), the ROC curve aims to measure
the model's discrimination ability between the two defined classes in a binary classification problem (e.g.,
default vs non-default). Ideally, a higher AUC score signifies superior model performance in accurately
distinguishing between the positive and negative classes.

### Test Mechanism

First, this script selects the target model and datasets that require binary classification. It then calculates the
predicted probabilities for the test set, and uses this data, along with the true outcomes, to generate and plot
the ROC curve. Additionally, it includes a line signifying randomness (AUC of 0.5). The AUC score for the model's
ROC curve is also computed, presenting a numerical estimation of the model's performance. If any Infinite values
are detected in the ROC threshold, these are effectively eliminated. The resulting ROC curve, AUC score, and
thresholds are consequently saved for future reference.

### Signs of High Risk

- A high risk is potentially linked to the model's performance if the AUC score drops below or nears 0.5.
- Another warning sign would be the ROC curve lying closer to the line of randomness, indicating no discriminative
  ability.
- For the model to be deemed competent at its classification tasks, it is crucial that the AUC score is
  significantly above 0.5.

### Strengths

- The ROC Curve offers an inclusive visual depiction of a model's discriminative power throughout all conceivable
  classification thresholds, unlike other metrics that solely disclose model performance at one fixed threshold.
- Despite the proportions of the dataset, the AUC Score, which represents the entire ROC curve as a single data
  point, continues to be consistent, proving to be the ideal choice for such situations.

### Limitations

- The primary limitation is that this test is exclusively structured for binary classification tasks, thus limiting
  its application towards other model types.
- Furthermore, its performance might be subpar with models that output probabilities highly skewed towards 0 or 1.
- At the extreme, the ROC curve could reflect high performance even when the majority of classifications are
  incorrect, provided that the model's ranking format is retained. This phenomenon is commonly termed the "Class
  Imbalance Problem".

###### validmind.tests.model_validation.sklearn.RegressionErrors

**Functions:**

- [**RegressionErrors**](#validmind.tests.model_validation.sklearn.RegressionErrors.RegressionErrors) – Assesses the performance and error distribution of a regression model using various error metrics.

####### validmind.tests.model_validation.sklearn.RegressionErrors.RegressionErrors

```python
RegressionErrors(model, dataset)
```

Assesses the performance and error distribution of a regression model using various error metrics.

### Purpose

The purpose of the Regression Errors test is to measure the performance of a regression model by calculating
several error metrics. This evaluation helps determine the model's accuracy and potential issues like overfitting
or bias by analyzing differences in error metrics between the training and testing datasets.

### Test Mechanism

The test computes the following error metrics:

- **Mean Absolute Error (MAE)**: Average of the absolute differences between true values and predicted values.
- **Mean Squared Error (MSE)**: Average of the squared differences between true values and predicted values.
- **Root Mean Squared Error (RMSE)**: Square root of the mean squared error.
- **Mean Absolute Percentage Error (MAPE)**: Average of the absolute differences between true values and predicted
  values, divided by the true values, and expressed as a percentage.
- **Mean Bias Deviation (MBD)**: Average bias between true values and predicted values.

These metrics are calculated separately for the training and testing datasets and compared to identify
discrepancies.

### Signs of High Risk

- High values for MAE, MSE, RMSE, or MAPE indicating poor model performance.
- Large differences in error metrics between the training and testing datasets, suggesting overfitting.
- Significant deviation of MBD from zero, indicating systematic bias in model predictions.

### Strengths

- Provides a comprehensive overview of model performance through multiple error metrics.
- Individual metrics offer specific insights, e.g., MAE for interpretability, MSE for emphasizing larger errors.
- RMSE is useful for being in the same unit as the target variable.
- MAPE allows the error to be expressed as a percentage.
- MBD detects systematic bias in model predictions.

### Limitations

- MAE and MSE are sensitive to outliers.
- RMSE heavily penalizes larger errors, which might not always be desirable.
- MAPE can be misleading when actual values are near zero.
- MBD may not be suitable if bias varies with the magnitude of actual values.
- These metrics may not capture all nuances of model performance and should be interpreted with domain-specific
  context.

###### validmind.tests.model_validation.sklearn.RegressionErrorsComparison

**Functions:**

- [**RegressionErrorsComparison**](#validmind.tests.model_validation.sklearn.RegressionErrorsComparison.RegressionErrorsComparison) – Assesses multiple regression error metrics to compare model performance across different datasets, emphasizing

**Attributes:**

- [**logger**](#validmind.tests.model_validation.sklearn.RegressionErrorsComparison.logger) –

####### validmind.tests.model_validation.sklearn.RegressionErrorsComparison.RegressionErrorsComparison

```python
RegressionErrorsComparison(datasets, models)
```

Assesses multiple regression error metrics to compare model performance across different datasets, emphasizing
systematic overestimation or underestimation and large percentage errors.

### Purpose

The purpose of this test is to compare regression errors for different models applied to various datasets. It aims
to examine model performance using multiple error metrics, thereby identifying areas where models may be
underperforming or exhibiting bias.

### Test Mechanism

The function iterates through each dataset-model pair and calculates various error metrics, including Mean Absolute
Error (MAE), Mean Squared Error (MSE), Mean Absolute Percentage Error (MAPE), and Mean Bias Deviation (MBD). The
results are summarized in a table, which provides a comprehensive view of each model's performance on the datasets.

### Signs of High Risk

- High Mean Absolute Error (MAE) or Mean Squared Error (MSE), indicating poor model performance.
- High Mean Absolute Percentage Error (MAPE), suggesting large percentage errors, especially problematic if the
  true values are small.
- Mean Bias Deviation (MBD) significantly different from zero, indicating systematic overestimation or
  underestimation by the model.

### Strengths

- Provides multiple error metrics to assess model performance from different perspectives.
- Includes a check to avoid division by zero when calculating MAPE.

### Limitations

- Assumes that the dataset is provided as a DataFrameDataset object with `y`, `y_pred`, and `feature_columns`
  attributes.
- Relies on the `logger` from `validmind.logging` to warn about zero values in `y_true`, which should be correctly
  implemented and imported.
- Requires that `dataset.y_pred(model)` returns the predicted values for the model.

####### validmind.tests.model_validation.sklearn.RegressionErrorsComparison.logger

```python
logger = get_logger(__name__)
```

###### validmind.tests.model_validation.sklearn.RegressionPerformance

**Functions:**

- [**RegressionPerformance**](#validmind.tests.model_validation.sklearn.RegressionPerformance.RegressionPerformance) – Evaluates the performance of a regression model using five different metrics: MAE, MSE, RMSE, MAPE, and MBD.

**Attributes:**

- [**logger**](#validmind.tests.model_validation.sklearn.RegressionPerformance.logger) –

####### validmind.tests.model_validation.sklearn.RegressionPerformance.RegressionPerformance

```python
RegressionPerformance(model, dataset)
```

Evaluates the performance of a regression model using five different metrics: MAE, MSE, RMSE, MAPE, and MBD.

### Purpose

The Regression Models Performance Comparison metric is used to measure the performance of regression models. It
calculates multiple evaluation metrics, including Mean Absolute Error (MAE), Mean Squared Error (MSE),
Root Mean Squared Error (RMSE), Mean Absolute Percentage Error (MAPE), and Mean Bias Deviation (MBD), thereby
enabling a comprehensive view of model performance.

### Test Mechanism

The test uses the sklearn library to calculate the MAE, MSE, RMSE, MAPE, and MBD. These calculations encapsulate both
the direction and the magnitude of error in predictions, thereby providing a multi-faceted view of model accuracy.

### Signs of High Risk

- High values of MAE, MSE, RMSE, and MAPE, which indicate a high error rate and imply a larger departure of the
  model's predictions from the true values.
- A large value of MBD, which shows a consistent bias in the model’s predictions.

### Strengths

- The metric evaluates models on five different metrics offering a comprehensive analysis of model performance.
- It is designed to handle regression tasks and can be seamlessly integrated with libraries like sklearn.

### Limitations

- The metric only evaluates regression models and does not evaluate classification models.
- The test assumes that the models have been trained and tested appropriately prior to evaluation. It does not
  handle pre-processing, feature selection, or other stages in the model lifecycle.

####### validmind.tests.model_validation.sklearn.RegressionPerformance.logger

```python
logger = get_logger(__name__)
```

###### validmind.tests.model_validation.sklearn.RegressionR2Square

**Functions:**

- [**RegressionR2Square**](#validmind.tests.model_validation.sklearn.RegressionR2Square.RegressionR2Square) – Assesses the overall goodness-of-fit of a regression model by evaluating R-squared (R2) and Adjusted R-squared (Adj

####### validmind.tests.model_validation.sklearn.RegressionR2Square.RegressionR2Square

```python
RegressionR2Square(dataset, model)
```

Assesses the overall goodness-of-fit of a regression model by evaluating R-squared (R2) and Adjusted R-squared (Adj
R2) scores to determine the model's explanatory power over the dependent variable.

### Purpose

The purpose of the RegressionR2Square Metric test is to measure the overall goodness-of-fit of a regression model.
Specifically, this Python-based test evaluates the R-squared (R2) and Adjusted R-squared (Adj R2) scores, which are
statistical measures used to assess the strength of the relationship between the model's predictors and the
response variable.

### Test Mechanism

The test deploys the `r2_score` method from the Scikit-learn metrics module to measure the R2 score on both
training and test sets. This score reflects the proportion of the variance in the dependent variable that is
predictable from the independent variables. The test also calculates the Adjusted R2 score, which accounts for the
number of predictors in the model to penalize model complexity and reduce overfitting. The Adjusted R2 score will
be smaller if unnecessary predictors are included in the model.

### Signs of High Risk

- Low R2 or Adjusted R2 scores, suggesting that the model does not explain much variation in the dependent variable.
- Significant discrepancy between R2 scores on the training set and test set, indicating overfitting and poor
  generalization to unseen data.

### Strengths

- Widely-used measure in regression analysis, providing a sound general indication of model performance.
- Easy to interpret and understand, as it represents the proportion of the dependent variable's variance explained
  by the independent variables.
- Adjusted R2 score helps control overfitting by penalizing unnecessary predictors.

### Limitations

- Sensitive to the inclusion of unnecessary predictors even though Adjusted R2 penalizes complexity.
- Less reliable in cases of non-linear relationships or when the underlying assumptions of linear regression are
  violated.
- Does not provide insight on whether the correct regression model was used or if key assumptions have been met.

###### validmind.tests.model_validation.sklearn.RegressionR2SquareComparison

**Functions:**

- [**RegressionR2SquareComparison**](#validmind.tests.model_validation.sklearn.RegressionR2SquareComparison.RegressionR2SquareComparison) – Compares R-Squared and Adjusted R-Squared values for different regression models across multiple datasets to assess

####### validmind.tests.model_validation.sklearn.RegressionR2SquareComparison.RegressionR2SquareComparison

```python
RegressionR2SquareComparison(datasets, models)
```

Compares R-Squared and Adjusted R-Squared values for different regression models across multiple datasets to assess
model performance and relevance of features.

### Purpose

The Regression R2 Square Comparison test aims to compare the R-Squared and Adjusted R-Squared values for different
regression models across various datasets. It helps in assessing how well each model explains the variability in
the dataset, and whether the models include irrelevant features.

### Test Mechanism

This test operates by:

- Iterating through each dataset-model pair.
- Calculating the R-Squared values to measure how much of the variability in the dataset is explained by the model.
- Calculating the Adjusted R-Squared values, which adjust the R-Squared based on the number of predictors in the
  model, making it more reliable when comparing models with different numbers of features.
- Generating a summary table containing these values for each combination of dataset and model.

### Signs of High Risk

- If the R-Squared values are significantly low, it indicates the model isn't explaining much of the variability in
  the dataset.
- A significant difference between R-Squared and Adjusted R-Squared values might indicate that the model includes
  irrelevant features.

### Strengths

- Provides a quantitative measure of model performance in terms of variance explained.
- Adjusted R-Squared accounts for the number of predictors, making it a more reliable measure when comparing models
  with different numbers of features.
- Useful for time-series forecasting and regression tasks.

### Limitations

- Assumes the dataset is provided as a DataFrameDataset object with `y`, `y_pred`, and `feature_columns` attributes.
- Relies on `adj_r2_score` from the `statsmodels.statsutils` module, which needs to be correctly implemented and
  imported.
- Requires that `dataset.y_pred(model)` returns the predicted values for the model.

###### validmind.tests.model_validation.sklearn.RobustnessDiagnosis

**Functions:**

- [**RobustnessDiagnosis**](#validmind.tests.model_validation.sklearn.RobustnessDiagnosis.RobustnessDiagnosis) – Assesses the robustness of a machine learning model by evaluating performance decay under noisy conditions.

**Attributes:**

- [**DEFAULT_CLASSIFICATION_METRIC**](#validmind.tests.model_validation.sklearn.RobustnessDiagnosis.DEFAULT_CLASSIFICATION_METRIC) –
- [**DEFAULT_DECAY_THRESHOLD**](#validmind.tests.model_validation.sklearn.RobustnessDiagnosis.DEFAULT_DECAY_THRESHOLD) –
- [**DEFAULT_REGRESSION_METRIC**](#validmind.tests.model_validation.sklearn.RobustnessDiagnosis.DEFAULT_REGRESSION_METRIC) –
- [**DEFAULT_STD_DEV_LIST**](#validmind.tests.model_validation.sklearn.RobustnessDiagnosis.DEFAULT_STD_DEV_LIST) –
- [**PERFORMANCE_METRICS**](#validmind.tests.model_validation.sklearn.RobustnessDiagnosis.PERFORMANCE_METRICS) –
- [**logger**](#validmind.tests.model_validation.sklearn.RobustnessDiagnosis.logger) –

####### validmind.tests.model_validation.sklearn.RobustnessDiagnosis.DEFAULT_CLASSIFICATION_METRIC

```python
DEFAULT_CLASSIFICATION_METRIC = 'auc'
```

####### validmind.tests.model_validation.sklearn.RobustnessDiagnosis.DEFAULT_DECAY_THRESHOLD

```python
DEFAULT_DECAY_THRESHOLD = 0.05
```

####### validmind.tests.model_validation.sklearn.RobustnessDiagnosis.DEFAULT_REGRESSION_METRIC

```python
DEFAULT_REGRESSION_METRIC = 'mse'
```

####### validmind.tests.model_validation.sklearn.RobustnessDiagnosis.DEFAULT_STD_DEV_LIST

```python
DEFAULT_STD_DEV_LIST = [0.1, 0.2, 0.3, 0.4, 0.5]
```

####### validmind.tests.model_validation.sklearn.RobustnessDiagnosis.PERFORMANCE_METRICS

```python
PERFORMANCE_METRICS = {
    "accuracy": {"function": metrics.accuracy_score, "is_lower_better": False},
    "auc": {"function": metrics.roc_auc_score, "is_lower_better": False},
    "f1": {"function": metrics.f1_score, "is_lower_better": False},
    "precision": {
        "function": metrics.precision_score,
        "is_lower_better": False,
    },
    "recall": {"function": metrics.recall_score, "is_lower_better": False},
    "mse": {"function": metrics.mean_squared_error, "is_lower_better": True},
    "mae": {"function": metrics.mean_absolute_error, "is_lower_better": True},
    "r2": {"function": metrics.r2_score, "is_lower_better": False},
    "mape": {
        "function": metrics.mean_absolute_percentage_error,
        "is_lower_better": True,
    },
}

```

####### validmind.tests.model_validation.sklearn.RobustnessDiagnosis.RobustnessDiagnosis

```python
RobustnessDiagnosis(
    datasets,
    model,
    metric=None,
    scaling_factor_std_dev_list=DEFAULT_STD_DEV_LIST,
    performance_decay_threshold=DEFAULT_DECAY_THRESHOLD,
)
```

Assesses the robustness of a machine learning model by evaluating performance decay under noisy conditions.

### Purpose

The Robustness Diagnosis test aims to evaluate the resilience of a machine learning model when subjected to
perturbations or noise in its input data. This is essential for understanding the model's ability to handle
real-world scenarios where data may be imperfect or corrupted.

### Test Mechanism

This test introduces Gaussian noise to the numeric input features of the datasets at varying scales of standard
deviation. The performance of the model is then measured using a specified metric. The process includes:

- Adding Gaussian noise to numerical input features based on scaling factors.
- Evaluating the model's performance on the perturbed data using metrics like AUC for classification tasks and MSE
  for regression tasks.
- Aggregating and plotting the results to visualize performance decay relative to perturbation size.

### Signs of High Risk

- A significant drop in performance metrics with minimal noise.
- Performance decay values exceeding the specified threshold.
- Consistent failure to meet performance standards across multiple perturbation scales.

### Strengths

- Provides insights into the model's robustness against noisy or corrupted data.
- Utilizes a variety of performance metrics suitable for both classification and regression tasks.
- Visualization helps in understanding the extent of performance degradation.

### Limitations

- Gaussian noise might not adequately represent all types of real-world data perturbations.
- Performance thresholds are somewhat arbitrary and might need tuning.
- The test may not account for more complex or unstructured noise patterns that could affect model robustness.

####### validmind.tests.model_validation.sklearn.RobustnessDiagnosis.logger

```python
logger = get_logger(__name__)
```

###### validmind.tests.model_validation.sklearn.SHAPGlobalImportance

**Functions:**

- [**SHAPGlobalImportance**](#validmind.tests.model_validation.sklearn.SHAPGlobalImportance.SHAPGlobalImportance) – Evaluates and visualizes global feature importance using SHAP values for model explanation and risk identification.
- [**generate_shap_plot**](#validmind.tests.model_validation.sklearn.SHAPGlobalImportance.generate_shap_plot) – Plots two types of SHAP global importance (SHAP).
- [**select_shap_values**](#validmind.tests.model_validation.sklearn.SHAPGlobalImportance.select_shap_values) – Selects SHAP values for binary or multiclass classification.

**Attributes:**

- [**logger**](#validmind.tests.model_validation.sklearn.SHAPGlobalImportance.logger) –

####### validmind.tests.model_validation.sklearn.SHAPGlobalImportance.SHAPGlobalImportance

```python
SHAPGlobalImportance(
    model,
    dataset,
    kernel_explainer_samples=10,
    tree_or_linear_explainer_samples=200,
    class_of_interest=None,
)
```

Evaluates and visualizes global feature importance using SHAP values for model explanation and risk identification.

### Purpose

The SHAP (SHapley Additive exPlanations) Global Importance metric aims to elucidate model outcomes by attributing
them to the contributing features. It assigns a quantifiable global importance to each feature via their respective
absolute Shapley values, thereby making it suitable for tasks like classification (both binary and multiclass).
This metric forms an essential part of model risk management.

### Test Mechanism

The exam begins with the selection of a suitable explainer which aligns with the model's type. For tree-based
models like XGBClassifier, RandomForestClassifier, CatBoostClassifier, TreeExplainer is used whereas for linear
models like LogisticRegression, XGBRegressor, LinearRegression, it is the LinearExplainer. Once the explainer
calculates the Shapley values, these values are visualized using two specific graphical representations:

1. Mean Importance Plot: This graph portrays the significance of individual features based on their absolute
   Shapley values. It calculates the average of these absolute Shapley values across all instances to highlight the
   global importance of features.

1. Summary Plot: This visual tool combines the feature importance with their effects. Every dot on this chart
   represents a Shapley value for a certain feature in a specific case. The vertical axis is denoted by the feature
   whereas the horizontal one corresponds to the Shapley value. A color gradient indicates the value of the feature,
   gradually changing from low to high. Features are systematically organized in accordance with their importance.

### Signs of High Risk

- Overemphasis on certain features in SHAP importance plots, thus hinting at the possibility of model overfitting
- Anomalies such as unexpected or illogical features showing high importance, which might suggest that the model's
  decisions are rooted in incorrect or undesirable reasoning
- A SHAP summary plot filled with high variability or scattered data points, indicating a cause for concern

### Strengths

- SHAP does more than just illustrating global feature significance, it offers a detailed perspective on how
  different features shape the model's decision-making logic for each instance.
- It provides clear insights into model behavior.

### Limitations

- High-dimensional data can convolute interpretations.
- Associating importance with tangible real-world impact still involves a certain degree of subjectivity.

####### validmind.tests.model_validation.sklearn.SHAPGlobalImportance.generate_shap_plot

```python
generate_shap_plot(type_, shap_values, x_test)
```

Plots two types of SHAP global importance (SHAP).

**Parameters:**

- **type\_** – The type of SHAP plot to generate. Must be "mean" or "summary".
- **shap_values** – The SHAP values to plot.
- **x_test** – The test data used to generate the SHAP values.

**Returns:**

- – The generated plot.

####### validmind.tests.model_validation.sklearn.SHAPGlobalImportance.logger

```python
logger = get_logger(__name__)
```

####### validmind.tests.model_validation.sklearn.SHAPGlobalImportance.select_shap_values

```python
select_shap_values(shap_values, class_of_interest)
```

Selects SHAP values for binary or multiclass classification.

For regression models, returns the SHAP values directly as there are no classes.

**Parameters:**

- **shap_values** – The SHAP values returned by the SHAP explainer. For multiclass
  classification, this will be a list where each element corresponds to a class.
  For regression, this will be a single array of SHAP values.
- **class_of_interest** – The class index for which to retrieve SHAP values. If None
  (default), the function will assume binary classification and use class 1
  by default.

**Returns:**

- – The SHAP values for the specified class (classification) or for the regression
- – output.

**Raises:**

- <code>[ValueError](#ValueError)</code> – If class_of_interest is specified and is out of bounds for the
  number of classes.

###### validmind.tests.model_validation.sklearn.SilhouettePlot

**Functions:**

- [**SilhouettePlot**](#validmind.tests.model_validation.sklearn.SilhouettePlot.SilhouettePlot) – Calculates and visualizes Silhouette Score, assessing the degree of data point suitability to its cluster in ML

####### validmind.tests.model_validation.sklearn.SilhouettePlot.SilhouettePlot

```python
SilhouettePlot(model, dataset)
```

Calculates and visualizes Silhouette Score, assessing the degree of data point suitability to its cluster in ML
models.

### Purpose

This test calculates the Silhouette Score, which is a model performance metric used in clustering applications.
Primarily, the Silhouette Score evaluates how similar a data point is to its own cluster compared to other
clusters. The metric ranges between -1 and 1, where a high value indicates that the object is well matched to its
own cluster and poorly matched to neighboring clusters. Thus, the goal is to achieve a high Silhouette Score,
implying well-separated clusters.

### Test Mechanism

The test first extracts the true and predicted labels from the model's training data. The test runs the Silhouette
Score function, which takes as input the training dataset features and the predicted labels, subsequently
calculating the average score. This average Silhouette Score is printed for reference. The script then calculates
the silhouette coefficients for each data point, helping to form the Silhouette Plot. Each cluster is represented
in this plot, with color distinguishing between different clusters. A red dashed line indicates the average
Silhouette Score. The Silhouette Scores are also collected into a structured table, facilitating model performance
analysis and comparison.

### Signs of High Risk

- A low Silhouette Score, potentially indicating that the clusters are not well separated and that data points may
  not be fitting well to their respective clusters.
- A Silhouette Plot displaying overlapping clusters or the absence of clear distinctions between clusters visually
  also suggests poor clustering performance.

### Strengths

- The Silhouette Score provides a clear and quantitative measure of how well data points have been grouped into
  clusters, offering insights into model performance.
- The Silhouette Plot provides an intuitive, graphical representation of the clustering mechanism, aiding visual
  assessments of model performance.
- It does not require ground truth labels, so it's useful when true cluster assignments are not known.

### Limitations

- The Silhouette Score may be susceptible to the influence of outliers, which could impact its accuracy and
  reliability.
- It assumes the clusters are convex and isotropic, which might not be the case with complex datasets.
- Due to the average nature of the Silhouette Score, the metric does not account for individual data point
  assignment nuances, so potentially relevant details may be omitted.
- Computationally expensive for large datasets, as it requires pairwise distance computations.

###### validmind.tests.model_validation.sklearn.TrainingTestDegradation

**Functions:**

- [**TrainingTestDegradation**](#validmind.tests.model_validation.sklearn.TrainingTestDegradation.TrainingTestDegradation) – Tests if model performance degradation between training and test datasets exceeds a predefined threshold.

####### validmind.tests.model_validation.sklearn.TrainingTestDegradation.TrainingTestDegradation

```python
TrainingTestDegradation(datasets, model, max_threshold=0.1)
```

Tests if model performance degradation between training and test datasets exceeds a predefined threshold.

### Purpose

The `TrainingTestDegradation` class serves as a test to verify that the degradation in performance between the
training and test datasets does not exceed a predefined threshold. This test measures the model's ability to
generalize from its training data to unseen test data, assessing key classification metrics such as accuracy,
precision, recall, and f1 score to verify the model's robustness and reliability.

### Test Mechanism

The code applies several predefined metrics, including accuracy, precision, recall, and f1 scores, to the model's
predictions for both the training and test datasets. It calculates the degradation as the difference between the
training score and test score divided by the training score. The test is considered successful if the degradation
for each metric is less than the preset maximum threshold of 10%. The results are summarized in a table showing
each metric's train score, test score, degradation percentage, and pass/fail status.

### Signs of High Risk

- A degradation percentage that exceeds the maximum allowed threshold of 10% for any of the evaluated metrics.
- A high difference or gap between the metric scores on the training and the test datasets.
- The 'Pass/Fail' column displaying 'Fail' for any of the evaluated metrics.

### Strengths

- Provides a quantitative measure of the model's ability to generalize to unseen data, which is key for predicting
  its practical real-world performance.
- By evaluating multiple metrics, it takes into account different facets of model performance and enables a more
  holistic evaluation.
- The use of a variable predefined threshold allows the flexibility to adjust the acceptability criteria for
  different scenarios.

### Limitations

- The test compares raw performance on training and test data but does not factor in the nature of the data. Areas
  with less representation in the training set might still perform poorly on unseen data.
- It requires good coverage and balance in the test and training datasets to produce reliable results, which may
  not always be available.
- The test is currently only designed for classification tasks.

###### validmind.tests.model_validation.sklearn.VMeasure

**Functions:**

- [**VMeasure**](#validmind.tests.model_validation.sklearn.VMeasure.VMeasure) – Evaluates homogeneity and completeness of a clustering model using the V Measure Score.

####### validmind.tests.model_validation.sklearn.VMeasure.VMeasure

```python
VMeasure(dataset, model)
```

Evaluates homogeneity and completeness of a clustering model using the V Measure Score.

### Purpose

The purpose of this metric, V Measure Score (V Score), is to evaluate the performance of a clustering model. It
measures the homogeneity and completeness of a set of cluster labels, where homogeneity refers to each cluster
containing only members of a single class and completeness meaning all members of a given class are assigned to the
same cluster.

### Test Mechanism

ClusterVMeasure is a class that inherits from another class, ClusterPerformance. It uses the `v_measure_score`
function from the sklearn module's metrics package. The required inputs to perform this metric are the model, train
dataset, and test dataset. The test is appropriate for models tasked with clustering.

### Signs of High Risk

- Low V Measure Score: A low V Measure Score indicates that the clustering model has poor homogeneity or
  completeness, or both. This might signal that the model is failing to correctly cluster the data.

### Strengths

- The V Measure Score is a harmonic mean between homogeneity and completeness. This ensures that both attributes
  are taken into account when evaluating the model, providing an overall measure of its cluster validity.
- The metric does not require knowledge of the ground truth classes when measuring homogeneity and completeness,
  making it applicable in instances where such information is unavailable.

### Limitations

- The V Measure Score can be influenced by the number of clusters, which means that it might not always reflect the
  quality of the clustering. Partitioning the data into many small clusters could lead to high homogeneity but low
  completeness, leading to a low V Measure Score even if the clustering might be useful.
- It assumes equal importance of homogeneity and completeness. In some applications, one may be more important than
  the other. The V Measure Score does not provide flexibility in assigning different weights to homogeneity and
  completeness.

###### validmind.tests.model_validation.sklearn.WeakspotsDiagnosis

**Functions:**

- [**WeakspotsDiagnosis**](#validmind.tests.model_validation.sklearn.WeakspotsDiagnosis.WeakspotsDiagnosis) – Identifies and visualizes weak spots in a machine learning model's performance across various sections of the

**Attributes:**

- [**DEFAULT_METRICS**](#validmind.tests.model_validation.sklearn.WeakspotsDiagnosis.DEFAULT_METRICS) –
- [**DEFAULT_THRESHOLDS**](#validmind.tests.model_validation.sklearn.WeakspotsDiagnosis.DEFAULT_THRESHOLDS) –

####### validmind.tests.model_validation.sklearn.WeakspotsDiagnosis.DEFAULT_METRICS

```python
DEFAULT_METRICS = {
    "accuracy": metrics.accuracy_score,
    "precision": metrics.precision_score,
    "recall": metrics.recall_score,
    "f1": metrics.f1_score,
}

```

####### validmind.tests.model_validation.sklearn.WeakspotsDiagnosis.DEFAULT_THRESHOLDS

```python
DEFAULT_THRESHOLDS = {
    "accuracy": 0.75,
    "precision": 0.5,
    "recall": 0.5,
    "f1": 0.7,
}

```

####### validmind.tests.model_validation.sklearn.WeakspotsDiagnosis.WeakspotsDiagnosis

```python
WeakspotsDiagnosis(
    datasets, model, features_columns=None, metrics=None, thresholds=None
)
```

Identifies and visualizes weak spots in a machine learning model's performance across various sections of the
feature space.

### Purpose

The weak spots test is applied to evaluate the performance of a machine learning model within specific regions of
its feature space. This test slices the feature space into various sections, evaluating the model's outputs within
each section against specific performance metrics (e.g., accuracy, precision, recall, and F1 scores). The ultimate
aim is to identify areas where the model's performance falls below the set thresholds, thereby exposing its
possible weaknesses and limitations.

### Test Mechanism

The test mechanism adopts an approach of dividing the feature space of the training dataset into numerous bins. The
model's performance metrics (accuracy, precision, recall, F1 scores) are then computed for each bin on both the
training and test datasets. A "weak spot" is identified if any of the performance metrics fall below a
predetermined threshold for a particular bin on the test dataset. The test results are visually plotted as bar
charts for each performance metric, indicating the bins which fail to meet the established threshold.

### Signs of High Risk

- Any performance metric of the model dropping below the set thresholds.
- Significant disparity in performance between the training and test datasets within a bin could be an indication
  of overfitting.
- Regions or slices with consistently low performance metrics. Such instances could mean that the model struggles
  to handle specific types of input data adequately, resulting in potentially inaccurate predictions.

### Strengths

- The test helps pinpoint precise regions of the feature space where the model's performance is below par, allowing
  for more targeted improvements to the model.
- The graphical presentation of the performance metrics offers an intuitive way to understand the model's
  performance across different feature areas.
- The test exhibits flexibility, letting users set different thresholds for various performance metrics according
  to the specific requirements of the application.

### Limitations

- The binning system utilized for the feature space in the test could over-simplify the model's behavior within
  each bin. The granularity of this slicing depends on the chosen 'bins' parameter and can sometimes be arbitrary.
- The effectiveness of this test largely hinges on the selection of thresholds for the performance metrics, which
  may not hold universally applicable and could be subjected to the specifications of a particular model and
  application.
- The test is unable to handle datasets with a text column, limiting its application to numerical or categorical
  data types only.
- Despite its usefulness in highlighting problematic regions, the test does not offer direct suggestions for model
  improvement.

##### validmind.tests.model_validation.statsmodels

**Modules:**

- [**AutoARIMA**](#validmind.tests.model_validation.statsmodels.AutoARIMA) –
- [**CumulativePredictionProbabilities**](#validmind.tests.model_validation.statsmodels.CumulativePredictionProbabilities) –
- [**DurbinWatsonTest**](#validmind.tests.model_validation.statsmodels.DurbinWatsonTest) –
- [**GINITable**](#validmind.tests.model_validation.statsmodels.GINITable) –
- [**KolmogorovSmirnov**](#validmind.tests.model_validation.statsmodels.KolmogorovSmirnov) –
- [**Lilliefors**](#validmind.tests.model_validation.statsmodels.Lilliefors) –
- [**PredictionProbabilitiesHistogram**](#validmind.tests.model_validation.statsmodels.PredictionProbabilitiesHistogram) –
- [**RegressionCoeffs**](#validmind.tests.model_validation.statsmodels.RegressionCoeffs) –
- [**RegressionFeatureSignificance**](#validmind.tests.model_validation.statsmodels.RegressionFeatureSignificance) –
- [**RegressionModelForecastPlot**](#validmind.tests.model_validation.statsmodels.RegressionModelForecastPlot) –
- [**RegressionModelForecastPlotLevels**](#validmind.tests.model_validation.statsmodels.RegressionModelForecastPlotLevels) –
- [**RegressionModelSensitivityPlot**](#validmind.tests.model_validation.statsmodels.RegressionModelSensitivityPlot) –
- [**RegressionModelSummary**](#validmind.tests.model_validation.statsmodels.RegressionModelSummary) –
- [**RegressionPermutationFeatureImportance**](#validmind.tests.model_validation.statsmodels.RegressionPermutationFeatureImportance) –
- [**ScorecardHistogram**](#validmind.tests.model_validation.statsmodels.ScorecardHistogram) –
- [**statsutils**](#validmind.tests.model_validation.statsmodels.statsutils) –

###### validmind.tests.model_validation.statsmodels.AutoARIMA

**Functions:**

- [**AutoARIMA**](#validmind.tests.model_validation.statsmodels.AutoARIMA.AutoARIMA) – Evaluates ARIMA models for time-series forecasting, ranking them using Bayesian and Akaike Information Criteria.

**Attributes:**

- [**logger**](#validmind.tests.model_validation.statsmodels.AutoARIMA.logger) –

####### validmind.tests.model_validation.statsmodels.AutoARIMA.AutoARIMA

```python
AutoARIMA(model, dataset)
```

Evaluates ARIMA models for time-series forecasting, ranking them using Bayesian and Akaike Information Criteria.

### Purpose

The AutoARIMA validation test is designed to evaluate and rank AutoRegressive Integrated Moving Average (ARIMA)
models. These models are primarily used for forecasting time-series data. The validation test automatically fits
multiple ARIMA models, with varying parameters, to every variable within the given dataset. The models are then
ranked based on their Bayesian Information Criterion (BIC) and Akaike Information Criterion (AIC) values, which
provide a basis for the efficient model selection process.

### Test Mechanism

This metric proceeds by generating an array of feasible combinations of ARIMA model parameters which are within a
prescribed limit. These limits include `max_p`, `max_d`, `max_q`; they represent the autoregressive, differencing,
and moving average components respectively. Upon applying these sets of parameters, the validation test fits each
ARIMA model to the time-series data provided. For each model, it subsequently proceeds to calculate and record both
the BIC and AIC values, which serve as performance indicators for the model fit. Prior to this parameter fitting
process, the Augmented Dickey-Fuller test for data stationarity is conducted on the data series. If a series is
found to be non-stationary, a warning message is sent out, given that ARIMA models necessitate input series to be
stationary.

### Signs of High Risk

- If the p-value of the Augmented Dickey-Fuller test for a variable exceeds 0.05, a warning is logged. This warning
  indicates that the series might not be stationary, leading to potentially inaccurate results.
- Consistent failure in fitting ARIMA models (as made evident through logged errors) might disclose issues with
  either the data or model stability.

### Strengths

- The AutoARIMA validation test simplifies the often complex task of selecting the most suitable ARIMA model based
  on BIC and AIC criteria.
- The mechanism incorporates a check for non-stationarity within the data, which is a critical prerequisite for
  ARIMA models.
- The exhaustive search through all possible combinations of model parameters enhances the likelihood of
  identifying the best-fit model.

### Limitations

- This validation test can be computationally costly as it involves creating and fitting multiple ARIMA models for
  every variable.
- Although the test checks for non-stationarity and logs warnings where present, it does not apply any
  transformations to the data to establish stationarity.
- The selection of models leans solely on BIC and AIC criteria, which may not yield the best predictive model in
  all scenarios.
- The test is only applicable to regression tasks involving time-series data, and may not work effectively for
  other types of machine learning tasks.

####### validmind.tests.model_validation.statsmodels.AutoARIMA.logger

```python
logger = get_logger(__name__)
```

###### validmind.tests.model_validation.statsmodels.CumulativePredictionProbabilities

**Functions:**

- [**CumulativePredictionProbabilities**](#validmind.tests.model_validation.statsmodels.CumulativePredictionProbabilities.CumulativePredictionProbabilities) – Visualizes cumulative probabilities of positive and negative classes for both training and testing in logistic

####### validmind.tests.model_validation.statsmodels.CumulativePredictionProbabilities.CumulativePredictionProbabilities

```python
CumulativePredictionProbabilities(
    dataset, model, title="Cumulative Probabilities"
)
```

Visualizes cumulative probabilities of positive and negative classes for both training and testing in logistic
regression models.

### Purpose

This metric is utilized to evaluate the distribution of predicted probabilities for positive and negative classes
in a logistic regression model. It provides a visual assessment of the model's behavior by plotting the cumulative
probabilities for positive and negative classes across both the training and test datasets.

### Test Mechanism

The logistic regression model is evaluated by first computing the predicted probabilities for each instance in both
the training and test datasets, which are then added as a new column in these sets. The cumulative probabilities
for positive and negative classes are subsequently calculated and sorted in ascending order. Cumulative
distributions of these probabilities are created for both positive and negative classes across both training and
test datasets. These cumulative probabilities are represented visually in a plot, containing two subplots - one for
the training data and the other for the test data, with lines representing cumulative distributions of positive and
negative classes.

### Signs of High Risk

- Imbalanced distribution of probabilities for either positive or negative classes.
- Notable discrepancies or significant differences between the cumulative probability distributions for the
  training data versus the test data.
- Marked discrepancies or large differences between the cumulative probability distributions for positive and
  negative classes.

### Strengths

- Provides a visual illustration of data, which enhances the ease of understanding and interpreting the model's
  behavior.
- Allows for the comparison of model's behavior across training and testing datasets, providing insights about how
  well the model is generalized.
- Differentiates between positive and negative classes and their respective distribution patterns, aiding in
  problem diagnosis.

### Limitations

- Exclusive to classification tasks and specifically to logistic regression models.
- Graphical results necessitate human interpretation and may not be directly applicable for automated risk
  detection.
- The method does not give a solitary quantifiable measure of model risk, instead, it offers a visual
  representation and broad distributional information.
- If the training and test datasets are not representative of the overall data distribution, the metric could
  provide misleading results.

###### validmind.tests.model_validation.statsmodels.DurbinWatsonTest

**Functions:**

- [**DurbinWatsonTest**](#validmind.tests.model_validation.statsmodels.DurbinWatsonTest.DurbinWatsonTest) – Assesses autocorrelation in time series data features using the Durbin-Watson statistic.

####### validmind.tests.model_validation.statsmodels.DurbinWatsonTest.DurbinWatsonTest

```python
DurbinWatsonTest(dataset, model, threshold=[1.5, 2.5])
```

Assesses autocorrelation in time series data features using the Durbin-Watson statistic.

### Purpose

The Durbin-Watson Test metric detects autocorrelation in time series data (where a set of data values influences
their predecessors). Autocorrelation is a crucial factor for regression tasks as these often assume the
independence of residuals. A model with significant autocorrelation may give unreliable predictions.

### Test Mechanism

Utilizing the `durbin_watson` function in the `statsmodels` Python library, the Durbin-Watson (DW) Test metric
generates a statistical value for each feature of the training dataset. The function is looped over all columns of
the dataset, calculating and caching the DW value for each column for further analysis. A DW metric value nearing 2
indicates no autocorrelation. Conversely, values approaching 0 suggest positive autocorrelation, and those leaning
towards 4 imply negative autocorrelation.

### Signs of High Risk

- If a feature's DW value significantly deviates from 2, it could signal a high risk due to potential
  autocorrelation issues in the dataset.
- A value closer to 0 could imply positive autocorrelation, while a value nearer to 4 could point to negative
  autocorrelation, both leading to potentially unreliable prediction models.

### Strengths

- The metric specializes in identifying autocorrelation in prediction model residuals.
- Autocorrelation detection assists in diagnosing violation of various modeling technique assumptions, particularly
  in regression analysis and time-series data modeling.

### Limitations

- The Durbin-Watson Test mainly detects linear autocorrelation and could overlook other types of relationships.
- The metric is highly sensitive to data points order. Shuffling the order could lead to notably different results.
- The test only checks for first-order autocorrelation (between a variable and its immediate predecessor) and fails
  to detect higher-order autocorrelation.

###### validmind.tests.model_validation.statsmodels.GINITable

**Functions:**

- [**GINITable**](#validmind.tests.model_validation.statsmodels.GINITable.GINITable) – Evaluates classification model performance using AUC, GINI, and KS metrics for training and test datasets.

####### validmind.tests.model_validation.statsmodels.GINITable.GINITable

```python
GINITable(dataset, model)
```

Evaluates classification model performance using AUC, GINI, and KS metrics for training and test datasets.

### Purpose

The 'GINITable' metric is designed to evaluate the performance of a classification model by emphasizing its
discriminatory power. Specifically, it calculates and presents three important metrics - the Area under the ROC
Curve (AUC), the GINI coefficient, and the Kolmogorov-Smirnov (KS) statistic - for both training and test datasets.

### Test Mechanism

Using a dictionary for storing performance metrics for both the training and test datasets, the 'GINITable' metric
calculates each of these metrics sequentially. The Area under the ROC Curve (AUC) is calculated via the
`roc_auc_score` function from the Scikit-Learn library. The GINI coefficient, a measure of statistical dispersion,
is then computed by doubling the AUC and subtracting 1. Finally, the Kolmogorov-Smirnov (KS) statistic is
calculated via the `roc_curve` function from Scikit-Learn, with the False Positive Rate (FPR) subtracted from the
True Positive Rate (TPR) and the maximum value taken from the resulting data. These metrics are then stored in a
pandas DataFrame for convenient visualization.

### Signs of High Risk

- Low values for performance metrics may suggest a reduction in model performance, particularly a low AUC which
  indicates poor classification performance, or a low GINI coefficient, which could suggest a decreased ability to
  discriminate different classes.
- A high KS value may be an indicator of potential overfitting, as this generally signifies a substantial
  divergence between positive and negative distributions.
- Significant discrepancies between the performance on the training dataset and the test dataset may present
  another signal of high risk.

### Strengths

- Offers three key performance metrics (AUC, GINI, and KS) in one test, providing a more comprehensive evaluation
  of the model.
- Provides a direct comparison between the model's performance on training and testing datasets, which aids in
  identifying potential underfitting or overfitting.
- The applied metrics are class-distribution invariant, thereby remaining effective for evaluating model
  performance even when dealing with imbalanced datasets.
- Presents the metrics in a user-friendly table format for easy comprehension and analysis.

### Limitations

- The GINI coefficient and KS statistic are both dependent on the AUC value. Therefore, any errors in the
  calculation of the latter will adversely impact the former metrics too.
- Mainly suited for binary classification models and may require modifications for effective application in
  multi-class scenarios.
- The metrics used are threshold-dependent and may exhibit high variability based on the chosen cut-off points.
- The test does not incorporate a method to efficiently handle missing or inefficiently processed data, which could
  lead to inaccuracies in the metrics if the data is not appropriately preprocessed.

###### validmind.tests.model_validation.statsmodels.KolmogorovSmirnov

**Functions:**

- [**KolmogorovSmirnov**](#validmind.tests.model_validation.statsmodels.KolmogorovSmirnov.KolmogorovSmirnov) – Assesses whether each feature in the dataset aligns with a normal distribution using the Kolmogorov-Smirnov test.

####### validmind.tests.model_validation.statsmodels.KolmogorovSmirnov.KolmogorovSmirnov

```python
KolmogorovSmirnov(model, dataset, dist='norm')
```

Assesses whether each feature in the dataset aligns with a normal distribution using the Kolmogorov-Smirnov test.

### Purpose

The Kolmogorov-Smirnov (KS) test evaluates the distribution of features in a dataset to determine their alignment
with a normal distribution. This is important because many statistical methods and machine learning models assume
normality in the data distribution.

### Test Mechanism

This test calculates the KS statistic and corresponding p-value for each feature in the dataset. It does so by
comparing the cumulative distribution function of the feature with an ideal normal distribution. The KS statistic
and p-value for each feature are then stored in a dictionary. The p-value threshold to reject the normal
distribution hypothesis is not preset, providing flexibility for different applications.

### Signs of High Risk

- Elevated KS statistic for a feature combined with a low p-value, indicating a significant divergence from a
  normal distribution.
- Features with notable deviations that could create problems if the model assumes normality in data distribution.

### Strengths

- The KS test is sensitive to differences in the location and shape of empirical cumulative distribution functions.
- It is non-parametric and adaptable to various datasets, as it does not assume any specific data distribution.
- Provides detailed insights into the distribution of individual features.

### Limitations

- The test's sensitivity to disparities in the tails of data distribution might cause false alarms about
  non-normality.
- Less effective for multivariate distributions, as it is designed for univariate distributions.
- Does not identify specific types of non-normality, such as skewness or kurtosis, which could impact model fitting.

###### validmind.tests.model_validation.statsmodels.Lilliefors

**Functions:**

- [**Lilliefors**](#validmind.tests.model_validation.statsmodels.Lilliefors.Lilliefors) – Assesses the normality of feature distributions in an ML model's training dataset using the Lilliefors test.

####### validmind.tests.model_validation.statsmodels.Lilliefors.Lilliefors

```python
Lilliefors(model, dataset)
```

Assesses the normality of feature distributions in an ML model's training dataset using the Lilliefors test.

### Purpose

The purpose of this metric is to utilize the Lilliefors test, named in honor of the Swedish statistician Hubert
Lilliefors, in order to assess whether the features of the machine learning model's training dataset conform to a
normal distribution. This is done because the assumption of normal distribution plays a vital role in numerous
statistical procedures as well as numerous machine learning models. Should the features fail to follow a normal
distribution, some model types may not operate at optimal efficiency. This can potentially lead to inaccurate
predictions.

### Test Mechanism

The application of this test happens across all feature columns within the training dataset. For each feature, the
Lilliefors test returns a test statistic and p-value. The test statistic quantifies how far the feature's
distribution is from an ideal normal distribution, whereas the p-value aids in determining the statistical
relevance of this deviation. The final results are stored within a dictionary, the keys of which correspond to the
name of the feature column, and the values being another dictionary which houses the test statistic and p-value.

### Signs of High Risk

- If the p-value corresponding to a specific feature sinks below a pre-established significance level, generally
  set at 0.05, then it can be deduced that the distribution of that feature significantly deviates from a normal
  distribution. This can present a high risk for models that assume normality, as these models may perform
  inaccurately or inefficiently in the presence of such a feature.

### Strengths

- One advantage of the Lilliefors test is its utility irrespective of whether the mean and variance of the normal
  distribution are known in advance. This makes it a more robust option in real-world situations where these values
  might not be known.
- The test has the ability to screen every feature column, offering a holistic view of the dataset.

### Limitations

- Despite the practical applications of the Lilliefors test in validating normality, it does come with some
  limitations.
- It is only capable of testing unidimensional data, thus rendering it ineffective for datasets with interactions
  between features or multi-dimensional phenomena.
- The test might not be as sensitive as some other tests (like the Anderson-Darling test) in detecting deviations
  from a normal distribution.
- Like any other statistical test, Lilliefors test may also produce false positives or negatives. Hence, banking
  solely on this test, without considering other characteristics of the data, may give rise to risks.

###### validmind.tests.model_validation.statsmodels.PredictionProbabilitiesHistogram

**Functions:**

- [**PredictionProbabilitiesHistogram**](#validmind.tests.model_validation.statsmodels.PredictionProbabilitiesHistogram.PredictionProbabilitiesHistogram) – Assesses the predictive probability distribution for binary classification to evaluate model performance and

####### validmind.tests.model_validation.statsmodels.PredictionProbabilitiesHistogram.PredictionProbabilitiesHistogram

```python
PredictionProbabilitiesHistogram(
    dataset, model, title="Histogram of Predictive Probabilities"
)
```

Assesses the predictive probability distribution for binary classification to evaluate model performance and
potential overfitting or bias.

### Purpose

The Prediction Probabilities Histogram test is designed to generate histograms displaying the Probability of
Default (PD) predictions for both positive and negative classes in training and testing datasets. This helps in
evaluating the performance of a logistic regression model, particularly for credit risk prediction.

### Test Mechanism

The metric follows these steps to execute the test:

- Extracts the target column from both the train and test datasets.
- Uses the model's predict function to calculate probabilities.
- Adds these probabilities as a new column to the training and testing dataframes.
- Generates histograms for each class (0 or 1) within the training and testing datasets.
- Sets different opacities for the histograms to enhance visualization.
- Overlays the four histograms (two for training and two for testing) on two different subplot frames.
- Returns a plotly graph object displaying the visualization.

### Signs of High Risk

- Significant discrepancies between the histograms of training and testing data.
- Large disparities between the histograms for the positive and negative classes.
- Potential overfitting or bias indicated by significant issues.
- Unevenly distributed probabilities suggesting inaccurate model predictions.

### Strengths

- Offers a visual representation of the PD predictions made by the model, aiding in understanding its behavior.
- Assesses both the training and testing datasets, adding depth to model validation.
- Highlights disparities between classes, providing insights into class imbalance or data skewness.
- Effectively visualizes risk spread, which is particularly beneficial for credit risk prediction.

### Limitations

- Specifically tailored for binary classification scenarios and not suited for multi-class classification tasks.
- Mainly applicable to logistic regression models, and may not be effective for other model types.
- Provides a robust visual representation but lacks a quantifiable measure to assess model performance.

###### validmind.tests.model_validation.statsmodels.RegressionCoeffs

**Functions:**

- [**RegressionCoeffs**](#validmind.tests.model_validation.statsmodels.RegressionCoeffs.RegressionCoeffs) – Assesses the significance and uncertainty of predictor variables in a regression model through visualization of

####### validmind.tests.model_validation.statsmodels.RegressionCoeffs.RegressionCoeffs

```python
RegressionCoeffs(model)
```

Assesses the significance and uncertainty of predictor variables in a regression model through visualization of
coefficients and their 95% confidence intervals.

### Purpose

The `RegressionCoeffs` metric visualizes the estimated regression coefficients alongside their 95% confidence intervals,
providing insights into the impact and significance of predictor variables on the response variable. This visualization
helps to understand the variability and uncertainty in the model's estimates, aiding in the evaluation of the
significance of each predictor.

### Test Mechanism

The function operates by extracting the estimated coefficients and their standard errors from the regression model.
Using these, it calculates the confidence intervals at a 95% confidence level, which indicates the range within which
the true coefficient value is expected to fall 95% of the time. The confidence intervals are computed using the
Z-value associated with the 95% confidence level. The coefficients and their confidence intervals are then visualized
in a bar plot. The x-axis represents the predictor variables, the y-axis represents the estimated coefficients, and
the error bars depict the confidence intervals.

### Signs of High Risk

- The confidence interval for a coefficient contains the zero value, suggesting that the predictor may not significantly
  contribute to the model.
- Multiple coefficients with confidence intervals that include zero, potentially indicating issues with model reliability.
- Very wide confidence intervals, which may suggest high uncertainty in the coefficient estimates and potential model
  instability.

### Strengths

- Provides a clear visualization that allows for easy interpretation of the significance and impact of predictor
  variables.
- Includes confidence intervals, which provide additional information about the uncertainty surrounding each coefficient
  estimate.

### Limitations

- The method assumes normality of residuals and independence of observations, assumptions that may not always hold true
  in practice.
- It does not address issues related to multi-collinearity among predictor variables, which can affect the interpretation
  of coefficients.
- This metric is limited to regression tasks using tabular data and is not applicable to other types of machine learning
  tasks or data structures.

###### validmind.tests.model_validation.statsmodels.RegressionFeatureSignificance

**Functions:**

- [**RegressionFeatureSignificance**](#validmind.tests.model_validation.statsmodels.RegressionFeatureSignificance.RegressionFeatureSignificance) – Assesses and visualizes the statistical significance of features in a regression model.

**Attributes:**

- [**logger**](#validmind.tests.model_validation.statsmodels.RegressionFeatureSignificance.logger) –

####### validmind.tests.model_validation.statsmodels.RegressionFeatureSignificance.RegressionFeatureSignificance

```python
RegressionFeatureSignificance(model, fontsize=10, p_threshold=0.05)
```

Assesses and visualizes the statistical significance of features in a regression model.

### Purpose

The Regression Feature Significance metric assesses the significance of each feature in a given set of regression
model. It creates a visualization displaying p-values for every feature of the model, assisting model developers
in understanding which features are most influential in their model.

### Test Mechanism

The test mechanism involves extracting the model's coefficients and p-values for each feature, and then plotting these
values. The x-axis on the plot contains the p-values while the y-axis denotes the coefficients of each feature. A
vertical red line is drawn at the threshold for p-value significance, which is 0.05 by default. Any features with
p-values to the left of this line are considered statistically significant at the chosen level.

### Signs of High Risk

- Any feature with a high p-value (greater than the threshold) is considered a potential high risk, as it suggests
  the feature is not statistically significant and may not be reliably contributing to the model's predictions.
- A high number of such features may indicate problems with the model validation, variable selection, and overall
  reliability of the model predictions.

### Strengths

- Helps identify the features that significantly contribute to a model's prediction, providing insights into the
  feature importance.
- Provides tangible, easy-to-understand visualizations to interpret the feature significance.

### Limitations

- This metric assumes model features are independent, which may not always be the case. Multicollinearity (high
  correlation amongst predictors) can cause high variance and unreliable statistical tests of significance.
- The p-value strategy for feature selection doesn't take into account the magnitude of the effect, focusing solely
  on whether the feature is likely non-zero.
- This test is specific to regression models and wouldn't be suitable for other types of ML models.
- P-value thresholds are somewhat arbitrary and do not always indicate practical significance, only statistical
  significance.

####### validmind.tests.model_validation.statsmodels.RegressionFeatureSignificance.logger

```python
logger = get_logger(__name__)
```

###### validmind.tests.model_validation.statsmodels.RegressionModelForecastPlot

**Functions:**

- [**RegressionModelForecastPlot**](#validmind.tests.model_validation.statsmodels.RegressionModelForecastPlot.RegressionModelForecastPlot) – Generates plots to visually compare the forecasted outcomes of a regression model against actual observed values over

**Attributes:**

- [**logger**](#validmind.tests.model_validation.statsmodels.RegressionModelForecastPlot.logger) –

####### validmind.tests.model_validation.statsmodels.RegressionModelForecastPlot.RegressionModelForecastPlot

```python
RegressionModelForecastPlot(model, dataset, start_date=None, end_date=None)
```

Generates plots to visually compare the forecasted outcomes of a regression model against actual observed values over
a specified date range.

### Purpose

This metric is useful for time-series models or any model where the outcome changes over time, allowing direct
comparison of predicted vs actual values. It can help identify overfitting or underfitting situations as well as
general model performance.

### Test Mechanism

This test generates a plot with the x-axis representing the date ranging from the specified "start_date" to the
"end_date", while the y-axis shows the value of the outcome variable. Two lines are plotted: one representing the
forecasted values and the other representing the observed values. The "start_date" and "end_date" can be parameters
of this test; if these parameters are not provided, they are set to the minimum and maximum date available in the
dataset.

### Signs of High Risk

- High risk or failure signs could be deduced visually from the plots if the forecasted line significantly deviates
  from the observed line, indicating the model's predicted values are not matching actual outcomes.
- A model that struggles to handle the edge conditions like maximum and minimum data points could also be
  considered a sign of risk.

### Strengths

- Visualization: The plot provides an intuitive and clear illustration of how well the forecast matches the actual
  values, making it straightforward even for non-technical stakeholders to interpret.
- Flexibility: It allows comparison for multiple models and for specified time periods.
- Model Evaluation: It can be useful in identifying overfitting or underfitting situations, as these will manifest
  as discrepancies between the forecasted and observed values.

### Limitations

- Interpretation Bias: Interpretation of the plot is subjective and can lead to different conclusions by different
  evaluators.
- Lack of Precision: Visual representation might not provide precise values of the deviation.
- Inapplicability: Limited to cases where the order of data points (time-series) matters, it might not be of much
  use in problems that are not related to time series prediction.

####### validmind.tests.model_validation.statsmodels.RegressionModelForecastPlot.logger

```python
logger = get_logger(__name__)
```

###### validmind.tests.model_validation.statsmodels.RegressionModelForecastPlotLevels

**Functions:**

- [**RegressionModelForecastPlotLevels**](#validmind.tests.model_validation.statsmodels.RegressionModelForecastPlotLevels.RegressionModelForecastPlotLevels) – Assesses the alignment between forecasted and observed values in regression models through visual plots
- [**integrate_diff**](#validmind.tests.model_validation.statsmodels.RegressionModelForecastPlotLevels.integrate_diff) –

####### validmind.tests.model_validation.statsmodels.RegressionModelForecastPlotLevels.RegressionModelForecastPlotLevels

```python
RegressionModelForecastPlotLevels(model, dataset)
```

Assesses the alignment between forecasted and observed values in regression models through visual plots

### Purpose

This test aims to visually assess the performance of a regression model by comparing its forecasted values against
the actual observed values for both the raw and transformed (integrated) data. This helps determine the accuracy
of the model and can help identify overfitting or underfitting. The integration is applied to highlight the trend
rather than the absolute level.

### Test Mechanism

This test generates two plots:

- Raw data vs forecast
- Transformed data vs forecast

The transformed data is created by performing a cumulative sum on the raw data.

### Signs of High Risk

- Significant deviation between forecasted and observed values.
- Patterns suggesting overfitting or underfitting.
- Large discrepancies in the plotted forecasts, indicating potential issues with model generalizability and
  precision.

### Strengths

- Provides an intuitive, visual way to assess multiple regression models, aiding in easier interpretation and
  evaluation of forecast accuracy.

### Limitations

- Relies heavily on visual interpretation, which may vary between individuals.
- Does not provide a numerical metric to quantify forecast accuracy, relying solely on visual assessment.

####### validmind.tests.model_validation.statsmodels.RegressionModelForecastPlotLevels.integrate_diff

```python
integrate_diff(series_diff, start_value)
```

###### validmind.tests.model_validation.statsmodels.RegressionModelSensitivityPlot

**Functions:**

- [**RegressionModelSensitivityPlot**](#validmind.tests.model_validation.statsmodels.RegressionModelSensitivityPlot.RegressionModelSensitivityPlot) – Assesses the sensitivity of a regression model to changes in independent variables by applying shocks and
- [**integrate_diff**](#validmind.tests.model_validation.statsmodels.RegressionModelSensitivityPlot.integrate_diff) –

**Attributes:**

- [**logger**](#validmind.tests.model_validation.statsmodels.RegressionModelSensitivityPlot.logger) –

####### validmind.tests.model_validation.statsmodels.RegressionModelSensitivityPlot.RegressionModelSensitivityPlot

```python
RegressionModelSensitivityPlot(
    dataset, model, shocks=[0.1], transformation=None
)
```

Assesses the sensitivity of a regression model to changes in independent variables by applying shocks and
visualizing the impact.

### Purpose

The Regression Sensitivity Plot test is designed to perform sensitivity analysis on regression models. This test
aims to measure the impact of slight changes (shocks) applied to individual variables on the system's outcome while
keeping all other variables constant. By doing so, it analyzes the effects of each independent variable on the
dependent variable within the regression model, helping identify significant risk factors that could substantially
influence the model's output.

### Test Mechanism

This test operates by initially applying shocks of varying magnitudes, defined by specific parameters, to each of
the model's features, one at a time. With all other variables held constant, a new prediction is made for each
dataset subjected to shocks. Any changes in the model's predictions are directly attributed to the shocks applied.
If the transformation parameter is set to "integrate," initial predictions and target values undergo transformation
via an integration function before being plotted. Finally, a plot demonstrating observed values against predicted
values for each model is generated, showcasing a distinct line graph illustrating predictions for each shock.

### Signs of High Risk

- Drastic alterations in model predictions due to minor shocks to an individual variable, indicating high
  sensitivity and potential over-dependence on that variable.
- Unusually high or unpredictable shifts in response to shocks, suggesting potential model instability or
  overfitting.

### Strengths

- Helps identify variables that strongly influence model outcomes, aiding in understanding feature importance.
- Generates visual plots, making results easily interpretable even to non-technical stakeholders.
- Useful in identifying overfitting and detecting unstable models that react excessively to minor variable changes.

### Limitations

- Operates on the assumption that all other variables remain unchanged during the application of a shock, which may
  not reflect real-world interdependencies.
- Best compatible with linear models and may not effectively evaluate the sensitivity of non-linear models.
- Provides a visual representation without a numerical risk measure, potentially introducing subjectivity in
  interpretation.

####### validmind.tests.model_validation.statsmodels.RegressionModelSensitivityPlot.integrate_diff

```python
integrate_diff(series_diff, start_value)
```

####### validmind.tests.model_validation.statsmodels.RegressionModelSensitivityPlot.logger

```python
logger = get_logger(__name__)
```

###### validmind.tests.model_validation.statsmodels.RegressionModelSummary

**Functions:**

- [**RegressionModelSummary**](#validmind.tests.model_validation.statsmodels.RegressionModelSummary.RegressionModelSummary) – Evaluates regression model performance using metrics including R-Squared, Adjusted R-Squared, MSE, and RMSE.

####### validmind.tests.model_validation.statsmodels.RegressionModelSummary.RegressionModelSummary

```python
RegressionModelSummary(dataset, model)
```

Evaluates regression model performance using metrics including R-Squared, Adjusted R-Squared, MSE, and RMSE.

### Purpose

The Regression Model Summary test evaluates the performance of regression models by measuring their predictive
ability regarding dependent variables given changes in the independent variables. It uses conventional regression
metrics such as R-Squared, Adjusted R-Squared, Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) to
assess the model's accuracy and fit.

### Test Mechanism

This test uses the sklearn library to calculate the R-Squared, Adjusted R-Squared, MSE, and RMSE. It outputs a
table with the results of these metrics along with the feature columns used by the model.

### Signs of High Risk

- Low R-Squared and Adjusted R-Squared values.
- High MSE and RMSE values.

### Strengths

- Offers an extensive evaluation of regression models by combining four key measures of model accuracy and fit.
- Provides a comprehensive view of the model's performance.
- Both the R-Squared and Adjusted R-Squared measures are readily interpretable.

### Limitations

- RMSE and MSE might be sensitive to outliers.
- A high R-Squared or Adjusted R-Squared may not necessarily indicate a good model, especially in cases of
  overfitting.

###### validmind.tests.model_validation.statsmodels.RegressionPermutationFeatureImportance

**Functions:**

- [**RegressionPermutationFeatureImportance**](#validmind.tests.model_validation.statsmodels.RegressionPermutationFeatureImportance.RegressionPermutationFeatureImportance) – Assesses the significance of each feature in a model by evaluating the impact on model performance when feature

**Attributes:**

- [**logger**](#validmind.tests.model_validation.statsmodels.RegressionPermutationFeatureImportance.logger) –

####### validmind.tests.model_validation.statsmodels.RegressionPermutationFeatureImportance.RegressionPermutationFeatureImportance

```python
RegressionPermutationFeatureImportance(
    dataset, model, fontsize=12, figure_height=500
)
```

Assesses the significance of each feature in a model by evaluating the impact on model performance when feature
values are randomly rearranged.

### Purpose

The primary purpose of this metric is to determine which features significantly impact the performance of a
regression model developed using statsmodels. The metric measures how much the prediction accuracy deteriorates
when each feature's values are permuted.

### Test Mechanism

This metric shuffles the values of each feature one at a time in the dataset, computes the model's performance
after each permutation, and compares it to the baseline performance. A significant decrease in performance
indicates the importance of the feature.

### Signs of High Risk

- Significant reliance on a feature that, when permuted, leads to a substantial decrease in performance, suggesting
  overfitting or high model dependency on that feature.
- Features identified as unimportant despite known impacts from domain knowledge, suggesting potential issues in
  model training or data preprocessing.

### Strengths

- Directly assesses the impact of each feature on model performance, providing clear insights into model
  dependencies.
- Model-agnostic within the scope of statsmodels, applicable to any regression model that outputs predictions.

### Limitations

- The metric is specific to statsmodels and cannot be used with other types of models without adaptation.
- It does not capture interactions between features, which can lead to underestimating the importance of correlated
  features.
- Assumes independence of features when calculating importance, which might not always hold true.

####### validmind.tests.model_validation.statsmodels.RegressionPermutationFeatureImportance.logger

```python
logger = get_logger(__name__)
```

###### validmind.tests.model_validation.statsmodels.ScorecardHistogram

**Functions:**

- [**ScorecardHistogram**](#validmind.tests.model_validation.statsmodels.ScorecardHistogram.ScorecardHistogram) – The Scorecard Histogram test evaluates the distribution of credit scores between default and non-default instances,

####### validmind.tests.model_validation.statsmodels.ScorecardHistogram.ScorecardHistogram

```python
ScorecardHistogram(dataset, title='Histogram of Scores', score_column='score')
```

The Scorecard Histogram test evaluates the distribution of credit scores between default and non-default instances,
providing critical insights into the performance and generalizability of credit-risk models.

### Purpose

The Scorecard Histogram test metric provides a visual interpretation of the credit scores generated by a machine
learning model for credit-risk classification tasks. It aims to compare the alignment of the model's scoring
decisions with the actual outcomes of credit loan applications. It helps in identifying potential discrepancies
between the model's predictions and real-world risk levels.

### Test Mechanism

This metric uses logistic regression to generate a histogram of credit scores for both default (negative class) and
non-default (positive class) instances. Using both training and test datasets, the metric calculates the credit
score of each instance with a scorecard method, considering the impact of different features on the likelihood of
default. It includes the default point to odds (PDO) scaling factor and predefined target score and odds settings.
Histograms for training and test sets are computed and plotted separately to offer insights into the model's
generalizability to unseen data.

### Signs of High Risk

- Discrepancies between the distributions of training and testing data, indicating a model's poor generalization
  ability
- Skewed distributions favoring specific scores or classes, representing potential bias

### Strengths

- Provides a visual interpretation of the model's credit scoring system, enhancing comprehension of model behavior
- Enables a direct comparison between actual and predicted scores for both training and testing data
- Its intuitive visualization helps understand the model's ability to differentiate between positive and negative
  classes
- Can unveil patterns or anomalies not easily discerned through numerical metrics alone

### Limitations

- Despite its value for visual interpretation, it doesn't quantify the performance of the model and therefore may
  lack precision for thorough model evaluation
- The quality of input data can strongly influence the metric, as bias or noise in the data will affect both the
  score calculation and resultant histogram
- Its specificity to credit scoring models limits its applicability across a wider variety of machine learning
  tasks and models
- The metric's effectiveness is somewhat tied to the subjective interpretation of the analyst, relying on their
  judgment of the characteristics and implications of the plot.

###### validmind.tests.model_validation.statsmodels.statsutils

**Functions:**

- [**adj_r2_score**](#validmind.tests.model_validation.statsmodels.statsutils.adj_r2_score) – Adjusted R2 Score

####### validmind.tests.model_validation.statsmodels.statsutils.adj_r2_score

```python
adj_r2_score(actual, predicted, rowcount, featurecount)
```

Adjusted R2 Score

#### validmind.tests.output

**Classes:**

- [**BooleanOutputHandler**](#validmind.tests.output.BooleanOutputHandler) –
- [**FigureOutputHandler**](#validmind.tests.output.FigureOutputHandler) –
- [**MetricOutputHandler**](#validmind.tests.output.MetricOutputHandler) –
- [**OutputHandler**](#validmind.tests.output.OutputHandler) – Base class for handling different types of test outputs
- [**TableOutputHandler**](#validmind.tests.output.TableOutputHandler) –

**Functions:**

- [**process_output**](#validmind.tests.output.process_output) – Process a single test output item and update the TestResult.

##### validmind.tests.output.BooleanOutputHandler

Bases: <code>[OutputHandler](#validmind.tests.output.OutputHandler)</code>

**Functions:**

- [**can_handle**](#validmind.tests.output.BooleanOutputHandler.can_handle) –
- [**process**](#validmind.tests.output.BooleanOutputHandler.process) –

###### validmind.tests.output.BooleanOutputHandler.can_handle

```python
can_handle(item)
```

###### validmind.tests.output.BooleanOutputHandler.process

```python
process(item, result)
```

##### validmind.tests.output.FigureOutputHandler

Bases: <code>[OutputHandler](#validmind.tests.output.OutputHandler)</code>

**Functions:**

- [**can_handle**](#validmind.tests.output.FigureOutputHandler.can_handle) –
- [**process**](#validmind.tests.output.FigureOutputHandler.process) –

###### validmind.tests.output.FigureOutputHandler.can_handle

```python
can_handle(item)
```

###### validmind.tests.output.FigureOutputHandler.process

```python
process(item, result)
```

##### validmind.tests.output.MetricOutputHandler

Bases: <code>[OutputHandler](#validmind.tests.output.OutputHandler)</code>

**Functions:**

- [**can_handle**](#validmind.tests.output.MetricOutputHandler.can_handle) –
- [**process**](#validmind.tests.output.MetricOutputHandler.process) –

###### validmind.tests.output.MetricOutputHandler.can_handle

```python
can_handle(item)
```

###### validmind.tests.output.MetricOutputHandler.process

```python
process(item, result)
```

##### validmind.tests.output.OutputHandler

Bases: <code>[ABC](#abc.ABC)</code>

Base class for handling different types of test outputs

**Functions:**

- [**can_handle**](#validmind.tests.output.OutputHandler.can_handle) – Check if this handler can process the given item
- [**process**](#validmind.tests.output.OutputHandler.process) – Process the item and update the TestResult

###### validmind.tests.output.OutputHandler.can_handle

```python
can_handle(item)
```

Check if this handler can process the given item

###### validmind.tests.output.OutputHandler.process

```python
process(item, result)
```

Process the item and update the TestResult

##### validmind.tests.output.TableOutputHandler

Bases: <code>[OutputHandler](#validmind.tests.output.OutputHandler)</code>

**Functions:**

- [**can_handle**](#validmind.tests.output.TableOutputHandler.can_handle) –
- [**process**](#validmind.tests.output.TableOutputHandler.process) –

###### validmind.tests.output.TableOutputHandler.can_handle

```python
can_handle(item)
```

###### validmind.tests.output.TableOutputHandler.process

```python
process(item, result)
```

##### validmind.tests.output.process_output

```python
process_output(item, result)
```

Process a single test output item and update the TestResult.

#### validmind.tests.prompt_validation

**Modules:**

- [**Bias**](#validmind.tests.prompt_validation.Bias) –
- [**Clarity**](#validmind.tests.prompt_validation.Clarity) –
- [**Conciseness**](#validmind.tests.prompt_validation.Conciseness) –
- [**Delimitation**](#validmind.tests.prompt_validation.Delimitation) –
- [**NegativeInstruction**](#validmind.tests.prompt_validation.NegativeInstruction) –
- [**Robustness**](#validmind.tests.prompt_validation.Robustness) –
- [**Specificity**](#validmind.tests.prompt_validation.Specificity) –
- [**ai_powered_test**](#validmind.tests.prompt_validation.ai_powered_test) –

##### validmind.tests.prompt_validation.Bias

**Functions:**

- [**Bias**](#validmind.tests.prompt_validation.Bias.Bias) – Assesses potential bias in a Large Language Model by analyzing the distribution and order of exemplars in the

**Attributes:**

- [**SYSTEM**](#validmind.tests.prompt_validation.Bias.SYSTEM) –
- [**USER**](#validmind.tests.prompt_validation.Bias.USER) –

###### validmind.tests.prompt_validation.Bias.Bias

```python
Bias(model, min_threshold=7)
```

Assesses potential bias in a Large Language Model by analyzing the distribution and order of exemplars in the
prompt.

### Purpose

The Bias Evaluation test calculates if and how the order and distribution of exemplars (examples) in a few-shot
learning prompt affect the output of a Large Language Model (LLM). The results of this evaluation can be used to
fine-tune the model's performance and manage any unintended biases in its results.

### Test Mechanism

This test uses two checks:

1. **Distribution of Exemplars:** The number of positive vs. negative examples in a prompt is varied. The test then
   examines the LLM's classification of a neutral or ambiguous statement under these circumstances.
1. **Order of Exemplars:** The sequence in which positive and negative examples are presented to the model is
   modified. Their resultant effect on the LLM's response is studied.

For each test case, the LLM grades the input prompt on a scale of 1 to 10. It evaluates whether the examples in the
prompt could produce biased responses. The test only passes if the score meets or exceeds a predetermined minimum
threshold. This threshold is set at 7 by default but can be modified as per the requirements via the test
parameters.

### Signs of High Risk

- A skewed result favoring either positive or negative responses may suggest potential bias in the model. This skew
  could be caused by an unbalanced distribution of positive and negative exemplars.
- If the score given by the model is less than the set minimum threshold, it might indicate a risk of high bias and
  hence poor performance.

### Strengths

- This test provides a quantitative measure of potential bias, offering clear guidelines for developers about
  whether their Large Language Model (LLM) contains significant bias.
- It is useful in evaluating the impartiality of the model based on the distribution and sequence of examples.
- The flexibility to adjust the minimum required threshold allows tailoring this test to stricter or more lenient
  bias standards.

### Limitations

- The test may not pick up on more subtle forms of bias or biases that are not directly related to the distribution
  or order of exemplars.
- The test's effectiveness will decrease if the quality or balance of positive and negative exemplars is not
  representative of the problem space the model is intended to solve.
- The use of a grading mechanism to gauge bias may not be entirely accurate in every case, particularly when the
  difference between threshold and score is narrow.

###### validmind.tests.prompt_validation.Bias.SYSTEM

````python
SYSTEM = '\nYou are a prompt evaluation AI. You are aware of all prompt engineering best practices and can score prompts based on how well they satisfy different best practices. You analyse the prompts step-by-step based on provided documentation and provide a score and an explanation for how you produced that score.\n\nConsider the following best practice documentation:\n```\nIts been shown that, when passing examples to an LLM via the prompt for the purpose of Sentiment Analysis, a distribution with a majority of positive examples led the LLM to classify ambiguous sentences as "Positive", and vice versa. However, for more straightforward tasks, such as sentiment classification, biases may be harder to induce. The order of presentation also appeared to influence the LLM\'s outputs, especially when combined with a skewed distribution of exemplars.\nTactics for Avoiding Bias in Prompting:\n1. Balanced Distribution: Avoid heavily skewed distributions of examples. Instead, offer amore balanced number of examples for each label.\n2. Randomize Order: To prevent order-induced biases, shuffle the sequence of examples ensuring no fixed pattern, such as presenting all positive examples first.\n3. Continued Experimentation: Regularly test and tweak prompts, especially for complex tasks where the LLM might not have extensive knowledge. This iterative process helps in identifying potential pitfalls and refining prompting strategies.\nExample:\nFor instance, using 8 positive and 2 negative examples led the LLM to classify an ambiguous sentence "I feel something" as "Positive". However, with a more balanced distribution, the LLM showed unbiased behavior.\n```\n\nScore the bias of the user-submitted prompt. Return a score from 1 to 10 where 10 is a perfect score. Also provide a short explanation for your score.\n\nResponse Format:\n```\nScore: <score>\nExplanation: <explanation>\n```\n'.strip()

````

###### validmind.tests.prompt_validation.Bias.USER

```python
USER = '\nPrompt:\n"""\n{prompt_to_test}\n"""\n'.strip()
```

##### validmind.tests.prompt_validation.Clarity

**Functions:**

- [**Clarity**](#validmind.tests.prompt_validation.Clarity.Clarity) – Evaluates and scores the clarity of prompts in a Large Language Model based on specified guidelines.

**Attributes:**

- [**SYSTEM**](#validmind.tests.prompt_validation.Clarity.SYSTEM) –
- [**USER**](#validmind.tests.prompt_validation.Clarity.USER) –

###### validmind.tests.prompt_validation.Clarity.Clarity

```python
Clarity(model, min_threshold=7)
```

Evaluates and scores the clarity of prompts in a Large Language Model based on specified guidelines.

### Purpose

The Clarity evaluation metric is used to assess how clear the prompts of a Large Language Model (LLM) are. This
assessment is particularly important because clear prompts assist the LLM in more accurately interpreting and
responding to instructions.

### Test Mechanism

The evaluation uses an LLM to scrutinize the clarity of prompts, factoring in considerations such as the inclusion
of relevant details, persona adoption, step-by-step instructions, usage of examples, and specification of desired
output length. Each prompt is rated on a clarity scale of 1 to 10, and any prompt scoring at or above the preset
threshold (default of 7) will be marked as clear. It is important to note that this threshold can be adjusted via
test parameters, providing flexibility in the evaluation process.

### Signs of High Risk

- Prompts that consistently score below the clarity threshold
- Repeated failure of prompts to adhere to guidelines for clarity, including detail inclusion, persona adoption,
  explicit step-by-step instructions, use of examples, and specification of output length

### Strengths

- Encourages the development of more effective prompts that aid the LLM in interpreting instructions accurately
- Applies a quantifiable measure (a score from 1 to 10) to evaluate the clarity of prompts
- Threshold for clarity is adjustable, allowing for flexible evaluation depending on the context

### Limitations

- Scoring system is subjective and relies on the AI’s interpretation of 'clarity'
- The test assumes that all required factors (detail inclusion, persona adoption, step-by-step instructions, use of
  examples, and specification of output length) contribute equally to clarity, which might not always be the case
- The evaluation may not be as effective if used on non-textual models

###### validmind.tests.prompt_validation.Clarity.SYSTEM

````python
SYSTEM = "\nYou are a prompt evaluation AI. You are aware of all prompt engineering best practices and can score prompts based on how well they satisfy different metrics. You analyse the prompts step-by-step based on provided documentation and provide a score and an explanation for how you produced that score.\n\nConsider the following documentation on prompt clarity guidelines when evaluating the prompt:\n'''\nClear prompts minimize the room for misinterpretation, allowing the LLM to generate more relevant and accurate responses. Ambiguous or vague instructions might leave the model guessing, leading to suboptimal outputs.\n\nTactics for Ensuring Clarity that will be referenced during evaluation:\n1. Detail Inclusion: Provide essential details or context to prevent the LLM from making assumptions.\n2. Adopt a Persona: Use system messages to specify the desired persona for the LLM's responses.\n3. Specify Steps: For certain tasks, delineate the required steps explicitly, helping the model in sequential understanding.\n4. Provide Examples: While general instructions are efficient, in some scenarios, \"few-shot\" prompting or style examples can guide the LLM more effectively.\n5. Determine Output Length: Define the targeted length of the response, whether in terms of paragraphs, bullet points, or other units. While word counts aren't always precise, specifying formats like paragraphs can offer more predictable results.\n'''\n\nScore the clarity of the user-submitted prompt. Return a score from 1 to 10 where 10 is a perfect score. Also provide a short explanation for your score.\n\nResponse Format:\n```\nScore: <score>\nExplanation: <explanation>\n```\n"

````

###### validmind.tests.prompt_validation.Clarity.USER

```python
USER = "\nPrompt:\n'''\n{prompt_to_test}\n'''\n"
```

##### validmind.tests.prompt_validation.Conciseness

**Functions:**

- [**Conciseness**](#validmind.tests.prompt_validation.Conciseness.Conciseness) – Analyzes and grades the conciseness of prompts provided to a Large Language Model.

**Attributes:**

- [**SYSTEM**](#validmind.tests.prompt_validation.Conciseness.SYSTEM) –
- [**USER**](#validmind.tests.prompt_validation.Conciseness.USER) –

###### validmind.tests.prompt_validation.Conciseness.Conciseness

```python
Conciseness(model, min_threshold=7)
```

Analyzes and grades the conciseness of prompts provided to a Large Language Model.

### Purpose

The Conciseness Assessment is designed to evaluate the brevity and succinctness of prompts provided to a Language
Learning Model (LLM). A concise prompt strikes a balance between offering clear instructions and eliminating
redundant or unnecessary information, ensuring that the LLM receives relevant input without being overwhelmed.

### Test Mechanism

Using an LLM, this test conducts a conciseness analysis on input prompts. The analysis grades the prompt on a scale
from 1 to 10, where the grade reflects how well the prompt delivers clear instructions without being verbose.
Prompts that score equal to or above a predefined threshold (default set to 7) are deemed successfully concise.
This threshold can be adjusted to meet specific requirements.

### Signs of High Risk

- Prompts that consistently score below the predefined threshold.
- Prompts that are overly wordy or contain unnecessary information.
- Prompts that create confusion or ambiguity due to excess or unnecessary information.

### Strengths

- Ensures clarity and effectiveness of the prompts.
- Promotes brevity and preciseness in prompts without sacrificing essential information.
- Useful for models like LLMs, where input prompt length and clarity greatly influence model performance.
- Provides a quantifiable measure of prompt conciseness.

### Limitations

- The conciseness score is based on an AI's assessment, which might not fully capture human interpretation of
  conciseness.
- The predefined threshold for conciseness could be subjective and might need adjustment based on application.
- The test is dependent on the LLM’s understanding of conciseness, which might vary from model to model.

###### validmind.tests.prompt_validation.Conciseness.SYSTEM

````python
SYSTEM = "\nYou are a prompt evaluation AI.\nYou are aware of all prompt engineering best practices and can score prompts based on how well they satisfy different metrics.\nYou analyse the prompts step-by-step based on provided documentation and provide a score and an explanation for how you produced that score.\n\nConsider the following documentation regarding conciseness in prompts and utilize it to grade the user-submitted prompt:\n'''\nWhile detailed prompts can guide an LLM towards accurate results, excessive details can clutter the instruction and potentially lead to undesired outputs.\nConcise prompts are straightforward, reducing ambiguity and focusing the LLM's attention on the primary task.\nThis is especially important considering there are limitations to the length of prompts that can be fed to an LLM.\n\nFor an LLM tasked with summarizing a document, a verbose prompt might introduce unnecessary constraints or biases.\nA concise, effective prompt like:\n\"Provide a brief summary highlighting the main points of the document\"\nensures that the LLM captures the essence of the content without being sidetracked.\n\nFor example this prompt:\n\"The description for this product should be fairly short, a few sentences only, and not too much more.\"\ncould be better written like this:\n\"Use a 3 to 5 sentence paragraph to describe this product.\"\n'''\n\nScore the user-submitted prompt on a scale of 1 to 10, with 10 being the best possible score.\nProvide an explanation for your score.\n\nResponse Format:\n```\nScore: <score>\nExplanation: <explanation>\n```\n"

````

###### validmind.tests.prompt_validation.Conciseness.USER

````python
USER = '\nPrompt:\n```\n{prompt_to_test}\n```\n'
````

##### validmind.tests.prompt_validation.Delimitation

**Functions:**

- [**Delimitation**](#validmind.tests.prompt_validation.Delimitation.Delimitation) – Evaluates the proper use of delimiters in prompts provided to Large Language Models.

**Attributes:**

- [**SYSTEM**](#validmind.tests.prompt_validation.Delimitation.SYSTEM) –
- [**USER**](#validmind.tests.prompt_validation.Delimitation.USER) –

###### validmind.tests.prompt_validation.Delimitation.Delimitation

```python
Delimitation(model, min_threshold=7)
```

Evaluates the proper use of delimiters in prompts provided to Large Language Models.

### Purpose

The Delimitation Test aims to assess whether prompts provided to the Language Learning Model (LLM) correctly use
delimiters to mark different sections of the input. Well-delimited prompts help simplify the interpretation process
for the LLM, ensuring that the responses are precise and accurate.

### Test Mechanism

The test employs an LLM to examine prompts for appropriate use of delimiters such as triple quotation marks, XML
tags, and section titles. Each prompt is assigned a score from 1 to 10 based on its delimitation integrity. Prompts
with scores equal to or above the preset threshold (which is 7 by default, although it can be adjusted as
necessary) pass the test.

### Signs of High Risk

- Prompts missing, improperly placed, or incorrectly used delimiters, leading to misinterpretation by the LLM.
- High-risk scenarios with complex prompts involving multiple tasks or diverse data where correct delimitation is
  crucial.
- Scores below the threshold, indicating a high risk.

### Strengths

- Ensures clarity in demarcating different components of given prompts.
- Reduces ambiguity in understanding prompts, especially for complex tasks.
- Provides a quantified insight into the appropriateness of delimiter usage, aiding continuous improvement.

### Limitations

- Only checks for the presence and placement of delimiters, not whether the correct delimiter type is used for the
  specific data or task.
- May not fully reveal the impacts of poor delimitation on the LLM's final performance.
- The preset score threshold may not be refined enough for complex tasks and prompts, requiring regular manual
  adjustment.

###### validmind.tests.prompt_validation.Delimitation.SYSTEM

````python
SYSTEM = "\nYou are a prompt evaluation AI.\nYou are aware of all prompt engineering best practices and can score prompts based on how well they satisfy different metrics.\nYou analyse the prompts step-by-step based on provided documentation and provide a score and an explanation for how you produced that score.\n\nLLM Prompts that include different sections and user inputs should be properly delimitated.\nIdeally, the prompt should use triple quotes or backticks or at least single quotes around any user input, reference text or code block etc.\nThis is to ensure that the prompt is parsed correctly by the model, different pieces of the prompt are understood as separate and any user-provided inputs are not interpreted as part of the prompt.\nIdentify any issues in the user-submitted prompt and give a score from 1 to 10, where 10 is a perfect score, based on the number and severity of issues.\n\nResponse Format:\n```\nScore: <score>\nExplanation: <explanation>\n```\n"

````

###### validmind.tests.prompt_validation.Delimitation.USER

```python
USER = "\nPrompt:\n'''\n{prompt_to_test}\n'''\n"
```

##### validmind.tests.prompt_validation.NegativeInstruction

**Functions:**

- [**NegativeInstruction**](#validmind.tests.prompt_validation.NegativeInstruction.NegativeInstruction) – Evaluates and grades the use of affirmative, proactive language over negative instructions in LLM prompts.

**Attributes:**

- [**SYSTEM**](#validmind.tests.prompt_validation.NegativeInstruction.SYSTEM) –
- [**USER**](#validmind.tests.prompt_validation.NegativeInstruction.USER) –

###### validmind.tests.prompt_validation.NegativeInstruction.NegativeInstruction

```python
NegativeInstruction(model, min_threshold=7)
```

Evaluates and grades the use of affirmative, proactive language over negative instructions in LLM prompts.

### Purpose

The Negative Instruction test is utilized to scrutinize the prompts given to a Large Language Model (LLM). The
objective is to ensure these prompts are expressed using proactive, affirmative language. The focus is on
instructions indicating what needs to be done rather than what needs to be avoided, thereby guiding the LLM more
efficiently towards the desired output.

### Test Mechanism

An LLM is employed to evaluate each prompt. The prompt is graded based on its use of positive instructions with
scores ranging between 1-10. This grade reflects how effectively the prompt leverages affirmative language while
shying away from negative or restrictive instructions. A prompt that attains a grade equal to or above a
predetermined threshold (7 by default) is regarded as adhering effectively to the best practices of positive
instruction. This threshold can be custom-tailored through the test parameters.

### Signs of High Risk

- Low score obtained from the LLM analysis, indicating heavy reliance on negative instructions in the prompts.
- Failure to surpass the preset minimum threshold.
- The LLM generates ambiguous or undesirable outputs as a consequence of the negative instructions used in the
  prompt.

### Strengths

- Encourages the usage of affirmative, proactive language in prompts, aiding in more accurate and advantageous
  model responses.
- The test result provides a comprehensible score, helping to understand how well a prompt follows the positive
  instruction best practices.

### Limitations

- Despite an adequate score, a prompt could still be misleading or could lead to undesired responses due to factors
  not covered by this test.
- The test necessitates an LLM for evaluation, which might not be available or feasible in certain scenarios.
- A numeric scoring system, while straightforward, may oversimplify complex issues related to prompt designing and
  instruction clarity.
- The effectiveness of the test hinges significantly on the predetermined threshold level, which can be subjective
  and may need to be adjusted according to specific use-cases.

###### validmind.tests.prompt_validation.NegativeInstruction.SYSTEM

````python
SYSTEM = "\nYou are a prompt evaluation AI.\nYou are aware of all prompt engineering best practices and can score prompts based on how well they satisfy different metrics.\nYou analyse the prompts step-by-step based on provided documentation and provide a score and an explanation for how you produced that score.\n\nConsider the following documentation regarding negative instructions in prompts and utilize it to grade the user-submitted prompt:\n'''\nBest practices for LLM prompt engineering suggest that positive instructions should be preferred over negative instructions.\nFor example, instead of saying \"Don't do X\", it is better to say \"Do Y\".\nThis is because the model is more likely to generate the desired output if it is given a positive instruction.\nPrompts that are phrased in the affirmative, emphasizing what to do, tend to direct the LLM more clearly than those that focus on what not to do.\nNegative instructions can lead to ambiguities and undesired model responses.\nBy emphasizing clarity and proactive guidance, we optimize the chances of obtaining relevant and targeted responses from the LLM.\n\nExample:\nConsider a scenario involving a chatbot designed to recommend movies.\nAn instruction framed as, \"Don't recommend movies that are horror or thriller\", might cause the LLM to fixate on the genres mentioned,inadvertently producing undesired results.\nOn the other hand, a positively-framed prompt like, \"Recommend family-friendly movies or romantic comedies\" provides clear guidance on the desired output.\n'''\n\nBased on this best practice, please score the user-submitted prompt on a scale of 1-10, where 10 is a perfect score.\nProvide an explanation for your score.\n\nResponse Format:\n```\nScore: <score>\nExplanation: <explanation>\n```\n"

````

###### validmind.tests.prompt_validation.NegativeInstruction.USER

```python
USER = "\nPrompt:\n'''\n{prompt_to_test}\n'''\n"
```

##### validmind.tests.prompt_validation.Robustness

**Functions:**

- [**Robustness**](#validmind.tests.prompt_validation.Robustness.Robustness) – Assesses the robustness of prompts provided to a Large Language Model under varying conditions and contexts. This test

**Attributes:**

- [**SYSTEM**](#validmind.tests.prompt_validation.Robustness.SYSTEM) –
- [**USER**](#validmind.tests.prompt_validation.Robustness.USER) –

###### validmind.tests.prompt_validation.Robustness.Robustness

```python
Robustness(model, dataset, num_tests=10)
```

Assesses the robustness of prompts provided to a Large Language Model under varying conditions and contexts. This test
specifically measures the model's ability to generate correct classifications with the given prompt even when the
inputs are edge cases or otherwise difficult to classify.

### Purpose

The Robustness test is meant to evaluate the resilience and reliability of prompts provided to a Language Learning
Model (LLM). The aim of this test is to guarantee that the prompts consistently generate accurate and expected
outputs, even in diverse or challenging scenarios. This test is only applicable to LLM-powered text classification
tasks where the prompt has a single input variable.

### Test Mechanism

The Robustness test appraises prompts under various conditions, alterations, and contexts to ascertain their
stability in producing consistent responses from the LLM. Factors evaluated include different phrasings, inclusion
of potential distracting elements, and various input complexities. By default, the test generates 10 inputs for a
prompt but can be adjusted according to test parameters.

### Signs of High Risk

- If the output from the tests diverges extensively from the expected results, this indicates high risk.
- When the prompt doesn't give a consistent performance across various tests.
- A high risk is indicated when the prompt is susceptible to breaking, especially when the output is expected to be
  of a specific type.

### Strengths

- The robustness test helps to ensure stable performance of the LLM prompts and lowers the chances of generating
  unexpected or off-target outputs.
- This test is vital for applications where predictability and reliability of the LLM’s output are crucial.

### Limitations

- Currently, the test only supports single-variable prompts, which restricts its application to more complex models.
- When there are too many target classes (over 10), the test is skipped, which can leave potential vulnerabilities
  unchecked in complex multi-class models.
- The test may not account for all potential conditions or alterations that could show up in practical use
  scenarios.

###### validmind.tests.prompt_validation.Robustness.SYSTEM

````python
SYSTEM = "\nYou are a prompt evaluation researcher AI who is tasked with testing the robustness of LLM prompts.\n\nConsider the following guidelines:\n'''\nLLM prompts are used to guide a model to generate specific outputs or solve specific tasks.\nThese prompts can be more or less robust, meaning that they can be more or less susceptible to breaking especially when the output needs to be a specific type.\nA robust prompt ensures consistent performance and reduces the likelihood of unexpected or off-tangent outputs.\nThis consistency is vital for applications where predictability and reliability of the LLM's response are paramount.\n'''\n\nConsider the user-submitted prompt template and generate an input for the variable in the template (denoted by brackets) that tests the robustness of the prompt.\nContradictions, edge cases, typos, bad phrasing, distracting, complex or out-of-place words and phrases are just some of the strategies you can use when generating inputs.\nBe creative and think step-by-step how you would break the prompt.\nThen generate {num_tests} inputs for the user-submitted prompt template that would break the prompt.\nEach input should be different from the others.\nEach input should be retured as a new line in your response.\nRespond only with the values to be inserted into the prompt template and do not include quotes, explanations or any extra text.\n\nExample:\n\nUser-provided prompt:\n```\nAnalyse the following sentence and output its sentiment:\n\\{sentence\\}\n```\n\nYour response (generated inputs):\n```\nI am a happy cat\nYou are a bad person\nMy name is bob\nJames' friend is really sick\n```\n"

````

###### validmind.tests.prompt_validation.Robustness.USER

````python
USER = '\nPrompt:\n```\n{prompt_to_test}\n```\nInput:\n'
````

##### validmind.tests.prompt_validation.Specificity

**Functions:**

- [**Specificity**](#validmind.tests.prompt_validation.Specificity.Specificity) – Evaluates and scores the specificity of prompts provided to a Large Language Model (LLM), based on clarity, detail,

**Attributes:**

- [**SYSTEM**](#validmind.tests.prompt_validation.Specificity.SYSTEM) –
- [**USER**](#validmind.tests.prompt_validation.Specificity.USER) –

###### validmind.tests.prompt_validation.Specificity.SYSTEM

````python
SYSTEM = "\nYou are a prompt evaluation AI.\nYou are aware of all prompt engineering best practices and can score prompts based on how well they satisfy different metrics.\nYou analyse the prompts step-by-step based on provided documentation and provide a score and an explanation for how you produced that score.\n\nConsider the following documentation regarding specificity in prompts and utilize it to grade the user-submitted prompt:\n```\nPrompts that are detailed and descriptive often yield better and more accurate results from an LLM.\nRather than relying on specific keywords or tokens, it's crucial to have a well-structured and descriptive prompt.\nIncluding relevant examples within the prompt can be particularly effective, guiding the LLM to produce outputs in desired formats.\nHowever, it's essential to strike a balance. While prompts need to be detailed, they shouldn't be overloaded with unnecessary information.\nThe emphasis should always be on relevancy and conciseness, considering there are limitations to how long a prompt can be.\n\nExample:\nImagine wanting an LLM to extract specific details from a given text.\nA vague prompt might yield varied results.\nHowever, with a prompt like, \"Extract the names of all characters and the cities they visited from the text\", the LLM is guided more precisely towards the desired information extraction.\n```\n\nScore the specificity of the user-submitted prompt.\nReturn a score from 1 to 10 where 10 is a perfect score.\nAlso provide a short explanation for your score.\n\nResponse Format:\n```\nScore: <score>\nExplanation: <explanation>\n```\n"

````

###### validmind.tests.prompt_validation.Specificity.Specificity

```python
Specificity(model, min_threshold=7)
```

Evaluates and scores the specificity of prompts provided to a Large Language Model (LLM), based on clarity, detail,
and relevance.

### Purpose

The Specificity Test evaluates the clarity, precision, and effectiveness of the prompts provided to a Language
Model (LLM). It aims to ensure that the instructions embedded in a prompt are indisputably clear and relevant,
thereby helping to remove ambiguity and steer the LLM towards desired outputs. This level of specificity
significantly affects the accuracy and relevance of LLM outputs.

### Test Mechanism

The Specificity Test employs an LLM to grade each prompt based on clarity, detail, and relevance parameters within
a specificity scale that extends from 1 to 10. On this scale, prompts scoring equal to or more than a predefined
threshold (set to 7 by default) pass the evaluation, while those scoring below this threshold fail it. Users can
adjust this threshold as per their requirements.

### Signs of High Risk

- Prompts scoring consistently below the established threshold
- Vague or ambiguous prompts that do not provide clear direction to the LLM
- Overly verbose prompts that may confuse the LLM instead of providing clear guidance

### Strengths

- Enables precise and clear communication with the LLM to achieve desired outputs
- Serves as a crucial means to measure the effectiveness of prompts
- Highly customizable, allowing users to set their threshold based on specific use cases

### Limitations

- This test doesn't consider the content comprehension capability of the LLM
- High specificity score doesn't guarantee a high-quality response from the LLM, as the model's performance is also
  dependent on various other factors
- Striking a balance between specificity and verbosity can be challenging, as overly detailed prompts might confuse
  or mislead the model

###### validmind.tests.prompt_validation.Specificity.USER

```python
USER = "\nPrompt:\n'''\n{prompt_to_test}\n'''\n"
```

##### validmind.tests.prompt_validation.ai_powered_test

**Functions:**

- [**call_model**](#validmind.tests.prompt_validation.ai_powered_test.call_model) – Call LLM with the given prompts and return the response
- [**get_explanation**](#validmind.tests.prompt_validation.ai_powered_test.get_explanation) – Get just the explanation from the response string
- [**get_score**](#validmind.tests.prompt_validation.ai_powered_test.get_score) – Get just the score from the response string

**Attributes:**

- [**missing_prompt_message**](#validmind.tests.prompt_validation.ai_powered_test.missing_prompt_message) –

###### validmind.tests.prompt_validation.ai_powered_test.call_model

```python
call_model(system_prompt, user_prompt, temperature=0.0, seed=42)
```

Call LLM with the given prompts and return the response

###### validmind.tests.prompt_validation.ai_powered_test.get_explanation

```python
get_explanation(response)
```

Get just the explanation from the response string
TODO: use json response mode instead of this

```
e.g. "Score: 8
```

Explanation: <some-explanation>" -> "<some-explanation>"

###### validmind.tests.prompt_validation.ai_powered_test.get_score

```python
get_score(response)
```

Get just the score from the response string
TODO: use json response mode instead of this

```
e.g. "Score: 8
```

Explanation: <some-explanation>" -> 8

###### validmind.tests.prompt_validation.ai_powered_test.missing_prompt_message

```python
missing_prompt_message = '\nCannot run prompt validation tests on a model with no prompt.\nYou can set a prompt when creating a vm_model object like this:\nmy_vm_model = vm.init_model(\n    predict_fn=call_model,\n    prompt=Prompt(\n        template="<your-prompt-here>",\n        variables=[],\n    ),\n    input_id="my_llm_model",\n)\n'

```

#### validmind.tests.register_test_provider

```python
register_test_provider(namespace, test_provider)
```

Register an external test provider

**Parameters:**

- **namespace** (<code>[str](#str)</code>) – The namespace of the test provider
- **test_provider** (<code>[TestProvider](#validmind.tests.test_providers.TestProvider)</code>) – The test provider

#### validmind.tests.run

**Functions:**

- [**build_test_result**](#validmind.tests.run.build_test_result) – Build a TestResult object from a set of raw test function outputs
- [**run_test**](#validmind.tests.run.run_test) – Run a ValidMind or custom test

**Attributes:**

- [**logger**](#validmind.tests.run.logger) –

##### validmind.tests.run.build_test_result

```python
build_test_result(
    outputs,
    test_id,
    inputs,
    params,
    description,
    generate_description=True,
    title=None,
)
```

Build a TestResult object from a set of raw test function outputs

##### validmind.tests.run.logger

```python
logger = get_logger(__name__)
```

##### validmind.tests.run.run_test

```python
run_test(
    test_id=None,
    name=None,
    unit_metrics=None,
    inputs=None,
    input_grid=None,
    params=None,
    param_grid=None,
    show=True,
    generate_description=True,
    title=None,
    **kwargs
)
```

Run a ValidMind or custom test

This function is the main entry point for running tests. It can run simple unit metrics,
ValidMind and custom tests, composite tests made up of multiple unit metrics and comparison
tests made up of multiple tests.

**Parameters:**

- **test_id** (<code>[TestID](#validmind.tests.__types__.TestID)</code>) – Test ID to run. Not required if `name` and `unit_metrics` provided.
- **params** (<code>[dict](#dict)</code>) – Parameters to customize test behavior. See test details for available parameters.
- **param_grid** (<code>[Union](#typing.Union)\[[Dict](#typing.Dict)\[[str](#str), [List](#typing.List)\[[Any](#typing.Any)\]\], [List](#typing.List)\[[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]\]\]</code>) – For comparison tests, either:
- Dict mapping parameter names to lists of values (creates Cartesian product)
- List of parameter dictionaries to test
- **inputs** (<code>[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]</code>) – Test inputs (models/datasets initialized with vm.init_model/dataset)
- **input_grid** (<code>[Union](#typing.Union)\[[Dict](#typing.Dict)\[[str](#str), [List](#typing.List)\[[Any](#typing.Any)\]\], [List](#typing.List)\[[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]\]\]</code>) – For comparison tests, either:
- Dict mapping input names to lists of values (creates Cartesian product)
- List of input dictionaries to test
- **name** (<code>[str](#str)</code>) – Test name (required for composite metrics)
- **unit_metrics** (<code>[list](#list)</code>) – Unit metric IDs to run as composite metric
- **show** (<code>[bool](#bool)</code>) – Whether to display results. Defaults to True.
- **generate_description** (<code>[bool](#bool)</code>) – Whether to generate a description. Defaults to True.
- **title** (<code>[str](#str)</code>) – Custom title for the test result

**Returns:**

- **TestResult** (<code>[TestResult](#validmind.vm_models.result.TestResult)</code>) – A TestResult object containing the test results

**Raises:**

- <code>[ValueError](#ValueError)</code> – If the test inputs are invalid
- <code>[LoadTestError](#validmind.errors.LoadTestError)</code> – If the test class fails to load

#### validmind.tests.run_test

```python
run_test(
    test_id=None,
    name=None,
    unit_metrics=None,
    inputs=None,
    input_grid=None,
    params=None,
    param_grid=None,
    show=True,
    generate_description=True,
    title=None,
    **kwargs
)
```

Run a ValidMind or custom test

This function is the main entry point for running tests. It can run simple unit metrics,
ValidMind and custom tests, composite tests made up of multiple unit metrics and comparison
tests made up of multiple tests.

**Parameters:**

- **test_id** (<code>[TestID](#validmind.tests.__types__.TestID)</code>) – Test ID to run. Not required if `name` and `unit_metrics` provided.
- **params** (<code>[dict](#dict)</code>) – Parameters to customize test behavior. See test details for available parameters.
- **param_grid** (<code>[Union](#typing.Union)\[[Dict](#typing.Dict)\[[str](#str), [List](#typing.List)\[[Any](#typing.Any)\]\], [List](#typing.List)\[[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]\]\]</code>) – For comparison tests, either:
- Dict mapping parameter names to lists of values (creates Cartesian product)
- List of parameter dictionaries to test
- **inputs** (<code>[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]</code>) – Test inputs (models/datasets initialized with vm.init_model/dataset)
- **input_grid** (<code>[Union](#typing.Union)\[[Dict](#typing.Dict)\[[str](#str), [List](#typing.List)\[[Any](#typing.Any)\]\], [List](#typing.List)\[[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]\]\]</code>) – For comparison tests, either:
- Dict mapping input names to lists of values (creates Cartesian product)
- List of input dictionaries to test
- **name** (<code>[str](#str)</code>) – Test name (required for composite metrics)
- **unit_metrics** (<code>[list](#list)</code>) – Unit metric IDs to run as composite metric
- **show** (<code>[bool](#bool)</code>) – Whether to display results. Defaults to True.
- **generate_description** (<code>[bool](#bool)</code>) – Whether to generate a description. Defaults to True.
- **title** (<code>[str](#str)</code>) – Custom title for the test result

**Returns:**

- **TestResult** (<code>[TestResult](#validmind.vm_models.result.TestResult)</code>) – A TestResult object containing the test results

**Raises:**

- <code>[ValueError](#ValueError)</code> – If the test inputs are invalid
- <code>[LoadTestError](#validmind.errors.LoadTestError)</code> – If the test class fails to load

#### validmind.tests.tags

```python
tags(*tags)
```

Decorator for specifying tags for a test.

**Parameters:**

- \***tags** – The tags to apply to the test.

#### validmind.tests.tasks

```python
tasks(*tasks)
```

Decorator for specifying the task types that a test is designed for.

**Parameters:**

- \***tasks** – The task types that the test is designed for.

#### validmind.tests.test

```python
test(func_or_id)
```

Decorator for creating and registering custom tests

This decorator registers the function it wraps as a test function within ValidMind
under the provided ID. Once decorated, the function can be run using the
`validmind.tests.run_test` function.

The function can take two different types of arguments:

- Inputs: ValidMind model or dataset (or list of models/datasets). These arguments
  must use the following names: `model`, `models`, `dataset`, `datasets`.
- Parameters: Any additional keyword arguments of any type (must have a default
  value) that can have any name.

The function should return one of the following types:

- Table: Either a list of dictionaries or a pandas DataFrame
- Plot: Either a matplotlib figure or a plotly figure
- Scalar: A single number (int or float)
- Boolean: A single boolean value indicating whether the test passed or failed

The function may also include a docstring. This docstring will be used and logged
as the metric's description.

**Parameters:**

- **func** – The function to decorate
- **test_id** – The identifier for the metric. If not provided, the function name is used.

**Returns:**

- – The decorated function.

#### validmind.tests.test_providers

**Classes:**

- [**LocalTestProvider**](#validmind.tests.test_providers.LocalTestProvider) – Test providers in ValidMind are responsible for loading tests from different sources,
- [**TestProvider**](#validmind.tests.test_providers.TestProvider) – Protocol for user-defined test providers
- [**ValidMindTestProvider**](#validmind.tests.test_providers.ValidMindTestProvider) – Test provider for ValidMind tests

**Attributes:**

- [**logger**](#validmind.tests.test_providers.logger) –

##### validmind.tests.test_providers.LocalTestProvider

```python
LocalTestProvider(root_folder)
```

Test providers in ValidMind are responsible for loading tests from different sources,
such as local files, databases, or remote services. The LocalTestProvider specifically
loads tests from the local file system.

To use the LocalTestProvider, you need to provide the root_folder, which is the
root directory for local tests. The test_id is a combination of the namespace (set
when registering the test provider) and the path to the test class module, where
slashes are replaced by dots and the .py extension is left out.

Example usage:

```
# Create an instance of LocalTestProvider with the root folder
test_provider = LocalTestProvider("/path/to/tests/folder")

# Register the test provider with a namespace
register_test_provider("my_namespace", test_provider)

# List all tests in the namespace (returns a list of test IDs)
test_provider.list_tests()
# this is used by the validmind.tests.list_tests() function to aggregate all tests
# from all test providers

# Load a test using the test_id (namespace + path to test class module)
test = test_provider.load_test("my_namespace.my_test_class")
# full path to the test class module is /path/to/tests/folder/my_test_class.py
```

**Attributes:**

- [**root_folder**](#validmind.tests.test_providers.LocalTestProvider.root_folder) (<code>[str](#str)</code>) – The root directory for local tests.

**Functions:**

- [**list_tests**](#validmind.tests.test_providers.LocalTestProvider.list_tests) – List all tests in the given namespace
- [**load_test**](#validmind.tests.test_providers.LocalTestProvider.load_test) – Load the test identified by the given test_id.

**Attributes:**

- [**root_folder**](#validmind.tests.test_providers.LocalTestProvider.root_folder) –

Initialize the LocalTestProvider with the given root_folder
(see class docstring for details)

**Parameters:**

- **root_folder** (<code>[str](#str)</code>) – The root directory for local tests.

###### validmind.tests.test_providers.LocalTestProvider.list_tests

```python
list_tests()
```

List all tests in the given namespace

**Returns:**

- **list** – A list of test IDs

###### validmind.tests.test_providers.LocalTestProvider.load_test

```python
load_test(test_id)
```

Load the test identified by the given test_id.

**Parameters:**

- **test_id** (<code>[str](#str)</code>) – The identifier of the test. This corresponds to the relative

**Returns:**

- – The test class that matches the last part of the test_id.

**Raises:**

- <code>[LocalTestProviderLoadModuleError](#LocalTestProviderLoadModuleError)</code> – If the test module cannot be imported
- <code>[LocalTestProviderLoadTestError](#LocalTestProviderLoadTestError)</code> – If the test class cannot be found in the module

###### validmind.tests.test_providers.LocalTestProvider.root_folder

```python
root_folder = os.path.abspath(root_folder)
```

##### validmind.tests.test_providers.TestProvider

Bases: <code>[Protocol](#typing.Protocol)</code>

Protocol for user-defined test providers

**Functions:**

- [**list_tests**](#validmind.tests.test_providers.TestProvider.list_tests) – List all tests in the given namespace
- [**load_test**](#validmind.tests.test_providers.TestProvider.load_test) – Load the test function identified by the given test_id

###### validmind.tests.test_providers.TestProvider.list_tests

```python
list_tests()
```

List all tests in the given namespace

**Returns:**

- **list** (<code>[List](#typing.List)\[[str](#str)\]</code>) – A list of test IDs

###### validmind.tests.test_providers.TestProvider.load_test

```python
load_test(test_id)
```

Load the test function identified by the given test_id

**Parameters:**

- **test_id** (<code>[str](#str)</code>) – The test ID (does not contain the namespace under which
  the test is registered)

**Returns:**

- **callable** (<code>[callable](#callable)</code>) – The test function

**Raises:**

- <code>[FileNotFoundError](#FileNotFoundError)</code> – If the test is not found

##### validmind.tests.test_providers.ValidMindTestProvider

```python
ValidMindTestProvider()
```

Test provider for ValidMind tests

**Functions:**

- [**list_tests**](#validmind.tests.test_providers.ValidMindTestProvider.list_tests) – List all tests in the ValidMind test provider
- [**load_test**](#validmind.tests.test_providers.ValidMindTestProvider.load_test) – Load a ValidMind test or unit metric

**Attributes:**

- [**metrics_provider**](#validmind.tests.test_providers.ValidMindTestProvider.metrics_provider) –
- [**tests_provider**](#validmind.tests.test_providers.ValidMindTestProvider.tests_provider) –

###### validmind.tests.test_providers.ValidMindTestProvider.list_tests

```python
list_tests()
```

List all tests in the ValidMind test provider

###### validmind.tests.test_providers.ValidMindTestProvider.load_test

```python
load_test(test_id)
```

Load a ValidMind test or unit metric

###### validmind.tests.test_providers.ValidMindTestProvider.metrics_provider

```python
metrics_provider = LocalTestProvider(
    os.path.join(os.path.dirname(__file__), "..", "unit_metrics")
)

```

###### validmind.tests.test_providers.ValidMindTestProvider.tests_provider

```python
tests_provider = LocalTestProvider(os.path.dirname(__file__))
```

##### validmind.tests.test_providers.logger

```python
logger = get_logger(__name__)
```

### validmind.unit_metrics

**Functions:**

- [**describe_metric**](#validmind.unit_metrics.describe_metric) – Describe a metric
- [**list_metrics**](#validmind.unit_metrics.list_metrics) – List all metrics
- [**run_metric**](#validmind.unit_metrics.run_metric) – Run a metric

#### validmind.unit_metrics.describe_metric

```python
describe_metric(metric_id, **kwargs)
```

Describe a metric

#### validmind.unit_metrics.list_metrics

```python
list_metrics(**kwargs)
```

List all metrics

#### validmind.unit_metrics.run_metric

```python
run_metric(metric_id, **kwargs)
```

Run a metric

### validmind.utils

**Classes:**

- [**NumpyEncoder**](#validmind.utils.NumpyEncoder) –

**Functions:**

- [**display**](#validmind.utils.display) – Display widgets with extra goodies (syntax highlighting, MathJax, etc.)
- [**format_dataframe**](#validmind.utils.format_dataframe) – Format a pandas DataFrame for display purposes
- [**format_key_values**](#validmind.utils.format_key_values) – Round the values on each dict's value to a given number of decimal places.
- [**format_number**](#validmind.utils.format_number) – Format a number for display purposes. If the number is a float, round it
- [**format_records**](#validmind.utils.format_records) – Round the values on each dataframe's column to a given number of decimal places.
- [**fuzzy_match**](#validmind.utils.fuzzy_match) – Check if a string matches another string using fuzzy matching
- [**get_dataset_info**](#validmind.utils.get_dataset_info) – Attempts to extract all dataset info from a dataset object instance
- [**get_full_typename**](#validmind.utils.get_full_typename) – We determine types based on type names so we don't have to import
- [**get_model_info**](#validmind.utils.get_model_info) – Attempts to extract all model info from a model object instance
- [**inspect_obj**](#validmind.utils.inspect_obj) –
- [**is_matplotlib_typename**](#validmind.utils.is_matplotlib_typename) –
- [**is_notebook**](#validmind.utils.is_notebook) – Checks if the code is running in a Jupyter notebook or IPython shell
- [**is_plotly_typename**](#validmind.utils.is_plotly_typename) –
- [**md_to_html**](#validmind.utils.md_to_html) – Converts Markdown to HTML using mistune with plugins
- [**nan_to_none**](#validmind.utils.nan_to_none) –
- [**precision_and_scale**](#validmind.utils.precision_and_scale) – https://stackoverflow.com/questions/3018758/determine-precision-and-scale-of-particular-number-in-python
- [**preview_test_config**](#validmind.utils.preview_test_config) –
- [**run_async**](#validmind.utils.run_async) – Helper function to run functions asynchronously
- [**run_async_check**](#validmind.utils.run_async_check) – Helper function to run functions asynchronously if the task doesn't already exist
- [**summarize_data_quality_results**](#validmind.utils.summarize_data_quality_results) – TODO: generalize this to work with metrics and test results
- [**test_id_to_name**](#validmind.utils.test_id_to_name) – Convert a test ID to a human-readable name.

**Attributes:**

- [**DEFAULT_BIG_NUMBER_DECIMALS**](#validmind.utils.DEFAULT_BIG_NUMBER_DECIMALS) –
- [**DEFAULT_SMALL_NUMBER_DECIMALS**](#validmind.utils.DEFAULT_SMALL_NUMBER_DECIMALS) –
- [**logger**](#validmind.utils.logger) –
- [**params**](#validmind.utils.params) –

#### validmind.utils.DEFAULT_BIG_NUMBER_DECIMALS

```python
DEFAULT_BIG_NUMBER_DECIMALS = 2
```

#### validmind.utils.DEFAULT_SMALL_NUMBER_DECIMALS

```python
DEFAULT_SMALL_NUMBER_DECIMALS = 4
```

#### validmind.utils.NumpyEncoder

```python
NumpyEncoder(*args, **kwargs)
```

Bases: <code>[JSONEncoder](#json.JSONEncoder)</code>

**Functions:**

- [**default**](#validmind.utils.NumpyEncoder.default) –
- [**encode**](#validmind.utils.NumpyEncoder.encode) –
- [**handle_generic_object**](#validmind.utils.NumpyEncoder.handle_generic_object) –
- [**is_datetime**](#validmind.utils.NumpyEncoder.is_datetime) –
- [**is_generic_object**](#validmind.utils.NumpyEncoder.is_generic_object) –
- [**is_numpy_bool**](#validmind.utils.NumpyEncoder.is_numpy_bool) –
- [**is_numpy_floating**](#validmind.utils.NumpyEncoder.is_numpy_floating) –
- [**is_numpy_integer**](#validmind.utils.NumpyEncoder.is_numpy_integer) –
- [**is_numpy_ndarray**](#validmind.utils.NumpyEncoder.is_numpy_ndarray) –
- [**is_pandas_interval**](#validmind.utils.NumpyEncoder.is_pandas_interval) –
- [**is_pandas_timestamp**](#validmind.utils.NumpyEncoder.is_pandas_timestamp) –
- [**is_quantlib_date**](#validmind.utils.NumpyEncoder.is_quantlib_date) –
- [**is_set**](#validmind.utils.NumpyEncoder.is_set) –
- [**iterencode**](#validmind.utils.NumpyEncoder.iterencode) –

**Attributes:**

- [**type_handlers**](#validmind.utils.NumpyEncoder.type_handlers) –

##### validmind.utils.NumpyEncoder.default

```python
default(obj)
```

##### validmind.utils.NumpyEncoder.encode

```python
encode(obj)
```

##### validmind.utils.NumpyEncoder.handle_generic_object

```python
handle_generic_object(obj)
```

##### validmind.utils.NumpyEncoder.is_datetime

```python
is_datetime(obj)
```

##### validmind.utils.NumpyEncoder.is_generic_object

```python
is_generic_object(obj)
```

##### validmind.utils.NumpyEncoder.is_numpy_bool

```python
is_numpy_bool(obj)
```

##### validmind.utils.NumpyEncoder.is_numpy_floating

```python
is_numpy_floating(obj)
```

##### validmind.utils.NumpyEncoder.is_numpy_integer

```python
is_numpy_integer(obj)
```

##### validmind.utils.NumpyEncoder.is_numpy_ndarray

```python
is_numpy_ndarray(obj)
```

##### validmind.utils.NumpyEncoder.is_pandas_interval

```python
is_pandas_interval(obj)
```

##### validmind.utils.NumpyEncoder.is_pandas_timestamp

```python
is_pandas_timestamp(obj)
```

##### validmind.utils.NumpyEncoder.is_quantlib_date

```python
is_quantlib_date(obj)
```

##### validmind.utils.NumpyEncoder.is_set

```python
is_set(obj)
```

##### validmind.utils.NumpyEncoder.iterencode

```python
iterencode(obj, _one_shot=...)
```

##### validmind.utils.NumpyEncoder.type_handlers

```python
type_handlers = {
    self.is_datetime: lambda obj: obj.isoformat(),
    self.is_pandas_interval: lambda obj: f"[{obj.left}, {obj.right}]",
    self.is_numpy_integer: lambda obj: int(obj),
    self.is_numpy_floating: lambda obj: float(obj),
    self.is_numpy_ndarray: lambda obj: obj.tolist(),
    self.is_numpy_bool: lambda obj: bool(obj),
    self.is_pandas_timestamp: lambda obj: str(obj),
    self.is_set: lambda obj: list(obj),
    self.is_quantlib_date: lambda obj: obj.ISO(),
    self.is_generic_object: self.handle_generic_object,
}

```

#### validmind.utils.display

```python
display(widget_or_html, syntax_highlighting=True, mathjax=True)
```

Display widgets with extra goodies (syntax highlighting, MathJax, etc.)

#### validmind.utils.format_dataframe

```python
format_dataframe(df)
```

Format a pandas DataFrame for display purposes

#### validmind.utils.format_key_values

```python
format_key_values(key_values)
```

Round the values on each dict's value to a given number of decimal places.

We do this for display purposes before sending data to ValidMind. Rules:

- Assume the dict is in this form: {key1: value1, key2: value2, ...}
- Check if we are rendering "big" numbers greater than 10 or just numbers between 0 and 1
- If the column's smallest number has more decimals 6, use that number's precision
  so we can avoid rendering a 0 instead
- If the column's smallest number has less decimals than 6, use 6 decimal places

#### validmind.utils.format_number

```python
format_number(number)
```

Format a number for display purposes. If the number is a float, round it
to 4 decimal places.

#### validmind.utils.format_records

```python
format_records(df)
```

Round the values on each dataframe's column to a given number of decimal places.
The returned value is converted to a dict in "records" with Pandas's to_dict() function.

We do this for display purposes before sending data to ValidMind. Rules:

- Check if we are rendering "big" numbers greater than 10 or just numbers between 0 and 1
- If the column's smallest number has more decimals 6, use that number's precision
  so we can avoid rendering a 0 instead
- If the column's smallest number has less decimals than 6, use 6 decimal places

#### validmind.utils.fuzzy_match

```python
fuzzy_match(string, search_string, threshold=0.7)
```

Check if a string matches another string using fuzzy matching

**Parameters:**

- **string** (<code>[str](#str)</code>) – The string to check
- **search_string** (<code>[str](#str)</code>) – The string to search for
- **threshold** (<code>[float](#float)</code>) – The similarity threshold to use (Default: 0.7)

**Returns:**

- – True if the string matches the search string, False otherwise

#### validmind.utils.get_dataset_info

```python
get_dataset_info(dataset)
```

Attempts to extract all dataset info from a dataset object instance

#### validmind.utils.get_full_typename

```python
get_full_typename(o)
```

We determine types based on type names so we don't have to import
(and therefore depend on) PyTorch, TensorFlow, etc.

#### validmind.utils.get_model_info

```python
get_model_info(model)
```

Attempts to extract all model info from a model object instance

#### validmind.utils.inspect_obj

```python
inspect_obj(obj)
```

#### validmind.utils.is_matplotlib_typename

```python
is_matplotlib_typename(typename)
```

#### validmind.utils.is_notebook

```python
is_notebook()
```

Checks if the code is running in a Jupyter notebook or IPython shell

https://stackoverflow.com/questions/15411967/how-can-i-check-if-code-is-executed-in-the-ipython-notebook

#### validmind.utils.is_plotly_typename

```python
is_plotly_typename(typename)
```

#### validmind.utils.logger

```python
logger = get_logger(__name__)
```

#### validmind.utils.md_to_html

```python
md_to_html(md, mathml=False)
```

Converts Markdown to HTML using mistune with plugins

#### validmind.utils.nan_to_none

```python
nan_to_none(obj)
```

#### validmind.utils.params

```python
params = {
    "legend.fontsize": "x-large",
    "axes.labelsize": "x-large",
    "axes.titlesize": "x-large",
    "xtick.labelsize": "x-large",
    "ytick.labelsize": "x-large",
}

```

#### validmind.utils.precision_and_scale

```python
precision_and_scale(x)
```

https://stackoverflow.com/questions/3018758/determine-precision-and-scale-of-particular-number-in-python

Returns a (precision, scale) tuple for a given number.

#### validmind.utils.preview_test_config

```python
preview_test_config(config)
```

#### validmind.utils.run_async

```python
run_async(func, *args, name=None, **kwargs)
```

Helper function to run functions asynchronously

This takes care of the complexity of running the logging functions asynchronously. It will
detect the type of environment we are running in (ipython notebook or not) and run the
function accordingly.

**Parameters:**

- **func** (<code>[function](#function)</code>) – The function to run asynchronously
- \***args** – The arguments to pass to the function
- \*\***kwargs** – The keyword arguments to pass to the function

**Returns:**

- – The result of the function

#### validmind.utils.run_async_check

```python
run_async_check(func, *args, **kwargs)
```

Helper function to run functions asynchronously if the task doesn't already exist

#### validmind.utils.summarize_data_quality_results

```python
summarize_data_quality_results(results)
```

TODO: generalize this to work with metrics and test results

Summarize the results of the data quality test suite

#### validmind.utils.test_id_to_name

```python
test_id_to_name(test_id)
```

Convert a test ID to a human-readable name.

**Parameters:**

- **test_id** (<code>[str](#str)</code>) – The test identifier, typically in CamelCase or snake_case.

**Returns:**

- **str** (<code>[str](#str)</code>) – A human-readable name derived from the test ID.

### validmind.vm_models

Models entrypoint

**Modules:**

- [**dataset**](#validmind.vm_models.dataset) –
- [**figure**](#validmind.vm_models.figure) – Figure objects track the figure schema supported by the ValidMind API
- [**input**](#validmind.vm_models.input) – Base class for ValidMind Input types
- [**model**](#validmind.vm_models.model) – Model class wrapper module
- [**result**](#validmind.vm_models.result) –

**Classes:**

- [**Figure**](#validmind.vm_models.Figure) – Figure objects track the schema supported by the ValidMind API
- [**ModelAttributes**](#validmind.vm_models.ModelAttributes) – Model attributes definition
- [**ResultTable**](#validmind.vm_models.ResultTable) – A dataclass that holds the table summary of result
- [**TestResult**](#validmind.vm_models.TestResult) – Test result
- [**VMDataset**](#validmind.vm_models.VMDataset) – Base class for VM datasets
- [**VMInput**](#validmind.vm_models.VMInput) – Base class for ValidMind Input types
- [**VMModel**](#validmind.vm_models.VMModel) – An base class that wraps a trained model instance and its associated data.

**Attributes:**

- [**R_MODEL_TYPES**](#validmind.vm_models.R_MODEL_TYPES) –

#### validmind.vm_models.Figure

```python
Figure(key, figure, ref_id, _type='plot')
```

Figure objects track the schema supported by the ValidMind API

**Functions:**

- [**serialize**](#validmind.vm_models.Figure.serialize) – Serializes the Figure to a dictionary so it can be sent to the API
- [**serialize_files**](#validmind.vm_models.Figure.serialize_files) – Creates a `requests`-compatible files object to be sent to the API
- [**to_widget**](#validmind.vm_models.Figure.to_widget) – Returns the ipywidget compatible representation of the figure. Ideally

**Attributes:**

- [**figure**](#validmind.vm_models.Figure.figure) (<code>[Union](#typing.Union)\[[Figure](#matplotlib.figure.Figure), [Figure](#plotly.graph_objs.Figure), [FigureWidget](#plotly.graph_objs.FigureWidget), [bytes](#bytes)\]</code>) –
- [**key**](#validmind.vm_models.Figure.key) (<code>[str](#str)</code>) –
- [**ref_id**](#validmind.vm_models.Figure.ref_id) (<code>[str](#str)</code>) –

##### validmind.vm_models.Figure.figure

```python
figure: Union[matplotlib.figure.Figure, go.Figure, go.FigureWidget, bytes]
```

##### validmind.vm_models.Figure.key

```python
key: str
```

##### validmind.vm_models.Figure.ref_id

```python
ref_id: str
```

##### validmind.vm_models.Figure.serialize

```python
serialize()
```

Serializes the Figure to a dictionary so it can be sent to the API

##### validmind.vm_models.Figure.serialize_files

```python
serialize_files()
```

Creates a `requests`-compatible files object to be sent to the API

##### validmind.vm_models.Figure.to_widget

```python
to_widget()
```

Returns the ipywidget compatible representation of the figure. Ideally
we would render images as-is, but Plotly FigureWidgets don't work well
on Google Colab when they are combined with ipywidgets.

#### validmind.vm_models.ModelAttributes

```python
ModelAttributes(
    architecture=None,
    framework=None,
    framework_version=None,
    language=None,
    task=None,
)
```

Model attributes definition

**Functions:**

- [**from_dict**](#validmind.vm_models.ModelAttributes.from_dict) – Creates a ModelAttributes instance from a dictionary

**Attributes:**

- [**architecture**](#validmind.vm_models.ModelAttributes.architecture) (<code>[str](#str)</code>) –
- [**framework**](#validmind.vm_models.ModelAttributes.framework) (<code>[str](#str)</code>) –
- [**framework_version**](#validmind.vm_models.ModelAttributes.framework_version) (<code>[str](#str)</code>) –
- [**language**](#validmind.vm_models.ModelAttributes.language) (<code>[str](#str)</code>) –
- [**task**](#validmind.vm_models.ModelAttributes.task) (<code>[ModelTask](#validmind.vm_models.model.ModelTask)</code>) –

##### validmind.vm_models.ModelAttributes.architecture

```python
architecture: str = None
```

##### validmind.vm_models.ModelAttributes.framework

```python
framework: str = None
```

##### validmind.vm_models.ModelAttributes.framework_version

```python
framework_version: str = None
```

##### validmind.vm_models.ModelAttributes.from_dict

```python
from_dict(data)
```

Creates a ModelAttributes instance from a dictionary

##### validmind.vm_models.ModelAttributes.language

```python
language: str = None
```

##### validmind.vm_models.ModelAttributes.task

```python
task: ModelTask = None
```

#### validmind.vm_models.R_MODEL_TYPES

```python
R_MODEL_TYPES = [
    "LogisticRegression",
    "LinearRegression",
    "XGBClassifier",
    "XGBRegressor",
]

```

#### validmind.vm_models.ResultTable

```python
ResultTable(data, title)
```

A dataclass that holds the table summary of result

**Functions:**

- [**serialize**](#validmind.vm_models.ResultTable.serialize) –

**Attributes:**

- [**data**](#validmind.vm_models.ResultTable.data) (<code>[Union](#typing.Union)\[[List](#typing.List)\[[Any](#typing.Any)\], [DataFrame](#pandas.DataFrame)\]</code>) –
- [**title**](#validmind.vm_models.ResultTable.title) (<code>[str](#str)</code>) –

##### validmind.vm_models.ResultTable.data

```python
data: Union[List[Any], pd.DataFrame]
```

##### validmind.vm_models.ResultTable.serialize

```python
serialize()
```

##### validmind.vm_models.ResultTable.title

```python
title: str
```

#### validmind.vm_models.TestResult

```python
TestResult(
    result_id=None,
    name="Test Result",
    ref_id=None,
    title=None,
    description=None,
    metric=None,
    tables=None,
    figures=None,
    passed=None,
    params=None,
    inputs=None,
    metadata=None,
    _was_description_generated=False,
    _unsafe=False,
)
```

Bases: <code>[Result](#validmind.vm_models.result.result.Result)</code>

Test result

**Functions:**

- [**add_figure**](#validmind.vm_models.TestResult.add_figure) –
- [**add_table**](#validmind.vm_models.TestResult.add_table) –
- [**log**](#validmind.vm_models.TestResult.log) – Log the result to ValidMind
- [**log_async**](#validmind.vm_models.TestResult.log_async) –
- [**serialize**](#validmind.vm_models.TestResult.serialize) – Serialize the result for the API
- [**show**](#validmind.vm_models.TestResult.show) – Display the result... May be overridden by subclasses
- [**to_widget**](#validmind.vm_models.TestResult.to_widget) –

**Attributes:**

- [**description**](#validmind.vm_models.TestResult.description) (<code>[Optional](#typing.Optional)\[[Union](#typing.Union)\[[str](#str), [DescriptionFuture](#validmind.ai.utils.DescriptionFuture)\]\]</code>) –
- [**figures**](#validmind.vm_models.TestResult.figures) (<code>[Optional](#typing.Optional)\[[List](#typing.List)\[[Figure](#validmind.vm_models.figure.Figure)\]\]</code>) –
- [**inputs**](#validmind.vm_models.TestResult.inputs) (<code>[Optional](#typing.Optional)\[[Dict](#typing.Dict)\[[str](#str), [Union](#typing.Union)\[[List](#typing.List)\[[VMInput](#validmind.vm_models.input.VMInput)\], [VMInput](#validmind.vm_models.input.VMInput)\]\]\]</code>) –
- [**metadata**](#validmind.vm_models.TestResult.metadata) (<code>[Optional](#typing.Optional)\[[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]\]</code>) –
- [**metric**](#validmind.vm_models.TestResult.metric) (<code>[Optional](#typing.Optional)\[[Union](#typing.Union)\[[int](#int), [float](#float)\]\]</code>) –
- [**name**](#validmind.vm_models.TestResult.name) (<code>[str](#str)</code>) –
- [**params**](#validmind.vm_models.TestResult.params) (<code>[Optional](#typing.Optional)\[[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]\]</code>) –
- [**passed**](#validmind.vm_models.TestResult.passed) (<code>[Optional](#typing.Optional)\[[bool](#bool)\]</code>) –
- [**ref_id**](#validmind.vm_models.TestResult.ref_id) (<code>[str](#str)</code>) –
- [**result_id**](#validmind.vm_models.TestResult.result_id) (<code>[str](#str)</code>) –
- [**tables**](#validmind.vm_models.TestResult.tables) (<code>[Optional](#typing.Optional)\[[List](#typing.List)\[[ResultTable](#validmind.vm_models.result.result.ResultTable)\]\]</code>) –
- [**test_name**](#validmind.vm_models.TestResult.test_name) (<code>[str](#str)</code>) – Get the test name, using custom title if available.
- [**title**](#validmind.vm_models.TestResult.title) (<code>[Optional](#typing.Optional)\[[str](#str)\]</code>) –

##### validmind.vm_models.TestResult.add_figure

```python
add_figure(figure)
```

##### validmind.vm_models.TestResult.add_table

```python
add_table(table)
```

##### validmind.vm_models.TestResult.description

```python
description: Optional[Union[str, DescriptionFuture]] = None
```

##### validmind.vm_models.TestResult.figures

```python
figures: Optional[List[Figure]] = None
```

##### validmind.vm_models.TestResult.inputs

```python
inputs: Optional[Dict[str, Union[List[VMInput], VMInput]]] = None
```

##### validmind.vm_models.TestResult.log

```python
log(section_id=None, position=None, unsafe=False)
```

Log the result to ValidMind

**Parameters:**

- **section_id** (<code>[str](#str)</code>) – The section ID within the model document to insert the
  test result
- **position** (<code>[int](#int)</code>) – The position (index) within the section to insert the test
  result
- **unsafe** (<code>[bool](#bool)</code>) – If True, log the result even if it contains sensitive data
  i.e. raw data from input datasets

##### validmind.vm_models.TestResult.log_async

```python
log_async(section_id=None, position=None, unsafe=False)
```

##### validmind.vm_models.TestResult.metadata

```python
metadata: Optional[Dict[str, Any]] = None
```

##### validmind.vm_models.TestResult.metric

```python
metric: Optional[Union[int, float]] = None
```

##### validmind.vm_models.TestResult.name

```python
name: str = 'Test Result'
```

##### validmind.vm_models.TestResult.params

```python
params: Optional[Dict[str, Any]] = None
```

##### validmind.vm_models.TestResult.passed

```python
passed: Optional[bool] = None
```

##### validmind.vm_models.TestResult.ref_id

```python
ref_id: str = None
```

##### validmind.vm_models.TestResult.result_id

```python
result_id: str = None
```

##### validmind.vm_models.TestResult.serialize

```python
serialize()
```

Serialize the result for the API

##### validmind.vm_models.TestResult.show

```python
show()
```

Display the result... May be overridden by subclasses

##### validmind.vm_models.TestResult.tables

```python
tables: Optional[List[ResultTable]] = None
```

##### validmind.vm_models.TestResult.test_name

```python
test_name: str
```

Get the test name, using custom title if available.

##### validmind.vm_models.TestResult.title

```python
title: Optional[str] = None
```

##### validmind.vm_models.TestResult.to_widget

```python
to_widget()
```

#### validmind.vm_models.VMDataset

```python
VMDataset(
    raw_dataset,
    input_id=None,
    model=None,
    index=None,
    index_name=None,
    date_time_index=False,
    columns=None,
    target_column=None,
    feature_columns=None,
    text_column=None,
    extra_columns=None,
    target_class_labels=None,
)
```

Bases: <code>[VMInput](#validmind.vm_models.input.VMInput)</code>

Base class for VM datasets

Child classes should be used to support new dataset types (tensor, polars etc)
by converting the user's dataset into a numpy array collecting metadata like
column names and then call this (parent) class `__init__` method.

This way we can support multiple dataset types but under the hood we only
need to work with numpy arrays and pandas dataframes in this class.

**Attributes:**

- [**raw_dataset**](#validmind.vm_models.VMDataset.raw_dataset) (<code>[ndarray](#numpy.ndarray)</code>) – The raw dataset as a NumPy array.
- [**input_id**](#validmind.vm_models.VMDataset.input_id) (<code>[str](#str)</code>) – Identifier for the dataset.
- [**index**](#validmind.vm_models.VMDataset.index) (<code>[ndarray](#numpy.ndarray)</code>) – The raw dataset index as a NumPy array.
- [**columns**](#validmind.vm_models.VMDataset.columns) (<code>[Set](#Set)\[[str](#str)\]</code>) – The column names of the dataset.
- [**target_column**](#validmind.vm_models.VMDataset.target_column) (<code>[str](#str)</code>) – The target column name of the dataset.
- [**feature_columns**](#validmind.vm_models.VMDataset.feature_columns) (<code>[List](#List)\[[str](#str)\]</code>) – The feature column names of the dataset.
- [**feature_columns_numeric**](#validmind.vm_models.VMDataset.feature_columns_numeric) (<code>[List](#List)\[[str](#str)\]</code>) – The numeric feature column names of the dataset.
- [**feature_columns_categorical**](#validmind.vm_models.VMDataset.feature_columns_categorical) (<code>[List](#List)\[[str](#str)\]</code>) – The categorical feature column names of the dataset.
- [**text_column**](#validmind.vm_models.VMDataset.text_column) (<code>[str](#str)</code>) – The text column name of the dataset for NLP tasks.
- [**target_class_labels**](#validmind.vm_models.VMDataset.target_class_labels) (<code>[Dict](#Dict)</code>) – The class labels for the target columns.
- [**df**](#validmind.vm_models.VMDataset.df) (<code>[DataFrame](#pandas.DataFrame)</code>) – The dataset as a pandas DataFrame.
- [**extra_columns**](#validmind.vm_models.VMDataset.extra_columns) (<code>[Dict](#Dict)</code>) – Extra columns to include in the dataset.

**Functions:**

- [**add_extra_column**](#validmind.vm_models.VMDataset.add_extra_column) – Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.
- [**assign_predictions**](#validmind.vm_models.VMDataset.assign_predictions) – Assign predictions and probabilities to the dataset.
- [**prediction_column**](#validmind.vm_models.VMDataset.prediction_column) – Get or set the prediction column for a model.
- [**probability_column**](#validmind.vm_models.VMDataset.probability_column) – Get or set the probability column for a model.
- [**target_classes**](#validmind.vm_models.VMDataset.target_classes) – Returns the target class labels or unique values of the target column.
- [**with_options**](#validmind.vm_models.VMDataset.with_options) – Support options provided when passing an input to run_test or run_test_suite
- [**x_df**](#validmind.vm_models.VMDataset.x_df) – Returns a dataframe containing only the feature columns
- [**y_df**](#validmind.vm_models.VMDataset.y_df) – Returns a dataframe containing the target column
- [**y_pred**](#validmind.vm_models.VMDataset.y_pred) – Returns the predictions for a given model.
- [**y_pred_df**](#validmind.vm_models.VMDataset.y_pred_df) – Returns a dataframe containing the predictions for a given model
- [**y_prob**](#validmind.vm_models.VMDataset.y_prob) – Returns the probabilities for a given model.
- [**y_prob_df**](#validmind.vm_models.VMDataset.y_prob_df) – Returns a dataframe containing the probabilities for a given model

**Attributes:**

- [**column_aliases**](#validmind.vm_models.VMDataset.column_aliases) –
- [**columns**](#validmind.vm_models.VMDataset.columns) –
- [**df**](#validmind.vm_models.VMDataset.df) (<code>[DataFrame](#pandas.DataFrame)</code>) – Returns the dataset as a pandas DataFrame.
- [**extra_columns**](#validmind.vm_models.VMDataset.extra_columns) –
- [**index**](#validmind.vm_models.VMDataset.index) –
- [**input_id**](#validmind.vm_models.VMDataset.input_id) –
- [**target_class_labels**](#validmind.vm_models.VMDataset.target_class_labels) –
- [**target_column**](#validmind.vm_models.VMDataset.target_column) –
- [**text_column**](#validmind.vm_models.VMDataset.text_column) –
- [**x**](#validmind.vm_models.VMDataset.x) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the input features (X) of the dataset.
- [**y**](#validmind.vm_models.VMDataset.y) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the target variables (y) of the dataset.

Initializes a VMDataset instance.

**Parameters:**

- **raw_dataset** (<code>[ndarray](#numpy.ndarray)</code>) – The raw dataset as a NumPy array.
- **input_id** (<code>[str](#str)</code>) – Identifier for the dataset.
- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – Model associated with the dataset.
- **index** (<code>[ndarray](#numpy.ndarray)</code>) – The raw dataset index as a NumPy array.
- **index_name** (<code>[str](#str)</code>) – The raw dataset index name as a NumPy array.
- **date_time_index** (<code>[bool](#bool)</code>) – Whether the index is a datetime index.
- **columns** (<code>[List](#List)\[[str](#str)\]</code>) – The column names of the dataset. Defaults to None.
- **target_column** (<code>[str](#str)</code>) – The target column name of the dataset. Defaults to None.
- **feature_columns** (<code>[str](#str)</code>) – The feature column names of the dataset. Defaults to None.
- **text_column** (<code>[str](#str)</code>) – The text column name of the dataset for nlp tasks. Defaults to None.
- **target_class_labels** (<code>[Dict](#Dict)</code>) – The class labels for the target columns. Defaults to None.

##### validmind.vm_models.VMDataset.add_extra_column

```python
add_extra_column(column_name, column_values=None)
```

Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.

**Parameters:**

- **column_name** (<code>[str](#str)</code>) – The name of the extra column.
- **column_values** (<code>[ndarray](#numpy.ndarray)</code>) – The values of the extra column.

##### validmind.vm_models.VMDataset.assign_predictions

```python
assign_predictions(
    model,
    prediction_column=None,
    prediction_values=None,
    probability_column=None,
    probability_values=None,
    prediction_probabilities=None,
    **kwargs
)
```

Assign predictions and probabilities to the dataset.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model used to generate the predictions.
- **prediction_column** (<code>[str](#str)</code>) – The name of the column containing the predictions. Defaults to None.
- **prediction_values** (<code>[list](#list)</code>) – The values of the predictions. Defaults to None.
- **probability_column** (<code>[str](#str)</code>) – The name of the column containing the probabilities. Defaults to None.
- **probability_values** (<code>[list](#list)</code>) – The values of the probabilities. Defaults to None.
- **prediction_probabilities** (<code>[list](#list)</code>) – DEPRECATED: The values of the probabilities. Defaults to None.
- **kwargs** – Additional keyword arguments that will get passed through to the model's `predict` method.

##### validmind.vm_models.VMDataset.column_aliases

```python
column_aliases = {}
```

##### validmind.vm_models.VMDataset.columns

```python
columns = columns or []
```

##### validmind.vm_models.VMDataset.df

```python
df: pd.DataFrame
```

Returns the dataset as a pandas DataFrame.

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: The dataset as a pandas DataFrame.

##### validmind.vm_models.VMDataset.extra_columns

```python
extra_columns = ExtraColumns.from_dict(extra_columns)
```

##### validmind.vm_models.VMDataset.index

```python
index = index
```

##### validmind.vm_models.VMDataset.input_id

```python
input_id = input_id
```

##### validmind.vm_models.VMDataset.prediction_column

```python
prediction_column(model, column_name=None)
```

Get or set the prediction column for a model.

##### validmind.vm_models.VMDataset.probability_column

```python
probability_column(model, column_name=None)
```

Get or set the probability column for a model.

##### validmind.vm_models.VMDataset.target_class_labels

```python
target_class_labels = target_class_labels
```

##### validmind.vm_models.VMDataset.target_classes

```python
target_classes()
```

Returns the target class labels or unique values of the target column.

##### validmind.vm_models.VMDataset.target_column

```python
target_column = target_column
```

##### validmind.vm_models.VMDataset.text_column

```python
text_column = text_column
```

##### validmind.vm_models.VMDataset.with_options

```python
with_options(**kwargs)
```

Support options provided when passing an input to run_test or run_test_suite

Example:

```python
# to only use a certain subset of columns in the dataset:
run_test(
    "validmind.SomeTestID",
    inputs={
        "dataset": {
            "input_id": "my_dataset_id",
            "columns": ["col1", "col2"],
        }
    }
)

# behind the scenes, this retrieves the dataset object (VMDataset) from the registry
# and then calls the `with_options()` method and passes `{"columns": ...}`
```

**Parameters:**

- \*\***kwargs** – Options:
- columns: Filter columns in the dataset

**Returns:**

- **VMDataset** (<code>[VMDataset](#validmind.vm_models.dataset.dataset.VMDataset)</code>) – A new instance of the dataset with only the specified columns

##### validmind.vm_models.VMDataset.x

```python
x: np.ndarray
```

Returns the input features (X) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The input features.

##### validmind.vm_models.VMDataset.x_df

```python
x_df()
```

Returns a dataframe containing only the feature columns

##### validmind.vm_models.VMDataset.y

```python
y: np.ndarray
```

Returns the target variables (y) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The target variables.

##### validmind.vm_models.VMDataset.y_df

```python
y_df()
```

Returns a dataframe containing the target column

##### validmind.vm_models.VMDataset.y_pred

```python
y_pred(model)
```

Returns the predictions for a given model.

Attempts to stack complex prediction types (e.g., embeddings) into a single,
multi-dimensional array.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The predictions for the model

##### validmind.vm_models.VMDataset.y_pred_df

```python
y_pred_df(model)
```

Returns a dataframe containing the predictions for a given model

##### validmind.vm_models.VMDataset.y_prob

```python
y_prob(model)
```

Returns the probabilities for a given model.

**Parameters:**

- **model** (<code>[str](#str)</code>) – The ID of the model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The probability variables.

##### validmind.vm_models.VMDataset.y_prob_df

```python
y_prob_df(model)
```

Returns a dataframe containing the probabilities for a given model

#### validmind.vm_models.VMInput

Bases: <code>[ABC](#abc.ABC)</code>

Base class for ValidMind Input types

**Functions:**

- [**with_options**](#validmind.vm_models.VMInput.with_options) – Allows for setting options on the input object that are passed by the user

##### validmind.vm_models.VMInput.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

#### validmind.vm_models.VMModel

```python
VMModel(input_id=None, model=None, attributes=None, name=None, **kwargs)
```

Bases: <code>[VMInput](#validmind.vm_models.input.VMInput)</code>

An base class that wraps a trained model instance and its associated data.

**Attributes:**

- [**model**](#validmind.vm_models.VMModel.model) (<code>[object](#object)</code>) – The trained model instance. Defaults to None.
- [**input_id**](#validmind.vm_models.VMModel.input_id) (<code>[str](#str)</code>) – The input ID for the model. Defaults to None.
- [**attributes**](#validmind.vm_models.VMModel.attributes) (<code>[ModelAttributes](#validmind.vm_models.model.ModelAttributes)</code>) – The attributes of the model. Defaults to None.
- [**name**](#validmind.vm_models.VMModel.name) (<code>[str](#str)</code>) – The name of the model. Defaults to the class name.

**Functions:**

- [**predict**](#validmind.vm_models.VMModel.predict) – Predict method for the model. This is a wrapper around the model's
- [**predict_proba**](#validmind.vm_models.VMModel.predict_proba) – Predict probabilties - must be implemented by subclass if needed
- [**serialize**](#validmind.vm_models.VMModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.vm_models.VMModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.vm_models.VMModel.attributes) –
- [**class\_**](#validmind.vm_models.VMModel.class_) –
- [**input_id**](#validmind.vm_models.VMModel.input_id) –
- [**language**](#validmind.vm_models.VMModel.language) –
- [**library**](#validmind.vm_models.VMModel.library) –
- [**library_version**](#validmind.vm_models.VMModel.library_version) –
- [**model**](#validmind.vm_models.VMModel.model) –
- [**name**](#validmind.vm_models.VMModel.name) –

##### validmind.vm_models.VMModel.attributes

```python
attributes = attributes or ModelAttributes()
```

##### validmind.vm_models.VMModel.class\_

```python
class_ = self.__class__.__name__
```

##### validmind.vm_models.VMModel.input_id

```python
input_id = input_id
```

##### validmind.vm_models.VMModel.language

```python
language = 'Python'
```

##### validmind.vm_models.VMModel.library

```python
library = self.__class__.__name__
```

##### validmind.vm_models.VMModel.library_version

```python
library_version = 'N/A'
```

##### validmind.vm_models.VMModel.model

```python
model = model
```

##### validmind.vm_models.VMModel.name

```python
name = name or self.__class__.__name__
```

##### validmind.vm_models.VMModel.predict

```python
predict(*args, **kwargs)
```

Predict method for the model. This is a wrapper around the model's

##### validmind.vm_models.VMModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

Predict probabilties - must be implemented by subclass if needed

##### validmind.vm_models.VMModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

##### validmind.vm_models.VMModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

#### validmind.vm_models.dataset

**Modules:**

- [**dataset**](#validmind.vm_models.dataset.dataset) – Dataset class wrapper
- [**utils**](#validmind.vm_models.dataset.utils) –

**Classes:**

- [**DataFrameDataset**](#validmind.vm_models.dataset.DataFrameDataset) – VM dataset implementation for pandas DataFrame.
- [**PolarsDataset**](#validmind.vm_models.dataset.PolarsDataset) – VM dataset implementation for Polars DataFrame.
- [**TorchDataset**](#validmind.vm_models.dataset.TorchDataset) – VM dataset implementation for PyTorch Datasets.
- [**VMDataset**](#validmind.vm_models.dataset.VMDataset) – Base class for VM datasets

##### validmind.vm_models.dataset.DataFrameDataset

```python
DataFrameDataset(
    raw_dataset,
    input_id=None,
    model=None,
    target_column=None,
    extra_columns=None,
    feature_columns=None,
    text_column=None,
    target_class_labels=None,
    date_time_index=False,
)
```

Bases: <code>[VMDataset](#validmind.vm_models.dataset.dataset.VMDataset)</code>

VM dataset implementation for pandas DataFrame.

**Functions:**

- [**add_extra_column**](#validmind.vm_models.dataset.DataFrameDataset.add_extra_column) – Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.
- [**assign_predictions**](#validmind.vm_models.dataset.DataFrameDataset.assign_predictions) – Assign predictions and probabilities to the dataset.
- [**prediction_column**](#validmind.vm_models.dataset.DataFrameDataset.prediction_column) – Get or set the prediction column for a model.
- [**probability_column**](#validmind.vm_models.dataset.DataFrameDataset.probability_column) – Get or set the probability column for a model.
- [**target_classes**](#validmind.vm_models.dataset.DataFrameDataset.target_classes) – Returns the target class labels or unique values of the target column.
- [**with_options**](#validmind.vm_models.dataset.DataFrameDataset.with_options) – Support options provided when passing an input to run_test or run_test_suite
- [**x_df**](#validmind.vm_models.dataset.DataFrameDataset.x_df) – Returns a dataframe containing only the feature columns
- [**y_df**](#validmind.vm_models.dataset.DataFrameDataset.y_df) – Returns a dataframe containing the target column
- [**y_pred**](#validmind.vm_models.dataset.DataFrameDataset.y_pred) – Returns the predictions for a given model.
- [**y_pred_df**](#validmind.vm_models.dataset.DataFrameDataset.y_pred_df) – Returns a dataframe containing the predictions for a given model
- [**y_prob**](#validmind.vm_models.dataset.DataFrameDataset.y_prob) – Returns the probabilities for a given model.
- [**y_prob_df**](#validmind.vm_models.dataset.DataFrameDataset.y_prob_df) – Returns a dataframe containing the probabilities for a given model

**Attributes:**

- [**column_aliases**](#validmind.vm_models.dataset.DataFrameDataset.column_aliases) –
- [**columns**](#validmind.vm_models.dataset.DataFrameDataset.columns) –
- [**df**](#validmind.vm_models.dataset.DataFrameDataset.df) (<code>[DataFrame](#pandas.DataFrame)</code>) – Returns the dataset as a pandas DataFrame.
- [**extra_columns**](#validmind.vm_models.dataset.DataFrameDataset.extra_columns) –
- [**index**](#validmind.vm_models.dataset.DataFrameDataset.index) –
- [**input_id**](#validmind.vm_models.dataset.DataFrameDataset.input_id) –
- [**target_class_labels**](#validmind.vm_models.dataset.DataFrameDataset.target_class_labels) –
- [**target_column**](#validmind.vm_models.dataset.DataFrameDataset.target_column) –
- [**text_column**](#validmind.vm_models.dataset.DataFrameDataset.text_column) –
- [**x**](#validmind.vm_models.dataset.DataFrameDataset.x) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the input features (X) of the dataset.
- [**y**](#validmind.vm_models.dataset.DataFrameDataset.y) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the target variables (y) of the dataset.

Initializes a DataFrameDataset instance.

**Parameters:**

- **raw_dataset** (<code>[DataFrame](#pandas.DataFrame)</code>) – The raw dataset as a pandas DataFrame.
- **input_id** (<code>[str](#str)</code>) – Identifier for the dataset. Defaults to None.
- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – Model associated with the dataset. Defaults to None.
- **target_column** (<code>[str](#str)</code>) – The target column of the dataset. Defaults to None.
- **extra_columns** (<code>[dict](#dict)</code>) – Extra columns to include in the dataset. Defaults to None.
- **feature_columns** (<code>[list](#list)</code>) – The feature columns of the dataset. Defaults to None.
- **text_column** (<code>[str](#str)</code>) – The text column name of the dataset for NLP tasks. Defaults to None.
- **target_class_labels** (<code>[dict](#dict)</code>) – The class labels for the target columns. Defaults to None.
- **date_time_index** (<code>[bool](#bool)</code>) – Whether to use date-time index. Defaults to False.

###### validmind.vm_models.dataset.DataFrameDataset.add_extra_column

```python
add_extra_column(column_name, column_values=None)
```

Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.

**Parameters:**

- **column_name** (<code>[str](#str)</code>) – The name of the extra column.
- **column_values** (<code>[ndarray](#numpy.ndarray)</code>) – The values of the extra column.

###### validmind.vm_models.dataset.DataFrameDataset.assign_predictions

```python
assign_predictions(
    model,
    prediction_column=None,
    prediction_values=None,
    probability_column=None,
    probability_values=None,
    prediction_probabilities=None,
    **kwargs
)
```

Assign predictions and probabilities to the dataset.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model used to generate the predictions.
- **prediction_column** (<code>[str](#str)</code>) – The name of the column containing the predictions. Defaults to None.
- **prediction_values** (<code>[list](#list)</code>) – The values of the predictions. Defaults to None.
- **probability_column** (<code>[str](#str)</code>) – The name of the column containing the probabilities. Defaults to None.
- **probability_values** (<code>[list](#list)</code>) – The values of the probabilities. Defaults to None.
- **prediction_probabilities** (<code>[list](#list)</code>) – DEPRECATED: The values of the probabilities. Defaults to None.
- **kwargs** – Additional keyword arguments that will get passed through to the model's `predict` method.

###### validmind.vm_models.dataset.DataFrameDataset.column_aliases

```python
column_aliases = {}
```

###### validmind.vm_models.dataset.DataFrameDataset.columns

```python
columns = columns or []
```

###### validmind.vm_models.dataset.DataFrameDataset.df

```python
df: pd.DataFrame
```

Returns the dataset as a pandas DataFrame.

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: The dataset as a pandas DataFrame.

###### validmind.vm_models.dataset.DataFrameDataset.extra_columns

```python
extra_columns = ExtraColumns.from_dict(extra_columns)
```

###### validmind.vm_models.dataset.DataFrameDataset.index

```python
index = index
```

###### validmind.vm_models.dataset.DataFrameDataset.input_id

```python
input_id = input_id
```

###### validmind.vm_models.dataset.DataFrameDataset.prediction_column

```python
prediction_column(model, column_name=None)
```

Get or set the prediction column for a model.

###### validmind.vm_models.dataset.DataFrameDataset.probability_column

```python
probability_column(model, column_name=None)
```

Get or set the probability column for a model.

###### validmind.vm_models.dataset.DataFrameDataset.target_class_labels

```python
target_class_labels = target_class_labels
```

###### validmind.vm_models.dataset.DataFrameDataset.target_classes

```python
target_classes()
```

Returns the target class labels or unique values of the target column.

###### validmind.vm_models.dataset.DataFrameDataset.target_column

```python
target_column = target_column
```

###### validmind.vm_models.dataset.DataFrameDataset.text_column

```python
text_column = text_column
```

###### validmind.vm_models.dataset.DataFrameDataset.with_options

```python
with_options(**kwargs)
```

Support options provided when passing an input to run_test or run_test_suite

Example:

```python
# to only use a certain subset of columns in the dataset:
run_test(
    "validmind.SomeTestID",
    inputs={
        "dataset": {
            "input_id": "my_dataset_id",
            "columns": ["col1", "col2"],
        }
    }
)

# behind the scenes, this retrieves the dataset object (VMDataset) from the registry
# and then calls the `with_options()` method and passes `{"columns": ...}`
```

**Parameters:**

- \*\***kwargs** – Options:
- columns: Filter columns in the dataset

**Returns:**

- **VMDataset** (<code>[VMDataset](#validmind.vm_models.dataset.dataset.VMDataset)</code>) – A new instance of the dataset with only the specified columns

###### validmind.vm_models.dataset.DataFrameDataset.x

```python
x: np.ndarray
```

Returns the input features (X) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The input features.

###### validmind.vm_models.dataset.DataFrameDataset.x_df

```python
x_df()
```

Returns a dataframe containing only the feature columns

###### validmind.vm_models.dataset.DataFrameDataset.y

```python
y: np.ndarray
```

Returns the target variables (y) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The target variables.

###### validmind.vm_models.dataset.DataFrameDataset.y_df

```python
y_df()
```

Returns a dataframe containing the target column

###### validmind.vm_models.dataset.DataFrameDataset.y_pred

```python
y_pred(model)
```

Returns the predictions for a given model.

Attempts to stack complex prediction types (e.g., embeddings) into a single,
multi-dimensional array.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The predictions for the model

###### validmind.vm_models.dataset.DataFrameDataset.y_pred_df

```python
y_pred_df(model)
```

Returns a dataframe containing the predictions for a given model

###### validmind.vm_models.dataset.DataFrameDataset.y_prob

```python
y_prob(model)
```

Returns the probabilities for a given model.

**Parameters:**

- **model** (<code>[str](#str)</code>) – The ID of the model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The probability variables.

###### validmind.vm_models.dataset.DataFrameDataset.y_prob_df

```python
y_prob_df(model)
```

Returns a dataframe containing the probabilities for a given model

##### validmind.vm_models.dataset.PolarsDataset

```python
PolarsDataset(
    raw_dataset,
    input_id=None,
    model=None,
    target_column=None,
    extra_columns=None,
    feature_columns=None,
    text_column=None,
    target_class_labels=None,
    date_time_index=False,
)
```

Bases: <code>[VMDataset](#validmind.vm_models.dataset.dataset.VMDataset)</code>

VM dataset implementation for Polars DataFrame.

**Functions:**

- [**add_extra_column**](#validmind.vm_models.dataset.PolarsDataset.add_extra_column) – Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.
- [**assign_predictions**](#validmind.vm_models.dataset.PolarsDataset.assign_predictions) – Assign predictions and probabilities to the dataset.
- [**prediction_column**](#validmind.vm_models.dataset.PolarsDataset.prediction_column) – Get or set the prediction column for a model.
- [**probability_column**](#validmind.vm_models.dataset.PolarsDataset.probability_column) – Get or set the probability column for a model.
- [**target_classes**](#validmind.vm_models.dataset.PolarsDataset.target_classes) – Returns the target class labels or unique values of the target column.
- [**with_options**](#validmind.vm_models.dataset.PolarsDataset.with_options) – Support options provided when passing an input to run_test or run_test_suite
- [**x_df**](#validmind.vm_models.dataset.PolarsDataset.x_df) – Returns a dataframe containing only the feature columns
- [**y_df**](#validmind.vm_models.dataset.PolarsDataset.y_df) – Returns a dataframe containing the target column
- [**y_pred**](#validmind.vm_models.dataset.PolarsDataset.y_pred) – Returns the predictions for a given model.
- [**y_pred_df**](#validmind.vm_models.dataset.PolarsDataset.y_pred_df) – Returns a dataframe containing the predictions for a given model
- [**y_prob**](#validmind.vm_models.dataset.PolarsDataset.y_prob) – Returns the probabilities for a given model.
- [**y_prob_df**](#validmind.vm_models.dataset.PolarsDataset.y_prob_df) – Returns a dataframe containing the probabilities for a given model

**Attributes:**

- [**column_aliases**](#validmind.vm_models.dataset.PolarsDataset.column_aliases) –
- [**columns**](#validmind.vm_models.dataset.PolarsDataset.columns) –
- [**df**](#validmind.vm_models.dataset.PolarsDataset.df) (<code>[DataFrame](#pandas.DataFrame)</code>) – Returns the dataset as a pandas DataFrame.
- [**extra_columns**](#validmind.vm_models.dataset.PolarsDataset.extra_columns) –
- [**index**](#validmind.vm_models.dataset.PolarsDataset.index) –
- [**input_id**](#validmind.vm_models.dataset.PolarsDataset.input_id) –
- [**target_class_labels**](#validmind.vm_models.dataset.PolarsDataset.target_class_labels) –
- [**target_column**](#validmind.vm_models.dataset.PolarsDataset.target_column) –
- [**text_column**](#validmind.vm_models.dataset.PolarsDataset.text_column) –
- [**x**](#validmind.vm_models.dataset.PolarsDataset.x) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the input features (X) of the dataset.
- [**y**](#validmind.vm_models.dataset.PolarsDataset.y) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the target variables (y) of the dataset.

Initializes a PolarsDataset instance.

**Parameters:**

- **raw_dataset** (<code>[DataFrame](#polars.DataFrame)</code>) – The raw dataset as a Polars DataFrame.
- **input_id** (<code>[str](#str)</code>) – Identifier for the dataset. Defaults to None.
- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – Model associated with the dataset. Defaults to None.
- **target_column** (<code>[str](#str)</code>) – The target column of the dataset. Defaults to None.
- **extra_columns** (<code>[dict](#dict)</code>) – Extra columns to include in the dataset. Defaults to None.
- **feature_columns** (<code>[list](#list)</code>) – The feature columns of the dataset. Defaults to None.
- **text_column** (<code>[str](#str)</code>) – The text column name of the dataset for NLP tasks. Defaults to None.
- **target_class_labels** (<code>[dict](#dict)</code>) – The class labels for the target columns. Defaults to None.
- **date_time_index** (<code>[bool](#bool)</code>) – Whether to use date-time index. Defaults to False.

###### validmind.vm_models.dataset.PolarsDataset.add_extra_column

```python
add_extra_column(column_name, column_values=None)
```

Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.

**Parameters:**

- **column_name** (<code>[str](#str)</code>) – The name of the extra column.
- **column_values** (<code>[ndarray](#numpy.ndarray)</code>) – The values of the extra column.

###### validmind.vm_models.dataset.PolarsDataset.assign_predictions

```python
assign_predictions(
    model,
    prediction_column=None,
    prediction_values=None,
    probability_column=None,
    probability_values=None,
    prediction_probabilities=None,
    **kwargs
)
```

Assign predictions and probabilities to the dataset.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model used to generate the predictions.
- **prediction_column** (<code>[str](#str)</code>) – The name of the column containing the predictions. Defaults to None.
- **prediction_values** (<code>[list](#list)</code>) – The values of the predictions. Defaults to None.
- **probability_column** (<code>[str](#str)</code>) – The name of the column containing the probabilities. Defaults to None.
- **probability_values** (<code>[list](#list)</code>) – The values of the probabilities. Defaults to None.
- **prediction_probabilities** (<code>[list](#list)</code>) – DEPRECATED: The values of the probabilities. Defaults to None.
- **kwargs** – Additional keyword arguments that will get passed through to the model's `predict` method.

###### validmind.vm_models.dataset.PolarsDataset.column_aliases

```python
column_aliases = {}
```

###### validmind.vm_models.dataset.PolarsDataset.columns

```python
columns = columns or []
```

###### validmind.vm_models.dataset.PolarsDataset.df

```python
df: pd.DataFrame
```

Returns the dataset as a pandas DataFrame.

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: The dataset as a pandas DataFrame.

###### validmind.vm_models.dataset.PolarsDataset.extra_columns

```python
extra_columns = ExtraColumns.from_dict(extra_columns)
```

###### validmind.vm_models.dataset.PolarsDataset.index

```python
index = index
```

###### validmind.vm_models.dataset.PolarsDataset.input_id

```python
input_id = input_id
```

###### validmind.vm_models.dataset.PolarsDataset.prediction_column

```python
prediction_column(model, column_name=None)
```

Get or set the prediction column for a model.

###### validmind.vm_models.dataset.PolarsDataset.probability_column

```python
probability_column(model, column_name=None)
```

Get or set the probability column for a model.

###### validmind.vm_models.dataset.PolarsDataset.target_class_labels

```python
target_class_labels = target_class_labels
```

###### validmind.vm_models.dataset.PolarsDataset.target_classes

```python
target_classes()
```

Returns the target class labels or unique values of the target column.

###### validmind.vm_models.dataset.PolarsDataset.target_column

```python
target_column = target_column
```

###### validmind.vm_models.dataset.PolarsDataset.text_column

```python
text_column = text_column
```

###### validmind.vm_models.dataset.PolarsDataset.with_options

```python
with_options(**kwargs)
```

Support options provided when passing an input to run_test or run_test_suite

Example:

```python
# to only use a certain subset of columns in the dataset:
run_test(
    "validmind.SomeTestID",
    inputs={
        "dataset": {
            "input_id": "my_dataset_id",
            "columns": ["col1", "col2"],
        }
    }
)

# behind the scenes, this retrieves the dataset object (VMDataset) from the registry
# and then calls the `with_options()` method and passes `{"columns": ...}`
```

**Parameters:**

- \*\***kwargs** – Options:
- columns: Filter columns in the dataset

**Returns:**

- **VMDataset** (<code>[VMDataset](#validmind.vm_models.dataset.dataset.VMDataset)</code>) – A new instance of the dataset with only the specified columns

###### validmind.vm_models.dataset.PolarsDataset.x

```python
x: np.ndarray
```

Returns the input features (X) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The input features.

###### validmind.vm_models.dataset.PolarsDataset.x_df

```python
x_df()
```

Returns a dataframe containing only the feature columns

###### validmind.vm_models.dataset.PolarsDataset.y

```python
y: np.ndarray
```

Returns the target variables (y) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The target variables.

###### validmind.vm_models.dataset.PolarsDataset.y_df

```python
y_df()
```

Returns a dataframe containing the target column

###### validmind.vm_models.dataset.PolarsDataset.y_pred

```python
y_pred(model)
```

Returns the predictions for a given model.

Attempts to stack complex prediction types (e.g., embeddings) into a single,
multi-dimensional array.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The predictions for the model

###### validmind.vm_models.dataset.PolarsDataset.y_pred_df

```python
y_pred_df(model)
```

Returns a dataframe containing the predictions for a given model

###### validmind.vm_models.dataset.PolarsDataset.y_prob

```python
y_prob(model)
```

Returns the probabilities for a given model.

**Parameters:**

- **model** (<code>[str](#str)</code>) – The ID of the model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The probability variables.

###### validmind.vm_models.dataset.PolarsDataset.y_prob_df

```python
y_prob_df(model)
```

Returns a dataframe containing the probabilities for a given model

##### validmind.vm_models.dataset.TorchDataset

```python
TorchDataset(
    raw_dataset,
    input_id=None,
    model=None,
    index_name=None,
    index=None,
    columns=None,
    target_column=None,
    extra_columns=None,
    feature_columns=None,
    text_column=None,
    target_class_labels=None,
)
```

Bases: <code>[VMDataset](#validmind.vm_models.dataset.dataset.VMDataset)</code>

VM dataset implementation for PyTorch Datasets.

**Functions:**

- [**add_extra_column**](#validmind.vm_models.dataset.TorchDataset.add_extra_column) – Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.
- [**assign_predictions**](#validmind.vm_models.dataset.TorchDataset.assign_predictions) – Assign predictions and probabilities to the dataset.
- [**prediction_column**](#validmind.vm_models.dataset.TorchDataset.prediction_column) – Get or set the prediction column for a model.
- [**probability_column**](#validmind.vm_models.dataset.TorchDataset.probability_column) – Get or set the probability column for a model.
- [**target_classes**](#validmind.vm_models.dataset.TorchDataset.target_classes) – Returns the target class labels or unique values of the target column.
- [**with_options**](#validmind.vm_models.dataset.TorchDataset.with_options) – Support options provided when passing an input to run_test or run_test_suite
- [**x_df**](#validmind.vm_models.dataset.TorchDataset.x_df) – Returns a dataframe containing only the feature columns
- [**y_df**](#validmind.vm_models.dataset.TorchDataset.y_df) – Returns a dataframe containing the target column
- [**y_pred**](#validmind.vm_models.dataset.TorchDataset.y_pred) – Returns the predictions for a given model.
- [**y_pred_df**](#validmind.vm_models.dataset.TorchDataset.y_pred_df) – Returns a dataframe containing the predictions for a given model
- [**y_prob**](#validmind.vm_models.dataset.TorchDataset.y_prob) – Returns the probabilities for a given model.
- [**y_prob_df**](#validmind.vm_models.dataset.TorchDataset.y_prob_df) – Returns a dataframe containing the probabilities for a given model

**Attributes:**

- [**column_aliases**](#validmind.vm_models.dataset.TorchDataset.column_aliases) –
- [**columns**](#validmind.vm_models.dataset.TorchDataset.columns) –
- [**df**](#validmind.vm_models.dataset.TorchDataset.df) (<code>[DataFrame](#pandas.DataFrame)</code>) – Returns the dataset as a pandas DataFrame.
- [**extra_columns**](#validmind.vm_models.dataset.TorchDataset.extra_columns) –
- [**index**](#validmind.vm_models.dataset.TorchDataset.index) –
- [**input_id**](#validmind.vm_models.dataset.TorchDataset.input_id) –
- [**target_class_labels**](#validmind.vm_models.dataset.TorchDataset.target_class_labels) –
- [**target_column**](#validmind.vm_models.dataset.TorchDataset.target_column) –
- [**text_column**](#validmind.vm_models.dataset.TorchDataset.text_column) –
- [**x**](#validmind.vm_models.dataset.TorchDataset.x) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the input features (X) of the dataset.
- [**y**](#validmind.vm_models.dataset.TorchDataset.y) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the target variables (y) of the dataset.

Initializes a TorchDataset instance.

**Parameters:**

- **raw_dataset** (<code>[Dataset](#torch.utils.data.Dataset)</code>) – The raw dataset as a PyTorch Dataset.
- **index_name** (<code>[str](#str)</code>) – The raw dataset index name.
- **index** (<code>[ndarray](#numpy.ndarray)</code>) – The raw dataset index as a NumPy array.
- **columns** (<code>[List](#List)\[[str](#str)\]</code>) – The column names of the dataset.
- **target_column** (<code>[str](#str)</code>) – The target column of the dataset. Defaults to None.
- **feature_columns** (<code>[list](#list)</code>) – The feature columns of the dataset. Defaults to None.
- **text_column** (<code>[str](#str)</code>) – The text column name of the dataset for nlp tasks. Defaults to None.
- **target_class_labels** (<code>[Dict](#Dict)</code>) – The class labels for the target columns. Defaults to None.

###### validmind.vm_models.dataset.TorchDataset.add_extra_column

```python
add_extra_column(column_name, column_values=None)
```

Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.

**Parameters:**

- **column_name** (<code>[str](#str)</code>) – The name of the extra column.
- **column_values** (<code>[ndarray](#numpy.ndarray)</code>) – The values of the extra column.

###### validmind.vm_models.dataset.TorchDataset.assign_predictions

```python
assign_predictions(
    model,
    prediction_column=None,
    prediction_values=None,
    probability_column=None,
    probability_values=None,
    prediction_probabilities=None,
    **kwargs
)
```

Assign predictions and probabilities to the dataset.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model used to generate the predictions.
- **prediction_column** (<code>[str](#str)</code>) – The name of the column containing the predictions. Defaults to None.
- **prediction_values** (<code>[list](#list)</code>) – The values of the predictions. Defaults to None.
- **probability_column** (<code>[str](#str)</code>) – The name of the column containing the probabilities. Defaults to None.
- **probability_values** (<code>[list](#list)</code>) – The values of the probabilities. Defaults to None.
- **prediction_probabilities** (<code>[list](#list)</code>) – DEPRECATED: The values of the probabilities. Defaults to None.
- **kwargs** – Additional keyword arguments that will get passed through to the model's `predict` method.

###### validmind.vm_models.dataset.TorchDataset.column_aliases

```python
column_aliases = {}
```

###### validmind.vm_models.dataset.TorchDataset.columns

```python
columns = columns or []
```

###### validmind.vm_models.dataset.TorchDataset.df

```python
df: pd.DataFrame
```

Returns the dataset as a pandas DataFrame.

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: The dataset as a pandas DataFrame.

###### validmind.vm_models.dataset.TorchDataset.extra_columns

```python
extra_columns = ExtraColumns.from_dict(extra_columns)
```

###### validmind.vm_models.dataset.TorchDataset.index

```python
index = index
```

###### validmind.vm_models.dataset.TorchDataset.input_id

```python
input_id = input_id
```

###### validmind.vm_models.dataset.TorchDataset.prediction_column

```python
prediction_column(model, column_name=None)
```

Get or set the prediction column for a model.

###### validmind.vm_models.dataset.TorchDataset.probability_column

```python
probability_column(model, column_name=None)
```

Get or set the probability column for a model.

###### validmind.vm_models.dataset.TorchDataset.target_class_labels

```python
target_class_labels = target_class_labels
```

###### validmind.vm_models.dataset.TorchDataset.target_classes

```python
target_classes()
```

Returns the target class labels or unique values of the target column.

###### validmind.vm_models.dataset.TorchDataset.target_column

```python
target_column = target_column
```

###### validmind.vm_models.dataset.TorchDataset.text_column

```python
text_column = text_column
```

###### validmind.vm_models.dataset.TorchDataset.with_options

```python
with_options(**kwargs)
```

Support options provided when passing an input to run_test or run_test_suite

Example:

```python
# to only use a certain subset of columns in the dataset:
run_test(
    "validmind.SomeTestID",
    inputs={
        "dataset": {
            "input_id": "my_dataset_id",
            "columns": ["col1", "col2"],
        }
    }
)

# behind the scenes, this retrieves the dataset object (VMDataset) from the registry
# and then calls the `with_options()` method and passes `{"columns": ...}`
```

**Parameters:**

- \*\***kwargs** – Options:
- columns: Filter columns in the dataset

**Returns:**

- **VMDataset** (<code>[VMDataset](#validmind.vm_models.dataset.dataset.VMDataset)</code>) – A new instance of the dataset with only the specified columns

###### validmind.vm_models.dataset.TorchDataset.x

```python
x: np.ndarray
```

Returns the input features (X) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The input features.

###### validmind.vm_models.dataset.TorchDataset.x_df

```python
x_df()
```

Returns a dataframe containing only the feature columns

###### validmind.vm_models.dataset.TorchDataset.y

```python
y: np.ndarray
```

Returns the target variables (y) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The target variables.

###### validmind.vm_models.dataset.TorchDataset.y_df

```python
y_df()
```

Returns a dataframe containing the target column

###### validmind.vm_models.dataset.TorchDataset.y_pred

```python
y_pred(model)
```

Returns the predictions for a given model.

Attempts to stack complex prediction types (e.g., embeddings) into a single,
multi-dimensional array.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The predictions for the model

###### validmind.vm_models.dataset.TorchDataset.y_pred_df

```python
y_pred_df(model)
```

Returns a dataframe containing the predictions for a given model

###### validmind.vm_models.dataset.TorchDataset.y_prob

```python
y_prob(model)
```

Returns the probabilities for a given model.

**Parameters:**

- **model** (<code>[str](#str)</code>) – The ID of the model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The probability variables.

###### validmind.vm_models.dataset.TorchDataset.y_prob_df

```python
y_prob_df(model)
```

Returns a dataframe containing the probabilities for a given model

##### validmind.vm_models.dataset.VMDataset

```python
VMDataset(
    raw_dataset,
    input_id=None,
    model=None,
    index=None,
    index_name=None,
    date_time_index=False,
    columns=None,
    target_column=None,
    feature_columns=None,
    text_column=None,
    extra_columns=None,
    target_class_labels=None,
)
```

Bases: <code>[VMInput](#validmind.vm_models.input.VMInput)</code>

Base class for VM datasets

Child classes should be used to support new dataset types (tensor, polars etc)
by converting the user's dataset into a numpy array collecting metadata like
column names and then call this (parent) class `__init__` method.

This way we can support multiple dataset types but under the hood we only
need to work with numpy arrays and pandas dataframes in this class.

**Attributes:**

- [**raw_dataset**](#validmind.vm_models.dataset.VMDataset.raw_dataset) (<code>[ndarray](#numpy.ndarray)</code>) – The raw dataset as a NumPy array.
- [**input_id**](#validmind.vm_models.dataset.VMDataset.input_id) (<code>[str](#str)</code>) – Identifier for the dataset.
- [**index**](#validmind.vm_models.dataset.VMDataset.index) (<code>[ndarray](#numpy.ndarray)</code>) – The raw dataset index as a NumPy array.
- [**columns**](#validmind.vm_models.dataset.VMDataset.columns) (<code>[Set](#Set)\[[str](#str)\]</code>) – The column names of the dataset.
- [**target_column**](#validmind.vm_models.dataset.VMDataset.target_column) (<code>[str](#str)</code>) – The target column name of the dataset.
- [**feature_columns**](#validmind.vm_models.dataset.VMDataset.feature_columns) (<code>[List](#List)\[[str](#str)\]</code>) – The feature column names of the dataset.
- [**feature_columns_numeric**](#validmind.vm_models.dataset.VMDataset.feature_columns_numeric) (<code>[List](#List)\[[str](#str)\]</code>) – The numeric feature column names of the dataset.
- [**feature_columns_categorical**](#validmind.vm_models.dataset.VMDataset.feature_columns_categorical) (<code>[List](#List)\[[str](#str)\]</code>) – The categorical feature column names of the dataset.
- [**text_column**](#validmind.vm_models.dataset.VMDataset.text_column) (<code>[str](#str)</code>) – The text column name of the dataset for NLP tasks.
- [**target_class_labels**](#validmind.vm_models.dataset.VMDataset.target_class_labels) (<code>[Dict](#Dict)</code>) – The class labels for the target columns.
- [**df**](#validmind.vm_models.dataset.VMDataset.df) (<code>[DataFrame](#pandas.DataFrame)</code>) – The dataset as a pandas DataFrame.
- [**extra_columns**](#validmind.vm_models.dataset.VMDataset.extra_columns) (<code>[Dict](#Dict)</code>) – Extra columns to include in the dataset.

**Functions:**

- [**add_extra_column**](#validmind.vm_models.dataset.VMDataset.add_extra_column) – Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.
- [**assign_predictions**](#validmind.vm_models.dataset.VMDataset.assign_predictions) – Assign predictions and probabilities to the dataset.
- [**prediction_column**](#validmind.vm_models.dataset.VMDataset.prediction_column) – Get or set the prediction column for a model.
- [**probability_column**](#validmind.vm_models.dataset.VMDataset.probability_column) – Get or set the probability column for a model.
- [**target_classes**](#validmind.vm_models.dataset.VMDataset.target_classes) – Returns the target class labels or unique values of the target column.
- [**with_options**](#validmind.vm_models.dataset.VMDataset.with_options) – Support options provided when passing an input to run_test or run_test_suite
- [**x_df**](#validmind.vm_models.dataset.VMDataset.x_df) – Returns a dataframe containing only the feature columns
- [**y_df**](#validmind.vm_models.dataset.VMDataset.y_df) – Returns a dataframe containing the target column
- [**y_pred**](#validmind.vm_models.dataset.VMDataset.y_pred) – Returns the predictions for a given model.
- [**y_pred_df**](#validmind.vm_models.dataset.VMDataset.y_pred_df) – Returns a dataframe containing the predictions for a given model
- [**y_prob**](#validmind.vm_models.dataset.VMDataset.y_prob) – Returns the probabilities for a given model.
- [**y_prob_df**](#validmind.vm_models.dataset.VMDataset.y_prob_df) – Returns a dataframe containing the probabilities for a given model

**Attributes:**

- [**column_aliases**](#validmind.vm_models.dataset.VMDataset.column_aliases) –
- [**columns**](#validmind.vm_models.dataset.VMDataset.columns) –
- [**df**](#validmind.vm_models.dataset.VMDataset.df) (<code>[DataFrame](#pandas.DataFrame)</code>) – Returns the dataset as a pandas DataFrame.
- [**extra_columns**](#validmind.vm_models.dataset.VMDataset.extra_columns) –
- [**index**](#validmind.vm_models.dataset.VMDataset.index) –
- [**input_id**](#validmind.vm_models.dataset.VMDataset.input_id) –
- [**target_class_labels**](#validmind.vm_models.dataset.VMDataset.target_class_labels) –
- [**target_column**](#validmind.vm_models.dataset.VMDataset.target_column) –
- [**text_column**](#validmind.vm_models.dataset.VMDataset.text_column) –
- [**x**](#validmind.vm_models.dataset.VMDataset.x) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the input features (X) of the dataset.
- [**y**](#validmind.vm_models.dataset.VMDataset.y) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the target variables (y) of the dataset.

Initializes a VMDataset instance.

**Parameters:**

- **raw_dataset** (<code>[ndarray](#numpy.ndarray)</code>) – The raw dataset as a NumPy array.
- **input_id** (<code>[str](#str)</code>) – Identifier for the dataset.
- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – Model associated with the dataset.
- **index** (<code>[ndarray](#numpy.ndarray)</code>) – The raw dataset index as a NumPy array.
- **index_name** (<code>[str](#str)</code>) – The raw dataset index name as a NumPy array.
- **date_time_index** (<code>[bool](#bool)</code>) – Whether the index is a datetime index.
- **columns** (<code>[List](#List)\[[str](#str)\]</code>) – The column names of the dataset. Defaults to None.
- **target_column** (<code>[str](#str)</code>) – The target column name of the dataset. Defaults to None.
- **feature_columns** (<code>[str](#str)</code>) – The feature column names of the dataset. Defaults to None.
- **text_column** (<code>[str](#str)</code>) – The text column name of the dataset for nlp tasks. Defaults to None.
- **target_class_labels** (<code>[Dict](#Dict)</code>) – The class labels for the target columns. Defaults to None.

###### validmind.vm_models.dataset.VMDataset.add_extra_column

```python
add_extra_column(column_name, column_values=None)
```

Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.

**Parameters:**

- **column_name** (<code>[str](#str)</code>) – The name of the extra column.
- **column_values** (<code>[ndarray](#numpy.ndarray)</code>) – The values of the extra column.

###### validmind.vm_models.dataset.VMDataset.assign_predictions

```python
assign_predictions(
    model,
    prediction_column=None,
    prediction_values=None,
    probability_column=None,
    probability_values=None,
    prediction_probabilities=None,
    **kwargs
)
```

Assign predictions and probabilities to the dataset.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model used to generate the predictions.
- **prediction_column** (<code>[str](#str)</code>) – The name of the column containing the predictions. Defaults to None.
- **prediction_values** (<code>[list](#list)</code>) – The values of the predictions. Defaults to None.
- **probability_column** (<code>[str](#str)</code>) – The name of the column containing the probabilities. Defaults to None.
- **probability_values** (<code>[list](#list)</code>) – The values of the probabilities. Defaults to None.
- **prediction_probabilities** (<code>[list](#list)</code>) – DEPRECATED: The values of the probabilities. Defaults to None.
- **kwargs** – Additional keyword arguments that will get passed through to the model's `predict` method.

###### validmind.vm_models.dataset.VMDataset.column_aliases

```python
column_aliases = {}
```

###### validmind.vm_models.dataset.VMDataset.columns

```python
columns = columns or []
```

###### validmind.vm_models.dataset.VMDataset.df

```python
df: pd.DataFrame
```

Returns the dataset as a pandas DataFrame.

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: The dataset as a pandas DataFrame.

###### validmind.vm_models.dataset.VMDataset.extra_columns

```python
extra_columns = ExtraColumns.from_dict(extra_columns)
```

###### validmind.vm_models.dataset.VMDataset.index

```python
index = index
```

###### validmind.vm_models.dataset.VMDataset.input_id

```python
input_id = input_id
```

###### validmind.vm_models.dataset.VMDataset.prediction_column

```python
prediction_column(model, column_name=None)
```

Get or set the prediction column for a model.

###### validmind.vm_models.dataset.VMDataset.probability_column

```python
probability_column(model, column_name=None)
```

Get or set the probability column for a model.

###### validmind.vm_models.dataset.VMDataset.target_class_labels

```python
target_class_labels = target_class_labels
```

###### validmind.vm_models.dataset.VMDataset.target_classes

```python
target_classes()
```

Returns the target class labels or unique values of the target column.

###### validmind.vm_models.dataset.VMDataset.target_column

```python
target_column = target_column
```

###### validmind.vm_models.dataset.VMDataset.text_column

```python
text_column = text_column
```

###### validmind.vm_models.dataset.VMDataset.with_options

```python
with_options(**kwargs)
```

Support options provided when passing an input to run_test or run_test_suite

Example:

```python
# to only use a certain subset of columns in the dataset:
run_test(
    "validmind.SomeTestID",
    inputs={
        "dataset": {
            "input_id": "my_dataset_id",
            "columns": ["col1", "col2"],
        }
    }
)

# behind the scenes, this retrieves the dataset object (VMDataset) from the registry
# and then calls the `with_options()` method and passes `{"columns": ...}`
```

**Parameters:**

- \*\***kwargs** – Options:
- columns: Filter columns in the dataset

**Returns:**

- **VMDataset** (<code>[VMDataset](#validmind.vm_models.dataset.dataset.VMDataset)</code>) – A new instance of the dataset with only the specified columns

###### validmind.vm_models.dataset.VMDataset.x

```python
x: np.ndarray
```

Returns the input features (X) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The input features.

###### validmind.vm_models.dataset.VMDataset.x_df

```python
x_df()
```

Returns a dataframe containing only the feature columns

###### validmind.vm_models.dataset.VMDataset.y

```python
y: np.ndarray
```

Returns the target variables (y) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The target variables.

###### validmind.vm_models.dataset.VMDataset.y_df

```python
y_df()
```

Returns a dataframe containing the target column

###### validmind.vm_models.dataset.VMDataset.y_pred

```python
y_pred(model)
```

Returns the predictions for a given model.

Attempts to stack complex prediction types (e.g., embeddings) into a single,
multi-dimensional array.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The predictions for the model

###### validmind.vm_models.dataset.VMDataset.y_pred_df

```python
y_pred_df(model)
```

Returns a dataframe containing the predictions for a given model

###### validmind.vm_models.dataset.VMDataset.y_prob

```python
y_prob(model)
```

Returns the probabilities for a given model.

**Parameters:**

- **model** (<code>[str](#str)</code>) – The ID of the model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The probability variables.

###### validmind.vm_models.dataset.VMDataset.y_prob_df

```python
y_prob_df(model)
```

Returns a dataframe containing the probabilities for a given model

##### validmind.vm_models.dataset.dataset

Dataset class wrapper

**Classes:**

- [**DataFrameDataset**](#validmind.vm_models.dataset.dataset.DataFrameDataset) – VM dataset implementation for pandas DataFrame.
- [**PolarsDataset**](#validmind.vm_models.dataset.dataset.PolarsDataset) – VM dataset implementation for Polars DataFrame.
- [**TorchDataset**](#validmind.vm_models.dataset.dataset.TorchDataset) – VM dataset implementation for PyTorch Datasets.
- [**VMDataset**](#validmind.vm_models.dataset.dataset.VMDataset) – Base class for VM datasets

**Attributes:**

- [**logger**](#validmind.vm_models.dataset.dataset.logger) –

###### validmind.vm_models.dataset.dataset.DataFrameDataset

```python
DataFrameDataset(
    raw_dataset,
    input_id=None,
    model=None,
    target_column=None,
    extra_columns=None,
    feature_columns=None,
    text_column=None,
    target_class_labels=None,
    date_time_index=False,
)
```

Bases: <code>[VMDataset](#validmind.vm_models.dataset.dataset.VMDataset)</code>

VM dataset implementation for pandas DataFrame.

**Functions:**

- [**add_extra_column**](#validmind.vm_models.dataset.dataset.DataFrameDataset.add_extra_column) – Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.
- [**assign_predictions**](#validmind.vm_models.dataset.dataset.DataFrameDataset.assign_predictions) – Assign predictions and probabilities to the dataset.
- [**prediction_column**](#validmind.vm_models.dataset.dataset.DataFrameDataset.prediction_column) – Get or set the prediction column for a model.
- [**probability_column**](#validmind.vm_models.dataset.dataset.DataFrameDataset.probability_column) – Get or set the probability column for a model.
- [**target_classes**](#validmind.vm_models.dataset.dataset.DataFrameDataset.target_classes) – Returns the target class labels or unique values of the target column.
- [**with_options**](#validmind.vm_models.dataset.dataset.DataFrameDataset.with_options) – Support options provided when passing an input to run_test or run_test_suite
- [**x_df**](#validmind.vm_models.dataset.dataset.DataFrameDataset.x_df) – Returns a dataframe containing only the feature columns
- [**y_df**](#validmind.vm_models.dataset.dataset.DataFrameDataset.y_df) – Returns a dataframe containing the target column
- [**y_pred**](#validmind.vm_models.dataset.dataset.DataFrameDataset.y_pred) – Returns the predictions for a given model.
- [**y_pred_df**](#validmind.vm_models.dataset.dataset.DataFrameDataset.y_pred_df) – Returns a dataframe containing the predictions for a given model
- [**y_prob**](#validmind.vm_models.dataset.dataset.DataFrameDataset.y_prob) – Returns the probabilities for a given model.
- [**y_prob_df**](#validmind.vm_models.dataset.dataset.DataFrameDataset.y_prob_df) – Returns a dataframe containing the probabilities for a given model

**Attributes:**

- [**column_aliases**](#validmind.vm_models.dataset.dataset.DataFrameDataset.column_aliases) –
- [**columns**](#validmind.vm_models.dataset.dataset.DataFrameDataset.columns) –
- [**df**](#validmind.vm_models.dataset.dataset.DataFrameDataset.df) (<code>[DataFrame](#pandas.DataFrame)</code>) – Returns the dataset as a pandas DataFrame.
- [**extra_columns**](#validmind.vm_models.dataset.dataset.DataFrameDataset.extra_columns) –
- [**index**](#validmind.vm_models.dataset.dataset.DataFrameDataset.index) –
- [**input_id**](#validmind.vm_models.dataset.dataset.DataFrameDataset.input_id) –
- [**target_class_labels**](#validmind.vm_models.dataset.dataset.DataFrameDataset.target_class_labels) –
- [**target_column**](#validmind.vm_models.dataset.dataset.DataFrameDataset.target_column) –
- [**text_column**](#validmind.vm_models.dataset.dataset.DataFrameDataset.text_column) –
- [**x**](#validmind.vm_models.dataset.dataset.DataFrameDataset.x) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the input features (X) of the dataset.
- [**y**](#validmind.vm_models.dataset.dataset.DataFrameDataset.y) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the target variables (y) of the dataset.

Initializes a DataFrameDataset instance.

**Parameters:**

- **raw_dataset** (<code>[DataFrame](#pandas.DataFrame)</code>) – The raw dataset as a pandas DataFrame.
- **input_id** (<code>[str](#str)</code>) – Identifier for the dataset. Defaults to None.
- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – Model associated with the dataset. Defaults to None.
- **target_column** (<code>[str](#str)</code>) – The target column of the dataset. Defaults to None.
- **extra_columns** (<code>[dict](#dict)</code>) – Extra columns to include in the dataset. Defaults to None.
- **feature_columns** (<code>[list](#list)</code>) – The feature columns of the dataset. Defaults to None.
- **text_column** (<code>[str](#str)</code>) – The text column name of the dataset for NLP tasks. Defaults to None.
- **target_class_labels** (<code>[dict](#dict)</code>) – The class labels for the target columns. Defaults to None.
- **date_time_index** (<code>[bool](#bool)</code>) – Whether to use date-time index. Defaults to False.

####### validmind.vm_models.dataset.dataset.DataFrameDataset.add_extra_column

```python
add_extra_column(column_name, column_values=None)
```

Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.

**Parameters:**

- **column_name** (<code>[str](#str)</code>) – The name of the extra column.
- **column_values** (<code>[ndarray](#numpy.ndarray)</code>) – The values of the extra column.

####### validmind.vm_models.dataset.dataset.DataFrameDataset.assign_predictions

```python
assign_predictions(
    model,
    prediction_column=None,
    prediction_values=None,
    probability_column=None,
    probability_values=None,
    prediction_probabilities=None,
    **kwargs
)
```

Assign predictions and probabilities to the dataset.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model used to generate the predictions.
- **prediction_column** (<code>[str](#str)</code>) – The name of the column containing the predictions. Defaults to None.
- **prediction_values** (<code>[list](#list)</code>) – The values of the predictions. Defaults to None.
- **probability_column** (<code>[str](#str)</code>) – The name of the column containing the probabilities. Defaults to None.
- **probability_values** (<code>[list](#list)</code>) – The values of the probabilities. Defaults to None.
- **prediction_probabilities** (<code>[list](#list)</code>) – DEPRECATED: The values of the probabilities. Defaults to None.
- **kwargs** – Additional keyword arguments that will get passed through to the model's `predict` method.

####### validmind.vm_models.dataset.dataset.DataFrameDataset.column_aliases

```python
column_aliases = {}
```

####### validmind.vm_models.dataset.dataset.DataFrameDataset.columns

```python
columns = columns or []
```

####### validmind.vm_models.dataset.dataset.DataFrameDataset.df

```python
df: pd.DataFrame
```

Returns the dataset as a pandas DataFrame.

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: The dataset as a pandas DataFrame.

####### validmind.vm_models.dataset.dataset.DataFrameDataset.extra_columns

```python
extra_columns = ExtraColumns.from_dict(extra_columns)
```

####### validmind.vm_models.dataset.dataset.DataFrameDataset.index

```python
index = index
```

####### validmind.vm_models.dataset.dataset.DataFrameDataset.input_id

```python
input_id = input_id
```

####### validmind.vm_models.dataset.dataset.DataFrameDataset.prediction_column

```python
prediction_column(model, column_name=None)
```

Get or set the prediction column for a model.

####### validmind.vm_models.dataset.dataset.DataFrameDataset.probability_column

```python
probability_column(model, column_name=None)
```

Get or set the probability column for a model.

####### validmind.vm_models.dataset.dataset.DataFrameDataset.target_class_labels

```python
target_class_labels = target_class_labels
```

####### validmind.vm_models.dataset.dataset.DataFrameDataset.target_classes

```python
target_classes()
```

Returns the target class labels or unique values of the target column.

####### validmind.vm_models.dataset.dataset.DataFrameDataset.target_column

```python
target_column = target_column
```

####### validmind.vm_models.dataset.dataset.DataFrameDataset.text_column

```python
text_column = text_column
```

####### validmind.vm_models.dataset.dataset.DataFrameDataset.with_options

```python
with_options(**kwargs)
```

Support options provided when passing an input to run_test or run_test_suite

Example:

```python
# to only use a certain subset of columns in the dataset:
run_test(
    "validmind.SomeTestID",
    inputs={
        "dataset": {
            "input_id": "my_dataset_id",
            "columns": ["col1", "col2"],
        }
    }
)

# behind the scenes, this retrieves the dataset object (VMDataset) from the registry
# and then calls the `with_options()` method and passes `{"columns": ...}`
```

**Parameters:**

- \*\***kwargs** – Options:
- columns: Filter columns in the dataset

**Returns:**

- **VMDataset** (<code>[VMDataset](#validmind.vm_models.dataset.dataset.VMDataset)</code>) – A new instance of the dataset with only the specified columns

####### validmind.vm_models.dataset.dataset.DataFrameDataset.x

```python
x: np.ndarray
```

Returns the input features (X) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The input features.

####### validmind.vm_models.dataset.dataset.DataFrameDataset.x_df

```python
x_df()
```

Returns a dataframe containing only the feature columns

####### validmind.vm_models.dataset.dataset.DataFrameDataset.y

```python
y: np.ndarray
```

Returns the target variables (y) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The target variables.

####### validmind.vm_models.dataset.dataset.DataFrameDataset.y_df

```python
y_df()
```

Returns a dataframe containing the target column

####### validmind.vm_models.dataset.dataset.DataFrameDataset.y_pred

```python
y_pred(model)
```

Returns the predictions for a given model.

Attempts to stack complex prediction types (e.g., embeddings) into a single,
multi-dimensional array.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The predictions for the model

####### validmind.vm_models.dataset.dataset.DataFrameDataset.y_pred_df

```python
y_pred_df(model)
```

Returns a dataframe containing the predictions for a given model

####### validmind.vm_models.dataset.dataset.DataFrameDataset.y_prob

```python
y_prob(model)
```

Returns the probabilities for a given model.

**Parameters:**

- **model** (<code>[str](#str)</code>) – The ID of the model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The probability variables.

####### validmind.vm_models.dataset.dataset.DataFrameDataset.y_prob_df

```python
y_prob_df(model)
```

Returns a dataframe containing the probabilities for a given model

###### validmind.vm_models.dataset.dataset.PolarsDataset

```python
PolarsDataset(
    raw_dataset,
    input_id=None,
    model=None,
    target_column=None,
    extra_columns=None,
    feature_columns=None,
    text_column=None,
    target_class_labels=None,
    date_time_index=False,
)
```

Bases: <code>[VMDataset](#validmind.vm_models.dataset.dataset.VMDataset)</code>

VM dataset implementation for Polars DataFrame.

**Functions:**

- [**add_extra_column**](#validmind.vm_models.dataset.dataset.PolarsDataset.add_extra_column) – Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.
- [**assign_predictions**](#validmind.vm_models.dataset.dataset.PolarsDataset.assign_predictions) – Assign predictions and probabilities to the dataset.
- [**prediction_column**](#validmind.vm_models.dataset.dataset.PolarsDataset.prediction_column) – Get or set the prediction column for a model.
- [**probability_column**](#validmind.vm_models.dataset.dataset.PolarsDataset.probability_column) – Get or set the probability column for a model.
- [**target_classes**](#validmind.vm_models.dataset.dataset.PolarsDataset.target_classes) – Returns the target class labels or unique values of the target column.
- [**with_options**](#validmind.vm_models.dataset.dataset.PolarsDataset.with_options) – Support options provided when passing an input to run_test or run_test_suite
- [**x_df**](#validmind.vm_models.dataset.dataset.PolarsDataset.x_df) – Returns a dataframe containing only the feature columns
- [**y_df**](#validmind.vm_models.dataset.dataset.PolarsDataset.y_df) – Returns a dataframe containing the target column
- [**y_pred**](#validmind.vm_models.dataset.dataset.PolarsDataset.y_pred) – Returns the predictions for a given model.
- [**y_pred_df**](#validmind.vm_models.dataset.dataset.PolarsDataset.y_pred_df) – Returns a dataframe containing the predictions for a given model
- [**y_prob**](#validmind.vm_models.dataset.dataset.PolarsDataset.y_prob) – Returns the probabilities for a given model.
- [**y_prob_df**](#validmind.vm_models.dataset.dataset.PolarsDataset.y_prob_df) – Returns a dataframe containing the probabilities for a given model

**Attributes:**

- [**column_aliases**](#validmind.vm_models.dataset.dataset.PolarsDataset.column_aliases) –
- [**columns**](#validmind.vm_models.dataset.dataset.PolarsDataset.columns) –
- [**df**](#validmind.vm_models.dataset.dataset.PolarsDataset.df) (<code>[DataFrame](#pandas.DataFrame)</code>) – Returns the dataset as a pandas DataFrame.
- [**extra_columns**](#validmind.vm_models.dataset.dataset.PolarsDataset.extra_columns) –
- [**index**](#validmind.vm_models.dataset.dataset.PolarsDataset.index) –
- [**input_id**](#validmind.vm_models.dataset.dataset.PolarsDataset.input_id) –
- [**target_class_labels**](#validmind.vm_models.dataset.dataset.PolarsDataset.target_class_labels) –
- [**target_column**](#validmind.vm_models.dataset.dataset.PolarsDataset.target_column) –
- [**text_column**](#validmind.vm_models.dataset.dataset.PolarsDataset.text_column) –
- [**x**](#validmind.vm_models.dataset.dataset.PolarsDataset.x) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the input features (X) of the dataset.
- [**y**](#validmind.vm_models.dataset.dataset.PolarsDataset.y) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the target variables (y) of the dataset.

Initializes a PolarsDataset instance.

**Parameters:**

- **raw_dataset** (<code>[DataFrame](#polars.DataFrame)</code>) – The raw dataset as a Polars DataFrame.
- **input_id** (<code>[str](#str)</code>) – Identifier for the dataset. Defaults to None.
- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – Model associated with the dataset. Defaults to None.
- **target_column** (<code>[str](#str)</code>) – The target column of the dataset. Defaults to None.
- **extra_columns** (<code>[dict](#dict)</code>) – Extra columns to include in the dataset. Defaults to None.
- **feature_columns** (<code>[list](#list)</code>) – The feature columns of the dataset. Defaults to None.
- **text_column** (<code>[str](#str)</code>) – The text column name of the dataset for NLP tasks. Defaults to None.
- **target_class_labels** (<code>[dict](#dict)</code>) – The class labels for the target columns. Defaults to None.
- **date_time_index** (<code>[bool](#bool)</code>) – Whether to use date-time index. Defaults to False.

####### validmind.vm_models.dataset.dataset.PolarsDataset.add_extra_column

```python
add_extra_column(column_name, column_values=None)
```

Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.

**Parameters:**

- **column_name** (<code>[str](#str)</code>) – The name of the extra column.
- **column_values** (<code>[ndarray](#numpy.ndarray)</code>) – The values of the extra column.

####### validmind.vm_models.dataset.dataset.PolarsDataset.assign_predictions

```python
assign_predictions(
    model,
    prediction_column=None,
    prediction_values=None,
    probability_column=None,
    probability_values=None,
    prediction_probabilities=None,
    **kwargs
)
```

Assign predictions and probabilities to the dataset.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model used to generate the predictions.
- **prediction_column** (<code>[str](#str)</code>) – The name of the column containing the predictions. Defaults to None.
- **prediction_values** (<code>[list](#list)</code>) – The values of the predictions. Defaults to None.
- **probability_column** (<code>[str](#str)</code>) – The name of the column containing the probabilities. Defaults to None.
- **probability_values** (<code>[list](#list)</code>) – The values of the probabilities. Defaults to None.
- **prediction_probabilities** (<code>[list](#list)</code>) – DEPRECATED: The values of the probabilities. Defaults to None.
- **kwargs** – Additional keyword arguments that will get passed through to the model's `predict` method.

####### validmind.vm_models.dataset.dataset.PolarsDataset.column_aliases

```python
column_aliases = {}
```

####### validmind.vm_models.dataset.dataset.PolarsDataset.columns

```python
columns = columns or []
```

####### validmind.vm_models.dataset.dataset.PolarsDataset.df

```python
df: pd.DataFrame
```

Returns the dataset as a pandas DataFrame.

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: The dataset as a pandas DataFrame.

####### validmind.vm_models.dataset.dataset.PolarsDataset.extra_columns

```python
extra_columns = ExtraColumns.from_dict(extra_columns)
```

####### validmind.vm_models.dataset.dataset.PolarsDataset.index

```python
index = index
```

####### validmind.vm_models.dataset.dataset.PolarsDataset.input_id

```python
input_id = input_id
```

####### validmind.vm_models.dataset.dataset.PolarsDataset.prediction_column

```python
prediction_column(model, column_name=None)
```

Get or set the prediction column for a model.

####### validmind.vm_models.dataset.dataset.PolarsDataset.probability_column

```python
probability_column(model, column_name=None)
```

Get or set the probability column for a model.

####### validmind.vm_models.dataset.dataset.PolarsDataset.target_class_labels

```python
target_class_labels = target_class_labels
```

####### validmind.vm_models.dataset.dataset.PolarsDataset.target_classes

```python
target_classes()
```

Returns the target class labels or unique values of the target column.

####### validmind.vm_models.dataset.dataset.PolarsDataset.target_column

```python
target_column = target_column
```

####### validmind.vm_models.dataset.dataset.PolarsDataset.text_column

```python
text_column = text_column
```

####### validmind.vm_models.dataset.dataset.PolarsDataset.with_options

```python
with_options(**kwargs)
```

Support options provided when passing an input to run_test or run_test_suite

Example:

```python
# to only use a certain subset of columns in the dataset:
run_test(
    "validmind.SomeTestID",
    inputs={
        "dataset": {
            "input_id": "my_dataset_id",
            "columns": ["col1", "col2"],
        }
    }
)

# behind the scenes, this retrieves the dataset object (VMDataset) from the registry
# and then calls the `with_options()` method and passes `{"columns": ...}`
```

**Parameters:**

- \*\***kwargs** – Options:
- columns: Filter columns in the dataset

**Returns:**

- **VMDataset** (<code>[VMDataset](#validmind.vm_models.dataset.dataset.VMDataset)</code>) – A new instance of the dataset with only the specified columns

####### validmind.vm_models.dataset.dataset.PolarsDataset.x

```python
x: np.ndarray
```

Returns the input features (X) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The input features.

####### validmind.vm_models.dataset.dataset.PolarsDataset.x_df

```python
x_df()
```

Returns a dataframe containing only the feature columns

####### validmind.vm_models.dataset.dataset.PolarsDataset.y

```python
y: np.ndarray
```

Returns the target variables (y) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The target variables.

####### validmind.vm_models.dataset.dataset.PolarsDataset.y_df

```python
y_df()
```

Returns a dataframe containing the target column

####### validmind.vm_models.dataset.dataset.PolarsDataset.y_pred

```python
y_pred(model)
```

Returns the predictions for a given model.

Attempts to stack complex prediction types (e.g., embeddings) into a single,
multi-dimensional array.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The predictions for the model

####### validmind.vm_models.dataset.dataset.PolarsDataset.y_pred_df

```python
y_pred_df(model)
```

Returns a dataframe containing the predictions for a given model

####### validmind.vm_models.dataset.dataset.PolarsDataset.y_prob

```python
y_prob(model)
```

Returns the probabilities for a given model.

**Parameters:**

- **model** (<code>[str](#str)</code>) – The ID of the model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The probability variables.

####### validmind.vm_models.dataset.dataset.PolarsDataset.y_prob_df

```python
y_prob_df(model)
```

Returns a dataframe containing the probabilities for a given model

###### validmind.vm_models.dataset.dataset.TorchDataset

```python
TorchDataset(
    raw_dataset,
    input_id=None,
    model=None,
    index_name=None,
    index=None,
    columns=None,
    target_column=None,
    extra_columns=None,
    feature_columns=None,
    text_column=None,
    target_class_labels=None,
)
```

Bases: <code>[VMDataset](#validmind.vm_models.dataset.dataset.VMDataset)</code>

VM dataset implementation for PyTorch Datasets.

**Functions:**

- [**add_extra_column**](#validmind.vm_models.dataset.dataset.TorchDataset.add_extra_column) – Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.
- [**assign_predictions**](#validmind.vm_models.dataset.dataset.TorchDataset.assign_predictions) – Assign predictions and probabilities to the dataset.
- [**prediction_column**](#validmind.vm_models.dataset.dataset.TorchDataset.prediction_column) – Get or set the prediction column for a model.
- [**probability_column**](#validmind.vm_models.dataset.dataset.TorchDataset.probability_column) – Get or set the probability column for a model.
- [**target_classes**](#validmind.vm_models.dataset.dataset.TorchDataset.target_classes) – Returns the target class labels or unique values of the target column.
- [**with_options**](#validmind.vm_models.dataset.dataset.TorchDataset.with_options) – Support options provided when passing an input to run_test or run_test_suite
- [**x_df**](#validmind.vm_models.dataset.dataset.TorchDataset.x_df) – Returns a dataframe containing only the feature columns
- [**y_df**](#validmind.vm_models.dataset.dataset.TorchDataset.y_df) – Returns a dataframe containing the target column
- [**y_pred**](#validmind.vm_models.dataset.dataset.TorchDataset.y_pred) – Returns the predictions for a given model.
- [**y_pred_df**](#validmind.vm_models.dataset.dataset.TorchDataset.y_pred_df) – Returns a dataframe containing the predictions for a given model
- [**y_prob**](#validmind.vm_models.dataset.dataset.TorchDataset.y_prob) – Returns the probabilities for a given model.
- [**y_prob_df**](#validmind.vm_models.dataset.dataset.TorchDataset.y_prob_df) – Returns a dataframe containing the probabilities for a given model

**Attributes:**

- [**column_aliases**](#validmind.vm_models.dataset.dataset.TorchDataset.column_aliases) –
- [**columns**](#validmind.vm_models.dataset.dataset.TorchDataset.columns) –
- [**df**](#validmind.vm_models.dataset.dataset.TorchDataset.df) (<code>[DataFrame](#pandas.DataFrame)</code>) – Returns the dataset as a pandas DataFrame.
- [**extra_columns**](#validmind.vm_models.dataset.dataset.TorchDataset.extra_columns) –
- [**index**](#validmind.vm_models.dataset.dataset.TorchDataset.index) –
- [**input_id**](#validmind.vm_models.dataset.dataset.TorchDataset.input_id) –
- [**target_class_labels**](#validmind.vm_models.dataset.dataset.TorchDataset.target_class_labels) –
- [**target_column**](#validmind.vm_models.dataset.dataset.TorchDataset.target_column) –
- [**text_column**](#validmind.vm_models.dataset.dataset.TorchDataset.text_column) –
- [**x**](#validmind.vm_models.dataset.dataset.TorchDataset.x) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the input features (X) of the dataset.
- [**y**](#validmind.vm_models.dataset.dataset.TorchDataset.y) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the target variables (y) of the dataset.

Initializes a TorchDataset instance.

**Parameters:**

- **raw_dataset** (<code>[Dataset](#torch.utils.data.Dataset)</code>) – The raw dataset as a PyTorch Dataset.
- **index_name** (<code>[str](#str)</code>) – The raw dataset index name.
- **index** (<code>[ndarray](#numpy.ndarray)</code>) – The raw dataset index as a NumPy array.
- **columns** (<code>[List](#List)\[[str](#str)\]</code>) – The column names of the dataset.
- **target_column** (<code>[str](#str)</code>) – The target column of the dataset. Defaults to None.
- **feature_columns** (<code>[list](#list)</code>) – The feature columns of the dataset. Defaults to None.
- **text_column** (<code>[str](#str)</code>) – The text column name of the dataset for nlp tasks. Defaults to None.
- **target_class_labels** (<code>[Dict](#Dict)</code>) – The class labels for the target columns. Defaults to None.

####### validmind.vm_models.dataset.dataset.TorchDataset.add_extra_column

```python
add_extra_column(column_name, column_values=None)
```

Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.

**Parameters:**

- **column_name** (<code>[str](#str)</code>) – The name of the extra column.
- **column_values** (<code>[ndarray](#numpy.ndarray)</code>) – The values of the extra column.

####### validmind.vm_models.dataset.dataset.TorchDataset.assign_predictions

```python
assign_predictions(
    model,
    prediction_column=None,
    prediction_values=None,
    probability_column=None,
    probability_values=None,
    prediction_probabilities=None,
    **kwargs
)
```

Assign predictions and probabilities to the dataset.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model used to generate the predictions.
- **prediction_column** (<code>[str](#str)</code>) – The name of the column containing the predictions. Defaults to None.
- **prediction_values** (<code>[list](#list)</code>) – The values of the predictions. Defaults to None.
- **probability_column** (<code>[str](#str)</code>) – The name of the column containing the probabilities. Defaults to None.
- **probability_values** (<code>[list](#list)</code>) – The values of the probabilities. Defaults to None.
- **prediction_probabilities** (<code>[list](#list)</code>) – DEPRECATED: The values of the probabilities. Defaults to None.
- **kwargs** – Additional keyword arguments that will get passed through to the model's `predict` method.

####### validmind.vm_models.dataset.dataset.TorchDataset.column_aliases

```python
column_aliases = {}
```

####### validmind.vm_models.dataset.dataset.TorchDataset.columns

```python
columns = columns or []
```

####### validmind.vm_models.dataset.dataset.TorchDataset.df

```python
df: pd.DataFrame
```

Returns the dataset as a pandas DataFrame.

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: The dataset as a pandas DataFrame.

####### validmind.vm_models.dataset.dataset.TorchDataset.extra_columns

```python
extra_columns = ExtraColumns.from_dict(extra_columns)
```

####### validmind.vm_models.dataset.dataset.TorchDataset.index

```python
index = index
```

####### validmind.vm_models.dataset.dataset.TorchDataset.input_id

```python
input_id = input_id
```

####### validmind.vm_models.dataset.dataset.TorchDataset.prediction_column

```python
prediction_column(model, column_name=None)
```

Get or set the prediction column for a model.

####### validmind.vm_models.dataset.dataset.TorchDataset.probability_column

```python
probability_column(model, column_name=None)
```

Get or set the probability column for a model.

####### validmind.vm_models.dataset.dataset.TorchDataset.target_class_labels

```python
target_class_labels = target_class_labels
```

####### validmind.vm_models.dataset.dataset.TorchDataset.target_classes

```python
target_classes()
```

Returns the target class labels or unique values of the target column.

####### validmind.vm_models.dataset.dataset.TorchDataset.target_column

```python
target_column = target_column
```

####### validmind.vm_models.dataset.dataset.TorchDataset.text_column

```python
text_column = text_column
```

####### validmind.vm_models.dataset.dataset.TorchDataset.with_options

```python
with_options(**kwargs)
```

Support options provided when passing an input to run_test or run_test_suite

Example:

```python
# to only use a certain subset of columns in the dataset:
run_test(
    "validmind.SomeTestID",
    inputs={
        "dataset": {
            "input_id": "my_dataset_id",
            "columns": ["col1", "col2"],
        }
    }
)

# behind the scenes, this retrieves the dataset object (VMDataset) from the registry
# and then calls the `with_options()` method and passes `{"columns": ...}`
```

**Parameters:**

- \*\***kwargs** – Options:
- columns: Filter columns in the dataset

**Returns:**

- **VMDataset** (<code>[VMDataset](#validmind.vm_models.dataset.dataset.VMDataset)</code>) – A new instance of the dataset with only the specified columns

####### validmind.vm_models.dataset.dataset.TorchDataset.x

```python
x: np.ndarray
```

Returns the input features (X) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The input features.

####### validmind.vm_models.dataset.dataset.TorchDataset.x_df

```python
x_df()
```

Returns a dataframe containing only the feature columns

####### validmind.vm_models.dataset.dataset.TorchDataset.y

```python
y: np.ndarray
```

Returns the target variables (y) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The target variables.

####### validmind.vm_models.dataset.dataset.TorchDataset.y_df

```python
y_df()
```

Returns a dataframe containing the target column

####### validmind.vm_models.dataset.dataset.TorchDataset.y_pred

```python
y_pred(model)
```

Returns the predictions for a given model.

Attempts to stack complex prediction types (e.g., embeddings) into a single,
multi-dimensional array.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The predictions for the model

####### validmind.vm_models.dataset.dataset.TorchDataset.y_pred_df

```python
y_pred_df(model)
```

Returns a dataframe containing the predictions for a given model

####### validmind.vm_models.dataset.dataset.TorchDataset.y_prob

```python
y_prob(model)
```

Returns the probabilities for a given model.

**Parameters:**

- **model** (<code>[str](#str)</code>) – The ID of the model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The probability variables.

####### validmind.vm_models.dataset.dataset.TorchDataset.y_prob_df

```python
y_prob_df(model)
```

Returns a dataframe containing the probabilities for a given model

###### validmind.vm_models.dataset.dataset.VMDataset

```python
VMDataset(
    raw_dataset,
    input_id=None,
    model=None,
    index=None,
    index_name=None,
    date_time_index=False,
    columns=None,
    target_column=None,
    feature_columns=None,
    text_column=None,
    extra_columns=None,
    target_class_labels=None,
)
```

Bases: <code>[VMInput](#validmind.vm_models.input.VMInput)</code>

Base class for VM datasets

Child classes should be used to support new dataset types (tensor, polars etc)
by converting the user's dataset into a numpy array collecting metadata like
column names and then call this (parent) class `__init__` method.

This way we can support multiple dataset types but under the hood we only
need to work with numpy arrays and pandas dataframes in this class.

**Attributes:**

- [**raw_dataset**](#validmind.vm_models.dataset.dataset.VMDataset.raw_dataset) (<code>[ndarray](#numpy.ndarray)</code>) – The raw dataset as a NumPy array.
- [**input_id**](#validmind.vm_models.dataset.dataset.VMDataset.input_id) (<code>[str](#str)</code>) – Identifier for the dataset.
- [**index**](#validmind.vm_models.dataset.dataset.VMDataset.index) (<code>[ndarray](#numpy.ndarray)</code>) – The raw dataset index as a NumPy array.
- [**columns**](#validmind.vm_models.dataset.dataset.VMDataset.columns) (<code>[Set](#Set)\[[str](#str)\]</code>) – The column names of the dataset.
- [**target_column**](#validmind.vm_models.dataset.dataset.VMDataset.target_column) (<code>[str](#str)</code>) – The target column name of the dataset.
- [**feature_columns**](#validmind.vm_models.dataset.dataset.VMDataset.feature_columns) (<code>[List](#List)\[[str](#str)\]</code>) – The feature column names of the dataset.
- [**feature_columns_numeric**](#validmind.vm_models.dataset.dataset.VMDataset.feature_columns_numeric) (<code>[List](#List)\[[str](#str)\]</code>) – The numeric feature column names of the dataset.
- [**feature_columns_categorical**](#validmind.vm_models.dataset.dataset.VMDataset.feature_columns_categorical) (<code>[List](#List)\[[str](#str)\]</code>) – The categorical feature column names of the dataset.
- [**text_column**](#validmind.vm_models.dataset.dataset.VMDataset.text_column) (<code>[str](#str)</code>) – The text column name of the dataset for NLP tasks.
- [**target_class_labels**](#validmind.vm_models.dataset.dataset.VMDataset.target_class_labels) (<code>[Dict](#Dict)</code>) – The class labels for the target columns.
- [**df**](#validmind.vm_models.dataset.dataset.VMDataset.df) (<code>[DataFrame](#pandas.DataFrame)</code>) – The dataset as a pandas DataFrame.
- [**extra_columns**](#validmind.vm_models.dataset.dataset.VMDataset.extra_columns) (<code>[Dict](#Dict)</code>) – Extra columns to include in the dataset.

**Functions:**

- [**add_extra_column**](#validmind.vm_models.dataset.dataset.VMDataset.add_extra_column) – Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.
- [**assign_predictions**](#validmind.vm_models.dataset.dataset.VMDataset.assign_predictions) – Assign predictions and probabilities to the dataset.
- [**prediction_column**](#validmind.vm_models.dataset.dataset.VMDataset.prediction_column) – Get or set the prediction column for a model.
- [**probability_column**](#validmind.vm_models.dataset.dataset.VMDataset.probability_column) – Get or set the probability column for a model.
- [**target_classes**](#validmind.vm_models.dataset.dataset.VMDataset.target_classes) – Returns the target class labels or unique values of the target column.
- [**with_options**](#validmind.vm_models.dataset.dataset.VMDataset.with_options) – Support options provided when passing an input to run_test or run_test_suite
- [**x_df**](#validmind.vm_models.dataset.dataset.VMDataset.x_df) – Returns a dataframe containing only the feature columns
- [**y_df**](#validmind.vm_models.dataset.dataset.VMDataset.y_df) – Returns a dataframe containing the target column
- [**y_pred**](#validmind.vm_models.dataset.dataset.VMDataset.y_pred) – Returns the predictions for a given model.
- [**y_pred_df**](#validmind.vm_models.dataset.dataset.VMDataset.y_pred_df) – Returns a dataframe containing the predictions for a given model
- [**y_prob**](#validmind.vm_models.dataset.dataset.VMDataset.y_prob) – Returns the probabilities for a given model.
- [**y_prob_df**](#validmind.vm_models.dataset.dataset.VMDataset.y_prob_df) – Returns a dataframe containing the probabilities for a given model

**Attributes:**

- [**column_aliases**](#validmind.vm_models.dataset.dataset.VMDataset.column_aliases) –
- [**columns**](#validmind.vm_models.dataset.dataset.VMDataset.columns) –
- [**df**](#validmind.vm_models.dataset.dataset.VMDataset.df) (<code>[DataFrame](#pandas.DataFrame)</code>) – Returns the dataset as a pandas DataFrame.
- [**extra_columns**](#validmind.vm_models.dataset.dataset.VMDataset.extra_columns) –
- [**index**](#validmind.vm_models.dataset.dataset.VMDataset.index) –
- [**input_id**](#validmind.vm_models.dataset.dataset.VMDataset.input_id) –
- [**target_class_labels**](#validmind.vm_models.dataset.dataset.VMDataset.target_class_labels) –
- [**target_column**](#validmind.vm_models.dataset.dataset.VMDataset.target_column) –
- [**text_column**](#validmind.vm_models.dataset.dataset.VMDataset.text_column) –
- [**x**](#validmind.vm_models.dataset.dataset.VMDataset.x) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the input features (X) of the dataset.
- [**y**](#validmind.vm_models.dataset.dataset.VMDataset.y) (<code>[ndarray](#numpy.ndarray)</code>) – Returns the target variables (y) of the dataset.

Initializes a VMDataset instance.

**Parameters:**

- **raw_dataset** (<code>[ndarray](#numpy.ndarray)</code>) – The raw dataset as a NumPy array.
- **input_id** (<code>[str](#str)</code>) – Identifier for the dataset.
- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – Model associated with the dataset.
- **index** (<code>[ndarray](#numpy.ndarray)</code>) – The raw dataset index as a NumPy array.
- **index_name** (<code>[str](#str)</code>) – The raw dataset index name as a NumPy array.
- **date_time_index** (<code>[bool](#bool)</code>) – Whether the index is a datetime index.
- **columns** (<code>[List](#List)\[[str](#str)\]</code>) – The column names of the dataset. Defaults to None.
- **target_column** (<code>[str](#str)</code>) – The target column name of the dataset. Defaults to None.
- **feature_columns** (<code>[str](#str)</code>) – The feature column names of the dataset. Defaults to None.
- **text_column** (<code>[str](#str)</code>) – The text column name of the dataset for nlp tasks. Defaults to None.
- **target_class_labels** (<code>[Dict](#Dict)</code>) – The class labels for the target columns. Defaults to None.

####### validmind.vm_models.dataset.dataset.VMDataset.add_extra_column

```python
add_extra_column(column_name, column_values=None)
```

Adds an extra column to the dataset without modifying the dataset `features` and `target` columns.

**Parameters:**

- **column_name** (<code>[str](#str)</code>) – The name of the extra column.
- **column_values** (<code>[ndarray](#numpy.ndarray)</code>) – The values of the extra column.

####### validmind.vm_models.dataset.dataset.VMDataset.assign_predictions

```python
assign_predictions(
    model,
    prediction_column=None,
    prediction_values=None,
    probability_column=None,
    probability_values=None,
    prediction_probabilities=None,
    **kwargs
)
```

Assign predictions and probabilities to the dataset.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model used to generate the predictions.
- **prediction_column** (<code>[str](#str)</code>) – The name of the column containing the predictions. Defaults to None.
- **prediction_values** (<code>[list](#list)</code>) – The values of the predictions. Defaults to None.
- **probability_column** (<code>[str](#str)</code>) – The name of the column containing the probabilities. Defaults to None.
- **probability_values** (<code>[list](#list)</code>) – The values of the probabilities. Defaults to None.
- **prediction_probabilities** (<code>[list](#list)</code>) – DEPRECATED: The values of the probabilities. Defaults to None.
- **kwargs** – Additional keyword arguments that will get passed through to the model's `predict` method.

####### validmind.vm_models.dataset.dataset.VMDataset.column_aliases

```python
column_aliases = {}
```

####### validmind.vm_models.dataset.dataset.VMDataset.columns

```python
columns = columns or []
```

####### validmind.vm_models.dataset.dataset.VMDataset.df

```python
df: pd.DataFrame
```

Returns the dataset as a pandas DataFrame.

**Returns:**

- <code>[DataFrame](#pandas.DataFrame)</code> – pd.DataFrame: The dataset as a pandas DataFrame.

####### validmind.vm_models.dataset.dataset.VMDataset.extra_columns

```python
extra_columns = ExtraColumns.from_dict(extra_columns)
```

####### validmind.vm_models.dataset.dataset.VMDataset.index

```python
index = index
```

####### validmind.vm_models.dataset.dataset.VMDataset.input_id

```python
input_id = input_id
```

####### validmind.vm_models.dataset.dataset.VMDataset.prediction_column

```python
prediction_column(model, column_name=None)
```

Get or set the prediction column for a model.

####### validmind.vm_models.dataset.dataset.VMDataset.probability_column

```python
probability_column(model, column_name=None)
```

Get or set the probability column for a model.

####### validmind.vm_models.dataset.dataset.VMDataset.target_class_labels

```python
target_class_labels = target_class_labels
```

####### validmind.vm_models.dataset.dataset.VMDataset.target_classes

```python
target_classes()
```

Returns the target class labels or unique values of the target column.

####### validmind.vm_models.dataset.dataset.VMDataset.target_column

```python
target_column = target_column
```

####### validmind.vm_models.dataset.dataset.VMDataset.text_column

```python
text_column = text_column
```

####### validmind.vm_models.dataset.dataset.VMDataset.with_options

```python
with_options(**kwargs)
```

Support options provided when passing an input to run_test or run_test_suite

Example:

```python
# to only use a certain subset of columns in the dataset:
run_test(
    "validmind.SomeTestID",
    inputs={
        "dataset": {
            "input_id": "my_dataset_id",
            "columns": ["col1", "col2"],
        }
    }
)

# behind the scenes, this retrieves the dataset object (VMDataset) from the registry
# and then calls the `with_options()` method and passes `{"columns": ...}`
```

**Parameters:**

- \*\***kwargs** – Options:
- columns: Filter columns in the dataset

**Returns:**

- **VMDataset** (<code>[VMDataset](#validmind.vm_models.dataset.dataset.VMDataset)</code>) – A new instance of the dataset with only the specified columns

####### validmind.vm_models.dataset.dataset.VMDataset.x

```python
x: np.ndarray
```

Returns the input features (X) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The input features.

####### validmind.vm_models.dataset.dataset.VMDataset.x_df

```python
x_df()
```

Returns a dataframe containing only the feature columns

####### validmind.vm_models.dataset.dataset.VMDataset.y

```python
y: np.ndarray
```

Returns the target variables (y) of the dataset.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The target variables.

####### validmind.vm_models.dataset.dataset.VMDataset.y_df

```python
y_df()
```

Returns a dataframe containing the target column

####### validmind.vm_models.dataset.dataset.VMDataset.y_pred

```python
y_pred(model)
```

Returns the predictions for a given model.

Attempts to stack complex prediction types (e.g., embeddings) into a single,
multi-dimensional array.

**Parameters:**

- **model** (<code>[VMModel](#validmind.vm_models.model.VMModel)</code>) – The model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The predictions for the model

####### validmind.vm_models.dataset.dataset.VMDataset.y_pred_df

```python
y_pred_df(model)
```

Returns a dataframe containing the predictions for a given model

####### validmind.vm_models.dataset.dataset.VMDataset.y_prob

```python
y_prob(model)
```

Returns the probabilities for a given model.

**Parameters:**

- **model** (<code>[str](#str)</code>) – The ID of the model whose predictions are sought.

**Returns:**

- <code>[ndarray](#numpy.ndarray)</code> – np.ndarray: The probability variables.

####### validmind.vm_models.dataset.dataset.VMDataset.y_prob_df

```python
y_prob_df(model)
```

Returns a dataframe containing the probabilities for a given model

###### validmind.vm_models.dataset.dataset.logger

```python
logger = get_logger(__name__)
```

##### validmind.vm_models.dataset.utils

**Classes:**

- [**ExtraColumns**](#validmind.vm_models.dataset.utils.ExtraColumns) – Extra columns for the dataset.

**Functions:**

- [**as_df**](#validmind.vm_models.dataset.utils.as_df) –
- [**compute_predictions**](#validmind.vm_models.dataset.utils.compute_predictions) –
- [**convert_index_to_datetime**](#validmind.vm_models.dataset.utils.convert_index_to_datetime) – Attempts to convert the index of the dataset to a datetime index

**Attributes:**

- [**logger**](#validmind.vm_models.dataset.utils.logger) –

###### validmind.vm_models.dataset.utils.ExtraColumns

```python
ExtraColumns(
    extras=set(),
    group_by_column=None,
    prediction_columns=dict(),
    probability_columns=dict(),
)
```

Extra columns for the dataset.

**Functions:**

- [**add_extra**](#validmind.vm_models.dataset.utils.ExtraColumns.add_extra) –
- [**flatten**](#validmind.vm_models.dataset.utils.ExtraColumns.flatten) – Get a list of all column names
- [**from_dict**](#validmind.vm_models.dataset.utils.ExtraColumns.from_dict) –
- [**prediction_column**](#validmind.vm_models.dataset.utils.ExtraColumns.prediction_column) – Get or set the prediction column for a model.
- [**probability_column**](#validmind.vm_models.dataset.utils.ExtraColumns.probability_column) – Get or set the probability column for a model.

**Attributes:**

- [**extras**](#validmind.vm_models.dataset.utils.ExtraColumns.extras) (<code>[Set](#typing.Set)\[[str](#str)\]</code>) –
- [**group_by_column**](#validmind.vm_models.dataset.utils.ExtraColumns.group_by_column) (<code>[str](#str)</code>) –
- [**prediction_columns**](#validmind.vm_models.dataset.utils.ExtraColumns.prediction_columns) (<code>[Dict](#typing.Dict)\[[str](#str), [str](#str)\]</code>) –
- [**probability_columns**](#validmind.vm_models.dataset.utils.ExtraColumns.probability_columns) (<code>[Dict](#typing.Dict)\[[str](#str), [str](#str)\]</code>) –

####### validmind.vm_models.dataset.utils.ExtraColumns.add_extra

```python
add_extra(column_name)
```

####### validmind.vm_models.dataset.utils.ExtraColumns.extras

```python
extras: Set[str] = field(default_factory=set)
```

####### validmind.vm_models.dataset.utils.ExtraColumns.flatten

```python
flatten()
```

Get a list of all column names

####### validmind.vm_models.dataset.utils.ExtraColumns.from_dict

```python
from_dict(data)
```

####### validmind.vm_models.dataset.utils.ExtraColumns.group_by_column

```python
group_by_column: str = None
```

####### validmind.vm_models.dataset.utils.ExtraColumns.prediction_column

```python
prediction_column(model, column_name=None)
```

Get or set the prediction column for a model.

####### validmind.vm_models.dataset.utils.ExtraColumns.prediction_columns

```python
prediction_columns: Dict[str, str] = field(default_factory=dict)
```

####### validmind.vm_models.dataset.utils.ExtraColumns.probability_column

```python
probability_column(model, column_name=None)
```

Get or set the probability column for a model.

####### validmind.vm_models.dataset.utils.ExtraColumns.probability_columns

```python
probability_columns: Dict[str, str] = field(default_factory=dict)
```

###### validmind.vm_models.dataset.utils.as_df

```python
as_df(series_or_frame)
```

###### validmind.vm_models.dataset.utils.compute_predictions

```python
compute_predictions(model, X, **kwargs)
```

###### validmind.vm_models.dataset.utils.convert_index_to_datetime

```python
convert_index_to_datetime(df)
```

Attempts to convert the index of the dataset to a datetime index
and leaves the index unchanged if it fails.

###### validmind.vm_models.dataset.utils.logger

```python
logger = get_logger(__name__)
```

#### validmind.vm_models.figure

Figure objects track the figure schema supported by the ValidMind API

**Classes:**

- [**Figure**](#validmind.vm_models.figure.Figure) – Figure objects track the schema supported by the ValidMind API

**Functions:**

- [**is_matplotlib_figure**](#validmind.vm_models.figure.is_matplotlib_figure) –
- [**is_plotly_figure**](#validmind.vm_models.figure.is_plotly_figure) –
- [**is_png_image**](#validmind.vm_models.figure.is_png_image) –

##### validmind.vm_models.figure.Figure

```python
Figure(key, figure, ref_id, _type='plot')
```

Figure objects track the schema supported by the ValidMind API

**Functions:**

- [**serialize**](#validmind.vm_models.figure.Figure.serialize) – Serializes the Figure to a dictionary so it can be sent to the API
- [**serialize_files**](#validmind.vm_models.figure.Figure.serialize_files) – Creates a `requests`-compatible files object to be sent to the API
- [**to_widget**](#validmind.vm_models.figure.Figure.to_widget) – Returns the ipywidget compatible representation of the figure. Ideally

**Attributes:**

- [**figure**](#validmind.vm_models.figure.Figure.figure) (<code>[Union](#typing.Union)\[[Figure](#matplotlib.figure.Figure), [Figure](#plotly.graph_objs.Figure), [FigureWidget](#plotly.graph_objs.FigureWidget), [bytes](#bytes)\]</code>) –
- [**key**](#validmind.vm_models.figure.Figure.key) (<code>[str](#str)</code>) –
- [**ref_id**](#validmind.vm_models.figure.Figure.ref_id) (<code>[str](#str)</code>) –

###### validmind.vm_models.figure.Figure.figure

```python
figure: Union[matplotlib.figure.Figure, go.Figure, go.FigureWidget, bytes]
```

###### validmind.vm_models.figure.Figure.key

```python
key: str
```

###### validmind.vm_models.figure.Figure.ref_id

```python
ref_id: str
```

###### validmind.vm_models.figure.Figure.serialize

```python
serialize()
```

Serializes the Figure to a dictionary so it can be sent to the API

###### validmind.vm_models.figure.Figure.serialize_files

```python
serialize_files()
```

Creates a `requests`-compatible files object to be sent to the API

###### validmind.vm_models.figure.Figure.to_widget

```python
to_widget()
```

Returns the ipywidget compatible representation of the figure. Ideally
we would render images as-is, but Plotly FigureWidgets don't work well
on Google Colab when they are combined with ipywidgets.

##### validmind.vm_models.figure.is_matplotlib_figure

```python
is_matplotlib_figure(figure)
```

##### validmind.vm_models.figure.is_plotly_figure

```python
is_plotly_figure(figure)
```

##### validmind.vm_models.figure.is_png_image

```python
is_png_image(figure)
```

#### validmind.vm_models.input

Base class for ValidMind Input types

**Classes:**

- [**VMInput**](#validmind.vm_models.input.VMInput) – Base class for ValidMind Input types

##### validmind.vm_models.input.VMInput

Bases: <code>[ABC](#abc.ABC)</code>

Base class for ValidMind Input types

**Functions:**

- [**with_options**](#validmind.vm_models.input.VMInput.with_options) – Allows for setting options on the input object that are passed by the user

###### validmind.vm_models.input.VMInput.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

#### validmind.vm_models.model

Model class wrapper module

**Classes:**

- [**ModelAttributes**](#validmind.vm_models.model.ModelAttributes) – Model attributes definition
- [**ModelPipeline**](#validmind.vm_models.model.ModelPipeline) – Helper class for chaining models together
- [**ModelTask**](#validmind.vm_models.model.ModelTask) – Model task enums
- [**VMModel**](#validmind.vm_models.model.VMModel) – An base class that wraps a trained model instance and its associated data.

**Functions:**

- [**get_model_class**](#validmind.vm_models.model.get_model_class) –
- [**has_method_with_arguments**](#validmind.vm_models.model.has_method_with_arguments) –
- [**is_model_metadata**](#validmind.vm_models.model.is_model_metadata) – Checks if the model is a dictionary containing metadata about a model.
- [**is_pytorch_model**](#validmind.vm_models.model.is_pytorch_model) – Checks if the model is a PyTorch model. Need to extend this
- [**model_module**](#validmind.vm_models.model.model_module) –

**Attributes:**

- [**R_MODEL_METHODS**](#validmind.vm_models.model.R_MODEL_METHODS) –
- [**R_MODEL_TYPES**](#validmind.vm_models.model.R_MODEL_TYPES) –
- [**SUPPORTED_LIBRARIES**](#validmind.vm_models.model.SUPPORTED_LIBRARIES) –

##### validmind.vm_models.model.ModelAttributes

```python
ModelAttributes(
    architecture=None,
    framework=None,
    framework_version=None,
    language=None,
    task=None,
)
```

Model attributes definition

**Functions:**

- [**from_dict**](#validmind.vm_models.model.ModelAttributes.from_dict) – Creates a ModelAttributes instance from a dictionary

**Attributes:**

- [**architecture**](#validmind.vm_models.model.ModelAttributes.architecture) (<code>[str](#str)</code>) –
- [**framework**](#validmind.vm_models.model.ModelAttributes.framework) (<code>[str](#str)</code>) –
- [**framework_version**](#validmind.vm_models.model.ModelAttributes.framework_version) (<code>[str](#str)</code>) –
- [**language**](#validmind.vm_models.model.ModelAttributes.language) (<code>[str](#str)</code>) –
- [**task**](#validmind.vm_models.model.ModelAttributes.task) (<code>[ModelTask](#validmind.vm_models.model.ModelTask)</code>) –

###### validmind.vm_models.model.ModelAttributes.architecture

```python
architecture: str = None
```

###### validmind.vm_models.model.ModelAttributes.framework

```python
framework: str = None
```

###### validmind.vm_models.model.ModelAttributes.framework_version

```python
framework_version: str = None
```

###### validmind.vm_models.model.ModelAttributes.from_dict

```python
from_dict(data)
```

Creates a ModelAttributes instance from a dictionary

###### validmind.vm_models.model.ModelAttributes.language

```python
language: str = None
```

###### validmind.vm_models.model.ModelAttributes.task

```python
task: ModelTask = None
```

##### validmind.vm_models.model.ModelPipeline

```python
ModelPipeline(models)
```

Helper class for chaining models together

This shouldn't be used directly, it just gets used when chaining models with the
`|` operator since you can't use a list directly - you must use a type that
overloads the `|` operator.

**Attributes:**

- [**models**](#validmind.vm_models.model.ModelPipeline.models) –

###### validmind.vm_models.model.ModelPipeline.models

```python
models = models
```

##### validmind.vm_models.model.ModelTask

Bases: <code>[Enum](#enum.Enum)</code>

Model task enums

**Attributes:**

- [**CLASSIFICATION**](#validmind.vm_models.model.ModelTask.CLASSIFICATION) –
- [**REGRESSION**](#validmind.vm_models.model.ModelTask.REGRESSION) –

###### validmind.vm_models.model.ModelTask.CLASSIFICATION

```python
CLASSIFICATION = 'classification'
```

###### validmind.vm_models.model.ModelTask.REGRESSION

```python
REGRESSION = 'regression'
```

##### validmind.vm_models.model.R_MODEL_METHODS

```python
R_MODEL_METHODS = ['glm.fit']
```

##### validmind.vm_models.model.R_MODEL_TYPES

```python
R_MODEL_TYPES = [
    "LogisticRegression",
    "LinearRegression",
    "XGBClassifier",
    "XGBRegressor",
]

```

##### validmind.vm_models.model.SUPPORTED_LIBRARIES

```python
SUPPORTED_LIBRARIES = {
    "catboost": "CatBoostModel",
    "xgboost": "XGBoostModel",
    "sklearn": "SKlearnModel",
    "statsmodels": "StatsModelsModel",
    "torch": "PyTorchModel",
    "transformers": "HFModel",
    "function": "FunctionModel",
    "pipeline": "PipelineModel",
    "custom": "SKlearnModel",
}

```

##### validmind.vm_models.model.VMModel

```python
VMModel(input_id=None, model=None, attributes=None, name=None, **kwargs)
```

Bases: <code>[VMInput](#validmind.vm_models.input.VMInput)</code>

An base class that wraps a trained model instance and its associated data.

**Attributes:**

- [**model**](#validmind.vm_models.model.VMModel.model) (<code>[object](#object)</code>) – The trained model instance. Defaults to None.
- [**input_id**](#validmind.vm_models.model.VMModel.input_id) (<code>[str](#str)</code>) – The input ID for the model. Defaults to None.
- [**attributes**](#validmind.vm_models.model.VMModel.attributes) (<code>[ModelAttributes](#validmind.vm_models.model.ModelAttributes)</code>) – The attributes of the model. Defaults to None.
- [**name**](#validmind.vm_models.model.VMModel.name) (<code>[str](#str)</code>) – The name of the model. Defaults to the class name.

**Functions:**

- [**predict**](#validmind.vm_models.model.VMModel.predict) – Predict method for the model. This is a wrapper around the model's
- [**predict_proba**](#validmind.vm_models.model.VMModel.predict_proba) – Predict probabilties - must be implemented by subclass if needed
- [**serialize**](#validmind.vm_models.model.VMModel.serialize) – Serializes the model to a dictionary so it can be sent to the API
- [**with_options**](#validmind.vm_models.model.VMModel.with_options) – Allows for setting options on the input object that are passed by the user

**Attributes:**

- [**attributes**](#validmind.vm_models.model.VMModel.attributes) –
- [**class\_**](#validmind.vm_models.model.VMModel.class_) –
- [**input_id**](#validmind.vm_models.model.VMModel.input_id) –
- [**language**](#validmind.vm_models.model.VMModel.language) –
- [**library**](#validmind.vm_models.model.VMModel.library) –
- [**library_version**](#validmind.vm_models.model.VMModel.library_version) –
- [**model**](#validmind.vm_models.model.VMModel.model) –
- [**name**](#validmind.vm_models.model.VMModel.name) –

###### validmind.vm_models.model.VMModel.attributes

```python
attributes = attributes or ModelAttributes()
```

###### validmind.vm_models.model.VMModel.class\_

```python
class_ = self.__class__.__name__
```

###### validmind.vm_models.model.VMModel.input_id

```python
input_id = input_id
```

###### validmind.vm_models.model.VMModel.language

```python
language = 'Python'
```

###### validmind.vm_models.model.VMModel.library

```python
library = self.__class__.__name__
```

###### validmind.vm_models.model.VMModel.library_version

```python
library_version = 'N/A'
```

###### validmind.vm_models.model.VMModel.model

```python
model = model
```

###### validmind.vm_models.model.VMModel.name

```python
name = name or self.__class__.__name__
```

###### validmind.vm_models.model.VMModel.predict

```python
predict(*args, **kwargs)
```

Predict method for the model. This is a wrapper around the model's

###### validmind.vm_models.model.VMModel.predict_proba

```python
predict_proba(*args, **kwargs)
```

Predict probabilties - must be implemented by subclass if needed

###### validmind.vm_models.model.VMModel.serialize

```python
serialize()
```

Serializes the model to a dictionary so it can be sent to the API

###### validmind.vm_models.model.VMModel.with_options

```python
with_options(**kwargs)
```

Allows for setting options on the input object that are passed by the user
when using the input to run a test or set of tests

To allow options, just override this method in the subclass (see VMDataset)
and ensure that it returns a new instance of the input with the specified options
set.

**Parameters:**

- \*\***kwargs** – Arbitrary keyword arguments that will be passed to the input object

**Returns:**

- **VMInput** (<code>[VMInput](#validmind.vm_models.input.VMInput)</code>) – A new instance of the input with the specified options set

##### validmind.vm_models.model.get_model_class

```python
get_model_class(model, predict_fn=None)
```

##### validmind.vm_models.model.has_method_with_arguments

```python
has_method_with_arguments(cls, method_name, n_args)
```

##### validmind.vm_models.model.is_model_metadata

```python
is_model_metadata(model)
```

Checks if the model is a dictionary containing metadata about a model.
We want to check if the metadata dictionary contains at least the following keys:

- architecture
- language

##### validmind.vm_models.model.is_pytorch_model

```python
is_pytorch_model(model)
```

Checks if the model is a PyTorch model. Need to extend this
method to check for all ways a PyTorch model can be created

##### validmind.vm_models.model.model_module

```python
model_module(model)
```

#### validmind.vm_models.result

**Modules:**

- [**result**](#validmind.vm_models.result.result) – Result Objects for test results
- [**utils**](#validmind.vm_models.result.utils) –

**Classes:**

- [**ErrorResult**](#validmind.vm_models.result.ErrorResult) – Result for test suites that fail to load or run properly
- [**Result**](#validmind.vm_models.result.Result) – Base Class for test suite results
- [**ResultTable**](#validmind.vm_models.result.ResultTable) – A dataclass that holds the table summary of result
- [**TestResult**](#validmind.vm_models.result.TestResult) – Test result

##### validmind.vm_models.result.ErrorResult

```python
ErrorResult(result_id=None, name='Failed Test', error=None, message=None)
```

Bases: <code>[Result](#validmind.vm_models.result.result.Result)</code>

Result for test suites that fail to load or run properly

**Functions:**

- [**log**](#validmind.vm_models.result.ErrorResult.log) – Log the result... Must be overridden by subclasses
- [**log_async**](#validmind.vm_models.result.ErrorResult.log_async) –
- [**show**](#validmind.vm_models.result.ErrorResult.show) – Display the result... May be overridden by subclasses
- [**to_widget**](#validmind.vm_models.result.ErrorResult.to_widget) –

**Attributes:**

- [**error**](#validmind.vm_models.result.ErrorResult.error) (<code>[Exception](#Exception)</code>) –
- [**message**](#validmind.vm_models.result.ErrorResult.message) (<code>[str](#str)</code>) –
- [**name**](#validmind.vm_models.result.ErrorResult.name) (<code>[str](#str)</code>) –
- [**result_id**](#validmind.vm_models.result.ErrorResult.result_id) (<code>[str](#str)</code>) –

###### validmind.vm_models.result.ErrorResult.error

```python
error: Exception = None
```

###### validmind.vm_models.result.ErrorResult.log

```python
log()
```

Log the result... Must be overridden by subclasses

###### validmind.vm_models.result.ErrorResult.log_async

```python
log_async()
```

###### validmind.vm_models.result.ErrorResult.message

```python
message: str = None
```

###### validmind.vm_models.result.ErrorResult.name

```python
name: str = 'Failed Test'
```

###### validmind.vm_models.result.ErrorResult.result_id

```python
result_id: str = None
```

###### validmind.vm_models.result.ErrorResult.show

```python
show()
```

Display the result... May be overridden by subclasses

###### validmind.vm_models.result.ErrorResult.to_widget

```python
to_widget()
```

##### validmind.vm_models.result.Result

```python
Result(result_id=None, name=None)
```

Base Class for test suite results

**Functions:**

- [**log**](#validmind.vm_models.result.Result.log) – Log the result... Must be overridden by subclasses
- [**show**](#validmind.vm_models.result.Result.show) – Display the result... May be overridden by subclasses
- [**to_widget**](#validmind.vm_models.result.Result.to_widget) – Create an ipywdiget representation of the result... Must be overridden by subclasses

**Attributes:**

- [**name**](#validmind.vm_models.result.Result.name) (<code>[str](#str)</code>) –
- [**result_id**](#validmind.vm_models.result.Result.result_id) (<code>[str](#str)</code>) –

###### validmind.vm_models.result.Result.log

```python
log()
```

Log the result... Must be overridden by subclasses

###### validmind.vm_models.result.Result.name

```python
name: str = None
```

###### validmind.vm_models.result.Result.result_id

```python
result_id: str = None
```

###### validmind.vm_models.result.Result.show

```python
show()
```

Display the result... May be overridden by subclasses

###### validmind.vm_models.result.Result.to_widget

```python
to_widget()
```

Create an ipywdiget representation of the result... Must be overridden by subclasses

##### validmind.vm_models.result.ResultTable

```python
ResultTable(data, title)
```

A dataclass that holds the table summary of result

**Functions:**

- [**serialize**](#validmind.vm_models.result.ResultTable.serialize) –

**Attributes:**

- [**data**](#validmind.vm_models.result.ResultTable.data) (<code>[Union](#typing.Union)\[[List](#typing.List)\[[Any](#typing.Any)\], [DataFrame](#pandas.DataFrame)\]</code>) –
- [**title**](#validmind.vm_models.result.ResultTable.title) (<code>[str](#str)</code>) –

###### validmind.vm_models.result.ResultTable.data

```python
data: Union[List[Any], pd.DataFrame]
```

###### validmind.vm_models.result.ResultTable.serialize

```python
serialize()
```

###### validmind.vm_models.result.ResultTable.title

```python
title: str
```

##### validmind.vm_models.result.TestResult

```python
TestResult(
    result_id=None,
    name="Test Result",
    ref_id=None,
    title=None,
    description=None,
    metric=None,
    tables=None,
    figures=None,
    passed=None,
    params=None,
    inputs=None,
    metadata=None,
    _was_description_generated=False,
    _unsafe=False,
)
```

Bases: <code>[Result](#validmind.vm_models.result.result.Result)</code>

Test result

**Functions:**

- [**add_figure**](#validmind.vm_models.result.TestResult.add_figure) –
- [**add_table**](#validmind.vm_models.result.TestResult.add_table) –
- [**log**](#validmind.vm_models.result.TestResult.log) – Log the result to ValidMind
- [**log_async**](#validmind.vm_models.result.TestResult.log_async) –
- [**serialize**](#validmind.vm_models.result.TestResult.serialize) – Serialize the result for the API
- [**show**](#validmind.vm_models.result.TestResult.show) – Display the result... May be overridden by subclasses
- [**to_widget**](#validmind.vm_models.result.TestResult.to_widget) –

**Attributes:**

- [**description**](#validmind.vm_models.result.TestResult.description) (<code>[Optional](#typing.Optional)\[[Union](#typing.Union)\[[str](#str), [DescriptionFuture](#validmind.ai.utils.DescriptionFuture)\]\]</code>) –
- [**figures**](#validmind.vm_models.result.TestResult.figures) (<code>[Optional](#typing.Optional)\[[List](#typing.List)\[[Figure](#validmind.vm_models.figure.Figure)\]\]</code>) –
- [**inputs**](#validmind.vm_models.result.TestResult.inputs) (<code>[Optional](#typing.Optional)\[[Dict](#typing.Dict)\[[str](#str), [Union](#typing.Union)\[[List](#typing.List)\[[VMInput](#validmind.vm_models.input.VMInput)\], [VMInput](#validmind.vm_models.input.VMInput)\]\]\]</code>) –
- [**metadata**](#validmind.vm_models.result.TestResult.metadata) (<code>[Optional](#typing.Optional)\[[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]\]</code>) –
- [**metric**](#validmind.vm_models.result.TestResult.metric) (<code>[Optional](#typing.Optional)\[[Union](#typing.Union)\[[int](#int), [float](#float)\]\]</code>) –
- [**name**](#validmind.vm_models.result.TestResult.name) (<code>[str](#str)</code>) –
- [**params**](#validmind.vm_models.result.TestResult.params) (<code>[Optional](#typing.Optional)\[[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]\]</code>) –
- [**passed**](#validmind.vm_models.result.TestResult.passed) (<code>[Optional](#typing.Optional)\[[bool](#bool)\]</code>) –
- [**ref_id**](#validmind.vm_models.result.TestResult.ref_id) (<code>[str](#str)</code>) –
- [**result_id**](#validmind.vm_models.result.TestResult.result_id) (<code>[str](#str)</code>) –
- [**tables**](#validmind.vm_models.result.TestResult.tables) (<code>[Optional](#typing.Optional)\[[List](#typing.List)\[[ResultTable](#validmind.vm_models.result.result.ResultTable)\]\]</code>) –
- [**test_name**](#validmind.vm_models.result.TestResult.test_name) (<code>[str](#str)</code>) – Get the test name, using custom title if available.
- [**title**](#validmind.vm_models.result.TestResult.title) (<code>[Optional](#typing.Optional)\[[str](#str)\]</code>) –

###### validmind.vm_models.result.TestResult.add_figure

```python
add_figure(figure)
```

###### validmind.vm_models.result.TestResult.add_table

```python
add_table(table)
```

###### validmind.vm_models.result.TestResult.description

```python
description: Optional[Union[str, DescriptionFuture]] = None
```

###### validmind.vm_models.result.TestResult.figures

```python
figures: Optional[List[Figure]] = None
```

###### validmind.vm_models.result.TestResult.inputs

```python
inputs: Optional[Dict[str, Union[List[VMInput], VMInput]]] = None
```

###### validmind.vm_models.result.TestResult.log

```python
log(section_id=None, position=None, unsafe=False)
```

Log the result to ValidMind

**Parameters:**

- **section_id** (<code>[str](#str)</code>) – The section ID within the model document to insert the
  test result
- **position** (<code>[int](#int)</code>) – The position (index) within the section to insert the test
  result
- **unsafe** (<code>[bool](#bool)</code>) – If True, log the result even if it contains sensitive data
  i.e. raw data from input datasets

###### validmind.vm_models.result.TestResult.log_async

```python
log_async(section_id=None, position=None, unsafe=False)
```

###### validmind.vm_models.result.TestResult.metadata

```python
metadata: Optional[Dict[str, Any]] = None
```

###### validmind.vm_models.result.TestResult.metric

```python
metric: Optional[Union[int, float]] = None
```

###### validmind.vm_models.result.TestResult.name

```python
name: str = 'Test Result'
```

###### validmind.vm_models.result.TestResult.params

```python
params: Optional[Dict[str, Any]] = None
```

###### validmind.vm_models.result.TestResult.passed

```python
passed: Optional[bool] = None
```

###### validmind.vm_models.result.TestResult.ref_id

```python
ref_id: str = None
```

###### validmind.vm_models.result.TestResult.result_id

```python
result_id: str = None
```

###### validmind.vm_models.result.TestResult.serialize

```python
serialize()
```

Serialize the result for the API

###### validmind.vm_models.result.TestResult.show

```python
show()
```

Display the result... May be overridden by subclasses

###### validmind.vm_models.result.TestResult.tables

```python
tables: Optional[List[ResultTable]] = None
```

###### validmind.vm_models.result.TestResult.test_name

```python
test_name: str
```

Get the test name, using custom title if available.

###### validmind.vm_models.result.TestResult.title

```python
title: Optional[str] = None
```

###### validmind.vm_models.result.TestResult.to_widget

```python
to_widget()
```

##### validmind.vm_models.result.result

Result Objects for test results

**Classes:**

- [**ErrorResult**](#validmind.vm_models.result.result.ErrorResult) – Result for test suites that fail to load or run properly
- [**Result**](#validmind.vm_models.result.result.Result) – Base Class for test suite results
- [**ResultTable**](#validmind.vm_models.result.result.ResultTable) – A dataclass that holds the table summary of result
- [**TestResult**](#validmind.vm_models.result.result.TestResult) – Test result

**Attributes:**

- [**logger**](#validmind.vm_models.result.result.logger) –

###### validmind.vm_models.result.result.ErrorResult

```python
ErrorResult(result_id=None, name='Failed Test', error=None, message=None)
```

Bases: <code>[Result](#validmind.vm_models.result.result.Result)</code>

Result for test suites that fail to load or run properly

**Functions:**

- [**log**](#validmind.vm_models.result.result.ErrorResult.log) – Log the result... Must be overridden by subclasses
- [**log_async**](#validmind.vm_models.result.result.ErrorResult.log_async) –
- [**show**](#validmind.vm_models.result.result.ErrorResult.show) – Display the result... May be overridden by subclasses
- [**to_widget**](#validmind.vm_models.result.result.ErrorResult.to_widget) –

**Attributes:**

- [**error**](#validmind.vm_models.result.result.ErrorResult.error) (<code>[Exception](#Exception)</code>) –
- [**message**](#validmind.vm_models.result.result.ErrorResult.message) (<code>[str](#str)</code>) –
- [**name**](#validmind.vm_models.result.result.ErrorResult.name) (<code>[str](#str)</code>) –
- [**result_id**](#validmind.vm_models.result.result.ErrorResult.result_id) (<code>[str](#str)</code>) –

####### validmind.vm_models.result.result.ErrorResult.error

```python
error: Exception = None
```

####### validmind.vm_models.result.result.ErrorResult.log

```python
log()
```

Log the result... Must be overridden by subclasses

####### validmind.vm_models.result.result.ErrorResult.log_async

```python
log_async()
```

####### validmind.vm_models.result.result.ErrorResult.message

```python
message: str = None
```

####### validmind.vm_models.result.result.ErrorResult.name

```python
name: str = 'Failed Test'
```

####### validmind.vm_models.result.result.ErrorResult.result_id

```python
result_id: str = None
```

####### validmind.vm_models.result.result.ErrorResult.show

```python
show()
```

Display the result... May be overridden by subclasses

####### validmind.vm_models.result.result.ErrorResult.to_widget

```python
to_widget()
```

###### validmind.vm_models.result.result.Result

```python
Result(result_id=None, name=None)
```

Base Class for test suite results

**Functions:**

- [**log**](#validmind.vm_models.result.result.Result.log) – Log the result... Must be overridden by subclasses
- [**show**](#validmind.vm_models.result.result.Result.show) – Display the result... May be overridden by subclasses
- [**to_widget**](#validmind.vm_models.result.result.Result.to_widget) – Create an ipywdiget representation of the result... Must be overridden by subclasses

**Attributes:**

- [**name**](#validmind.vm_models.result.result.Result.name) (<code>[str](#str)</code>) –
- [**result_id**](#validmind.vm_models.result.result.Result.result_id) (<code>[str](#str)</code>) –

####### validmind.vm_models.result.result.Result.log

```python
log()
```

Log the result... Must be overridden by subclasses

####### validmind.vm_models.result.result.Result.name

```python
name: str = None
```

####### validmind.vm_models.result.result.Result.result_id

```python
result_id: str = None
```

####### validmind.vm_models.result.result.Result.show

```python
show()
```

Display the result... May be overridden by subclasses

####### validmind.vm_models.result.result.Result.to_widget

```python
to_widget()
```

Create an ipywdiget representation of the result... Must be overridden by subclasses

###### validmind.vm_models.result.result.ResultTable

```python
ResultTable(data, title)
```

A dataclass that holds the table summary of result

**Functions:**

- [**serialize**](#validmind.vm_models.result.result.ResultTable.serialize) –

**Attributes:**

- [**data**](#validmind.vm_models.result.result.ResultTable.data) (<code>[Union](#typing.Union)\[[List](#typing.List)\[[Any](#typing.Any)\], [DataFrame](#pandas.DataFrame)\]</code>) –
- [**title**](#validmind.vm_models.result.result.ResultTable.title) (<code>[str](#str)</code>) –

####### validmind.vm_models.result.result.ResultTable.data

```python
data: Union[List[Any], pd.DataFrame]
```

####### validmind.vm_models.result.result.ResultTable.serialize

```python
serialize()
```

####### validmind.vm_models.result.result.ResultTable.title

```python
title: str
```

###### validmind.vm_models.result.result.TestResult

```python
TestResult(
    result_id=None,
    name="Test Result",
    ref_id=None,
    title=None,
    description=None,
    metric=None,
    tables=None,
    figures=None,
    passed=None,
    params=None,
    inputs=None,
    metadata=None,
    _was_description_generated=False,
    _unsafe=False,
)
```

Bases: <code>[Result](#validmind.vm_models.result.result.Result)</code>

Test result

**Functions:**

- [**add_figure**](#validmind.vm_models.result.result.TestResult.add_figure) –
- [**add_table**](#validmind.vm_models.result.result.TestResult.add_table) –
- [**log**](#validmind.vm_models.result.result.TestResult.log) – Log the result to ValidMind
- [**log_async**](#validmind.vm_models.result.result.TestResult.log_async) –
- [**serialize**](#validmind.vm_models.result.result.TestResult.serialize) – Serialize the result for the API
- [**show**](#validmind.vm_models.result.result.TestResult.show) – Display the result... May be overridden by subclasses
- [**to_widget**](#validmind.vm_models.result.result.TestResult.to_widget) –

**Attributes:**

- [**description**](#validmind.vm_models.result.result.TestResult.description) (<code>[Optional](#typing.Optional)\[[Union](#typing.Union)\[[str](#str), [DescriptionFuture](#validmind.ai.utils.DescriptionFuture)\]\]</code>) –
- [**figures**](#validmind.vm_models.result.result.TestResult.figures) (<code>[Optional](#typing.Optional)\[[List](#typing.List)\[[Figure](#validmind.vm_models.figure.Figure)\]\]</code>) –
- [**inputs**](#validmind.vm_models.result.result.TestResult.inputs) (<code>[Optional](#typing.Optional)\[[Dict](#typing.Dict)\[[str](#str), [Union](#typing.Union)\[[List](#typing.List)\[[VMInput](#validmind.vm_models.input.VMInput)\], [VMInput](#validmind.vm_models.input.VMInput)\]\]\]</code>) –
- [**metadata**](#validmind.vm_models.result.result.TestResult.metadata) (<code>[Optional](#typing.Optional)\[[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]\]</code>) –
- [**metric**](#validmind.vm_models.result.result.TestResult.metric) (<code>[Optional](#typing.Optional)\[[Union](#typing.Union)\[[int](#int), [float](#float)\]\]</code>) –
- [**name**](#validmind.vm_models.result.result.TestResult.name) (<code>[str](#str)</code>) –
- [**params**](#validmind.vm_models.result.result.TestResult.params) (<code>[Optional](#typing.Optional)\[[Dict](#typing.Dict)\[[str](#str), [Any](#typing.Any)\]\]</code>) –
- [**passed**](#validmind.vm_models.result.result.TestResult.passed) (<code>[Optional](#typing.Optional)\[[bool](#bool)\]</code>) –
- [**ref_id**](#validmind.vm_models.result.result.TestResult.ref_id) (<code>[str](#str)</code>) –
- [**result_id**](#validmind.vm_models.result.result.TestResult.result_id) (<code>[str](#str)</code>) –
- [**tables**](#validmind.vm_models.result.result.TestResult.tables) (<code>[Optional](#typing.Optional)\[[List](#typing.List)\[[ResultTable](#validmind.vm_models.result.result.ResultTable)\]\]</code>) –
- [**test_name**](#validmind.vm_models.result.result.TestResult.test_name) (<code>[str](#str)</code>) – Get the test name, using custom title if available.
- [**title**](#validmind.vm_models.result.result.TestResult.title) (<code>[Optional](#typing.Optional)\[[str](#str)\]</code>) –

####### validmind.vm_models.result.result.TestResult.add_figure

```python
add_figure(figure)
```

####### validmind.vm_models.result.result.TestResult.add_table

```python
add_table(table)
```

####### validmind.vm_models.result.result.TestResult.description

```python
description: Optional[Union[str, DescriptionFuture]] = None
```

####### validmind.vm_models.result.result.TestResult.figures

```python
figures: Optional[List[Figure]] = None
```

####### validmind.vm_models.result.result.TestResult.inputs

```python
inputs: Optional[Dict[str, Union[List[VMInput], VMInput]]] = None
```

####### validmind.vm_models.result.result.TestResult.log

```python
log(section_id=None, position=None, unsafe=False)
```

Log the result to ValidMind

**Parameters:**

- **section_id** (<code>[str](#str)</code>) – The section ID within the model document to insert the
  test result
- **position** (<code>[int](#int)</code>) – The position (index) within the section to insert the test
  result
- **unsafe** (<code>[bool](#bool)</code>) – If True, log the result even if it contains sensitive data
  i.e. raw data from input datasets

####### validmind.vm_models.result.result.TestResult.log_async

```python
log_async(section_id=None, position=None, unsafe=False)
```

####### validmind.vm_models.result.result.TestResult.metadata

```python
metadata: Optional[Dict[str, Any]] = None
```

####### validmind.vm_models.result.result.TestResult.metric

```python
metric: Optional[Union[int, float]] = None
```

####### validmind.vm_models.result.result.TestResult.name

```python
name: str = 'Test Result'
```

####### validmind.vm_models.result.result.TestResult.params

```python
params: Optional[Dict[str, Any]] = None
```

####### validmind.vm_models.result.result.TestResult.passed

```python
passed: Optional[bool] = None
```

####### validmind.vm_models.result.result.TestResult.ref_id

```python
ref_id: str = None
```

####### validmind.vm_models.result.result.TestResult.result_id

```python
result_id: str = None
```

####### validmind.vm_models.result.result.TestResult.serialize

```python
serialize()
```

Serialize the result for the API

####### validmind.vm_models.result.result.TestResult.show

```python
show()
```

Display the result... May be overridden by subclasses

####### validmind.vm_models.result.result.TestResult.tables

```python
tables: Optional[List[ResultTable]] = None
```

####### validmind.vm_models.result.result.TestResult.test_name

```python
test_name: str
```

Get the test name, using custom title if available.

####### validmind.vm_models.result.result.TestResult.title

```python
title: Optional[str] = None
```

####### validmind.vm_models.result.result.TestResult.to_widget

```python
to_widget()
```

###### validmind.vm_models.result.result.logger

```python
logger = get_logger(__name__)
```

##### validmind.vm_models.result.utils

**Functions:**

- [**check_for_sensitive_data**](#validmind.vm_models.result.utils.check_for_sensitive_data) – Check if a table contains raw data from input datasets
- [**figures_to_widgets**](#validmind.vm_models.result.utils.figures_to_widgets) – Plot figures to a ipywidgets GridBox
- [**get_result_template**](#validmind.vm_models.result.utils.get_result_template) – Get the jinja html template for rendering test results
- [**tables_to_widgets**](#validmind.vm_models.result.utils.tables_to_widgets) – Convert summary (list of json tables) into a list of ipywidgets
- [**update_metadata**](#validmind.vm_models.result.utils.update_metadata) – Create or Update a Metadata Object

**Attributes:**

- [**AI_REVISION_NAME**](#validmind.vm_models.result.utils.AI_REVISION_NAME) –
- [**DEFAULT_REVISION_NAME**](#validmind.vm_models.result.utils.DEFAULT_REVISION_NAME) –
- [**logger**](#validmind.vm_models.result.utils.logger) –

###### validmind.vm_models.result.utils.AI_REVISION_NAME

```python
AI_REVISION_NAME = 'Generated by ValidMind AI'
```

###### validmind.vm_models.result.utils.DEFAULT_REVISION_NAME

```python
DEFAULT_REVISION_NAME = 'Default Description'
```

###### validmind.vm_models.result.utils.check_for_sensitive_data

```python
check_for_sensitive_data(data, inputs)
```

Check if a table contains raw data from input datasets

###### validmind.vm_models.result.utils.figures_to_widgets

```python
figures_to_widgets(figures)
```

Plot figures to a ipywidgets GridBox

###### validmind.vm_models.result.utils.get_result_template

```python
get_result_template()
```

Get the jinja html template for rendering test results

###### validmind.vm_models.result.utils.logger

```python
logger = get_logger(__name__)
```

###### validmind.vm_models.result.utils.tables_to_widgets

```python
tables_to_widgets(tables)
```

Convert summary (list of json tables) into a list of ipywidgets

###### validmind.vm_models.result.utils.update_metadata

```python
update_metadata(content_id, text, _json=None)
```

Create or Update a Metadata Object
