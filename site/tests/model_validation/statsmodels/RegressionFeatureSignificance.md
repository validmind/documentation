# RegressionFeatureSignificance

Assesses and visualizes the statistical significance of features in a regression model.

### Purpose

The Regression Feature Significance metric assesses the significance of each feature in a given set of regression
model. It creates a visualization displaying p-values for every feature of the model, assisting model developers
in understanding which features are most influential in their model.

### Test Mechanism

The test mechanism involves extracting the model's coefficients and p-values for each feature, and then plotting these
values. The x-axis on the plot contains the p-values while the y-axis denotes the coefficients of each feature. A
vertical red line is drawn at the threshold for p-value significance, which is 0.05 by default. Any features with
p-values to the left of this line are considered statistically significant at the chosen level.

### Signs of High Risk

- Any feature with a high p-value (greater than the threshold) is considered a potential high risk, as it suggests
the feature is not statistically significant and may not be reliably contributing to the model's predictions.
- A high number of such features may indicate problems with the model validation, variable selection, and overall
reliability of the model predictions.

### Strengths

- Helps identify the features that significantly contribute to a model's prediction, providing insights into the
feature importance.
- Provides tangible, easy-to-understand visualizations to interpret the feature significance.

### Limitations

- This metric assumes model features are independent, which may not always be the case. Multicollinearity (high
correlation amongst predictors) can cause high variance and unreliable statistical tests of significance.
- The p-value strategy for feature selection doesn't take into account the magnitude of the effect, focusing solely
on whether the feature is likely non-zero.
- This test is specific to regression models and wouldn't be suitable for other types of ML models.
- P-value thresholds are somewhat arbitrary and do not always indicate practical significance, only statistical
significance.