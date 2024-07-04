# TimeSeriesR2SquareBySegments

Plot R-Squared values for each model over specified time segments and generate a bar chart
with the results.

**Purpose**: The purpose of this function is to plot the R-Squared values for different models applied to various segments of the time series data.

**Parameters**:
- datasets: List of datasets to evaluate.
- models: List of models to evaluate.
- segments: Dictionary with 'start_date' and 'end_date' keys containing lists of start and end dates for each segments. If None, the time series will be segmented into two halves.

**Test Mechanism**: The function iterates through each dataset-model pair, calculates the R-Squared values for specified time segments, and generates a bar chart with these results.

**Signs of High Risk**:
- If the R-Squared values are significantly low for certain segments, it could indicate that the model is not explaining much of the variability in the dataset for those segments.

**Strengths**:
- Provides a visual representation of model performance across different time segments.
- Allows for identification of segments where models perform poorly.

**Limitations**:
- Assumes that the dataset is provided as a DataFrameDataset object with `y`, `y_pred`, and `feature_columns` attributes.
- Requires that `dataset.y_pred(model)` returns the predicted values for the model.
- Assumes that `y_true` and `y_pred` are pandas Series with datetime indices.