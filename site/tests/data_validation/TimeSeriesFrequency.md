# TimeSeriesFrequency

Evaluates consistency of time series data frequency and generates a frequency plot.

### Purpose

The purpose of the TimeSeriesFrequency test is to evaluate the consistency in the frequency of data points in a
time-series dataset. This test inspects the intervals or duration between each data point to determine if a fixed
pattern (such as daily, weekly, or monthly) exists. The identification of such patterns is crucial to time-series
analysis as any irregularities could lead to erroneous results and hinder the model's capacity for identifying
trends and patterns.

### Test Mechanism

Initially, the test checks if the dataframe index is in datetime format. Subsequently, it utilizes pandas
`infer_freq` method to identify the frequency of each data series within the dataframe. The `infer_freq` method
attempts to establish the frequency of a time series and returns both the frequency string and a dictionary
relating these strings to their respective labels. The test compares the frequencies of all datasets. If they share
a common frequency, the test passes, but it fails if they do not. Additionally, Plotly is used to create a
frequency plot, offering a visual depiction of the time differences between consecutive entries in the dataframe
index.

### Signs of High Risk

- The test fails, indicating multiple unique frequencies within the dataset. This failure could suggest irregular
intervals between observations, potentially interrupting pattern recognition or trend analysis.
- The presence of missing or null frequencies could be an indication of inconsistencies in data or gaps within the
data collection process.

### Strengths

- This test uses a systematic approach to checking the consistency of data frequency within a time-series dataset.
- It increases the model's reliability by asserting the consistency of observations over time, an essential factor
in time-series analysis.
- The test generates a visual plot, providing an intuitive representation of the dataset's frequency distribution,
which caters to visual learners and aids in interpretation and explanation.

### Limitations

- This test is only applicable to time-series datasets and hence not suitable for other types of datasets.
- The `infer_freq` method might not always correctly infer frequency when faced with missing or irregular data
points.
- Depending on context or the model under development, mixed frequencies might sometimes be acceptable, but this
test considers them a failing condition.