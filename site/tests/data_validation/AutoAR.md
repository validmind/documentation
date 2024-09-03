# AutoAR

Automatically identifies the optimal Autoregressive (AR) order for a time series using BIC and AIC criteria.

### Purpose

The AutoAR test is intended to automatically identify the Autoregressive (AR) order of a time series by utilizing
the Bayesian Information Criterion (BIC) and Akaike Information Criterion (AIC). AR order is crucial in forecasting
tasks as it dictates the quantity of prior terms in the sequence to use for predicting the current term. The
objective is to select the most fitting AR model that encapsulates the trend and seasonality in the time series
data.

### Test Mechanism

The test mechanism operates by iterating through a possible range of AR orders up to a defined maximum. An AR model
is fitted for each order, and the corresponding BIC and AIC are computed. BIC and AIC statistical measures are
designed to penalize models for complexity, preferring simpler models that fit the data proficiently. To verify the
stationarity of the time series, the Augmented Dickey-Fuller test is executed. The AR order, BIC, and AIC findings
are compiled into a dataframe for effortless comparison. Then, the AR order with the smallest BIC is established as
the desirable order for each variable.

### Signs of High Risk

- An augmented Dickey Fuller test p-value > 0.05, indicating the time series isn't stationary, may lead to
inaccurate results.
- Problems with the model fitting procedure, such as computational or convergence issues.
- Continuous selection of the maximum specified AR order may suggest an insufficient set limit.

### Strengths

- The test independently pinpoints the optimal AR order, thereby reducing potential human bias.
- It strikes a balance between model simplicity and goodness-of-fit to avoid overfitting.
- Has the capability to account for stationarity in a time series, an essential aspect for dependable AR modeling.
- The results are aggregated into a comprehensive table, enabling an easy interpretation.

### Limitations

- The tests need a stationary time series input.
- They presume a linear relationship between the series and its lags.
- The search for the best model is constrained by the maximum AR order supplied in the parameters. Therefore, a low
max_ar_order could result in subpar outcomes.
- AIC and BIC may not always agree on the selection of the best model. This potentially requires the user to juggle
interpretational choices.