# CorrelationAnalysis

Performs comprehensive correlation analysis with significance testing for numerical features.

### Purpose

This test conducts detailed correlation analysis between numerical features, including
correlation coefficients, significance testing, and identification of significant
relationships. It helps identify multicollinearity, feature relationships, and
potential redundancies in the dataset.

### Test Mechanism

The test computes correlation coefficients using the specified method and performs
statistical significance testing for each correlation pair. It provides:
- Correlation matrix with significance indicators
- List of significant correlations above threshold
- Summary statistics about correlation patterns
- Identification of highly correlated feature pairs

### Signs of High Risk

- Very high correlations (>0.9) indicating potential multicollinearity
- Many significant correlations suggesting complex feature interactions
- Features with no significant correlations to others (potential isolation)
- Unexpected correlation patterns contradicting domain knowledge

### Strengths

- Provides statistical significance testing for correlations
- Supports multiple correlation methods (Pearson, Spearman, Kendall)
- Identifies potentially problematic high correlations
- Filters results by minimum correlation threshold
- Comprehensive summary of correlation patterns

### Limitations

- Limited to numerical features only
- Cannot detect non-linear relationships (except with Spearman)
- Significance testing assumes certain distributional properties
- Correlation does not imply causation