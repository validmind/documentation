<a id="validmind.test_plans"></a>

# validmind.test\_plans

Test Plans entry point

<a id="validmind.test_plans.list_plans"></a>

#### list\_plans

```python
def list_plans(pretty: bool = True)
```

Returns a list of all available test plans

<a id="validmind.test_plans.list_tests"></a>

#### list\_tests

```python
def list_tests(type: str = "all", pretty: bool = True)
```

Returns a list of all available tests

<a id="validmind.test_plans.get_by_name"></a>

#### get\_by\_name

```python
def get_by_name(name: str)
```

Returns the test plan by name

<a id="validmind.test_plans.describe_plan"></a>

#### describe\_plan

```python
def describe_plan(plan_id: str)
```

Returns a description of the test plan

<a id="validmind.test_plans.tabular_datasets"></a>

# validmind.test\_plans.tabular\_datasets

Test plan for tabular datasets

Ideal setup is to have the API client to read a
custom test plan from the project's configuration

<a id="validmind.test_plans.tabular_datasets.TabularDatasetDescription"></a>

## TabularDatasetDescription Objects

```python
class TabularDatasetDescription(TestPlan)
```

Test plan to extract metadata and descriptive
statistics from a tabular dataset

<a id="validmind.test_plans.tabular_datasets.TabularDataQuality"></a>

## TabularDataQuality Objects

```python
class TabularDataQuality(TestPlan)
```

Test plan for data quality on tabular datasets

<a id="validmind.test_plans.tabular_datasets.TabularDataset"></a>

## TabularDataset Objects

```python
class TabularDataset(TestPlan)
```

Test plan for generic tabular datasets

<a id="validmind.test_plans.sklearn_classifier"></a>

# validmind.test\_plans.sklearn\_classifier

Test plan for tabular datasets

Ideal setup is to have the API client to read a
custom test plan from the project's configuration

<a id="validmind.test_plans.sklearn_classifier.SKLearnClassifierMetrics"></a>

## SKLearnClassifierMetrics Objects

```python
class SKLearnClassifierMetrics(TestPlan)
```

Test plan for sklearn classifier metrics

<a id="validmind.test_plans.sklearn_classifier.SKLearnClassifierPerformance"></a>

## SKLearnClassifierPerformance Objects

```python
class SKLearnClassifierPerformance(TestPlan)
```

Test plan for sklearn classifier models

<a id="validmind.test_plans.sklearn_classifier.SKLearnClassifier"></a>

## SKLearnClassifier Objects

```python
class SKLearnClassifier(TestPlan)
```

Test plan for sklearn classifier models that includes
both metrics and validation tests

