# ACFandPACFPlot

Analyzes time series data using Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) plots to
reveal trends and correlations.

### Purpose

The ACF (Autocorrelation Function) and PACF (Partial Autocorrelation Function) plot test is employed to analyze
time series data in machine learning models. It illuminates the correlation of the data over time by plotting the
correlation of the series with its own lags (ACF), and the correlations after removing effects already accounted
for by earlier lags (PACF). This information can identify trends, such as seasonality, degrees of autocorrelation,
and inform the selection of order parameters for AutoRegressive Integrated Moving Average (ARIMA) models.

### Test Mechanism

The `ACFandPACFPlot` test accepts a dataset with a time-based index. It first confirms the index is of a datetime
type, then handles any NaN values. The test subsequently generates ACF and PACF plots for each column in the
dataset, producing a subplot for each. If the dataset doesn't include key columns, an error is returned.

### Signs of High Risk

- Sudden drops in the correlation at a specific lag might signal a model at high risk.
- Consistent high correlation across multiple lags could also indicate non-stationarity in the data, which may
suggest that a model estimated on this data won't generalize well to future, unknown data.

### Strengths

- ACF and PACF plots offer clear graphical representations of the correlations in time series data.
- These plots are effective at revealing important data characteristics such as seasonality, trends, and
correlation patterns.
- The insights from these plots aid in better model configuration, particularly in the selection of ARIMA model
parameters.

### Limitations

- ACF and PACF plots are exclusively for time series data and hence, can't be applied to all ML models.
- These plots require large, consistent datasets as gaps could lead to misleading results.
- The plots can only represent linear correlations and fail to capture any non-linear relationships within the data.
- The plots might be difficult for non-experts to interpret and should not replace more advanced analyses.