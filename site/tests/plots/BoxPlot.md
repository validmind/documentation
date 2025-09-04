# BoxPlot

Generates customizable box plots for numerical features in a dataset with optional grouping using Plotly.

### Purpose

This test provides a flexible way to visualize the distribution of numerical features
through interactive box plots, with optional grouping by categorical variables. Box plots are
effective for identifying outliers, comparing distributions across groups, and
understanding the spread and central tendency of the data.

### Test Mechanism

The test creates interactive box plots for specified numerical columns (or all numerical columns
if none specified). It supports various customization options including:
- Grouping by categorical variables
- Customizable colors and styling
- Outlier display options
- Interactive hover information
- Zoom and pan capabilities

### Signs of High Risk

- Presence of many outliers indicating data quality issues
- Highly skewed distributions
- Large differences in variance across groups
- Unexpected patterns in grouped data

### Strengths

- Clear visualization of distribution statistics (median, quartiles, outliers)
- Interactive Plotly plots with hover information and zoom capabilities
- Effective for comparing distributions across groups
- Handles missing values appropriately
- Highly customizable appearance

### Limitations

- Limited to numerical features only
- May not be suitable for continuous variables with many unique values
- Visual interpretation may be subjective
- Less effective with very large datasets