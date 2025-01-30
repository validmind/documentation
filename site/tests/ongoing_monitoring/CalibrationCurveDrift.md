# CalibrationCurveDrift

Evaluates changes in probability calibration between reference and monitoring datasets.

### Purpose

The Calibration Curve Drift test is designed to assess changes in the model's probability calibration
over time. By comparing calibration curves between reference and monitoring datasets, this test helps
identify whether the model's probability estimates remain reliable in production. This is crucial for
understanding if the model's risk predictions maintain their intended interpretation and whether
recalibration might be necessary.

### Test Mechanism

This test proceeds by generating calibration curves for both reference and monitoring datasets. For each
dataset, it bins the predicted probabilities and calculates the actual fraction of positives within each
bin. It then compares these values between datasets to identify significant shifts in calibration.
The test quantifies drift as percentage changes in both mean predicted probabilities and actual fractions
of positives per bin, providing both visual and numerical assessments of calibration stability.

### Signs of High Risk

- Large differences between reference and monitoring calibration curves
- Systematic over-estimation or under-estimation in monitoring dataset
- Significant drift percentages exceeding the threshold in multiple bins
- Changes in calibration concentrated in specific probability ranges
- Inconsistent drift patterns across the probability spectrum
- Empty or sparse bins indicating insufficient data for reliable comparison

### Strengths

- Provides visual and quantitative assessment of calibration changes
- Identifies specific probability ranges where calibration has shifted
- Enables early detection of systematic prediction biases
- Includes detailed bin-by-bin comparison of calibration metrics
- Handles edge cases with insufficient data in certain bins
- Supports both binary and probabilistic interpretation of results

### Limitations

- Requires sufficient data in each probability bin for reliable comparison
- Sensitive to choice of number of bins and binning strategy
- May not capture complex changes in probability distributions
- Cannot directly suggest recalibration parameters
- Limited to assessing probability calibration aspects
- Results may be affected by class imbalance changes