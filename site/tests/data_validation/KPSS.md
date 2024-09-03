# KPSS

Assesses the stationarity of time-series data in a machine learning model using the KPSS unit root test.

### Purpose

The KPSS (Kwiatkowski-Phillips-Schmidt-Shin) unit root test is utilized to ensure the stationarity of data within a
machine learning model. It specifically works on time-series data to establish the order of integration, which is
essential for accurate forecasting. A fundamental requirement for any time series model is that the series should
be stationary.

### Test Mechanism

This test calculates the KPSS score for each feature in the dataset. The KPSS score includes a statistic, a
p-value, a used lag, and critical values. The core principle behind the KPSS test is to evaluate the hypothesis
that an observable time series is stationary around a deterministic trend. If the computed statistic exceeds the
critical value, the null hypothesis (that the series is stationary) is rejected, indicating that the series is
non-stationary.

### Signs of High Risk

- High KPSS score, particularly if the calculated statistic is higher than the critical value.
- Rejection of the null hypothesis, indicating that the series is recognized as non-stationary, can severely affect
the model's forecasting capability.

### Strengths

- Directly measures the stationarity of a series, fulfilling a key prerequisite for many time-series models.
- The underlying logic of the test is intuitive and simple, making it easy to understand and accessible for both
developers and risk management teams.

### Limitations

- Assumes the absence of a unit root in the series and doesn't differentiate between series that are stationary and
those border-lining stationarity.
- The test may have restricted power against certain alternatives.
- The reliability of the test is contingent on the number of lags selected, which introduces potential bias in the
measurement.