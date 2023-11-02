# SeasonalDecompose

Decomposes dataset features into observed, trend, seasonal, and residual components to identify patterns and
validate dataset.

**Purpose**: This test utilizes the Seasonal Decomposition of Time Series by Loess (STL) method to decompose a
dataset into its fundamental components: observed, trend, seasonal, and residuals. The purpose is to identify
implicit patterns, majorly any seasonality, in the dataset's features which aid in developing a more comprehensive
understanding and effectively validating the dataset.

**Test Mechanism**: The testing process exploits the `seasonal_decompose` function from the
`statsmodels.tsa.seasonal` library to evaluate each feature in the dataset. It isolates each feature into four
components: observed, trend, seasonal, and residuals, and generates essentially six subplot graphs per feature for
visual interpretation of the results. Prior to the seasonal decomposition, non-finite values are scrutinized and
removed thus, ensuring reliability in the analysis.

**Signs of High Risk**:
- **Non-Finiteness**: If a dataset carries too many non-finite values it might flag high risk as these values are
omitted before conducting the seasonal decomposition.
- **Frequent Warnings**: The test could be at risk if it chronically fails to infer frequency for a scrutinized
feature.
- **High Seasonality**: A high seasonal component could potentially render forecasts unreliable due to overwhelming
seasonal variation.

**Strengths**:
- **Seasonality Detection**: The code aptly discerns hidden seasonality patterns in the features of datasets.
- **Visualization**: The test facilitates interpretation and comprehension via graphical representations.
- **Unrestricted Usage**: The code is not confined to any specific regression model, thereby promoting wide-ranging
applicability.

**Limitations**:
- **Dependence on Assumptions**: The test presumes that features in the dataset are periodically distributed. If no
frequency could be inferred for a variable, that feature is excluded from the test.
- **Handling Non-finite Values**: The test disregards non-finite values during the analysis which could potentially
result in incomplete understanding of the dataset.
- **Unreliability with Noisy Datasets**: The test tends to produce unreliable results when used with heavy noise
present in the dataset.