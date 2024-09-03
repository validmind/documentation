# FeatureImportanceComparison

Compares feature importance scores across different models and datasets to generate a summary table of top
important features.

### Purpose

The Feature Importance Comparison test is designed to compare the feature importance scores for different models
when applied to various datasets. By doing so, it aims to identify the most impactful features and assess the
consistency of feature importance across models.

### Test Mechanism

This test works by iterating through each dataset-model pair and calculating permutation feature importance (PFI)
scores. It then generates a summary table containing the top `num_features` important features for each model. The
process involves:

- Extracting features and target data from each dataset.
- Computing PFI scores using `sklearn.inspection.permutation_importance`.
- Sorting and selecting the top features based on their importance scores.
- Compiling these features into a summary table for comparison.

### Signs of High Risk

- Key features expected to be important are ranked low, indicating potential issues with model training or data
quality.
- High variance in feature importance scores across different models, suggesting instability in feature selection.

### Strengths

- Provides a clear comparison of the most important features for each model.
- Uses permutation importance, which is a model-agnostic method and can be applied to any estimator.

### Limitations

- Assumes that the dataset is provided as a DataFrameDataset object with `x_df` and `y_df` methods to access
feature and target data.
- Requires that `model.model` is compatible with `sklearn.inspection.permutation_importance`.
- The function's output is dependent on the number of features specified by `num_features`, which defaults to 3 but
can be adjusted.