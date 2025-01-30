# ConfusionMatrixDrift

Compares confusion matrix metrics between reference and monitoring datasets.

### Purpose

The Confusion Matrix Drift test is designed to evaluate changes in the model's error patterns
over time. By comparing confusion matrix elements between reference and monitoring datasets, this
test helps identify whether the model maintains consistent prediction behavior in production. This
is crucial for understanding if the model's error patterns have shifted and whether specific types
of misclassifications have become more prevalent.

### Test Mechanism

This test proceeds by generating confusion matrices for both reference and monitoring datasets.
For binary classification, it tracks True Positives, True Negatives, False Positives, and False
Negatives as percentages of total predictions. For multiclass problems, it analyzes per-class
metrics including true positives and error rates. The test quantifies drift as percentage changes
in these metrics between datasets, providing detailed insight into shifting prediction patterns.

### Signs of High Risk

- Large drifts in confusion matrix elements exceeding threshold
- Systematic changes in false positive or false negative rates
- Inconsistent changes across different classes
- Significant shifts in error patterns for specific classes
- Unexpected improvements in certain metrics
- Divergent trends between different types of errors

### Strengths

- Provides detailed analysis of prediction behavior
- Identifies specific types of prediction changes
- Enables early detection of systematic errors
- Includes comprehensive error pattern analysis
- Supports both binary and multiclass problems
- Maintains interpretable percentage-based metrics

### Limitations

- May be sensitive to class distribution changes
- Cannot identify root causes of prediction drift
- Requires sufficient samples for reliable comparison
- Limited to hard predictions (not probabilities)
- May not capture subtle changes in decision boundaries
- Complex interpretation for multiclass problems