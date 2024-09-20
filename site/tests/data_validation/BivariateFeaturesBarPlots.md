# BivariateFeaturesBarPlots

Generates visual bar plots to analyze the relationship between paired features within categorical data in the model.

**Purpose**: The BivariateFeaturesBarPlots metric is intended to perform a visual analysis of categorical data
within the model. The goal is to assess and understand the specific relationships between various feature pairs,
while simultaneously highlighting the model's target variable. This form of bivariate plotting is immensely
beneficial in uncovering trends, correlations, patterns, or inconsistencies that may not be readily apparent within
raw tabular data.

**Test Mechanism**: These tests establish bar plots for each pair of features defined within the parameters. The
dataset is grouped by each feature pair and then calculates the mean of the target variable within each specific
grouping. Each group is represented via a bar in the plot, and the height of this bar aligns with the calculated
mean. The colors assigned to these bars are based on the categorical section to which they pertain: these colors
can either come from a colormap or generated anew if the total number of categories exceeds the current colormap's
scope.

**Signs of High Risk**:
- If any values are found missing or inconsistent within the feature pairs.
- If there exist large discrepancies or irregularities between the mean values of certain categories within feature
pairs.
- If the parameters for feature pairs have not been specified or if they were wrongly defined.

**Strengths**:
- The BivariateFeaturesBarPlots provides a clear, visual comprehension of the relationships between feature pairs
and the target variable.
- It allows an easy comparison between different categories within feature pairs.
- The metric can handle a diverse array of categorical data, enhancing its universal applicability.
- It is highly customizable due to its allowance for users to define feature pairs based on their specific
requirements.

**Limitations**:
- It can only be used with categorical data, limiting its usability with numerical or textual data.
- It relies on manual input for feature pairs, which could result in the overlooking of important feature pairs if
not chosen judiciously.
- The generated bar plots could become overly cluttered and difficult to decipher when dealing with feature pairs
with a large number of categories.
- This metric only provides a visual evaluation and fails to offer any numerical or statistical measures to
quantify the relationship between feature pairs.