# SpreadPlot

Assesses potential correlations between pairs of time series variables through visualization to enhance
understanding of their relationships.

### Purpose

The SpreadPlot test aims to graphically illustrate and analyze the relationships between pairs of time series
variables within a given dataset. This facilitated understanding helps in identifying and assessing potential time
series correlations, such as cointegration, between the variables.

### Test Mechanism

The SpreadPlot test computes and represents the spread between each pair of time series variables in the dataset.
Specifically, the difference between two variables is calculated and presented as a line graph. This process is
iterated for each unique pair of variables in the dataset, allowing for comprehensive visualization of their
relationships.

### Signs of High Risk

- Large fluctuations in the spread over a given timespan.
- Unexpected patterns or trends that may signal potential risks in the underlying correlations between the
variables.
- Presence of significant missing data or extreme outlier values, which could potentially skew the spread and
indicate high risk.

### Strengths

- Allows for thorough visual examination and interpretation of the correlations between time-series pairs.
- Aids in revealing complex relationships like cointegration.
- Enhances interpretability by visualizing the relationships, thereby helping in spotting outliers and trends.
- Capable of handling numerous variable pairs from the dataset through a versatile and adaptable process.

### Limitations

- Primarily serves as a visualization tool and does not offer quantitative measurements or statistics to
objectively determine relationships.
- Heavily relies on the quality and granularity of the data—missing data or outliers can notably disturb the
interpretation of relationships.
- Can become inefficient or difficult to interpret with a high number of variables due to the profuse number of
plots.
- Might not completely capture intricate non-linear relationships between the variables.