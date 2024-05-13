# tests\data_validation\SpreadPlot

Visualizes the spread relationship between pairs of time-series variables in a dataset, thereby aiding in
identification of potential correlations.

**Purpose**:
The SpreadPlot metric is intended to graphically illustrate and analyse the relationships between pairs of time
series variables within a given dataset. This facilitated understanding helps in identifying and assessing
potential time series correlations, like cointegration, between the variables.

**Test Mechanism**:
The SpreadPlot metric operates by computing and representing the spread between each pair of time series variables
in the dataset. In particular, the difference between two variables is calculated and presented as a line graph.
This method is iterated for each unique pair of variables in the dataset.

**Signs of High Risk**:
Potential indicators of high risk related to the SpreadPlot metric might include:

- Large fluctuations in the spread over a given timespan
- Unexpected patterns or trends that may signal a potential risk in the underlying correlations between the
variables
- Presence of significant missing data or extreme outlier values, which could potentially skew the spread and
indicate high risk

**Strengths**:
The SpreadPlot metric provides several key advantages:

- It allows for thorough visual examination and interpretation of the correlations between time-series pairs
- It aids in revealing complex relationships like cointegration
- It enhances interpretability by visualising the relationships, thereby helping in spotting outliers and trends
- It is capable of handling numerous variable pairs from the dataset through a versatile and adaptable process

**Limitations**:
Despite its advantages, the SpreadPlot metric does have certain drawbacks:

- It primarily serves as a visualisation tool and does not offer quantitative measurements or statistics to
objectively determine relationships
- It heavily relies on the quality and granularity of the data - missing data or outliers can notably disturb the
interpretation of the relationships
- It can become inefficient or difficult to interpret with a high number of variables due to the profuse number of
plots
- It might not completely capture intricate non-linear relationships between the variables