# RegressionR2SquareComparison

Compares R-Squared and Adjusted R-Squared values for different regression models across multiple datasets to assess
model performance and relevance of features.

### Purpose

The Regression R2 Square Comparison test aims to compare the R-Squared and Adjusted R-Squared values for different
regression models across various datasets. It helps in assessing how well each model explains the variability in
the dataset, and whether the models include irrelevant features.

### Test Mechanism

This test operates by:

- Iterating through each dataset-model pair.
- Calculating the R-Squared values to measure how much of the variability in the dataset is explained by the model.
- Calculating the Adjusted R-Squared values, which adjust the R-Squared based on the number of predictors in the
model, making it more reliable when comparing models with different numbers of features.
- Generating a summary table containing these values for each combination of dataset and model.

### Signs of High Risk

- If the R-Squared values are significantly low, it indicates the model isn't explaining much of the variability in
the dataset.
- A significant difference between R-Squared and Adjusted R-Squared values might indicate that the model includes
irrelevant features.

### Strengths

- Provides a quantitative measure of model performance in terms of variance explained.
- Adjusted R-Squared accounts for the number of predictors, making it a more reliable measure when comparing models
with different numbers of features.
- Useful for time-series forecasting and regression tasks.

### Limitations

- Assumes the dataset is provided as a DataFrameDataset object with `y`, `y_pred`, and `feature_columns` attributes.
- Relies on `adj_r2_score` from the `statsmodels.statsutils` module, which needs to be correctly implemented and
imported.
- Requires that `dataset.y_pred(model)` returns the predicted values for the model.