<a id="validmind.vm_models"></a>

# validmind.vm\_models

Models entrypoint

<a id="validmind.vm_models.test_result"></a>

# validmind.vm\_models.test\_result

TestResult models

<a id="validmind.vm_models.test_plan"></a>

# validmind.vm\_models.test\_plan

TestPlan class

<a id="validmind.vm_models.test_plan.TestPlan"></a>

## TestPlan Objects

```python
@dataclass
class TestPlan()
```

Base class for test plans. Test plans are used to define any
arbitrary grouping of tests that will be run on a dataset or model.

<a id="validmind.vm_models.test_plan.TestPlan.validate_context"></a>

#### validate\_context

```python
def validate_context()
```

Validates that the context elements are present
in the instance so that the test plan can be run

<a id="validmind.vm_models.test_plan.TestPlan.run"></a>

#### run

```python
def run(send=True)
```

Runs the test plan

<a id="validmind.vm_models.figure"></a>

# validmind.vm\_models.figure

Figure objects track the figure schema supported by the ValidMind API

<a id="validmind.vm_models.figure.Figure"></a>

## Figure Objects

```python
@dataclass
class Figure()
```

Figure objects track the schema supported by the ValidMind API

<a id="validmind.vm_models.figure.Figure.serialize"></a>

#### serialize

```python
def serialize()
```

Serializes the Figure to a dictionary so it can be sent to the API

<a id="validmind.vm_models.dataset_utils"></a>

# validmind.vm\_models.dataset\_utils

Utilities for manipulating VMDataset objects

<a id="validmind.vm_models.dataset_utils.get_x_and_y"></a>

#### get\_x\_and\_y

```python
def get_x_and_y(df, target_column)
```

Get the X and Y dataframes from the input dataset.

<a id="validmind.vm_models.dataset_utils.parse_dataset_variables"></a>

#### parse\_dataset\_variables

```python
def parse_dataset_variables(df, options=None)
```

Infers the data types for each column using pandas_profiling's
typeset from visions library.

If dummy variables were specified with dataset_options, we will
not inter the types for these columns since they need to be described
as a group of columns (e.g. dummy_a, dummy_b, dummy_c, etc.)

When a type is inferred as Unsupported we check if it's a null column
and mark it appropriately.

<a id="validmind.vm_models.dataset_utils.describe_dataset_field"></a>

#### describe\_dataset\_field

```python
def describe_dataset_field(df, field)
```

Gets descriptive statistics for a single field in a Pandas DataFrame.

<a id="validmind.vm_models.dataset_utils.get_field_histograms"></a>

#### get\_field\_histograms

```python
def get_field_histograms(df, field, type_)
```

Returns a collection of histograms for a numerical or categorical field.
We store different combinations of bin sizes to allow analyzing the data better

Will be used in favor of _get_histogram in the future

<a id="validmind.vm_models.dataset_utils.get_numerical_histograms"></a>

#### get\_numerical\_histograms

```python
def get_numerical_histograms(df, field)
```

Returns a collection of histograms for a numerical field, each one
with a different bin size

<a id="validmind.vm_models.model"></a>

# validmind.vm\_models.model

Model class wrapper

<a id="validmind.vm_models.model.ModelAttributes"></a>

## ModelAttributes Objects

```python
@dataclass()
class ModelAttributes()
```

Model attributes definition

<a id="validmind.vm_models.model.Model"></a>

## Model Objects

```python
@dataclass
class Model()
```

Model class wrapper

<a id="validmind.vm_models.model.Model.serialize"></a>

#### serialize

```python
def serialize()
```

Serializes the model to a dictionary so it can be sent to the API

<a id="validmind.vm_models.model.Model.predict"></a>

#### predict

```python
def predict(*args, **kwargs)
```

Predict method for the model. This is a wrapper around the model's
predict_proba (for classification) or predict (for regression) method

NOTE: This only works for sklearn or xgboost models at the moment

<a id="validmind.vm_models.model.Model.is_supported_model"></a>

#### is\_supported\_model

```python
@classmethod
def is_supported_model(cls, model)
```

Checks if the model is supported by the API

<a id="validmind.vm_models.dataset"></a>

# validmind.vm\_models.dataset

Dataset class wrapper

<a id="validmind.vm_models.dataset.DatasetTargets"></a>

## DatasetTargets Objects

```python
@dataclass()
class DatasetTargets()
```

Dataset targets definition

<a id="validmind.vm_models.dataset.Dataset"></a>

## Dataset Objects

```python
@dataclass()
class Dataset()
```

Model class wrapper

<a id="validmind.vm_models.dataset.Dataset.__post_init__"></a>

#### \_\_post\_init\_\_

```python
def __post_init__()
```

Set target_column and class_labels from DatasetTargets

<a id="validmind.vm_models.dataset.Dataset.x"></a>

#### x

```python
@property
def x()
```

Returns the dataset's features

<a id="validmind.vm_models.dataset.Dataset.y"></a>

#### y

```python
@property
def y()
```

Returns the dataset's target column

<a id="validmind.vm_models.dataset.Dataset.get_feature_by_id"></a>

#### get\_feature\_by\_id

```python
def get_feature_by_id(feature_id)
```

Returns the feature with the given id. We also build a lazy
lookup cache in case the same feature is requested multiple times.

<a id="validmind.vm_models.dataset.Dataset.get_feature_type"></a>

#### get\_feature\_type

```python
def get_feature_type(feature_id)
```

Returns the type of the feature with the given id

<a id="validmind.vm_models.dataset.Dataset.serialize"></a>

#### serialize

```python
def serialize()
```

Serializes the model to a dictionary so it can be sent to the API

<a id="validmind.vm_models.dataset.Dataset.describe"></a>

#### describe

```python
def describe()
```

Extracts descriptive statistics for each field in the dataset

<a id="validmind.vm_models.dataset.Dataset.get_correlations"></a>

#### get\_correlations

```python
def get_correlations()
```

Extracts correlations for each field in the dataset

<a id="validmind.vm_models.dataset.Dataset.get_correlation_plots"></a>

#### get\_correlation\_plots

```python
def get_correlation_plots(n_top=15)
```

Extracts correlation plots for the n_top correlations in the dataset

<a id="validmind.vm_models.dataset.Dataset.transformed_dataset"></a>

#### transformed\_dataset

```python
@property
def transformed_dataset(force_refresh=False)
```

Returns a transformed dataset that uses the features from vm_dataset.
Some of the features in vm_dataset are of type Dummy so we need to
reverse the one hot encoding and drop the individual dummy columns

<a id="validmind.vm_models.metric"></a>

# validmind.vm\_models.metric

Class for storing ValidMind metric objects and associated
data for display and reporting purposes

<a id="validmind.vm_models.metric.Metric"></a>

## Metric Objects

```python
@dataclass
class Metric(TestContextUtils)
```

Metric objects track the schema supported by the ValidMind API

<a id="validmind.vm_models.metric.Metric.__post_init__"></a>

#### \_\_post\_init\_\_

```python
def __post_init__()
```

Set default params if not provided

<a id="validmind.vm_models.metric.Metric.run"></a>

#### run

```python
def run(*args, **kwargs)
```

Run the metric calculation and cache its results

<a id="validmind.vm_models.metric.Metric.cache_results"></a>

#### cache\_results

```python
def cache_results(metric_value: Union[dict, list, pd.DataFrame],
                  figures: Optional[object] = None)
```

Cache the results of the metric calculation and do any post-processing if needed

<a id="validmind.vm_models.plot_utils"></a>

# validmind.vm\_models.plot\_utils

Plot utilities

<a id="validmind.vm_models.plot_utils.get_box_plot"></a>

#### get\_box\_plot

```python
def get_box_plot(df, x, y)
```

Returns a box plot for a pair of features

<a id="validmind.vm_models.plot_utils.get_crosstab_plot"></a>

#### get\_crosstab\_plot

```python
def get_crosstab_plot(vm_dataset, x, y)
```

Returns a crosstab plot for a pair of features. If one of the features
is the target column, we should not use it as an index

<a id="validmind.vm_models.plot_utils.get_scatter_plot"></a>

#### get\_scatter\_plot

```python
def get_scatter_plot(df, x, y)
```

Returns a scatter plot for a pair of features

<a id="validmind.vm_models.plot_utils.get_plot_for_feature_pair"></a>

#### get\_plot\_for\_feature\_pair

```python
def get_plot_for_feature_pair(vm_dataset, x, y)
```

Checks the data types for each feature pair and creates the
appropriate plot to represent their relationship

<a id="validmind.vm_models.threshold_test"></a>

# validmind.vm\_models.threshold\_test

(Threshold)Test class wrapper. Our API exposes the concept of of a
Test (as test_results) but we'll refer to it as a ThresholdTest to
avoid confusion with the "tests" in the general data science/modeling sense.

TODO: Test definitions should be supported in the API too

<a id="validmind.vm_models.threshold_test.ThresholdTest"></a>

## ThresholdTest Objects

```python
@dataclass
class ThresholdTest(TestContextUtils)
```

A threshold test is a combination of a metric/plot we track and a
corresponding set of parameters and thresholds values that allow
us to determine whether the metric/plot passes or fails.

<a id="validmind.vm_models.threshold_test.ThresholdTest.__post_init__"></a>

#### \_\_post\_init\_\_

```python
def __post_init__()
```

Set default params if not provided

<a id="validmind.vm_models.threshold_test.ThresholdTest.run"></a>

#### run

```python
def run(*args, **kwargs)
```

Run the test and cache its results

<a id="validmind.vm_models.threshold_test.ThresholdTest.cache_results"></a>

#### cache\_results

```python
def cache_results(results: List[TestResult], passed: bool)
```

Cache the individual results of the threshold test as a list of TestResult objects

<a id="validmind.vm_models.test_plan_result"></a>

# validmind.vm\_models.test\_plan\_result

TestPlanResult

<a id="validmind.vm_models.test_plan_result.TestPlanResult"></a>

## TestPlanResult Objects

```python
@dataclass
class TestPlanResult()
```

Result wrapper tests that run as part of a test plan

<a id="validmind.vm_models.test_context"></a>

# validmind.vm\_models.test\_context

TestContext

<a id="validmind.vm_models.test_context.TestContext"></a>

## TestContext Objects

```python
@dataclass
class TestContext()
```

Holds context that can be used by tests to run.
Allows us to store data that needs to be reused
across different tests/metrics such as model predictions,
shared dataset metrics, etc.

<a id="validmind.vm_models.test_context.TestContextUtils"></a>

## TestContextUtils Objects

```python
class TestContextUtils()
```

Utility methods for classes that receive a TestContext

TODO: more validation

<a id="validmind.vm_models.test_context.TestContextUtils.class_predictions"></a>

#### class\_predictions

```python
def class_predictions(y_predict)
```

Converts a set of probability predictions to class predictions

<a id="validmind.vm_models.test_context.TestContextUtils.df"></a>

#### df

```python
@property
def df()
```

Returns a Pandas DataFrame for the dataset, first checking if
we passed in a Dataset or a DataFrame

<a id="validmind.vm_models.metric_result"></a>

# validmind.vm\_models.metric\_result

MetricResult wrapper

<a id="validmind.vm_models.metric_result.MetricResult"></a>

## MetricResult Objects

```python
@dataclass
class MetricResult()
```

MetricResult class definition. A MetricResult is returned by any internal method
that extracts metrics from a dataset or model, and returns 1) Metric and Figure
objects that can be sent to the API and 2) and plots and metadata for display purposes

<a id="validmind.vm_models.metric_result.MetricResult.serialize"></a>

#### serialize

```python
def serialize()
```

Serializes the Metric to a dictionary so it can be sent to the API

