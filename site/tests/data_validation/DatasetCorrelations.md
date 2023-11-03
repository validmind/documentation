# DatasetCorrelations

Assesses correlation and association among features in a dataset, leveraging Pearson's R, Cramer's V, and
Correlation ratios.

**Purpose**: The DatasetCorrelations metric is employed to examine the relationship between variables in a dataset,
specifically designed for numerical and categorical data types. Using Pearson's R, Cramer's V, and Correlation
ratios, it helps in understanding the linear relationship between numerical variables, association between
categorical ones, and between numerical-categorical variables respectively. This allows for better awareness
regarding dependency between features, which is crucial for optimizing model performance and understanding the
model's behavior and predictors.

**Test Mechanism**: During its execution, DatasetCorrelations initiates the calculation of the aforementioned
correlation coefficients for the provided dataset. It leverages the built-in method 'get_correlations()',
populating the 'correlations' attribute in the dataset object. It then invokes 'get_correlation_plots()' to
generate graphical representations of these correlations. Finally, the correlation details and figures are cached
for further study and analysis. The test does not dictate specific thresholds or grading scales.

**Signs of High Risk**:

- High correlation levels between input variables (multicollinearity), which can jeopardize the interpretability of
the model and lead to overfitting.
- The absence of any significant correlations, suggesting the variables may not have predictive power.

**Strengths**:

- Comprehensive coverage of the correlation study of numerical, categorical, and numerical-categorical variables,
negating the need for multiple individual tests.
- Along with numerical correlation values, it provides visualization plots for a more intuitive understanding of
relationships between variables.

**Limitations**:

- Limitations of this metric include detecting only linear relationships and associations; nonlinear relationships
may go unnoticed.
- The absence of specified thresholds for determining correlation significance means the interpretation of the
results is dependent on the user's expertise.
- It doesn't manage missing values in the dataset, which need to be treated beforehand.