# PermutationFeatureImportance

Assesses the significance of each feature in a model by evaluating the impact on model performance when feature
values are randomly rearranged.

### Purpose

The Permutation Feature Importance (PFI) metric aims to assess the importance of each feature used by the Machine
Learning model. The significance is measured by evaluating the decrease in the model's performance when the
feature's values are randomly arranged.

### Test Mechanism

PFI is calculated via the `permutation_importance` method from the `sklearn.inspection` module. This method
shuffles the columns of the feature dataset and measures the impact on the model's performance. A significant
decrease in performance after permutating a feature's values deems the feature as important. On the other hand, if
performance remains the same, the feature is likely not important. The output of the PFI metric is a figure
illustrating the importance of each feature.

### Signs of High Risk

- The model heavily relies on a feature with highly variable or easily permutable values, indicating instability.
- A feature deemed unimportant by the model but expected to have a significant effect on the outcome based on
domain knowledge is not influencing the model's predictions.

### Strengths

- Provides insights into the importance of different features and may reveal underlying data structure.
- Can indicate overfitting if a particular feature or set of features overly impacts the model's predictions.
- Model-agnostic and can be used with any classifier that provides a measure of prediction accuracy before and
after feature permutation.

### Limitations

- Does not imply causality; it only presents the amount of information that a feature provides for the prediction
task.
- Does not account for interactions between features. If features are correlated, the permutation importance may
allocate importance to one and not the other.
- Cannot interact with certain libraries like statsmodels, pytorch, catboost, etc., thus limiting its applicability.