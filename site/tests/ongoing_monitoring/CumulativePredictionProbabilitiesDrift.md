# CumulativePredictionProbabilitiesDrift

Compares cumulative prediction probability distributions between reference and monitoring datasets.

### Purpose

The Cumulative Prediction Probabilities Drift test is designed to evaluate changes in the model's
probability predictions over time. By comparing cumulative distribution functions of predicted
probabilities between reference and monitoring datasets, this test helps identify whether the
model's probability assignments remain stable in production. This is crucial for understanding if
the model's risk assessment behavior has shifted and whether its probability calibration remains
consistent.

### Test Mechanism

This test proceeds by generating cumulative distribution functions (CDFs) of predicted probabilities
for both reference and monitoring datasets. For each class, it plots the cumulative proportion of
predictions against probability values, enabling direct comparison of probability distributions.
The test visualizes both the CDFs and their differences, providing insight into how probability
assignments have shifted across the entire probability range.

### Signs of High Risk

- Large gaps between reference and monitoring CDFs
- Systematic shifts in probability assignments
- Concentration of differences in specific probability ranges
- Changes in the shape of probability distributions
- Unexpected patterns in cumulative differences
- Significant shifts in probability thresholds

### Strengths

- Provides comprehensive view of probability changes
- Identifies specific probability ranges with drift
- Enables visualization of distribution differences
- Supports analysis across multiple classes
- Maintains interpretable probability scale
- Captures subtle changes in probability assignments

### Limitations

- Does not provide single drift metric
- May be complex to interpret for multiple classes
- Cannot suggest probability recalibration
- Requires visual inspection for assessment
- Sensitive to sample size differences
- May not capture class-specific calibration issues