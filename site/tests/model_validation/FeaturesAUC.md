# FeaturesAUC

Evaluates the discriminatory power of each individual feature within a binary classification model by calculating
the Area Under the Curve (AUC) for each feature separately.

### Purpose

The central objective of this metric is to quantify how well each feature on its own can differentiate between the
two classes in a binary classification problem. It serves as a univariate analysis tool that can help in
pre-modeling feature selection or post-modeling interpretation.

### Test Mechanism

For each feature, the metric treats the feature values as raw scores to compute the AUC against the actual binary
outcomes. It provides an AUC value for each feature, offering a simple yet powerful indication of each feature's
univariate classification strength.

### Signs of High Risk

- A feature with a low AUC score may not be contributing significantly to the differentiation between the two
classes, which could be a concern if it is expected to be predictive.
- Conversely, a surprisingly high AUC for a feature not believed to be informative may suggest data leakage or
other issues with the data.

### Strengths

- By isolating each feature, it highlights the individual contribution of features to the classification task
without the influence of other variables.
- Useful for both initial feature evaluation and for providing insights into the model's reliance on individual
features after model training.

### Limitations

- Does not reflect the combined effects of features or any interaction between them, which can be critical in
certain models.
- The AUC values are calculated without considering the model's use of the features, which could lead to different
interpretations of feature importance when considering the model holistically.
- This metric is applicable only to binary classification tasks and cannot be directly extended to multiclass
classification or regression without modifications.