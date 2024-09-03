# DurbinWatsonTest

Assesses autocorrelation in time series data features using the Durbin-Watson statistic.

### Purpose

The Durbin-Watson Test metric detects autocorrelation in time series data (where a set of data values influences
their predecessors). Autocorrelation is a crucial factor for regression tasks as these often assume the
independence of residuals. A model with significant autocorrelation may give unreliable predictions.

### Test Mechanism

Utilizing the `durbin_watson` function in the `statsmodels` Python library, the Durbin-Watson (DW) Test metric
generates a statistical value for each feature of the training dataset. The function is looped over all columns of
the dataset, calculating and caching the DW value for each column for further analysis. A DW metric value nearing 2
indicates no autocorrelation. Conversely, values approaching 0 suggest positive autocorrelation, and those leaning
towards 4 imply negative autocorrelation.

### Signs of High Risk

- If a feature's DW value significantly deviates from 2, it could signal a high risk due to potential
autocorrelation issues in the dataset.
- A value closer to 0 could imply positive autocorrelation, while a value nearer to 4 could point to negative
autocorrelation, both leading to potentially unreliable prediction models.

### Strengths

- The metric specializes in identifying autocorrelation in prediction model residuals.
- Autocorrelation detection assists in diagnosing violation of various modeling technique assumptions, particularly
in regression analysis and time-series data modeling.

### Limitations

- The Durbin-Watson Test mainly detects linear autocorrelation and could overlook other types of relationships.
- The metric is highly sensitive to data points order. Shuffling the order could lead to notably different results.
- The test only checks for first-order autocorrelation (between a variable and its immediate predecessor) and fails
to detect higher-order autocorrelation.