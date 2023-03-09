<a id="validmind.data_validation"></a>

# validmind.data\_validation

Data Validation module

<a id="validmind.data_validation.get_threshold_tests"></a>

#### get\_threshold\_tests

```python
def get_threshold_tests(pretty: bool = False)
```

Returns a list of all available threshold tests

<a id="validmind.data_validation.metrics"></a>

# validmind.data\_validation.metrics

Metrics functions for any Pandas-compatible datasets

<a id="validmind.data_validation.metrics.DatasetMetadata"></a>

## DatasetMetadata Objects

```python
@dataclass
class DatasetMetadata(TestContextUtils)
```

Custom class to collect a set of descriptive statistics for a dataset.
This class will log dataset metadata via `log_dataset` instead of a metric.
Dataset metadat is necessary to initialize dataset object that can be related
to different metrics and test results

<a id="validmind.data_validation.metrics.DatasetMetadata.run"></a>

#### run

```python
def run()
```

Just set the dataset to the result attribute of the test plan result
and it will be logged via the `log_dataset` function

<a id="validmind.data_validation.metrics.DatasetCorrelations"></a>

## DatasetCorrelations Objects

```python
@dataclass
class DatasetCorrelations(Metric)
```

Extracts the correlation matrix for a dataset. The following coefficients
are calculated:
- Pearson's R for numerical variables
- Cramer's V for categorical variables
- Correlation ratios for categorical-numerical variables

<a id="validmind.data_validation.metrics.DatasetDescription"></a>

## DatasetDescription Objects

```python
@dataclass
class DatasetDescription(Metric)
```

Collects a set of descriptive statistics for a dataset

<a id="validmind.data_validation.threshold_tests"></a>

# validmind.data\_validation.threshold\_tests

Threshold based tests

<a id="validmind.data_validation.threshold_tests.ClassImbalanceTest"></a>

## ClassImbalanceTest Objects

```python
@dataclass
class ClassImbalanceTest(ThresholdTest)
```

Test that the minority class does not represent more than a threshold
of the total number of examples

<a id="validmind.data_validation.threshold_tests.DuplicatesTest"></a>

## DuplicatesTest Objects

```python
@dataclass
class DuplicatesTest(ThresholdTest)
```

Test that the number of duplicates is less than a threshold

<a id="validmind.data_validation.threshold_tests.HighCardinalityTest"></a>

## HighCardinalityTest Objects

```python
@dataclass
class HighCardinalityTest(ThresholdTest)
```

Test that the number of unique values in a column is less than a threshold

<a id="validmind.data_validation.threshold_tests.HighPearsonCorrelationTest"></a>

## HighPearsonCorrelationTest Objects

```python
@dataclass
class HighPearsonCorrelationTest(ThresholdTest)
```

Test that the Pearson correlation between two columns is less than a threshold

Inspired by: https://github.com/ydataai/pandas-profiling/blob/f8bad5dde27e3f87f11ac74fb8966c034bc22db8/src/pandas_profiling/model/correlations.py

<a id="validmind.data_validation.threshold_tests.MissingValuesTest"></a>

## MissingValuesTest Objects

```python
@dataclass
class MissingValuesTest(ThresholdTest)
```

Test that the number of missing values is less than a threshold

<a id="validmind.data_validation.threshold_tests.SkewnessTest"></a>

## SkewnessTest Objects

```python
@dataclass
class SkewnessTest(ThresholdTest)
```

Test that the skewness of a column is less than a threshold

<a id="validmind.data_validation.threshold_tests.UniqueRowsTest"></a>

## UniqueRowsTest Objects

```python
@dataclass
class UniqueRowsTest(ThresholdTest)
```

Test that the number of unique rows is greater than a threshold

<a id="validmind.data_validation.threshold_tests.ZerosTest"></a>

## ZerosTest Objects

```python
@dataclass
class ZerosTest(ThresholdTest)
```

Test that the number of zeros is less than a threshold

