# TargetRateBarPlots

Generates bar plots visualizing the default rates of categorical features for a classification machine learning
model.

### Purpose

This test, implemented as a metric, is designed to provide an intuitive, graphical summary of the decision-making
patterns exhibited by a categorical classification machine learning model. The model's performance is evaluated
using bar plots depicting the ratio of target rates—meaning the proportion of positive classes—for different
categorical inputs. This allows for an easy, at-a-glance understanding of the model's accuracy.

### Test Mechanism

The test involves creating a pair of bar plots for each categorical feature in the dataset. The first plot depicts
the frequency of each category in the dataset, with each category visually distinguished by its unique color. The
second plot shows the mean target rate of each category (sourced from the "default_column"). Plotly, a Python
library, is used to generate these plots, with distinct plots created for each feature. If no specific columns are
selected, the test will generate plots for each categorical column in the dataset.

### Signs of High Risk

- Inconsistent or non-binary values in the "default_column" could complicate or render impossible the calculation
of average target rates.
- Particularly low or high target rates for a specific category might suggest that the model is misclassifying
instances of that category.

### Strengths

- This test offers a visually interpretable breakdown of the model's decisions, providing an easy way to spot
irregularities, inconsistencies, or patterns.
- Its flexibility allows for the inspection of one or multiple columns, as needed.

### Limitations

- The test is less useful when dealing with numeric or continuous data, as it's designed specifically for
categorical features.
- If the model in question is dealing with a multi-class problem rather than binary classification, the test's
assumption of binary target values (0s and 1s) becomes a significant limitation.
- The readability of the bar plots drops as the number of distinct categories increases in the dataset, which can
make them harder to understand and less useful.