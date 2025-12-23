# CumulativePredictionProbabilities

Visualizes cumulative probabilities of positive and negative classes in classification models.

### Purpose

This metric is utilized to evaluate the distribution of predicted probabilities for positive and negative classes
in a classification model. It provides a visual assessment of the model's behavior by plotting the cumulative
probabilities for positive and negative classes within the provided dataset.

### Test Mechanism

The classification model is evaluated by first computing the predicted probabilities for each instance in the
dataset, which are then added as a new column. The cumulative probabilities for positive and negative classes are
subsequently calculated and sorted in ascending order. Cumulative distributions of these probabilities are created
for both positive and negative classes. These cumulative probabilities are represented visually in a plot with lines
representing cumulative distributions of positive and negative classes.

### Signs of High Risk

- Imbalanced distribution of probabilities for either positive or negative classes.
- Marked discrepancies or large differences between the cumulative probability distributions for positive and
negative classes.
- Unusual patterns in the cumulative probability distributions that may indicate model calibration issues.

### Strengths

- Provides a visual illustration of data, which enhances the ease of understanding and interpreting the model's
behavior.
- Differentiates between positive and negative classes and their respective distribution patterns, aiding in
problem diagnosis.
- Helps identify potential calibration issues by visualizing how probabilities are distributed across classes.

### Limitations

- Exclusive to classification tasks and specifically to classification models.
- Graphical results necessitate human interpretation and may not be directly applicable for automated risk
detection.
- The method does not give a solitary quantifiable measure of model risk, instead, it offers a visual
representation and broad distributional information.
- If the dataset is not representative of the overall data distribution, the metric could provide misleading results.