# ModelPredictionResiduals

Assesses normality and behavior of residuals in regression models through visualization and statistical tests.

### Purpose

The Model Prediction Residuals test aims to visualize the residuals of model predictions and assess their normality
using the Kolmogorov-Smirnov (KS) test. It helps to identify potential issues related to model assumptions and
effectiveness.

### Test Mechanism

The function calculates residuals and generates
two figures: one for the time series of residuals and one for the histogram of residuals.
It also calculates the KS test for normality and summarizes the results in a table.

### Signs of High Risk

- Residuals are not normally distributed, indicating potential issues with model assumptions.
- High skewness or kurtosis in the residuals, which may suggest model misspecification.

### Strengths

- Provides clear visualizations of residuals over time and their distribution.
- Includes statistical tests to assess the normality of residuals.
- Helps in identifying potential model misspecifications and assumption violations.

### Limitations

- Assumes that the dataset is provided as a DataFrameDataset object with a .df attribute to access the pandas
DataFrame.
- Only generates plots for datasets with a datetime index, resulting in errors for other types of indices.