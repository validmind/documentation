# ROCCurveDrift

Compares ROC curves between reference and monitoring datasets.

### Purpose

The ROC Curve Drift test is designed to evaluate changes in the model's discriminative ability
over time. By comparing Receiver Operating Characteristic (ROC) curves between reference and
monitoring datasets, this test helps identify whether the model maintains its ability to
distinguish between classes across different decision thresholds. This is crucial for
understanding if the model's trade-off between sensitivity and specificity remains stable
in production.

### Test Mechanism

This test proceeds by generating ROC curves for both reference and monitoring datasets. For each
dataset, it plots the True Positive Rate against the False Positive Rate across all possible
classification thresholds. The test also computes AUC scores and visualizes the difference
between ROC curves, providing both graphical and numerical assessments of discrimination
stability. Special attention is paid to regions where curves diverge significantly.

### Signs of High Risk

- Large differences between reference and monitoring ROC curves
- Significant drop in AUC score for monitoring dataset
- Systematic differences in specific FPR regions
- Changes in optimal operating points
- Inconsistent performance across different thresholds
- Unexpected crossovers between curves

### Strengths

- Provides comprehensive view of discriminative ability
- Identifies specific threshold ranges with drift
- Enables visualization of performance differences
- Includes AUC comparison for overall assessment
- Supports threshold-independent evaluation
- Maintains interpretable performance metrics

### Limitations

- Limited to binary classification problems
- May be sensitive to class distribution changes
- Cannot suggest optimal threshold adjustments
- Requires visual inspection for detailed analysis
- Complex interpretation of curve differences
- May not capture subtle performance changes