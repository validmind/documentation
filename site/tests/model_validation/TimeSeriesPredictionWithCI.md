# TimeSeriesPredictionWithCI

Plot actual vs predicted values for a time series with confidence intervals and compute breaches.

**Purpose**: The purpose of this function is to visualize the actual versus predicted values for time series data, including confidence intervals, and to compute and report the number of breaches beyond these intervals.

**Test Mechanism**: The function calculates the standard deviation of prediction errors, determines the confidence intervals, and counts the number of actual values that fall outside these intervals (breaches). It then generates a plot with the actual values, predicted values, and confidence intervals, and returns a DataFrame summarizing the breach information.

**Signs of High Risk**:
- A high number of breaches indicates that the model's predictions are not reliable within the specified confidence level.
- Significant deviations between actual and predicted values may highlight model inadequacies or issues with data quality.

**Strengths**:
- Provides a visual representation of prediction accuracy and the uncertainty around predictions.
- Includes a statistical measure of prediction reliability through confidence intervals.
- Computes and reports breaches, offering a quantitative assessment of prediction performance.

**Limitations**:
- Assumes that the dataset is provided as a DataFrameDataset object with a datetime index.
- Requires that `dataset.y_pred(model)` returns the predicted values for the model.
- The calculation of confidence intervals assumes normally distributed errors, which may not hold for all datasets.