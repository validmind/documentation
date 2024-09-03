# AutoMA

Automatically selects the optimal Moving Average (MA) order for each variable in a time series dataset based on
minimal BIC and AIC values.

### Purpose

The `AutoMA` metric serves an essential role of automated decision-making for selecting the optimal Moving Average
(MA) order for every variable in a given time series dataset. The selection is dependent on the minimalization of
BIC (Bayesian Information Criterion) and AIC (Akaike Information Criterion); these are established statistical
tools used for model selection. Furthermore, prior to the commencement of the model fitting process, the algorithm
conducts a stationarity test (Augmented Dickey-Fuller test) on each series.

### Test Mechanism

Starting off, the `AutoMA` algorithm checks whether the `max_ma_order` parameter has been provided. It consequently
loops through all variables in the dataset, carrying out the Dickey-Fuller test for stationarity. For each
stationary variable, it fits an ARIMA model for orders running from 0 to `max_ma_order`. The result is a list
showcasing the BIC and AIC values of the ARIMA models based on different orders. The MA order, which yields the
smallest BIC, is chosen as the 'best MA order' for every single variable. The final results include a table
summarizing the auto MA analysis and another table listing the best MA order for each variable.

### Signs of High Risk

- When a series is non-stationary (p-value>0.05 in the Dickey-Fuller test), the produced result could be inaccurate.
- Any error that arises in the process of fitting the ARIMA models, especially with a higher MA order, can
potentially indicate risks and might need further investigation.

### Strengths

- The metric facilitates automation in the process of selecting the MA order for time series forecasting. This
significantly saves time and reduces efforts conventionally necessary for manual hyperparameter tuning.
- The use of both BIC and AIC enhances the likelihood of selecting the most suitable model.
- The metric ascertains the stationarity of the series prior to model fitting, thus ensuring that the underlying
assumptions of the MA model are fulfilled.

### Limitations

- If the time series fails to be stationary, the metric may yield inaccurate results. Consequently, it necessitates
pre-processing steps to stabilize the series before fitting the ARIMA model.
- The metric adopts a rudimentary model selection process based on BIC and doesn't consider other potential model
selection strategies. Depending on the specific dataset, other strategies could be more appropriate.
- The 'max_ma_order' parameter must be manually input which doesn't always guarantee optimal performance,
especially when configured too low.
- The computation time increases with the rise in `max_ma_order`, hence, the metric may become computationally
costly for larger values.