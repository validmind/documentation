# RegressionModelsPerformanceComparison

Compares and evaluates the performance of multiple regression models using five different metrics: MAE, MSE, RMSE,
MAPE, and MBD.

### Purpose

The Regression Models Performance Comparison metric is used to measure and compare the performance of regression
models. It calculates multiple evaluation metrics, including Mean Absolute Error (MAE), Mean Squared Error (MSE),
Root Mean Squared Error (RMSE), Mean Absolute Percentage Error (MAPE), and Mean Bias Deviation (MBD), thereby
enabling a comprehensive view of model performance.

### Test Mechanism

The test starts by sourcing the true and predicted values from the models. It then computes the MAE, MSE, RMSE,
MAPE, and MBD. These calculations encapsulate both the direction and the magnitude of error in predictions, thereby
providing a multi-faceted view of model accuracy. It captures these results in a dictionary and compares the
performance of all models using these metrics. The results are then appended to a table for presenting a
comparative summary.

### Signs of High Risk

- High values of MAE, MSE, RMSE, and MAPE, which indicate a high error rate and imply a larger departure of the
model's predictions from the true values.
- A large value of MBD, which shows a consistent bias in the model’s predictions.
- If the test returns an error citing that no models were provided for comparison, it implies a risk in the
evaluation process itself.

### Strengths

- The metric evaluates models on five different metrics offering a comprehensive analysis of model performance.
- It compares multiple models simultaneously, aiding in the selection of the best-performing models.
- It is designed to handle regression tasks and can be seamlessly integrated with libraries like sklearn.

### Limitations

- The metric only evaluates regression models and does not evaluate classification models.
- The test assumes that the models have been trained and tested appropriately prior to evaluation. It does not
handle pre-processing, feature selection, or other stages in the model lifecycle.
- It may fail to run if it doesn't receive valid models as inputs. The models are passed externally and the test
doesn't have an internal mechanism to verify their validity.
- The test could exhibit performance limitations if a large number of models is input for comparison.