# GINITable

Evaluates classification model performance using AUC, GINI, and KS metrics for training and test datasets.

### Purpose

The 'GINITable' metric is designed to evaluate the performance of a classification model by emphasizing its
discriminatory power. Specifically, it calculates and presents three important metrics - the Area under the ROC
Curve (AUC), the GINI coefficient, and the Kolmogorov-Smirnov (KS) statistic - for both training and test datasets.

### Test Mechanism

Using a dictionary for storing performance metrics for both the training and test datasets, the 'GINITable' metric
calculates each of these metrics sequentially. The Area under the ROC Curve (AUC) is calculated via the
`roc_auc_score` function from the Scikit-Learn library. The GINI coefficient, a measure of statistical dispersion,
is then computed by doubling the AUC and subtracting 1. Finally, the Kolmogorov-Smirnov (KS) statistic is
calculated via the `roc_curve` function from Scikit-Learn, with the False Positive Rate (FPR) subtracted from the
True Positive Rate (TPR) and the maximum value taken from the resulting data. These metrics are then stored in a
pandas DataFrame for convenient visualization.

### Signs of High Risk

- Low values for performance metrics may suggest a reduction in model performance, particularly a low AUC which
indicates poor classification performance, or a low GINI coefficient, which could suggest a decreased ability to
discriminate different classes.
- A high KS value may be an indicator of potential overfitting, as this generally signifies a substantial
divergence between positive and negative distributions.
- Significant discrepancies between the performance on the training dataset and the test dataset may present
another signal of high risk.

### Strengths

- Offers three key performance metrics (AUC, GINI, and KS) in one test, providing a more comprehensive evaluation
of the model.
- Provides a direct comparison between the model's performance on training and testing datasets, which aids in
identifying potential underfitting or overfitting.
- The applied metrics are class-distribution invariant, thereby remaining effective for evaluating model
performance even when dealing with imbalanced datasets.
- Presents the metrics in a user-friendly table format for easy comprehension and analysis.

### Limitations

- The GINI coefficient and KS statistic are both dependent on the AUC value. Therefore, any errors in the
calculation of the latter will adversely impact the former metrics too.
- Mainly suited for binary classification models and may require modifications for effective application in
multi-class scenarios.
- The metrics used are threshold-dependent and may exhibit high variability based on the chosen cut-off points.
- The test does not incorporate a method to efficiently handle missing or inefficiently processed data, which could
lead to inaccuracies in the metrics if the data is not appropriately preprocessed.