# BivariateScatterPlots

Generates bivariate scatterplots to visually inspect relationships between pairs of numerical predictor variables
in machine learning classification tasks.

### Purpose

This function is intended for visual inspection and monitoring of relationships between pairs of numerical
variables in a machine learning model targeting classification tasks. It helps in understanding how predictor
variables (features) interact with each other, which can inform feature selection, model-building strategies, and
identify potential biases or irregularities in the data.

### Test Mechanism

The function creates scatter plots for each pair of numerical features in the dataset. It first filters out
non-numerical and binary features, ensuring the plots focus on meaningful numerical relationships. The resulting
scatterplots are color-coded uniformly to avoid visual distraction, and the function returns a tuple of Plotly
figure objects, each representing a scatter plot for a pair of features.

### Signs of High Risk

- Visual patterns suggesting non-linear relationships, multicollinearity, clustering, or outlier points in the
scatter plots.
- Such issues could affect the assumptions and performance of certain models, especially those assuming linearity,
like logistic regression.

### Strengths

- Scatterplots provide an intuitive and visual tool to explore relationships between two variables.
- They are useful for identifying outliers, variable associations, and trends, including non-linear patterns.
- Supports visualization of binary or multi-class classification datasets, focusing on numerical features.

### Limitations

- Scatterplots are limited to bivariate analysis, showing relationships between only two variables at a time.
- Not ideal for very large datasets where overlapping points can reduce the clarity of the visualization.
- Scatterplots are exploratory tools and do not provide quantitative measures of model quality or performance.
- Interpretation is subjective and relies on the domain knowledge and judgment of the viewer.