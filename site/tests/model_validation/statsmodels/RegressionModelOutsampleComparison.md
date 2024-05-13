# tests\model_validation\statsmodels\RegressionModelOutsampleComparison

Computes MSE and RMSE for multiple regression models using out-of-sample test to assess model's prediction accuracy
on unseen data.

**Purpose**: The RegressionModelOutsampleComparison test is designed to evaluate the predictive performance of
multiple regression models by means of an out-of-sample test. The primary aim of this test is to validate the
model's ability to generalize to unseen data, a common challenge in the context of overfitting. It does this by
computing two critical metrics — Mean Squared Error (MSE) and Root Mean Squared Error (RMSE), which provide a
quantifiable measure of the model's prediction accuracy on the testing dataset.

**Test Mechanism**: This test requires multiple models (specifically Ordinary Least Squares - OLS regression
models) and a test dataset as inputs. Each model generates predictions using the test dataset. The residuals are
then calculated and used to compute the MSE and RMSE for each model. The test outcomes, which include the model's
name, its MSE, and RMSE, are recorded and returned in a structured dataframe format.

**Signs of High Risk**:
- High values of MSE or RMSE indicate significant risk, signifying that the model's predictions considerably
deviate from the actual values in the test dataset.
- Consistently large discrepancies between training and testing performance across various models may indicate an
issue with the input data itself or the model selection strategies employed.

**Strengths**:
- This test offers a comparative evaluation of multiple models' out-of-sample performance, enabling the selection
of the best performing model.
- The use of both MSE and RMSE provides insights into the model's prediction error. While MSE is sensitive to
outliers, emphasizing larger errors, RMSE provides a more interpretable measure of average prediction error given
that it's in the same unit as the dependent variable.

**Limitations**:
- The applicability of this test is limited to regression tasks, specifically OLS models.
- The test operates under the assumption that the test dataset is a representative sample of the population. This
might not always hold true and can result in less accurate insights.
- The interpretability and the objectivity of the output (MSE and RMSE) can be influenced when the scale of the
dependent variable varies significantly, or the distribution of residuals is heavily skewed or contains outliers.