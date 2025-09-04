# ViolinPlot

Generates interactive violin plots for numerical features using Plotly.

### Purpose

This test creates violin plots to visualize the distribution of numerical features,
showing both the probability density and summary statistics. Violin plots combine
aspects of box plots and kernel density estimation for rich distribution visualization.

### Test Mechanism

The test creates violin plots for specified numerical columns, with optional
grouping by categorical variables. Each violin shows the distribution shape,
quartiles, and median values.

### Signs of High Risk

- Multimodal distributions that might indicate mixed populations
- Highly skewed distributions suggesting data quality issues
- Large differences in distribution shapes across groups
- Unusual distribution patterns that contradict domain expectations

### Strengths

- Shows detailed distribution shape information
- Interactive Plotly visualization with hover details
- Effective for comparing distributions across groups
- Combines density estimation with quartile information

### Limitations

- Limited to numerical features only
- Requires sufficient data points for meaningful density estimation
- May not be suitable for discrete variables
- Can be misleading with very small sample sizes