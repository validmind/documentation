# TimeSeriesPredictionWithCI

Assesses predictive accuracy and uncertainty in time series models, highlighting breaches beyond confidence
intervals.

### Purpose

The purpose of the Time Series Prediction with Confidence Intervals (CI) test is to visualize the actual versus
predicted values for time series data, including confidence intervals, and to compute and report the number of
breaches beyond these intervals. This helps in evaluating the reliability and accuracy of the model's predictions.

### Test Mechanism

The function performs the following steps:

- Calculates the standard deviation of prediction errors.
- Determines the confidence intervals using a specified confidence level, typically 95%.
- Counts the number of actual values that fall outside the confidence intervals, referred to as breaches.
- Generates a plot visualizing the actual values, predicted values, and confidence intervals.
- Returns a DataFrame summarizing the breach information, including the total breaches, upper breaches, and lower
breaches.

### Signs of High Risk

- A high number of breaches indicates that the model's predictions are not reliable within the specified confidence
level.
- Significant deviations between actual and predicted values may highlight model inadequacies or issues with data
quality.

### Strengths

- Provides a visual representation of prediction accuracy and the uncertainty around predictions.
- Includes a statistical measure of prediction reliability through confidence intervals.
- Computes and reports breaches, offering a quantitative assessment of prediction performance.

### Limitations

- Assumes that the dataset is provided as a DataFrameDataset object with a datetime index.
- Requires that `dataset.y_pred(model)` returns the predicted values for the model.
- The calculation of confidence intervals assumes normally distributed errors, which may not hold for all datasets.