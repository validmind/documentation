# ClassificationAccuracyDrift

Compares classification accuracy metrics between reference and monitoring datasets.

### Purpose

The Classification Accuracy Drift test is designed to evaluate changes in the model's predictive accuracy
over time. By comparing key accuracy metrics between reference and monitoring datasets, this test helps
identify whether the model maintains its performance levels in production. This is crucial for
understanding if the model's predictions remain reliable and whether its overall effectiveness has
degraded significantly.

### Test Mechanism

This test proceeds by calculating comprehensive accuracy metrics for both reference and monitoring
datasets. It computes overall accuracy, per-label precision, recall, and F1 scores, as well as
macro-averaged metrics. The test quantifies drift as percentage changes in these metrics between
datasets, providing both granular and aggregate views of accuracy changes. Special attention is paid
to per-label performance to identify class-specific degradation.

### Signs of High Risk

- Large drifts in accuracy metrics exceeding the threshold
- Inconsistent changes across different labels
- Significant drops in macro-averaged metrics
- Systematic degradation in specific class performance
- Unexpected improvements suggesting data quality issues
- Divergent trends between precision and recall

### Strengths

- Provides comprehensive accuracy assessment
- Identifies class-specific performance changes
- Enables early detection of model degradation
- Includes both micro and macro perspectives
- Supports multi-class classification evaluation
- Maintains interpretable drift thresholds

### Limitations

- May be sensitive to class distribution changes
- Does not account for prediction confidence
- Cannot identify root causes of accuracy drift
- Limited to accuracy-based metrics only
- Requires sufficient samples per class
- May not capture subtle performance changes