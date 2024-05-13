# tests\data_validation\MissingValuesRisk

Assesses and quantifies the risk related to missing values in a dataset used for training an ML model.

**Purpose**: The Missing Values Risk metric is specifically designed to assess and quantify the risk associated
with missing values in the dataset used for machine learning model training. It measures two specific risks: the
percentage of total data that are missing, and the percentage of all variables (columns) that contain some missing
values.

**Test Mechanism**: Initially, the metric calculates the total number of data points in the dataset and the count
of missing values. It then inspects each variable (column) to determine how many contain at least one missing
datapoint. By methodically counting missing datapoints across the entire dataset and each variable (column), it
identifies the percentage of missing values in the entire dataset and the percentage of variables (columns) with
such values.

**Signs of High Risk**:

- Record high percentages in either of the risk measures could suggest a high risk.
- If the dataset indicates a high percentage of missing values, it might significantly undermine the model's
performance and credibility.
- If a significant portion of variables (columns) in the dataset are missing values, this could make the model
susceptible to bias and overfitting.

**Strengths**:

- The metric offers valuable insights into the readiness of a dataset for model training as missing values can
heavily destabilize both the model's performance and predictive capabilities.
- The metric's quantification of the risks caused by missing values allows for the use of targeted methods to
manage these values correctly- either through removal, imputation, or alternative strategies.
- The metric has the flexibility to be applied to both classification and regression assignments, maintaining its
utility across a wide range of models and scenarios.

**Limitations**:

- The metric primarily identifies and quantifies the risk associated with missing values without suggesting
specific mitigation strategies.
- The metric does not ascertain whether the missing values are random or associated with an underlying issue in the
stages of data collection or preprocessing.
- However, the identification of the presence and scale of missing data is the essential initial step towards
improving data quality.