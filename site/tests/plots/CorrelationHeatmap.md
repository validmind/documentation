# CorrelationHeatmap

Generates customizable correlation heatmap plots for numerical features in a dataset using Plotly.

### Purpose

This test provides a flexible way to visualize correlations between numerical features
in a dataset using interactive Plotly heatmaps. It supports different correlation methods
and extensive customization options for the heatmap appearance, making it suitable for
exploring feature relationships in data analysis.

### Test Mechanism

The test computes correlation coefficients between specified numerical columns
(or all numerical columns if none specified) using the specified method.
It then creates an interactive heatmap visualization with customizable appearance options including:
- Different correlation methods (pearson, spearman, kendall)
- Color schemes and annotations
- Masking options for upper triangle
- Threshold filtering for significant correlations
- Interactive hover information

### Signs of High Risk

- Very high correlations (>0.9) between features indicating multicollinearity
- Unexpected correlation patterns that contradict domain knowledge
- Features with no correlation to any other variables
- Strong correlations with the target variable that might indicate data leakage

### Strengths

- Supports multiple correlation methods
- Interactive Plotly plots with hover information and zoom capabilities
- Highly customizable visualization options
- Can handle missing values appropriately
- Provides clear visual representation of feature relationships
- Optional thresholding to focus on significant correlations

### Limitations

- Limited to numerical features only
- Cannot capture non-linear relationships effectively
- May be difficult to interpret with many features
- Correlation does not imply causation