# RegressionModelsPerformance

Evaluates and compares regression models' performance using R-squared, Adjusted R-squared, and MSE metrics.

**Purpose**: This metric is used to evaluate and compare the performance of various regression models. Through the
use of key statistical measures such as R-squared, Adjusted R-squared, and Mean Squared Error (MSE), the
performance of different models in predicting dependent variables can be assessed both on the data used for
training (in-sample) and new, unseen data (out-of-sample).

**Test Mechanism**: The test evaluates a list of provided regression models. For each model, it calculates their
in-sample and out-of-sample performance by deriving the model predictions for the training and testing datasets
respectively, and then comparing these predictions to the actual values. In doing so, it calculates R-squared,
Adjusted R-squared, and MSE for each model, stores the results, and returns them for comparison.

**Signs of High Risk**:
- High Mean Squared Error (MSE) values.
- Strikingly low values of R-squared and Adjusted R-squared.
- A significant drop in performance when transitioning from in-sample to out-of-sample evaluations, signaling a
potential overfitting issue.

**Strengths**:
- The test permits comparisons of multiple models simultaneously, providing an objective base for identifying the
top-performing model.
- It delivers both in-sample and out-of-sample evaluations, presenting performance data on unseen data.
- The utilization of R-squared and Adjusted R-squared in conjunction with MSE allows for a detailed view of the
model's explainability and error rate.

**Limitations**:
- This test is built around the assumption that the residuals of the regression model are normally distributed,
which is a fundamental requirement for Ordinary Least Squares (OLS) regression; thus, it could be not suitable for
models where this assumption is broken.
- The test does not consider cases where higher R-squared or lower MSE values do not necessarily correlate with
better predictive performance, particularly in instances of excessively complex models.