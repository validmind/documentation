# RegressionModelSummary

Evaluates regression model performance using metrics including R-Squared, Adjusted R-Squared, MSE, and RMSE.

### Purpose

The Regression Model Summary test evaluates the performance of regression models by measuring their predictive
ability regarding dependent variables given changes in the independent variables. It uses conventional regression
metrics such as R-Squared, Adjusted R-Squared, Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) to
assess the model's accuracy and fit.

### Test Mechanism

This test employs the 'train_ds' attribute of the model to gather and analyze the training data. Initially, it
fetches the independent variables and uses the model to make predictions on these given features. Subsequently, it
calculates several standard regression performance metrics including R-Squared, Adjusted R-Squared, Mean Squared
Error (MSE), and Root Mean Squared Error (RMSE), which quantify the approximation of the predicted responses to the
actual responses.

### Signs of High Risk

- Low R-Squared and Adjusted R-Squared values.
- High MSE and RMSE values.

### Strengths

- Offers an extensive evaluation of regression models by combining four key measures of model accuracy and fit.
- Provides a comprehensive view of the model's performance.
- Both the R-Squared and Adjusted R-Squared measures are readily interpretable.

### Limitations

- Applicable exclusively to regression models.
- RMSE and MSE might be sensitive to outliers.
- A high R-Squared or Adjusted R-Squared may not necessarily indicate a good model, especially in cases of
overfitting.