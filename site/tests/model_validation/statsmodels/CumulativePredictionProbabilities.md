# CumulativePredictionProbabilities

Visualizes cumulative probabilities of positive and negative classes for both training and testing in logistic
regression models.

### Purpose

This metric is utilized to evaluate the distribution of predicted probabilities for positive and negative classes
in a logistic regression model. It provides a visual assessment of the model's behavior by plotting the cumulative
probabilities for positive and negative classes across both the training and test datasets.

### Test Mechanism

The logistic regression model is evaluated by first computing the predicted probabilities for each instance in both
the training and test datasets, which are then added as a new column in these sets. The cumulative probabilities
for positive and negative classes are subsequently calculated and sorted in ascending order. Cumulative
distributions of these probabilities are created for both positive and negative classes across both training and
test datasets. These cumulative probabilities are represented visually in a plot, containing two subplots - one for
the training data and the other for the test data, with lines representing cumulative distributions of positive and
negative classes.

### Signs of High Risk

- Imbalanced distribution of probabilities for either positive or negative classes.
- Notable discrepancies or significant differences between the cumulative probability distributions for the
training data versus the test data.
- Marked discrepancies or large differences between the cumulative probability distributions for positive and
negative classes.

### Strengths

- Provides a visual illustration of data, which enhances the ease of understanding and interpreting the model's
behavior.
- Allows for the comparison of model's behavior across training and testing datasets, providing insights about how
well the model is generalized.
- Differentiates between positive and negative classes and their respective distribution patterns, aiding in
problem diagnosis.

### Limitations

- Exclusive to classification tasks and specifically to logistic regression models.
- Graphical results necessitate human interpretation and may not be directly applicable for automated risk
detection.
- The method does not give a solitary quantifiable measure of model risk, instead, it offers a visual
representation and broad distributional information.
- If the training and test datasets are not representative of the overall data distribution, the metric could
provide misleading results.