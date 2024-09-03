# RegressionPermutationFeatureImportance

Assesses the significance of each feature in a model by evaluating the impact on model performance when feature
values are randomly rearranged.

### Purpose

The primary purpose of this metric is to determine which features significantly impact the performance of a
regression model developed using statsmodels. The metric measures how much the prediction accuracy deteriorates
when each feature's values are permuted.

### Test Mechanism

This metric shuffles the values of each feature one at a time in the dataset, computes the model's performance
after each permutation, and compares it to the baseline performance. A significant decrease in performance
indicates the importance of the feature.

### Signs of High Risk

- Significant reliance on a feature that, when permuted, leads to a substantial decrease in performance, suggesting
overfitting or high model dependency on that feature.
- Features identified as unimportant despite known impacts from domain knowledge, suggesting potential issues in
model training or data preprocessing.

### Strengths

- Directly assesses the impact of each feature on model performance, providing clear insights into model
dependencies.
- Model-agnostic within the scope of statsmodels, applicable to any regression model that outputs predictions.

### Limitations

- The metric is specific to statsmodels and cannot be used with other types of models without adaptation.
- It does not capture interactions between features, which can lead to underestimating the importance of correlated
features.
- Assumes independence of features when calculating importance, which might not always hold true.