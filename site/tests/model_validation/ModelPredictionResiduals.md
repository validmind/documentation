# ModelPredictionResiduals

Plot the residuals and histograms for each model, and generate a summary table
with the Kolmogorov-Smirnov normality test results.

**Purpose**: The purpose of this function is to visualize the residuals of model predictions and
assess the normality of residuals using the Kolmogorov-Smirnov test.

**Test Mechanism**: The function iterates through each dataset-model pair, calculates residuals, and generates
two figures for each model: one for the time series of residuals and one for the histogram of residuals.
It also calculates the KS test for normality and summarizes the results in a table.

**Signs of High Risk**:
- If the residuals are not normally distributed, it could indicate issues with model assumptions.
- High skewness or kurtosis in the residuals may indicate model misspecification.

**Strengths**:
- Provides a clear visualization of residuals over time and their distribution.
- Includes statistical tests to assess the normality of residuals.

**Limitations**:
- Assumes that the dataset is provided as a DataFrameDataset object with a .df attribute to access
the pandas DataFrame.
- Only generates plots for datasets with a datetime index, and will raise an error for other types of indices.