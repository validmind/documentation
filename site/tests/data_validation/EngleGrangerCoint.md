# EngleGrangerCoint

Assesses the degree of co-movement between pairs of time series data using the Engle-Granger cointegration test.

### Purpose

The intent of this Engle-Granger cointegration test is to explore and quantify the degree of co-movement between
pairs of time series variables in a dataset. This is particularly useful in enhancing the accuracy of predictive
regressions whenever the underlying variables are co-integrated, i.e., they move together over time.

### Test Mechanism

The test first drops any non-applicable values from the input dataset and then iterates over each pair of variables
to apply the Engle-Granger cointegration test. The test generates a 'p' value, which is then compared against a
pre-specified threshold (0.05 by default). The pair is labeled as 'Cointegrated' if the 'p' value is less than or
equal to the threshold or 'Not cointegrated' otherwise. A summary table is returned by the metric showing
cointegration results for each variable pair.

### Signs of High Risk

- A significant number of hypothesized cointegrated variables do not pass the test.
- A considerable number of 'p' values are close to the threshold, indicating minor data fluctuations can switch the
decision between 'Cointegrated' and 'Not cointegrated'.

### Strengths

- Provides an effective way to analyze relationships between time series, particularly in contexts where it's
essential to check if variables move together in a statistically significant manner.
- Useful in various domains, especially finance or economics, where predictive models often hinge on understanding
how different variables move together over time.

### Limitations

- Assumes that the time series are integrated of the same order, which isn't always true in multivariate time
series datasets.
- The presence of non-stationary characteristics in the series or structural breaks can result in falsely positive
or negative cointegration results.
- May not perform well for small sample sizes due to lack of statistical power and should be supplemented with
other predictive indicators for a more robust model evaluation.