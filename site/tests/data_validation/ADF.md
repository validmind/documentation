# ADF

Assesses the stationarity of a time series dataset using the Augmented Dickey-Fuller (ADF) test.

### Purpose

The Augmented Dickey-Fuller (ADF) test metric is used to determine the order of integration, i.e., the stationarity
of a given time series dataset. The stationary property of data is pivotal in many machine learning models as it
impacts the reliability and effectiveness of predictions and forecasts.

### Test Mechanism

The ADF test is executed using the `adfuller` function from the `statsmodels` library on each feature of the
dataset. Multiple outputs are generated for each run, including the ADF test statistic and p-value, count of lags
used, the number of observations considered in the test, critical values at various confidence levels, and the
information criterion. These results are stored for each feature for subsequent analysis.

### Signs of High Risk

- An inflated ADF statistic and high p-value (generally above 0.05) indicate a high risk to the model's performance
due to the presence of a unit root indicating non-stationarity.
- Non-stationarity might result in untrustworthy or insufficient forecasts.

### Strengths

- The ADF test is robust to sophisticated correlations within the data, making it suitable for settings where data
displays complex stochastic behavior.
- It provides explicit outputs like test statistics, critical values, and information criterion, enhancing
understanding and transparency in the model validation process.

### Limitations

- The ADF test might demonstrate low statistical power, making it challenging to differentiate between a unit root
and near-unit-root processes, potentially causing false negatives.
- It assumes the data follows an autoregressive process, which might not always be the case.
- The test struggles with time series data that have structural breaks.