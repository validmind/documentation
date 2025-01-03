# RegressionPerformance

Evaluates the performance of a regression model using five different metrics: MAE, MSE, RMSE, MAPE, and MBD.

### Purpose

The Regression Models Performance Comparison metric is used to measure the performance of regression models. It
calculates multiple evaluation metrics, including Mean Absolute Error (MAE), Mean Squared Error (MSE),
Root Mean Squared Error (RMSE), Mean Absolute Percentage Error (MAPE), and Mean Bias Deviation (MBD), thereby
enabling a comprehensive view of model performance.

### Test Mechanism

The test uses the sklearn library to calculate the MAE, MSE, RMSE, MAPE, and MBD. These calculations encapsulate both
the direction and the magnitude of error in predictions, thereby providing a multi-faceted view of model accuracy.

### Signs of High Risk

- High values of MAE, MSE, RMSE, and MAPE, which indicate a high error rate and imply a larger departure of the
model's predictions from the true values.
- A large value of MBD, which shows a consistent bias in the model’s predictions.

### Strengths

- The metric evaluates models on five different metrics offering a comprehensive analysis of model performance.
- It is designed to handle regression tasks and can be seamlessly integrated with libraries like sklearn.

### Limitations

- The metric only evaluates regression models and does not evaluate classification models.
- The test assumes that the models have been trained and tested appropriately prior to evaluation. It does not
handle pre-processing, feature selection, or other stages in the model lifecycle.