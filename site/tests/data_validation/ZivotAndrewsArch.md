# ZivotAndrewsArch

Evaluates the order of integration and stationarity of time series data using the Zivot-Andrews unit root test.

### Purpose

The Zivot-Andrews Arch metric is used to evaluate the order of integration for time series data in a machine
learning model. It's designed to test for stationarity, a crucial aspect of time series analysis, where data points
are independent of time. Stationarity means that the statistical properties such as mean, variance, and
autocorrelation are constant over time.

### Test Mechanism

The Zivot-Andrews unit root test is performed on each feature in the dataset using the `ZivotAndrews` function from
the `arch.unitroot` module. This function returns several metrics for each feature, including the statistical
value, p-value (probability value), the number of lags used, and the number of observations. The p-value is used to
decide on the null hypothesis (the time series has a unit root and is non-stationary) based on a chosen level of
significance.

### Signs of High Risk

- A high p-value suggests high risk, indicating insufficient evidence to reject the null hypothesis, implying that
the time series has a unit root and is non-stationary.
- Non-stationary time series data can lead to misleading statistics and unreliable machine learning models.

### Strengths

- Dynamically tests for stationarity against structural breaks in time series data, offering robust evaluation of
stationarity in features.
- Especially beneficial with financial, economic, or other time-series data where data observations lack a
consistent pattern and structural breaks may occur.

### Limitations

- Assumes data is derived from a single-equation, autoregressive model, making it less appropriate for multivariate
time series data or data not aligning with this model.
- May not account for unexpected shocks or changes in the series trend, both of which can significantly impact data
stationarity.