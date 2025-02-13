# TimeSeriesPredictionsPlot

Plot actual vs predicted values for time series data and generate a visual comparison for the model.

### Purpose

The purpose of this function is to visualize the actual versus predicted values for time
series data for a single model.

### Test Mechanism

The function plots the actual values from the dataset and overlays the predicted
values from the model using Plotly for interactive visualization.

- Large discrepancies between actual and predicted values indicate poor model performance.
- Systematic deviations in predicted values can highlight model bias or issues with data patterns.

### Strengths

- Provides a clear visual comparison of model predictions against actual values.
- Uses Plotly for interactive and visually appealing plots.

### Limitations

- Assumes that the dataset is provided as a DataFrameDataset object with a datetime index.
- Requires that `dataset.y_pred(model)` returns the predicted values for the model.