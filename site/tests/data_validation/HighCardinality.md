# HighCardinality

Assesses the number of unique values in categorical columns to detect high cardinality and potential overfitting.

### Purpose

The “High Cardinality” test is used to evaluate the number of unique values present in the categorical columns of a
dataset. In this context, high cardinality implies the presence of a large number of unique, non-repetitive values
in the dataset.

### Test Mechanism

The test first infers the dataset's type and then calculates an initial numeric threshold based on the test
parameters. It only considers columns classified as "Categorical". For each of these columns, the number of
distinct values (n_distinct) and the percentage of distinct values (p_distinct) are calculated. The test will pass
if n_distinct is less than the calculated numeric threshold. Lastly, the results, which include details such as
column name, number of distinct values, and pass/fail status, are compiled into a table.

### Signs of High Risk

- A large number of distinct values (high cardinality) in one or more categorical columns implies a high risk.
- A column failing the test (n_distinct >= num_threshold) is another indicator of high risk.

### Strengths

- The High Cardinality test is effective in early detection of potential overfitting and unwanted noise.
- It aids in identifying potential outliers and inconsistencies, thereby improving data quality.
- The test can be applied to both classification and regression task types, demonstrating its versatility.

### Limitations

- The test is restricted to only "Categorical" data types and is thus not suitable for numerical or continuous
features, limiting its scope.
- The test does not consider the relevance or importance of unique values in categorical features, potentially
causing it to overlook critical data points.
- The threshold (both number and percent) used for the test is static and may not be optimal for diverse datasets
and varied applications. Further mechanisms to adjust and refine this threshold could enhance its effectiveness.