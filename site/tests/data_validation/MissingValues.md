# tests\data_validation\MissingValues

Evaluates dataset quality by ensuring missing value ratio across all features does not exceed a set threshold.

**Purpose**: This test is designed to evaluate the quality of a dataset by measuring the number of missing values
across all features. The objective is to ensure that the ratio of missing data to total data is less than a
predefined threshold, defaulting to 1, to maintain the data quality necessary for reliable predictive strength in a
machine learning model.

**Test Mechanism**: The mechanism for this test involves iterating through each column of the dataset, counting
missing values (represented as NaNs), and calculating the percentage they represent against the total number of
rows. The test then checks if these missing value counts are less than the predefined `min_threshold`. The results
are shown in a table summarizing each column, the number of missing values, the percentage of missing values in
each column, and a Pass/Fail status based on the threshold comparison.

**Signs of High Risk**:
- When the number of missing values in any column exceeds the `min_threshold` value, it indicates a high risk.
- A high risk is also flagged when missing values are present across many columns. In both instances, the test
would return a "Fail" mark.

**Strengths**:
- The test offers a quick and granular identification of missing data across each feature in the dataset.
- It provides an effective, straightforward means of maintaining data quality, which is vital for constructing
efficient machine learning models.

**Limitations**:
- Even though the test can efficiently identify missing values, it does not suggest the root causes of these
missing values or recommend ways to impute or handle them.
- The test might overlook features with a significant amount of missing data, but still less than the
`min_threshold`. This could impact the model, especially if `min_threshold` is set too high.
- The test does not account for data encoded as values (like "-999" or "None"), which might not technically
classify as missing but could bear similar implications.