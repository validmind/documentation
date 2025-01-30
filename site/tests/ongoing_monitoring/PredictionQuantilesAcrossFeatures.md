# PredictionQuantilesAcrossFeatures

Assesses differences in model prediction distributions across individual features between reference
and monitoring datasets through quantile analysis.

### Purpose

This test aims to visualize how prediction distributions vary across feature values by showing
quantile information between reference and monitoring datasets. It helps identify significant
shifts in prediction patterns and potential areas of model instability.

### Test Mechanism

The test generates box plots for each feature, comparing prediction probability distributions
between the reference and monitoring datasets. Each plot consists of two subplots showing the
quantile distribution of predictions: one for reference data and one for monitoring data.

### Signs of High Risk

- Significant differences in prediction distributions between reference and monitoring data
- Unexpected shifts in prediction quantiles across feature values
- Large changes in prediction variability between datasets

### Strengths

- Provides clear visualization of prediction distribution changes
- Shows outliers and variability in predictions across features
- Enables quick identification of problematic feature ranges

### Limitations

- May not capture complex relationships between features and predictions
- Quantile analysis may smooth over important individual predictions
- Requires careful interpretation of distribution changes