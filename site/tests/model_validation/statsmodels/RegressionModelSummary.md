# RegressionModelSummary

Evaluates regression model performance using metrics including R-Squared, Adjusted R-Squared, MSE, and RMSE.

### Purpose

The Regression Model Summary test evaluates the performance of regression models by measuring their predictive
ability regarding dependent variables given changes in the independent variables. It uses conventional regression
metrics such as R-Squared, Adjusted R-Squared, Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) to
assess the model's accuracy and fit.

### Test Mechanism

This test uses the sklearn library to calculate the R-Squared, Adjusted R-Squared, MSE, and RMSE. It outputs a
table with the results of these metrics along with the feature columns used by the model.

### Signs of High Risk

- Low R-Squared and Adjusted R-Squared values.
- High MSE and RMSE values.

### Strengths

- Offers an extensive evaluation of regression models by combining four key measures of model accuracy and fit.
- Provides a comprehensive view of the model's performance.
- Both the R-Squared and Adjusted R-Squared measures are readily interpretable.

### Limitations

- RMSE and MSE might be sensitive to outliers.
- A high R-Squared or Adjusted R-Squared may not necessarily indicate a good model, especially in cases of
overfitting.