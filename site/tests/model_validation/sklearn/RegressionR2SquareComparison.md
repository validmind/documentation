# RegressionR2SquareComparison

Compare R-Squared and Adjusted R-Squared values for each model and generate a summary table
with the results.

**Purpose**: The purpose of this function is to compare the R-Squared and Adjusted R-Squared values for different models applied to various datasets.

**Test Mechanism**: The function iterates through each dataset-model pair, calculates the R-Squared and Adjusted R-Squared values, and generates a summary table with these results.

**Signs of High Risk**:
- If the R-Squared values are significantly low, it could indicate that the model is not explaining much of the variability in the dataset.
- A significant difference between R-Squared and Adjusted R-Squared values might indicate that the model includes irrelevant features.

**Strengths**:
- Provides a quantitative measure of model performance in terms of variance explained.
- Adjusted R-Squared accounts for the number of predictors, making it a more reliable measure when comparing models with different numbers of features.

**Limitations**:
- Assumes that the dataset is provided as a DataFrameDataset object with `y`, `y_pred`, and `feature_columns` attributes.
- The function relies on `adj_r2_score` from the `statsmodels.statsutils` module, which should be correctly implemented and imported.
- Requires that `dataset.y_pred(model)` returns the predicted values for the model.