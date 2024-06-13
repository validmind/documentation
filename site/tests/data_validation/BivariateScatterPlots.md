# BivariateScatterPlots

Generates bivariate scatterplots to visually inspect relationships between pairs of predictor variables in machine
learning classification tasks.

**Purpose**: This metric is intended for visual inspection and monitoring of relationships between pairs of
variables in a machine learning model targeting classification tasks. It is especially useful for understanding how
predictor variables (features) behave in relation to each other and how they are distributed for different classes
of the target variable, which could inform feature selection, model-building strategies, and even alert to possible
biases and irregularities in the data.

**Test Mechanism**: This metric operates by creating a scatter plot for each pair of the selected features in the
dataset. If the parameters "selected_columns" are not specified, an error will be thrown. The metric offers
flexibility by allowing the user to filter on a specific target class - specified by the "target_filter" parameter
- for more granified insights. Each scatterplot is then color-coded based on the category of the target variable
for better visual differentiation. The seaborn scatterplot library is used for generating the plots.

**Signs of High Risk**:
- Visual patterns which might suggest non-linear relationships, substantial skewness, multicollinearity,
clustering, or isolated outlier points in the scatter plot.
- Such issues could affect the assumptions and performance of some models, especially the ones assuming linearity
like linear regression or logistic regression.

**Strengths**:
- Scatterplots are simple and intuitive for users to understand, providing a visual tool to pinpoint complex
relationships between two variables.
- They are useful for outlier detection, identification of variable associations and trends, including non-linear
patterns which can be overlooked by other linear-focused metrics or tests.
- The implementation also supports visualizing binary or multi-class classification datasets.

**Limitations**:
- Scatterplots are limited to bivariate analysis - the relationship of two variables at a time - and might not
reveal the full picture in higher dimensions or where interactions are present.
- They are not ideal for very large datasets as points will overlap and render the visualization less informative.
- Scatterplots are more of an exploratory tool rather than a formal statistical test, so they don't provide any
quantitative measure of model quality or performance.
- Interpretation of scatterplots relies heavily on the domain knowledge and judgment of the viewer, which can
introduce subjective bias.