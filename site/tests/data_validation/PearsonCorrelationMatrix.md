# PearsonCorrelationMatrix

Evaluates linear dependency between numerical variables in a dataset via a Pearson Correlation coefficient heat map.

### Purpose

This test is intended to evaluate the extent of linear dependency between all pairs of numerical variables in the
given dataset. It provides the Pearson Correlation coefficient, which reveals any high correlations present. The
purpose of doing this is to identify potential redundancy, as variables that are highly correlated can often be
removed to reduce the dimensionality of the dataset without significantly impacting the model's performance.

### Test Mechanism

This metric test generates a correlation matrix for all numerical variables in the dataset using the Pearson
correlation formula. A heat map is subsequently created to visualize this matrix effectively. The color of each
point on the heat map corresponds to the magnitude and direction (positive or negative) of the correlation, with a
range from -1 (perfect negative correlation) to 1 (perfect positive correlation). Any correlation coefficients
higher than 0.7 (in absolute terms) are indicated in white in the heat map, suggesting a high degree of correlation.

### Signs of High Risk

- A large number of variables in the dataset showing a high degree of correlation (coefficients approaching ±1).
This indicates redundancy within the dataset, suggesting that some variables may not be contributing new
information to the model.
- Potential risk of overfitting.

### Strengths

- Detects and quantifies the linearity of relationships between variables, aiding in identifying redundant
variables to simplify models and potentially improve performance.
- The heatmap visualization provides an easy-to-understand overview of correlations, beneficial for users not
comfortable with numerical matrices.

### Limitations

- Limited to detecting linear relationships, potentially missing non-linear relationships which impede
opportunities for dimensionality reduction.
- Measures only the degree of linear relationship, not the strength of one variable's effect on another.
- The 0.7 correlation threshold is arbitrary and might exclude valid dependencies with lower coefficients.