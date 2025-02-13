# MutualInformation

Calculates mutual information scores between features and target variable to evaluate feature relevance.

### Purpose

The Mutual Information test quantifies the predictive power of each feature by measuring its statistical
dependency with the target variable. This helps identify relevant features for model training and
detect potential redundant or irrelevant variables, supporting feature selection decisions and model
interpretability.

### Test Mechanism

The test employs sklearn's mutual_info_classif/mutual_info_regression functions to compute mutual
information between each feature and the target. It produces a normalized score (0 to 1) for each
feature, where higher scores indicate stronger relationships. Results are presented in both tabular
format and visualized through a bar plot with a configurable threshold line.

### Signs of High Risk

- Many features showing very low mutual information scores
- Key business features exhibiting unexpectedly low scores
- All features showing similar, low information content
- Large discrepancy between business importance and MI scores
- Highly skewed distribution of MI scores
- Critical features below the minimum threshold
- Unexpected zero or near-zero scores for known important features
- Inconsistent scores across different data samples

### Strengths

- Captures non-linear relationships between features and target
- Scale-invariant measurement of feature relevance
- Works for both classification and regression tasks
- Provides interpretable scores (0 to 1 scale)
- Supports automated feature selection
- No assumptions about data distribution
- Handles numerical and categorical features
- Computationally efficient for most datasets

### Limitations

- Requires sufficient data for reliable estimates
- May be computationally intensive for very large datasets
- Cannot detect redundant features (pairwise relationships)
- Sensitive to feature discretization for continuous variables
- Does not account for feature interactions
- May underestimate importance of rare but crucial events
- Cannot handle missing values directly
- May be affected by extreme class imbalance