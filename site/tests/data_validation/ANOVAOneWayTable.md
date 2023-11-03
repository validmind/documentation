# ANOVAOneWayTable

Applies one-way ANOVA (Analysis of Variance) to identify statistically significant numerical features in the
dataset.

**Purpose**: The ANOVA (Analysis of Variance) One-Way Table metric is utilized to determine whether the mean of
numerical variables differs across different groups identified by target or categorical variables. Its primary
purpose is to scrutinize the significant impact of categorical variables on numerical ones. This method proves
essential in identifying statistically significant features corresponding to the target variable present in the
dataset.

**Test Mechanism**: The testing mechanism involves the ANOVA F-test's performance on each numerical variable
against the target. If no specific features are mentioned, all numerical features are tested. A p-value is produced
for each test and compared against a certain threshold (default being 0.05 if not specified). If the p-value is
less than or equal to this threshold, the feature is marked as 'Pass', indicating significant mean difference
across the groups. Otherwise, it's marked as 'Fail'. The test produces a DataFrame that includes variable name, F
statistic value, p-value, threshold, and pass/fail status for every numerical variable.

**Signs of High Risk**:
- A large number of 'Fail' results in the ANOVA F-test could signify high risk or underperformance in the model.
This issue may arise when multiple numerical variables in the dataset don't exhibit any significant difference
across the target variable groups.
- Features with high p-values also indicate a high risk as they imply a greater chance of obtaining observed data
given that the null hypothesis is true.

**Strengths**:
- The ANOVA One Way Table is highly efficient in identifying statistically significant features by simultaneously
comparing group means.
- Its flexibility allows the testing of all numerical features in the dataset when no specific ones are mentioned.
- This metric provides a convenient method to measure the statistical significance of numerical variables and
assists in selecting those variables influencing the classifier's predictions considerably.

**Limitations**:
- This metric assumes that the data is normally distributed, which may not always be the case leading to erroneous
test results.
- The sensitivity of the F-test to variance changes may hinder this metric's effectiveness, especially for datasets
with high variance.
- The ANOVA One Way test does not specify which group means differ statistically from others; it strictly asserts
the existence of a difference.
- The metric fails to provide insights into variable interactions, and significant effects due to these
interactions could easily be overlooked.