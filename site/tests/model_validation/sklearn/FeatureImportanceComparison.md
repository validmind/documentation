# FeatureImportanceComparison

Compare feature importance scores for each model and generate a summary table
with the top important features.

**Purpose**: The purpose of this function is to compare the feature importance scores for different models applied to various datasets.

**Test Mechanism**: The function iterates through each dataset-model pair, calculates permutation feature importance (PFI) scores, and generates a summary table with the top `num_features` important features for each model.

**Signs of High Risk**:
- If key features expected to be important are ranked low, it could indicate potential issues with model training or data quality.
- High variance in feature importance scores across different models may suggest instability in feature selection.

**Strengths**:
- Provides a clear comparison of the most important features for each model.
- Uses permutation importance, which is a model-agnostic method and can be applied to any estimator.

**Limitations**:
- Assumes that the dataset is provided as a DataFrameDataset object with `x_df` and `y_df` methods to access feature and target data.
- Requires that `model.model` is compatible with `sklearn.inspection.permutation_importance`.
- The function's output is dependent on the number of features specified by `num_features`, which defaults to 3 but can be adjusted.