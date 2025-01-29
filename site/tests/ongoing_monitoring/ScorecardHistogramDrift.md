# ScorecardHistogramDrift

Compares score distributions between reference and monitoring datasets for each class.

### Purpose

The Scorecard Histogram Drift test is designed to evaluate changes in the model's scoring
patterns over time. By comparing score distributions between reference and monitoring datasets
for each class, this test helps identify whether the model's scoring behavior remains stable
in production. This is crucial for understanding if the model's risk assessment maintains
consistent patterns and whether specific score ranges have experienced significant shifts
in their distribution.

### Test Mechanism

This test proceeds by generating histograms of scores for each class in both reference and
monitoring datasets. It analyzes distribution characteristics through multiple statistical
moments: mean, variance, skewness, and kurtosis. The test quantifies drift as percentage
changes in these moments between datasets, providing both visual and numerical assessments
of distribution stability. Special attention is paid to class-specific distribution changes.

### Signs of High Risk

- Significant shifts in score distribution shapes
- Large drifts in distribution moments exceeding threshold
- Changes in the relative positioning of class distributions
- Appearance of new modes or peaks in monitoring data
- Unexpected changes in score spread or concentration
- Systematic shifts in class-specific scoring patterns

### Strengths

- Provides class-specific distribution analysis
- Identifies detailed changes in scoring patterns
- Enables visual comparison of distributions
- Includes comprehensive moment analysis
- Supports multiple class evaluation
- Maintains interpretable score scale

### Limitations

- Sensitive to binning choices in visualization
- Requires sufficient samples per class
- Cannot suggest score adjustments
- May not capture subtle distribution changes
- Complex interpretation with multiple classes
- Limited to univariate score analysis