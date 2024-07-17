# TimeSeriesDescriptiveStatistics

Generates a detailed table of descriptive statistics for the provided time series dataset.

**Purpose**: The purpose of the TimeSeriesDescriptiveStatistics function is to analyze an individual time series
by providing a summary of key descriptive statistics. This helps in understanding trends, patterns, and data quality issues
within the time series.

**Test Mechanism**: The function extracts the time series data and provides a summary of key descriptive statistics.
The dataset is expected to have a datetime index. The function checks this and raises an error if the index is
not in datetime format. For each variable (column) in the dataset, appropriate statistics including start date,
end date, min, mean, max, skewness, kurtosis, and count are calculated.

**Signs of High Risk**:
- If the index of the dataset is not in datetime format, it could lead to errors in time-series analysis.
- Inconsistent or missing data within the dataset might affect the analysis of trends and patterns.

**Strengths**:
- This function provides a comprehensive summary of key descriptive statistics for each variable, helping to identify data quality
issues and understand the distribution of the data.

**Limitations**:
- This function assumes that the dataset is provided as a DataFrameDataset object with a .df attribute to access
the pandas DataFrame.
- It only analyzes datasets with a datetime index and will raise an error for other types of indices.
- The function does not handle large datasets efficiently, and performance may degrade with very large datasets.