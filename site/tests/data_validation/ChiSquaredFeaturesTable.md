# ChiSquaredFeaturesTable

Assesses the statistical association between categorical features and a target variable using the Chi-Squared test.

### Purpose

The `ChiSquaredFeaturesTable` function is designed to evaluate the relationship between categorical features and a
target variable in a dataset. It performs a Chi-Squared test of independence for each categorical feature to
determine whether a statistically significant association exists with the target variable. This is particularly
useful in Model Risk Management for understanding the relevance of features and identifying potential biases in a
classification model.

### Test Mechanism

The function creates a contingency table for each categorical feature and the target variable, then applies the
Chi-Squared test to compute the Chi-squared statistic and the p-value. The results for each feature include the
variable name, Chi-squared statistic, p-value, p-value threshold, and a pass/fail status based on whether the
p-value is below the specified threshold. The output is a DataFrame summarizing these results, sorted by p-value to
highlight the most statistically significant associations.

### Signs of High Risk

- High p-values (greater than the set threshold) indicate a lack of significant association between a feature and
the target variable, resulting in a 'Fail' status.
- Features with a 'Fail' status might not be relevant for the model, which could negatively impact model
performance.

### Strengths

- Provides a clear, statistical assessment of the relationship between categorical features and the target variable.
- Produces an easily interpretable summary with a 'Pass/Fail' outcome for each feature, helping in feature
selection.
- The p-value threshold is adjustable, allowing for flexibility in statistical rigor.

### Limitations

- Assumes the dataset is tabular and consists of categorical variables, which may not be suitable for all datasets.
- The test is designed for classification tasks and is not applicable to regression problems.
- As with all hypothesis tests, the Chi-Squared test can only detect associations, not causal relationships.
- The choice of p-value threshold can affect the interpretation of feature relevance, and different thresholds may
lead to different conclusions.