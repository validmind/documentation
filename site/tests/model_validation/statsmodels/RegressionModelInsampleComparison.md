# RegressionModelInsampleComparison

Evaluates and compares in-sample performance of multiple regression models using R-Squared, Adjusted R-Squared,
MSE, and RMSE.

**Purpose**: The RegressionModelInsampleComparison test metric is utilized to evaluate and compare the performance
of multiple regression models trained on the same dataset. Key performance indicators for this comparison include
statistics related to the goodness of fit - R-Squared, Adjusted R-Squared, Mean Squared Error (MSE), and Root Mean
Squared Error (RMSE).

**Test Mechanism**: The methodology behind this test is as follows -
- Firstly, a verification that the list of models to be tested is indeed not empty occurs.
- Once confirmed, the In-Sample performance of the models is calculated by a private function,
`_in_sample_performance_ols`, that executes the following steps:
- Iterates through each model in the supplied list.
- For each model, the function extracts the features (`X`) and the target (`y_true`) from the training dataset
and computes the predicted target values (`y_pred`).
- The performance metrics for the model are calculated using formulas for R-Squared, Adjusted R-Squared, MSE, and
RMSE.
- The results, including the computed metrics, variables of the model, and the model's identifier, are stored in
a dictionary that is appended to a list.
- The collected results are finally returned as a pandas dataframe.

**Signs of High Risk**:
- Significantly low values for R-Squared or Adjusted R-Squared.
- Significantly high values for MSE and RMSE.
Please note that what constitutes as "low" or "high" will vary based on the specific context or domain in which the
model is being utilized.

**Strengths**:
- Enables comparison of in-sample performance across different models on the same dataset, providing insights into
which model fits the data the best.
- Utilizes multiple evaluation methods (R-Squared, Adjusted R-Squared, MSE, RMSE), offering a comprehensive review
of a model's performance.

**Limitations**:
- The test measures only in-sample performance, i.e., how well a model fits the data it was trained on. However, it
does not give any information on the performance of the model on new, unseen, or out-of-sample data.
- Higher in-sample performance might be a result of overfitting, where the model is just memorizing the training
data. This test is sensitive to such cases.
- The test does not consider additional key factors such as the temporal dynamics of the data, that is, the pattern
of changes in data over time.
- The test does not provide an automated mechanism to determine if the reported metrics are within acceptable
ranges, necessitating human judgment.