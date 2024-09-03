# RegressionResidualsPlot

Evaluates regression model performance using residual distribution and actual vs. predicted plots.

### Purpose

The `RegressionResidualsPlot` metric aims to evaluate the performance of regression models. By generating and
analyzing two plots – a distribution of residuals and a scatter plot of actual versus predicted values – this tool
helps to visually appraise how well the model predicts and the nature of errors it makes.

### Test Mechanism

The process begins by extracting the true output values (`y_true`) and the model's predicted values (`y_pred`).
Residuals are computed by subtracting predicted from true values. These residuals are then visualized using a
histogram to display their distribution. Additionally, a scatter plot is derived to compare true values against
predicted values, together with a "Perfect Fit" line, which represents an ideal match (predicted values equal
actual values), facilitating the assessment of the model's predictive accuracy.

### Signs of High Risk

- Residuals showing a non-normal distribution, especially those with frequent extreme values.
- Significant deviations of predicted values from actual values in the scatter plot.
- Sparse density of data points near the "Perfect Fit" line in the scatter plot, indicating poor prediction
accuracy.
- Visible patterns or trends in the residuals plot, suggesting the model's failure to capture the underlying data
structure adequately.

### Strengths

- Provides a direct, visually intuitive assessment of a regression model’s accuracy and handling of data.
- Visual plots can highlight issues of underfitting or overfitting.
- Can reveal systematic deviations or trends that purely numerical metrics might miss.
- Applicable across various regression model types.

### Limitations

- Relies on visual interpretation, which can be subjective and less precise than numerical evaluations.
- May be difficult to interpret in cases with multi-dimensional outputs due to the plots’ two-dimensional nature.
- Overlapping data points in the residuals plot can complicate interpretation efforts.
- Does not summarize model performance into a single quantifiable metric, which might be needed for comparative or
summary analyses.