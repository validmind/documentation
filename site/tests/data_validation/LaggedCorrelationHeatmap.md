# LaggedCorrelationHeatmap

Assesses and visualizes correlation between target variable and lagged independent variables in a time-series
dataset.

### Purpose

The LaggedCorrelationHeatmap metric is utilized to appraise and illustrate the correlation between the target
variable and delayed copies (lags) of independent variables in a time-series dataset. It assists in revealing
relationships in time-series data where the influence of an independent variable on the dependent variable is not
immediate but occurs after a period (lags).

### Test Mechanism

To execute this test, Python's Pandas library pairs with Plotly to perform computations and present the
visualization in the form of a heatmap. The test begins by extracting the target variable and corresponding
independent variables from the dataset. Then, generation of lags of independent variables takes place, followed by
the calculation of correlation between these lagged variables and the target variable. The outcome is a correlation
matrix that gets recorded and illustrated as a heatmap, where different color intensities represent the strength of
the correlation, making patterns easier to identify.

### Signs of High Risk

- Insignificant correlations across the heatmap, indicating a lack of noteworthy relationships between variables.
- Correlations that break intuition or previous understanding, suggesting potential issues with the dataset or the
model.

### Strengths

- This metric serves as an exceptional tool for exploring and visualizing time-dependent relationships between
features and the target variable in a time-series dataset.
- It aids in identifying delayed effects that might go unnoticed with other correlation measures.
- The heatmap offers an intuitive visual representation of time-dependent correlations and influences.

### Limitations

- The metric presumes linear relationships between variables, potentially ignoring non-linear relationships.
- The correlation considered is linear; therefore, intricate non-linear interactions might be overlooked.
- The metric is only applicable for time-series data, limiting its utility outside of this context.
- The number of lags chosen can significantly influence the results; too many lags can render the heatmap difficult
to interpret, while too few might overlook delayed effects.
- This metric does not take into account any causal relationships, but merely demonstrates correlation.