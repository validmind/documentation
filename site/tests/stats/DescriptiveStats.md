# DescriptiveStats

Provides comprehensive descriptive statistics for numerical features in a dataset.

### Purpose

This test generates detailed descriptive statistics for numerical features, including
basic statistics, distribution measures, confidence intervals, and normality tests.
It provides a comprehensive overview of data characteristics essential for
understanding data quality and distribution properties.

### Test Mechanism

The test computes various statistical measures for each numerical column:
- Basic statistics: count, mean, median, std, min, max, quartiles
- Distribution measures: skewness, kurtosis, coefficient of variation
- Confidence intervals for the mean
- Normality tests (Shapiro-Wilk for small samples, Anderson-Darling for larger)
- Missing value analysis

### Signs of High Risk

- High skewness or kurtosis indicating non-normal distributions
- Large coefficients of variation suggesting high data variability
- Significant results in normality tests when normality is expected
- High percentage of missing values
- Extreme outliers based on IQR analysis

### Strengths

- Comprehensive statistical analysis in a single test
- Includes advanced statistical measures beyond basic descriptives
- Provides confidence intervals for uncertainty quantification
- Handles missing values appropriately
- Suitable for both exploratory and confirmatory analysis

### Limitations

- Limited to numerical features only
- Normality tests may not be meaningful for all data types
- Large datasets may make some tests computationally expensive
- Interpretation requires statistical knowledge