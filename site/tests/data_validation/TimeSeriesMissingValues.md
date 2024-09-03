# TimeSeriesMissingValues

Validates time-series data quality by confirming the count of missing values is below a certain threshold.

### Purpose

This test is designed to validate the quality of a historical time-series dataset by verifying that the number of
missing values is below a specified threshold. As time-series models greatly depend on the continuity and
temporality of data points, missing values could compromise the model's performance. Consequently, this test aims
to ensure data quality and readiness for the machine learning model, safeguarding its predictive capacity.

### Test Mechanism

The test method commences by validating if the dataset has a datetime index; if not, an error is raised. It
establishes a lower limit threshold for missing values and performs a missing values check on each column of the
dataset. An object for the test result is created stating whether the number of missing values is within the
specified threshold. Additionally, the test calculates the percentage of missing values alongside the raw count.

To aid in data visualization, the test generates two plots - a bar plot and a heatmap - to better illustrate the
distribution and quantity of missing values per variable. The test results, including a count of missing values,
the percentage of missing values, and a pass/fail status, are returned in a results table.

### Signs of High Risk

- The number of missing values in any column of the dataset surpasses the threshold, marking a failure and a
high-risk scenario. The reasons could range from incomplete data collection, faulty sensors to data preprocessing
errors.
- A continuous visual 'streak' in the heatmap may indicate a systematic error during data collection, pointing
towards another potential risk source.

### Strengths

- Effectively identifies missing values which could adversely affect the model’s performance.
- Applicable and customizable through the threshold parameter across different data sets.
- Goes beyond raw numbers by calculating the percentage of missing values, offering a more relative understanding
of data scarcity.
- Includes a robust visualization mechanism for easy and fast understanding of data quality.

### Limitations

- Although it identifies missing values, the test does not provide solutions to handle them.
- The test demands that the dataset should have a datetime index, hence limiting its use only to time series
analysis.
- The test's sensitivity to the 'min_threshold' parameter may raise false alarms if set too strictly or may
overlook problematic data if set too loosely.
- Solely focuses on the 'missingness' of the data and might fall short in addressing other aspects of data quality.