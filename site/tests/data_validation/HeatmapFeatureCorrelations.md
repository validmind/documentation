# tests\data_validation\HeatmapFeatureCorrelations

Creates a heatmap to visually represent correlation patterns between pairs of numerical features in a dataset.

**Purpose:** The HeatmapFeatureCorrelations metric is utilized to evaluate the degree of interrelationships between
pairs of input features within a dataset. This metric allows us to visually comprehend the correlation patterns
through a heatmap, which can be essential in understanding which features may contribute most significantly to the
performance of the model. Features that have high intercorrelation can potentially reduce the model's ability to
learn, thus impacting the overall performance and stability of the machine learning model.

**Test Mechanism:** The metric executes the correlation test by computing the Pearson correlations for all pairs of
numerical features. It then generates a heatmap plot using seaborn, a Python data visualization library. The
colormap ranges from -1 to 1, indicating perfect negative correlation and perfect positive correlation
respectively. A 'declutter' option is provided which, if set to true, removes variable names and numerical
correlations from the plot to provide a more streamlined view. The size of feature names and correlation
coefficients can be controlled through 'fontsize' parameters.

**Signs of High Risk:**

- Indicators of potential risk include features with high absolute correlation values.
- A significant degree of multicollinearity might lead to instabilities in the trained model and can also result in
overfitting.
- The presence of multiple homogeneous blocks of high positive or negative correlation within the plot might
indicate redundant or irrelevant features included within the dataset.

**Strengths:**

- The strength of this metric lies in its ability to visually represent the extent and direction of correlation
between any two numeric features, which aids in the interpretation and understanding of complex data relationships.
- The heatmap provides an immediate and intuitively understandable representation, hence, it is extremely useful
for high-dimensional datasets where extracting meaningful relationships might be challenging.

**Limitations:**

- The central limitation might be that it can only calculate correlation between numeric features, making it
unsuitable for categorical variables unless they are already numerically encoded in a meaningful manner.
- It uses Pearson's correlation, which only measures linear relationships between features. It may perform poorly
in cases where the relationship is non-linear.
- Large feature sets might result in cluttered and difficult-to-read correlation heatmaps, especially when the
declutter' option is set to false.