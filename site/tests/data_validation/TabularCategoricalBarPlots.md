# tests\data_validation\TabularCategoricalBarPlots

Generates and visualizes bar plots for each category in categorical features to evaluate dataset's composition.

**Purpose**: The purpose of this metric is to visually analyze categorical data using bar plots. It is intended to
evaluate the dataset's composition by displaying the counts of each category in each categorical feature.

**Test Mechanism**: The provided dataset is first checked to determine if it contains any categorical variables. If
no categorical columns are found, the tool raises a ValueError. For each categorical variable in the dataset, a
separate bar plot is generated. The number of occurrences for each category is calculated and displayed on the
plot. If a dataset contains multiple categorical columns, multiple bar plots are produced.

**Signs of High Risk**:

- High risk could occur if the categorical variables exhibit an extreme imbalance, with categories having very few
instances possibly being underrepresented in the model, which could affect the model's performance and its ability
to generalize.
- Another sign of risk is if there are too many categories in a single variable, which could lead to overfitting
and make the model complex.

**Strengths**: This metric provides a visual and intuitively understandable representation of categorical data,
which aids in the analysis of variable distributions. By presenting model inputs in this way, we can easily
identify imbalances or rare categories that could affect the model's performance.

**Limitations**:

- This method only works with categorical data, meaning it won't apply to numerical variables.
- In addition, the method does not provide any informative value when there are too many categories, as the bar
chart could become cluttered and hard to interpret.
- It offers no insights into the model's performance or precision, but rather provides a descriptive analysis of
the input.