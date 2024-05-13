# tests\model_validation\sklearn\RegressionErrors

**Purpose**: This metric is used to measure the performance of a regression model. It gauges the model's accuracy
by computing several error metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared
Error (RMSE), Mean Absolute Percentage Error (MAPE), and Mean Bias Deviation (MBD) on both the training and testing
dataset.

**Test Mechanism**: The test computes each of the aforementioned metrics. MAE calculates the average of the
absolute difference between the true value and the predicted value. MSE squares the difference before averaging it.
RMSE then takes the square root of the MSE. MAPE evaluates the average of the absolute difference between true and
predicted values divided by the true value, expressed as a percentage. Lastly, MBD is a measure of average bias in
the prediction. The results are compared between the training dataset and the testing dataset.

**Signs of High Risk**: High values for any of the metrics, or particularly different metric outcomes for the
training set versus the test set, are signs of high risk. Specifically, high MAE, MSE, RMSE, or MAPE values could
indicate poor model performance and overfitting. If MBD is significantly different from zero, it could signify that
the model's predictions are systematically biased.

**Strengths**: These metrics collectively provide a comprehensive view of model performance and error distribution.
Individually, MAE provides a linear score that could be more interpretable, while MSE gives more weight to larger
errors. RMSE is useful because it is in the same unit as the target variable. MAPE expresses error as a percentage,
making it a good measure of prediction accuracy. MBD helps to detect systematic bias in predictions.

**Limitations**: Each of these metrics has its own limitations. MAE and MSE are sensitive to outliers. While RMSE
is good for giving high weight to larger errors, it might too heavily penalize these errors. MAPE might be biased
if actual values are near zero, and MBD would not work well if the difference between predictions and actual values
changes with the magnitude of the actual values. Overall, these metrics will not capture all model performance
nuances, and they should be used with contextual understanding of the problem at hand.