<!-- ValidMind Developer Framework documentation master file, created by
sphinx-quickstart on Thu Mar  9 11:05:09 2023.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# ValidMind Developer Framework


## validmind.init

```python
validmind.init(project, api_key=None, api_secret=None, api_host=None)
```

Initializes the API client instances and /pings the API
to ensure the provided credentials are valid.

This is an example to test how to show the code in the documentation.

```python
import validmind as vm

vm.init(
    project="my-project",
    api_key="my-api-key",
    api_secret
)
```


* **Parameters**

    
    * **project** (*str*) – The project cuid.


    * **api_key** (*str*) – The API key.


    * **api_secret** (*str*) – The API secret.


    * **api_host** (*str*) – The API host.



* **Raises**

    **ValueError** – If the API key and secret are not provided.



* **Returns**

    True if the ping was successful.



* **Return type**

    bool



## validmind.init_dataset

```python
validmind.init_dataset(dataset, type='training', options=None, targets=None, target_column=None, class_labels=None)
```

Initializes a VM Dataset, which can then be passed to other functions
that can perform additional analysis and tests on the data. This function
also ensures we are reading a valid dataset type. We only support Pandas
DataFrames at the moment.


* **Parameters**

    
    * **dataset** (*pd.DataFrame*) – We only support Pandas DataFrames at the moment


    * **type** (*str*) – The dataset split type is necessary for mapping and relating multiple
    datasets together. Can be one of training, validation, test or generic


    * **options** (*dict*) – A dictionary of options for the dataset


    * **targets** (*vm.vm.DatasetTargets*) – A list of target variables


    * **target_column** (*str*) – The name of the target column in the dataset


    * **class_labels** (*dict*) – A list of class labels for classification problems



## validmind.init_model

```python
validmind.init_model(model)
```

Initializes a VM Model, which can then be passed to other functions
that can perform additional analysis and tests on the data. This function
also ensures we are reading a supported model type.


* **Parameters**

    **model** – A trained model instance



## validmind.log_dataset

```python
validmind.log_dataset(vm_dataset)
```

Logs metadata and statistics about a dataset to ValidMind API.


* **Parameters**

    
    * **dataset** – A VM dataset object


    * **dataset_type** – The type of dataset. Can be one of “training”, “test”, or “validation”.


    * **dataset_options** – Additional dataset options for analysis


    * **dataset_targets** (*validmind.DatasetTargets**, **optional*) – A list of targets for the dataset.


    * **features** – Optional. A list of features metadata.



## validmind.log_figure

```python
validmind.log_figure(data_or_path, key, metadata, run_cuid=None)
```

Logs a figure


* **Parameters**

    
    * **data_or_path** – the path of the image or the data of the plot


    * **key** – identifier of the figure


    * **metadata** – python data structure


    * **run_cuid** – run cuid from start_run



## validmind.log_metadata

```python
validmind.log_metadata(content_id, text=None, extra_json=None)
```

Logs free-form metadata to ValidMind API.


* **Parameters**

    
    * **content_id** – Unique content identifier for the metadata


    * **text** – Free-form text to assign to the metadata


    * **extra_json** – Free-form key-value pairs to assign to the metadata



## validmind.log_metrics

```python
validmind.log_metrics(metrics, run_cuid=None)
```

Logs metrics to ValidMind API.


* **Parameters**

    
    * **metrics** – A list of Metric objects.


    * **run_cuid** – The run CUID. If not provided, a new run will be created.



## validmind.log_model

```python
validmind.log_model(vm_model)
```

Logs model metadata and hyperparameters to ValidMind API.
:param vm_model: A ValidMind Model wrapper instance.


## validmind.log_test_results

```python
validmind.log_test_results(results, run_cuid=None, dataset_type='training')
```

Logs test results information. This method will be called automatically be any function
running tests but can also be called directly if the user wants to run tests on their own.


* **Parameters**

    
    * **results** – A list of TestResults objects


    * **run_cuid** – The run CUID. If not provided, a new run will be created.



## validmind.run_test_plan

```python
validmind.run_test_plan(test_plan_name, send=True, \*\*kwargs)
```

High Level function for running a test plan

This function provides a high level interface for running a test plan. It removes the need
to manually initialize a TestPlan instance and run it. This function will automatically
find the correct test plan class based on the test_plan_name, initialize the test plan, and
run it.


* **Parameters**

    
    * **test_plan_name** (*str*) – The test plan name (e.g. ‘sklearn_classifier’)


    * **send** (*bool*) – Whether to post the test results to the API. send=False is useful for testing


    * **kwargs** (*dict*) – Additional keyword arguments to pass to the test plan. These will provide
    the TestPlan instance with the necessary context to run the tests. e.g. dataset, model etc.
    See the documentation for the specific test plan for more details.
