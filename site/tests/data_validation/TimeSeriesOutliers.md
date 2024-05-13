# tests\data_validation\TimeSeriesOutliers

Identifies and visualizes outliers in time-series data using z-score method.

**Purpose**: This test is designed to identify outliers in time-series data using the z-score method. It's vital
for ensuring data quality before modeling, as outliers can skew predictive models and significantly impact their
overall performance.

**Test Mechanism**: The test processes a given dataset which must have datetime indexing, checks if a
zscore_threshold' parameter has been supplied, and identifies columns with numeric data types. After finding
numeric columns, the implementer then applies the z-score method to each numeric column, identifying outliers based
on the threshold provided. Each outlier is listed together with their variable name, z-score, timestamp and
relative threshold in a dictionary and converted to a DataFrame for convenient output. Additionally, it produces
visual plots for each time series illustrating outliers in the context of the broader dataset. The
zscore_threshold' parameter sets the limit beyond which a data point will be labeled as an outlier. The default
threshold is set at 3, indicating that any data point that falls 3 standard deviations away from the mean will be
marked as an outlier.

**Signs of High Risk**:
- If many or substantial outliers are present within a dataset, this may be an indicator of high risk as it
suggests that the dataset contains significant anomalies.
- This could potentially affect the performance of the machine learning models, if not properly addressed.
- Data points with z-scores higher than the set threshold would be flagged as outliers and could be considered as
high risk.

**Strengths**:
- The z-score method is a popular and robust method for identifying outliers in a dataset.
- Time series maintenance is simplified through requiring a datetime index.
- Outliers are identified for each numeric feature individually.
- Provides an elaborate report which shows variables, date, z-score and whether the test passed or failed.
- Offers visual inspection for detected outliers in the respective time-series through plots.

**Limitations**:
- This test only identifies outliers in numeric columns, and won't identify outliers in categorical variables.
- The utility and accuracy of z-scores can be limited if the data doesn't follow a normal distribution.
- The method relies on a subjective z-score threshold for deciding what constitutes an outlier, which might not
always be suitable depending on the dataset and the use case.
- It does not address possible ways to handle identified outliers in the data.
- The necessity for a datetime index could limit the extent of its application.