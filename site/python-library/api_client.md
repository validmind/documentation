<a id="validmind.api_client"></a>

# validmind.api\_client

API Client

<a id="validmind.api_client.init"></a>

#### init

```python
def init(project, api_key=None, api_secret=None, api_host=None)
```

Initializes the API client instances and calls the /ping endpoint to ensure
the provided credentials are valid and we can connect to the ValidMind API.

If the API key and secret are not provided, the client will attempt to
retrieve them from the environment variables `VM_API_KEY` and `VM_API_SECRET`.

**Arguments**:

- `project` _str_ - The project CUID
- `api_key` _str, optional_ - The API key. Defaults to None.
- `api_secret` _str, optional_ - The API secret. Defaults to None.
- `api_host` _str, optional_ - The API host. Defaults to None.
  

**Raises**:

- `ValueError` - If the API key and secret are not provided
  

**Returns**:

- `bool` - True if the ping was successful

<a id="validmind.api_client.log_dataset"></a>

#### log\_dataset

```python
def log_dataset(vm_dataset)
```

Logs metadata and statistics about a dataset to ValidMind API.

**Arguments**:

- `vm_dataset` _validmind.VMDataset_ - A VM dataset object
- `dataset_type` _str, optional_ - The type of dataset. Can be one of "training", "test", or "validation". Defaults to "training".
- `dataset_options` _dict, optional_ - Additional dataset options for analysis. Defaults to None.
- `dataset_targets` _validmind.DatasetTargets, optional_ - A list of targets for the dataset. Defaults to None.
- `features` _list, optional_ - Optional. A list of features metadata. Defaults to None.
  

**Raises**:

- `Exception` - If the API call fails
  

**Returns**:

- `validmind.VMDataset` - The VMDataset object

<a id="validmind.api_client.log_metadata"></a>

#### log\_metadata

```python
def log_metadata(content_id, text=None, extra_json=None)
```

Logs free-form metadata to ValidMind API.

**Arguments**:

- `content_id` _str_ - Unique content identifier for the metadata
- `text` _str, optional_ - Free-form text to assign to the metadata. Defaults to None.
- `extra_json` _dict, optional_ - Free-form key-value pairs to assign to the metadata. Defaults to None.
  

**Raises**:

- `Exception` - If the API call fails
  

**Returns**:

- `bool` - True if the API call was successful

<a id="validmind.api_client.log_model"></a>

#### log\_model

```python
def log_model(vm_model)
```

Logs model metadata and hyperparameters to ValidMind API.

**Arguments**:

- `vm_model` _validmind.VMModel_ - A VM model object
  

**Raises**:

- `Exception` - If the API call fails
  

**Returns**:

- `bool` - True if the API call was successful

<a id="validmind.api_client.log_metrics"></a>

#### log\_metrics

```python
def log_metrics(metrics, run_cuid=None)
```

Logs metrics to ValidMind API.

**Arguments**:

- `metrics` _list_ - A list of Metric objects
- `run_cuid` _str, optional_ - The run CUID. If not provided, a new run will be created. Defaults to None.
  

**Raises**:

- `Exception` - If the API call fails
  

**Returns**:

- `bool` - True if the API call was successful

<a id="validmind.api_client.log_test_result"></a>

#### log\_test\_result

```python
def log_test_result(result, run_cuid=None, dataset_type="training")
```

Logs test results information. This method will be called automatically be any function
running tests but can also be called directly if the user wants to run tests on their own.

**Arguments**:

- `result` _validmind.TestResults_ - A TestResults object
- `run_cuid` _str, optional_ - The run CUID. If not provided, a new run will be created. Defaults to None.
- `dataset_type` _str, optional_ - The type of dataset. Can be one of "training", "test", or "validation". Defaults to "training".
  

**Raises**:

- `Exception` - If the API call fails
  

**Returns**:

- `bool` - True if the API call was successful

<a id="validmind.api_client.log_test_results"></a>

#### log\_test\_results

```python
def log_test_results(results, run_cuid=None, dataset_type="training")
```

Logs test results information. This method will be called automatically be any function
running tests but can also be called directly if the user wants to run tests on their own.

**Arguments**:

- `results` _list_ - A list of TestResults objects
- `run_cuid` _str, optional_ - The run CUID. If not provided, a new run will be created. Defaults to None.
- `dataset_type` _str, optional_ - The type of dataset. Can be one of "training", "test", or "validation". Defaults to "training".
  

**Raises**:

- `Exception` - If the API call fails
  

**Returns**:

- `bool` - True if the API call was successful

<a id="validmind.api_client.start_run"></a>

#### start\_run

```python
def start_run()
```

Starts a new test run. This method will return a test run CUID that needs to be
passed to any functions logging test results to the ValidMind API.

If "X-RUN-CUID" was already set as an HTTP header to the session, we reuse it

<a id="validmind.api_client.log_figure"></a>

#### log\_figure

```python
def log_figure(data_or_path, key, metadata, run_cuid=None)
```

Logs a figure

**Arguments**:

- `data_or_path` _str or matplotlib.figure.Figure_ - The path of the image or the data of the plot
- `key` _str_ - Identifier of the figure
- `metadata` _dict_ - Python data structure
- `run_cuid` _str, optional_ - The run CUID. If not provided, a new run will be created. Defaults to None.
  

**Raises**:

- `Exception` - If the API call fails
  

**Returns**:

- `bool` - True if the API call was successful

