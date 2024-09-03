# RegressionErrorsComparison

Assesses multiple regression error metrics to compare model performance across different datasets, emphasizing
systematic overestimation or underestimation and large percentage errors.

### Purpose

The purpose of this test is to compare regression errors for different models applied to various datasets. It aims
to examine model performance using multiple error metrics, thereby identifying areas where models may be
underperforming or exhibiting bias.

### Test Mechanism

The function iterates through each dataset-model pair and calculates various error metrics, including Mean Absolute
Error (MAE), Mean Squared Error (MSE), Mean Absolute Percentage Error (MAPE), and Mean Bias Deviation (MBD). The
results are summarized in a table, which provides a comprehensive view of each model's performance on the datasets.

### Signs of High Risk

- High Mean Absolute Error (MAE) or Mean Squared Error (MSE), indicating poor model performance.
- High Mean Absolute Percentage Error (MAPE), suggesting large percentage errors, especially problematic if the
true values are small.
- Mean Bias Deviation (MBD) significantly different from zero, indicating systematic overestimation or
underestimation by the model.

### Strengths

- Provides multiple error metrics to assess model performance from different perspectives.
- Includes a check to avoid division by zero when calculating MAPE.

### Limitations

- Assumes that the dataset is provided as a DataFrameDataset object with `y`, `y_pred`, and `feature_columns`
attributes.
- Relies on the `logger` from `validmind.logging` to warn about zero values in `y_true`, which should be correctly
implemented and imported.
- Requires that `dataset.y_pred(model)` returns the predicted values for the model.