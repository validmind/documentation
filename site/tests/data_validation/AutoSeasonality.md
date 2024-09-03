# AutoSeasonality

Automatically identifies and quantifies optimal seasonality in time series data to improve forecasting model
performance.

### Purpose

The AutoSeasonality test aims to automatically detect and identify the best seasonal order or period for each
variable in a time series dataset. This detection helps to quantify periodic patterns and seasonality that reoccur
at fixed intervals in the data. Understanding the seasonality component can drastically improve prediction
accuracy, which is especially significant for forecasting-based models.

### Test Mechanism

This test uses the seasonal decomposition method from the Statsmodels Python library. The function takes the
additive' model type for each variable and applies it within the prescribed range of 'min_period' and
max_period'. It decomposes the seasonality for each period in the range and calculates the mean residual error for
each period. The seasonal period that results in the minimum residuals is marked as the 'Best Period'. The test
results include the 'Best Period', the calculated residual errors, and a determination of 'Seasonality' or 'No
Seasonality'.

### Signs of High Risk

- If the optimal seasonal period (or 'Best Period') is consistently at the maximum or minimum limit of the offered
range for a majority of variables, it may suggest that the range set does not adequately capture the true seasonal
pattern in the series.
- A high average 'Residual Error' for the selected 'Best Period' could indicate issues with the model's performance.

### Strengths

- The metric offers an automatic approach to identifying and quantifying the optimal seasonality, providing a
robust method for analyzing time series datasets.
- It is applicable to multiple variables in a dataset, providing a comprehensive evaluation of each variable's
seasonality.
- The use of concrete and measurable statistical methods improves the objectivity and reproducibility of the model.

### Limitations

- This AutoSeasonality metric may not be suitable if the time series data exhibits random walk behavior or lacks
clear seasonality, as the seasonal decomposition model may not be appropriate.
- The defined range for the seasonal period (min_period and max_period) can influence the outcomes. If the actual
seasonality period lies outside this range, this method will not be able to identify the true seasonal order.
- This metric may not be able to fully interpret complex patterns that go beyond the simple additive model for
seasonal decomposition.
- The tool may incorrectly infer seasonality if random fluctuations in the data match the predefined seasonal
period range.