# LJungBox

Assesses autocorrelations in dataset features by performing a Ljung-Box test on each feature.

### Purpose

The Ljung-Box test is a type of statistical test utilized to ascertain whether there are autocorrelations within a
given dataset that differ significantly from zero. In the context of a machine learning model, this test is
primarily used to evaluate data utilized in regression tasks, especially those involving time series and
forecasting.

### Test Mechanism

The test operates by iterating over each feature within the training dataset and applying the `acorr_ljungbox`
function from the `statsmodels.stats.diagnostic` library. This function calculates the Ljung-Box statistic and
p-value for each feature. These results are then stored in a dictionary where the keys are the feature names and
the values are dictionaries containing the statistic and p-value respectively. Generally, a lower p-value indicates
a higher likelihood of significant autocorrelations within the feature.

### Signs of High Risk

- High Ljung-Box statistic values or low p-values.
- Presence of significant autocorrelations in the respective features.
- Potential for negative impact on model performance or bias if autocorrelations are not properly handled.

### Strengths

- Powerful tool for detecting autocorrelations within datasets, especially in time series data.
- Provides quantitative measures (statistic and p-value) for precise evaluation.
- Helps avoid issues related to autoregressive residuals and other challenges in regression models.

### Limitations

- Cannot detect all types of non-linearity or complex interrelationships among variables.
- Testing individual features may not fully encapsulate the dynamics of the data if features interact with each
other.
- Designed more for traditional statistical models and may not be fully compatible with certain types of complex
machine learning models.