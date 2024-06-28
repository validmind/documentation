# ClassifierPerformance

Evaluates performance of binary or multiclass classification models using precision, recall, F1-Score, accuracy,
and ROC AUC scores.

**Purpose**: The supplied script is designed to evaluate the performance of Machine Learning classification models.
It accomplishes this by computing precision, recall, F1-Score, and accuracy, as well as the ROC AUC (Receiver
operating characteristic - Area under the curve) scores, thereby providing a comprehensive analytic view of the
models' performance. The test is adaptable, handling binary and multiclass models equally effectively.

**Test Mechanism**: The script produces a report that includes precision, recall, F1-Score, and accuracy, by
leveraging the `classification_report` from the scikit-learn's metrics module. For multiclass models, macro and
weighted averages for these scores are also calculated. Additionally, the ROC AUC scores are calculated and
included in the report using the script's unique `multiclass_roc_auc_score` function. The outcome of the test
(report format) differs based on whether the model is binary or multiclass.

**Signs of High Risk**:
- Low values for precision, recall, F1-Score, accuracy, and ROC AUC, indicating poor performance.
- Imbalance in precision and recall scores. Precision highlights correct positive class predictions, while recall
indicates the accurate identification of actual positive cases. Imbalance may indicate flawed model performance.
- A low ROC AUC score, especially scores close to 0.5 or lower, strongly suggests a failing model.

**Strengths**:
- The script is versatile, capable of assessing both binary and multiclass models.
- It uses a variety of commonly employed performance metrics, offering a comprehensive view of a model's
performance.
- The use of ROC-AUC as a metric aids in determining the most optimal threshold for classification, especially
beneficial when evaluation datasets are unbalanced.

**Limitations**:
- The test assumes correctly identified labels for binary classification models and raises an exception if the
positive class is not labeled as "1". However, this setup may not align with all practical applications.
- This script is specifically designed for classification models and is not suited to evaluate regression models.
- The metrics computed may provide limited insights in cases where the test dataset does not adequately represent
the data the model will encounter in real-world scenarios.