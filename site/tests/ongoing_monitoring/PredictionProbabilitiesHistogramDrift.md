# PredictionProbabilitiesHistogramDrift

Compares prediction probability distributions between reference and monitoring datasets.

### Purpose

The Prediction Probabilities Histogram Drift test is designed to evaluate changes in the model's
probability predictions over time. By comparing probability distributions between reference and
monitoring datasets using histograms, this test helps identify whether the model's probability
assignments have shifted in production. This is crucial for understanding if the model's risk
assessment behavior remains consistent and whether its probability estimates maintain their
original distribution patterns.

### Test Mechanism

This test proceeds by generating histograms of prediction probabilities for both reference and
monitoring datasets. For each class, it analyzes the distribution shape, central tendency, and
spread of probabilities. The test computes distribution moments (mean, variance, skewness,
kurtosis) and quantifies their drift between datasets. Visual comparison of overlaid histograms
provides immediate insight into distribution changes.

### Signs of High Risk

- Significant shifts in probability distribution shapes
- Large drifts in distribution moments exceeding threshold
- Appearance of new modes or peaks in monitoring data
- Changes in the spread or concentration of probabilities
- Systematic shifts in probability assignments
- Unexpected changes in distribution characteristics

### Strengths

- Provides intuitive visualization of probability changes
- Identifies specific changes in distribution shape
- Enables quantitative assessment of distribution drift
- Supports analysis across multiple classes
- Includes comprehensive moment analysis
- Maintains interpretable probability scale

### Limitations

- May be sensitive to binning choices
- Requires sufficient samples for reliable histograms
- Cannot suggest probability recalibration
- Complex interpretation for multiple classes
- May not capture subtle distribution changes
- Limited to univariate probability analysis