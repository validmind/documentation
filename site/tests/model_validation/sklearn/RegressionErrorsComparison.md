# RegressionErrorsComparison

Compare regression error metrics for each model and generate a summary table
with the results.

**Purpose**: The purpose of this function is to compare the regression errors for different models applied to various datasets.

**Test Mechanism**: The function iterates through each dataset-model pair, calculates various error metrics (MAE, MSE, MAPE, MBD), and generates a summary table with these results.

**Signs of High Risk**:
- High Mean Absolute Error (MAE) or Mean Squared Error (MSE) indicates poor model performance.
- High Mean Absolute Percentage Error (MAPE) suggests large percentage errors, especially problematic if the true values are small.
- Mean Bias Deviation (MBD) significantly different from zero indicates systematic overestimation or underestimation by the model.

**Strengths**:
- Provides multiple error metrics to assess model performance from different perspectives.
- Includes a check to avoid division by zero when calculating MAPE.

**Limitations**:
- Assumes that the dataset is provided as a DataFrameDataset object with `y`, `y_pred`, and `feature_columns` attributes.
- The function relies on the `logger` from `validmind.logging` to warn about zero values in `y_true`, which should be correctly implemented and imported.
- Requires that `dataset.y_pred(model)` returns the predicted values for the model.