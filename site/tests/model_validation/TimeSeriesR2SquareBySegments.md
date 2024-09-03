# TimeSeriesR2SquareBySegments

Evaluates the R-Squared values of regression models over specified time segments in time series data to assess
segment-wise model performance.

### Purpose

The TimeSeriesR2SquareBySegments test aims to evaluate the R-Squared values for several regression models across
different segments of time series data. This helps in determining how well the models explain the variability in
the data within each specific time segment.

### Test Mechanism

This test functions by:

- Iterating through each dataset-model pair provided.
- Segmenting the time series data either as specified by the user or by splitting the data into two halves if no
segments are provided.
- Calculating the R-Squared values for each segment.
- Generating a bar chart to visually represent the R-Squared values across different models and segments.

### Signs of High Risk

- Significantly low R-Squared values for certain time segments, indicating poor model performance in those periods.
- Large variability in R-Squared values across different segments for the same model, suggesting inconsistent
performance.

### Strengths

- Provides a visual representation of how well models perform over different time periods.
- Helps identify time segments where models may need improvement or retraining.
- Facilitates comparison between multiple models in a straightforward manner.

### Limitations

- Assumes datasets are provided as DataFrameDataset objects with the attributes `y`, `y_pred`, and
`feature_columns`.
- Requires that `dataset.y_pred(model)` returns predicted values for the model.
- Assumes that both `y_true` and `y_pred` are pandas Series with datetime indices, which may not always be the case.
- May not account for more nuanced temporal dependencies within the segments.