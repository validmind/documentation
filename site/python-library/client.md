<a id="validmind.client"></a>

# validmind.client

Client interface for all data and model validation functions

<a id="validmind.client.init_dataset"></a>

#### init\_dataset

```python
def init_dataset(dataset,
                 type="training",
                 options=None,
                 targets=None,
                 target_column=None,
                 class_labels=None)
```

Initializes a VM Dataset, which can then be passed to other functions
that can perform additional analysis and tests on the data. This function
also ensures we are reading a valid dataset type. We only support Pandas
DataFrames at the moment.

**Arguments**:

- `dataset` _pd.DataFrame_ - We only support Pandas DataFrames at the moment
- `type` _str_ - The dataset split type is necessary for mapping and relating multiple
  datasets together. Can be one of training, validation, test or generic
- `options` _dict_ - A dictionary of options for the dataset
- `targets` _vm.vm.DatasetTargets_ - A list of target variables
- `target_column` _str_ - The name of the target column in the dataset
- `class_labels` _dict_ - A list of class labels for classification problems
  

**Raises**:

- `ValueError` - If the dataset type is not supported
  

**Returns**:

- `vm.vm.Dataset` - A VM Dataset instance

<a id="validmind.client.init_model"></a>

#### init\_model

```python
def init_model(model)
```

Initializes a VM Model, which can then be passed to other functions
that can perform additional analysis and tests on the data. This function
also ensures we are reading a supported model type.

**Arguments**:

- `model` - A trained sklearn model
  

**Raises**:

- `ValueError` - If the model type is not supported
  

**Returns**:

- `vm.vm.Model` - A VM Model instance

<a id="validmind.client.run_test_plan"></a>

#### run\_test\_plan

```python
def run_test_plan(test_plan_name, send=True, **kwargs)
```

High Level function for running a test plan

This function provides a high level interface for running a test plan. It removes the need
to manually initialize a TestPlan instance and run it. This function will automatically
find the correct test plan class based on the test_plan_name, initialize the test plan, and
run it.

**Arguments**:

- `test_plan_name` _str_ - The test plan name (e.g. 'sklearn_classifier')
- `send` _bool, optional_ - Whether to post the test results to the API. send=False is useful for testing. Defaults to True.
- `**kwargs` - Additional keyword arguments to pass to the test plan. These will provide
  the TestPlan instance with the necessary context to run the tests. e.g. dataset, model etc.
  See the documentation for the specific test plan for more details.
  

**Raises**:

- `ValueError` - If the test plan name is not found or if there is an error initializing the test plan
  

**Returns**:

- `dict` - A dictionary of test results

