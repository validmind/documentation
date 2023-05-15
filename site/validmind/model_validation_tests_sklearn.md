# Core Library Tests

## Model Validation Tests for SKLearn-Compatible Models

### Model Validation Metrics

Metrics functions models trained with sklearn or that provide
a sklearn-like API


### _class_ validmind.model_validation.sklearn.metrics.AccuracyScore
Bases: `Metric`

Accuracy Score


#### type(_: ClassVar[str_ _ = 'evaluation_ )

#### scope(_: ClassVar[str_ _ = 'test_ )

#### key(_: ClassVar[str_ _ = 'accuracy_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### run()
Run the metric calculation and cache its results


### _class_ validmind.model_validation.sklearn.metrics.CharacteristicStabilityIndex
Bases: `Metric`

Characteristic Stability Index between two datasets


#### type(_: ClassVar[str_ _ = 'training_ )

#### key(_: ClassVar[str_ _ = 'csi_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### value_formatter(_: ClassVar[str | None_ _ = 'key_values_ )

#### run()
Calculates PSI for each of the dataset features


### _class_ validmind.model_validation.sklearn.metrics.ConfusionMatrix
Bases: `Metric`

Confusion Matrix


#### type(_: ClassVar[str_ _ = 'evaluation_ )

#### scope(_: ClassVar[str_ _ = 'test_ )

#### key(_: ClassVar[str_ _ = 'confusion_matrix_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### run()
Run the metric calculation and cache its results


### _class_ validmind.model_validation.sklearn.metrics.F1Score
Bases: `Metric`

F1 Score


#### type(_: ClassVar[str_ _ = 'evaluation_ )

#### scope(_: ClassVar[str_ _ = 'test_ )

#### key(_: ClassVar[str_ _ = 'f1_score_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### run()
Run the metric calculation and cache its results


### _class_ validmind.model_validation.sklearn.metrics.PermutationFeatureImportance
Bases: `Metric`

Permutation Feature Importance


#### type(_: ClassVar[str_ _ = 'training_ )

#### scope(_: ClassVar[str_ _ = 'training_dataset_ )

#### key(_: ClassVar[str_ _ = 'pfi_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### run()
Run the metric calculation and cache its results


### _class_ validmind.model_validation.sklearn.metrics.PrecisionRecallCurve
Bases: `Metric`

Precision Recall Curve


#### type(_: ClassVar[str_ _ = 'evaluation_ )

#### scope(_: ClassVar[str_ _ = 'test_ )

#### key(_: ClassVar[str_ _ = 'pr_curve_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### run()
Run the metric calculation and cache its results


### _class_ validmind.model_validation.sklearn.metrics.PrecisionScore
Bases: `Metric`

Precision Score


#### type(_: ClassVar[str_ _ = 'evaluation_ )

#### scope(_: ClassVar[str_ _ = 'test_ )

#### key(_: ClassVar[str_ _ = 'precision_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### run()
Run the metric calculation and cache its results


### _class_ validmind.model_validation.sklearn.metrics.RecallScore
Bases: `Metric`

Recall Score


#### type(_: ClassVar[str_ _ = 'evaluation_ )

#### scope(_: ClassVar[str_ _ = 'test_ )

#### key(_: ClassVar[str_ _ = 'recall_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### run()
Run the metric calculation and cache its results


### _class_ validmind.model_validation.sklearn.metrics.ROCAUCScore
Bases: `Metric`

ROC AUC Score


#### type(_: ClassVar[str_ _ = 'evaluation_ )

#### scope(_: ClassVar[str_ _ = 'test_ )

#### key(_: ClassVar[str_ _ = 'roc_auc_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### run()
Run the metric calculation and cache its results


### _class_ validmind.model_validation.sklearn.metrics.ROCCurve
Bases: `Metric`

ROC Curve


#### type(_: ClassVar[str_ _ = 'evaluation_ )

#### scope(_: ClassVar[str_ _ = 'test_ )

#### key(_: ClassVar[str_ _ = 'roc_curve_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### run()
Run the metric calculation and cache its results


### _class_ validmind.model_validation.sklearn.metrics.SHAPGlobalImportance
Bases: `Metric`

SHAP Global Importance


#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### name(_ = 'shap_ )

#### run()
Run the metric calculation and cache its results


### _class_ validmind.model_validation.sklearn.metrics.PopulationStabilityIndex
Bases: `Metric`

Population Stability Index between two datasets


#### type(_: ClassVar[str_ _ = 'training_ )

#### key(_: ClassVar[str_ _ = 'psi_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### value_formatter(_: ClassVar[str | None_ _ = 'records_ )

#### run()
Run the metric calculation and cache its results

### Data Validation Threshold Tests

Threshold based tests


### _class_ validmind.model_validation.sklearn.threshold_tests.MinimumAccuracy
Bases: `ThresholdTest`

Test that the model’s prediction accuracy on a dataset meets or
exceeds a predefined threshold.


#### category(_: ClassVar[str_ _ = 'model_performance_ )

#### name(_: ClassVar[str_ _ = 'accuracy_score_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### default_params(_: ClassVar[dict_ _ = {'min_threshold': 0.7_ )

#### run()
Run the test and cache its results


### _class_ validmind.model_validation.sklearn.threshold_tests.MinimumF1Score
Bases: `ThresholdTest`

Test that the model’s F1 score on the validation dataset meets or
exceeds a predefined threshold.


#### category(_: ClassVar[str_ _ = 'model_performance_ )

#### name(_: ClassVar[str_ _ = 'f1_score_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### default_params(_: ClassVar[dict_ _ = {'min_threshold': 0.5_ )

#### run()
Run the test and cache its results


### _class_ validmind.model_validation.sklearn.threshold_tests.MinimumROCAUCScore
Bases: `ThresholdTest`

Test that the model’s ROC AUC score on the validation dataset meets or
exceeds a predefined threshold.


#### category(_: ClassVar[str_ _ = 'model_performance_ )

#### name(_: ClassVar[str_ _ = 'roc_auc_score_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### default_params(_: ClassVar[dict_ _ = {'min_threshold': 0.5_ )

#### run()
Run the test and cache its results


### _class_ validmind.model_validation.sklearn.threshold_tests.TrainingTestDegradation
Bases: `ThresholdTest`

Test that the degradation in performance between the training and test datasets
does not exceed a predefined threshold.


#### category(_: ClassVar[str_ _ = 'model_performance_ )

#### name(_: ClassVar[str_ _ = 'training_test_degradation_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### default_params(_: ClassVar[dict_ _ = {'metrics': ['accuracy', 'precision', 'recall', 'f1']_ )

#### default_metrics(_ = {'accuracy': <function accuracy_score>, 'f1': functools.partial(<function f1_score>, zero_division=0), 'precision': functools.partial(<function precision_score>, zero_division=0), 'recall': functools.partial(<function recall_score>, zero_division=0)_ )

#### run()
Run the test and cache its results


### _class_ validmind.model_validation.sklearn.threshold_tests.OverfitDiagnosis
Bases: `ThresholdTest`

Test that identify overfit regions with high residuals by histogram slicing techniques.


#### category(_: ClassVar[str_ _ = 'model_diagnosis_ )

#### name(_: ClassVar[str_ _ = 'overfit_regions_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### default_params(_: ClassVar[dict_ _ = {'cut_off_percentage': 4, 'features_columns': None_ )

#### default_metrics(_ = {'accuracy': <function accuracy_score>_ )

#### run()
Run the test and cache its results


### _class_ validmind.model_validation.sklearn.threshold_tests.WeakspotsDiagnosis
Bases: `ThresholdTest`

Test that identify weak regions with high residuals by histogram slicing techniques.


#### category(_: ClassVar[str_ _ = 'model_diagnosis_ )

#### name(_: ClassVar[str_ _ = 'weak_spots_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### default_params(_: ClassVar[dict_ _ = {'features_columns': None, 'thresholds': {'accuracy': 0.75, 'f1': 0.7, 'precision': 0.5, 'recall': 0.5}_ )

#### default_metrics(_ = {'accuracy': <function accuracy_score>, 'f1': functools.partial(<function f1_score>, zero_division=0), 'precision': functools.partial(<function precision_score>, zero_division=0), 'recall': functools.partial(<function recall_score>, zero_division=0)_ )

#### run()
Run the test and cache its results


### _class_ validmind.model_validation.sklearn.threshold_tests.RobustnessDiagnosis
Bases: `ThresholdTest`

Test robustness of model by perturbing the features column values


#### category(_: ClassVar[str_ _ = 'model_diagnosis_ )

#### name(_: ClassVar[str_ _ = 'robustness_ )

#### required_context(_: ClassVar[List[str]_ _ = ['model'_ )

#### default_params(_: ClassVar[dict_ _ = {'features_columns': None, 'scaling_factor_std_dev_list': [0.01, 0.02]_ )

#### default_metrics(_ = {'accuracy': <function accuracy_score>_ )

#### run()
Run the test and cache its results


#### add_noise_std_dev(values: List[float], x_std_dev: float)
Adds Gaussian noise to a list of values.


* **Parameters**

    
    * **values** (*list**[**float**]*) – A list of numerical values to which noise is added.


    * **x_std_dev** (*float*) – A scaling factor for the standard deviation of the noise.



* **Returns**

    A tuple containing:


        * A list of noisy values, where each value is the sum of the corresponding value

        in the input list and a randomly generated value sampled from a Gaussian distribution
        with mean 0 and standard deviation x_std_dev times the standard deviation of the input list.
        - The standard deviation of the input list of values.




* **Return type**

    tuple[list[float], float]
