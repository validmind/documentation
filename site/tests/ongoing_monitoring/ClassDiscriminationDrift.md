# ClassDiscriminationDrift

Compares classification discrimination metrics between reference and monitoring datasets.

### Purpose

The Class Discrimination Drift test is designed to evaluate changes in the model's discriminative power
over time. By comparing key discrimination metrics between reference and monitoring datasets, this test
helps identify whether the model maintains its ability to separate classes in production. This is crucial
for understanding if the model's predictive power remains stable and whether its decision boundaries
continue to effectively distinguish between different classes.

### Test Mechanism

This test proceeds by calculating three key discrimination metrics for both reference and monitoring
datasets: ROC AUC (Area Under the Curve), GINI coefficient, and KS (Kolmogorov-Smirnov) statistic.
For binary classification, it computes all three metrics. For multiclass problems, it focuses on
macro-averaged ROC AUC. The test quantifies drift as percentage changes in these metrics between
datasets, providing a comprehensive assessment of discrimination stability.

### Signs of High Risk

- Large drifts in discrimination metrics exceeding the threshold
- Significant drops in ROC AUC indicating reduced ranking ability
- Decreased GINI coefficients showing diminished separation power
- Reduced KS statistics suggesting weaker class distinction
- Inconsistent changes across different metrics
- Systematic degradation in discriminative performance

### Strengths

- Combines multiple complementary discrimination metrics
- Handles both binary and multiclass classification
- Provides clear quantitative drift assessment
- Enables early detection of model degradation
- Includes standardized drift threshold evaluation
- Supports comprehensive performance monitoring

### Limitations

- Does not identify root causes of discrimination drift
- May be sensitive to changes in class distribution
- Cannot suggest optimal decision threshold adjustments
- Limited to discrimination aspects of performance
- Requires sufficient data for reliable metric calculation
- May not capture subtle changes in decision boundaries