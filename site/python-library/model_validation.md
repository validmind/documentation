<a id="validmind.model_validation"></a>

# validmind.model\_validation

Entrypoint to Model Evaluation API

<a id="validmind.model_validation.model_metadata"></a>

# validmind.model\_validation.model\_metadata

<a id="validmind.model_validation.model_metadata.get_xgboost_objective"></a>

#### get\_xgboost\_objective

```python
def get_xgboost_objective(model)
```

Attempts to extract the model subtask (binary, multi-class, etc.)
from the model's objective. Only binary classification is supported
at the moment

<a id="validmind.model_validation.model_metadata.get_info_from_model_instance"></a>

#### get\_info\_from\_model\_instance

```python
def get_info_from_model_instance(model)
```

Attempts to extract all model info from a model object instance

<a id="validmind.model_validation.model_metadata.get_statsmodels_model_params"></a>

#### get\_statsmodels\_model\_params

```python
def get_statsmodels_model_params(model)
```

Extracts the fit() method's parametesr from a
statsmodels model object instance

<a id="validmind.model_validation.model_metadata.get_params_from_model_instance"></a>

#### get\_params\_from\_model\_instance

```python
def get_params_from_model_instance(model)
```

Attempts to extract model hyperparameters from a model object instance

<a id="validmind.model_validation.model_metadata.ModelMetadata"></a>

## ModelMetadata Objects

```python
@dataclass
class ModelMetadata(TestContextUtils)
```

Custom class to collect the following metadata for a model:
- Model architecture
- Model hyperparameters
- Model task type

<a id="validmind.model_validation.model_metadata.ModelMetadata.run"></a>

#### run

```python
def run()
```

Just set the model to the result attribute of the test plan result
and it will be logged via the `log_model` function

<a id="validmind.model_validation.sklearn.metrics"></a>

# validmind.model\_validation.sklearn.metrics

Metrics functions models trained with sklearn or that provide
a sklearn-like API

<a id="validmind.model_validation.sklearn.metrics.AccuracyScore"></a>

## AccuracyScore Objects

```python
@dataclass
class AccuracyScore(Metric)
```

Accuracy Score

<a id="validmind.model_validation.sklearn.metrics.CharacteristicStabilityIndex"></a>

## CharacteristicStabilityIndex Objects

```python
@dataclass
class CharacteristicStabilityIndex(Metric)
```

Characteristic Stability Index between two datasets

<a id="validmind.model_validation.sklearn.metrics.CharacteristicStabilityIndex.run"></a>

#### run

```python
def run()
```

Calculates PSI for each of the dataset features

<a id="validmind.model_validation.sklearn.metrics.ConfusionMatrix"></a>

## ConfusionMatrix Objects

```python
@dataclass
class ConfusionMatrix(Metric)
```

Confusion Matrix

<a id="validmind.model_validation.sklearn.metrics.F1Score"></a>

## F1Score Objects

```python
@dataclass
class F1Score(Metric)
```

F1 Score

<a id="validmind.model_validation.sklearn.metrics.PermutationFeatureImportance"></a>

## PermutationFeatureImportance Objects

```python
@dataclass
class PermutationFeatureImportance(Metric)
```

Permutation Feature Importance

<a id="validmind.model_validation.sklearn.metrics.PrecisionRecallCurve"></a>

## PrecisionRecallCurve Objects

```python
@dataclass
class PrecisionRecallCurve(Metric)
```

Precision Recall Curve

<a id="validmind.model_validation.sklearn.metrics.PrecisionScore"></a>

## PrecisionScore Objects

```python
@dataclass
class PrecisionScore(Metric)
```

Precision Score

<a id="validmind.model_validation.sklearn.metrics.RecallScore"></a>

## RecallScore Objects

```python
@dataclass
class RecallScore(Metric)
```

Recall Score

<a id="validmind.model_validation.sklearn.metrics.ROCAUCScore"></a>

## ROCAUCScore Objects

```python
@dataclass
class ROCAUCScore(Metric)
```

ROC AUC Score

<a id="validmind.model_validation.sklearn.metrics.ROCCurve"></a>

## ROCCurve Objects

```python
@dataclass
class ROCCurve(Metric)
```

ROC Curve

<a id="validmind.model_validation.sklearn.metrics.SHAPGlobalImportance"></a>

## SHAPGlobalImportance Objects

```python
@dataclass
class SHAPGlobalImportance(TestContextUtils)
```

SHAP Global Importance. Custom metric

<a id="validmind.model_validation.sklearn.metrics.PopulationStabilityIndex"></a>

## PopulationStabilityIndex Objects

```python
@dataclass
class PopulationStabilityIndex(Metric)
```

Population Stability Index between two datasets

<a id="validmind.model_validation.sklearn.threshold_tests"></a>

# validmind.model\_validation.sklearn.threshold\_tests

Threshold based tests

<a id="validmind.model_validation.sklearn.threshold_tests.AccuracyTest"></a>

## AccuracyTest Objects

```python
@dataclass
class AccuracyTest(ThresholdTest)
```

Test that the accuracy score is above a threshold.

<a id="validmind.model_validation.sklearn.threshold_tests.F1ScoreTest"></a>

## F1ScoreTest Objects

```python
@dataclass
class F1ScoreTest(ThresholdTest)
```

Test that the F1 score is above a threshold.

<a id="validmind.model_validation.sklearn.threshold_tests.ROCAUCScoreTest"></a>

## ROCAUCScoreTest Objects

```python
@dataclass
class ROCAUCScoreTest(ThresholdTest)
```

Test that the ROC AUC score is above a threshold.

<a id="validmind.model_validation.sklearn.threshold_tests.TrainingTestDegradationTest"></a>

## TrainingTestDegradationTest Objects

```python
@dataclass
class TrainingTestDegradationTest(ThresholdTest)
```

Test that the training set metrics are better than the test set metrics.

<a id="validmind.model_validation.sklearn"></a>

# validmind.model\_validation.sklearn

<a id="validmind.model_validation.utils"></a>

# validmind.model\_validation.utils

TODO: update to work with test plans

Utils for Model Evaluation

<a id="validmind.model_validation.utils.summarize_evaluation_results"></a>

#### summarize\_evaluation\_results

```python
def summarize_evaluation_results(results)
```

Summarize the results of the model evaluation test suite

<a id="validmind.model_validation.utils.summarize_evaluation_metrics"></a>

#### summarize\_evaluation\_metrics

```python
def summarize_evaluation_metrics(metrics)
```

Summarize the results of the model evaluation test suite

