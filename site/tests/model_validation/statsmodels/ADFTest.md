# ADFTest

Assesses the stationarity of time series data using the Augmented Dickey-Fuller (ADF) test.

**Purpose**: The Augmented Dickey-Fuller (ADF) metric test is designed to evaluate the presence of a unit root in a
time series. This essentially translates to assessing the stationarity of a time series dataset. This is vital in
time series analysis, regression tasks, and forecasting, as these often need the data to be stationary.

**Test Mechanism**: This test application utilizes the "adfuller" function from Python's “statsmodels” library. It
applies this function to each column of the training dataset, subsequently calculating the ADF statistic, p-value,
the number of lags used, and the number of observations in the sample for each column. If a column's p-value is
lower than the predetermined threshold (usually 0.05), the series is considered stationary, and the test is deemed
passed for that column.

**Signs of High Risk**:
- A p-value that surpasses the threshold value indicates a high risk or potential model performance issue.
- A high p-value suggests that the null hypothesis (of a unit root being present) cannot be rejected. This in turn
suggests that the series is non-stationary which could potentially yield unreliable and falsified results for the
model's performance and forecast.

**Strengths**:
- Archetypal Test for Stationarity: The ADF test is a comprehensive approach towards testing the stationarity of
time series data. Such testing is vital for many machine learning and statistical models.
- Detailed Output: The function generates detailed output, including the number of lags used and the number of
observations, which adds to understanding a series’ behaviour.

**Limitations**:
- Dependence on Threshold: The result of this test freights heavily on the threshold chosen. Hence, an imprudent
threshold value might lead to false acceptance or rejection of the null hypothesis.
- Not Effective for Trending Data: The test suffers when it operates under the assumption that the data does not
encapsulate any deterministic trend. In the presence of such a trend, it might falsely identify a series as
non-stationary.
- Potential for False Positives: The ADF test especially in the case of larger datasets, tends to reject the null
hypothesis, escalating the chances of false positives.