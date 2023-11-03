# RegressionModelSummary

Evaluates regression model performance using metrics including R-Squared, Adjusted R-Squared, MSE, and RMSE.

**Purpose**: This metric test evaluates the performance of regression models by measuring their predictive ability
with regards to dependent variables given changes in the independent variables. Its measurement tools include
conventional regression metrics such as R-Squared, Adjusted R-Squared, Mean Squared Error (MSE), and Root Mean
Squared Error (RMSE).

**Test Mechanism**: This test employs the 'train_ds' attribute of the model to gather and analyze the training
data. Initially, it fetches the independent variables and uses the model to make predictions on these given
features. Subsequently, it calculates several standard regression performance metrics including R-Square, Adjusted
R-Squared, Mean Squared Error (MSE), and Root Mean Squared Error (RMSE), which quantify the approximation of the
predicted responses to the actual responses.

**Signs of High Risk**:
- Low R-Squared and Adjusted R-Squared values. A poor fit between the model predictions and the true responses is
indicated by low values of these metrics, suggesting the model explains a small fraction of the variance in the
target variable.
- High MSE and RMSE values represent a high prediction error and point to poor model performance.

**Strengths**:
- Offers an extensive evaluation of regression models by combining four key measures of model accuracy and fit.
- Provides a comprehensive view of the model's performance.
- Both the R-Squared and Adjusted R-Squared measures are readily interpretable. They represent the proportion of
total variation in the dependent variable that can be explained by the independent variables.

**Limitations**:
- Applicable exclusively to regression models. It is not suited for evaluating binary classification models or time
series models, thus limiting its scope.
- Although RMSE and MSE are sound measures of prediction error, they might be sensitive to outliers, potentially
leading to an overestimation of the model's prediction error.
- A high R-squared or adjusted R-squared may not necessarily indicate a good model, especially in cases where the
model is possibly overfitting the data.