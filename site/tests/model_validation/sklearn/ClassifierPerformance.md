# ClassifierPerformance

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