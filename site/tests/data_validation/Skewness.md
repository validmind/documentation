# Skewness

Evaluates the skewness of numerical data in a dataset to check against a defined threshold, aiming to ensure data
quality and optimize model performance.

### Purpose

The purpose of the Skewness test is to measure the asymmetry in the distribution of data within a predictive
machine learning model. Specifically, it evaluates the divergence of said distribution from a normal distribution.
Understanding the level of skewness helps identify data quality issues, which are crucial for optimizing the
performance of traditional machine learning models in both classification and regression settings.

### Test Mechanism

This test calculates the skewness of numerical columns in the dataset, focusing specifically on numerical data
types. The calculated skewness value is then compared against a predetermined maximum threshold, which is set by
default to 1. If the skewness value is less than this maximum threshold, the test passes; otherwise, it fails. The
test results, along with the skewness values and column names, are then recorded for further analysis.

### Signs of High Risk

- Substantial skewness levels that significantly exceed the maximum threshold.
- Persistent skewness in the data, indicating potential issues with the foundational assumptions of the machine
learning model.
- Subpar model performance, erroneous predictions, or biased inferences due to skewed data distributions.

### Strengths

- Fast and efficient identification of unequal data distributions within a machine learning model.
- Adjustable maximum threshold parameter, allowing for customization based on user needs.
- Provides a clear quantitative measure to mitigate model risks related to data skewness.

### Limitations

- Only evaluates numeric columns, potentially missing skewness or bias in non-numeric data.
- Assumes that data should follow a normal distribution, which may not always be applicable to real-world data.
- Subjective threshold for risk grading, requiring expert input and recurrent iterations for refinement.