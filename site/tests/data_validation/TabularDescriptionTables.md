# TabularDescriptionTables

Summarizes key descriptive statistics for numerical, categorical, and datetime variables in a dataset.

### Purpose

The main purpose of this metric is to gather and present the descriptive statistics of numerical, categorical, and
datetime variables present in a dataset. The attributes it measures include the count, mean, minimum and maximum
values, percentage of missing values, data types of fields, and unique values for categorical fields, among others.

### Test Mechanism

The test first segregates the variables in the dataset according to their data types (numerical, categorical, or
datetime). Then, it compiles summary statistics for each type of variable. The specifics of these statistics vary
depending on the type of variable:

- For numerical variables, the metric extracts descriptors like count, mean, minimum and maximum values, count of
missing values, and data types.
- For categorical variables, it counts the number of unique values, displays unique values, counts missing values,
and identifies data types.
- For datetime variables, it counts the number of unique values, identifies the earliest and latest dates, counts
missing values, and identifies data types.

### Signs of High Risk

- Masses of missing values in the descriptive statistics results could hint at high risk or failure, indicating
potential data collection, integrity, and quality issues.
- Detection of inappropriate distributions for numerical variables, like having negative values for variables that
are always supposed to be positive.
- Identifying inappropriate data types, like a continuous variable being encoded as a categorical type.

### Strengths

- Provides a comprehensive overview of the dataset.
- Gives a snapshot into the essence of the numerical, categorical, and datetime fields.
- Identifies potential data quality issues such as missing values or inconsistencies crucial for building credible
machine learning models.
- The metadata, including the data type and missing value information, are vital for anyone including data
scientists dealing with the dataset before the modeling process.

### Limitations

- It does not perform any deeper statistical analysis or tests on the data.
- It does not handle issues such as outliers, or relationships between variables.
- It offers no insights into potential correlations or possible interactions between variables.
- It does not investigate the potential impact of missing values on the performance of the machine learning models.
- It does not explore potential transformation requirements that may be necessary to enhance the performance of the
chosen algorithm.