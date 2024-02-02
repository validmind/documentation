# ChiSquaredFeaturesTable

Executes Chi-Squared test for each categorical feature against a target column to assess significant association.

**Purpose**: The `ChiSquaredFeaturesTable` metric is used to carry out a Chi-Squared test of independence for each
categorical feature variable against a designated target column. The primary goal is to determine if a significant
association exists between the categorical features and the target variable. This method typically finds its use in
the context of Model Risk Management to understand feature relevance and detect potential bias in a classification
model.

**Test Mechanism**: The testing process generates a contingency table for each categorical variable and the target
variable, after which a Chi-Squared test is performed. Using this approach, the Chi-Squared statistic and the
p-value for each feature are calculated. The p-value threshold is a modifiable parameter, and a test will qualify
as passed if the p-value is less than or equal to this threshold. If not, the test is labeled as failed. The
outcome for each feature - comprising the variable name, Chi-squared statistic, p-value, threshold, and pass/fail
status - is incorporated into a final summary table.

**Signs of High Risk**:
- High p-values (greater than the set threshold) for specific variables could indicate a high risk.
- These high p-values allude to the absence of a statistically significant relationship between the feature and the
target variables, resulting in a 'Fail' status.
- A categorical feature lacking a relevant association with the target variable could be a warning that the machine
learning model might not be performing optimally.

**Strengths**:
- The test allows for a comprehensive understanding of the interaction between a model's input features and the
target output, thus validating the relevance of categorical features.
- It also produces an unambiguous 'Pass/Fail' output for each categorical feature.
- The opportunity to adjust the p-value threshold contributes to flexibility in accommodating different statistical
standards.

**Limitations**:
- The metric presupposes that data is tabular and categorical, which may not always be the case with all datasets.
- It is distinctively designed for classification tasks, hence unsuitable for regression scenarios.
- The Chi-squared test, akin to any hypothesis testing-based test, cannot identify causal relationships, but only
associations.
- Furthermore, the test hinges on an adjustable p-value threshold, and varying threshold selections might lead to
different conclusions regarding feature relevance.