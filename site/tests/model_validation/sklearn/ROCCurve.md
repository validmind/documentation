# ROCCurve

Evaluates binary classification model performance by generating and plotting the Receiver Operating Characteristic
(ROC) curve and calculating the Area Under Curve (AUC) score.

### Purpose

The Receiver Operating Characteristic (ROC) curve is designed to evaluate the performance of binary classification
models. This curve illustrates the balance between the True Positive Rate (TPR) and False Positive Rate (FPR)
across various threshold levels. In combination with the Area Under the Curve (AUC), the ROC curve aims to measure
the model's discrimination ability between the two defined classes in a binary classification problem (e.g.,
default vs non-default). Ideally, a higher AUC score signifies superior model performance in accurately
distinguishing between the positive and negative classes.

### Test Mechanism

First, this script selects the target model and datasets that require binary classification. It then calculates the
predicted probabilities for the test set, and uses this data, along with the true outcomes, to generate and plot
the ROC curve. Additionally, it includes a line signifying randomness (AUC of 0.5). The AUC score for the model's
ROC curve is also computed, presenting a numerical estimation of the model's performance. If any Infinite values
are detected in the ROC threshold, these are effectively eliminated. The resulting ROC curve, AUC score, and
thresholds are consequently saved for future reference.

### Signs of High Risk

- A high risk is potentially linked to the model's performance if the AUC score drops below or nears 0.5.
- Another warning sign would be the ROC curve lying closer to the line of randomness, indicating no discriminative
ability.
- For the model to be deemed competent at its classification tasks, it is crucial that the AUC score is
significantly above 0.5.

### Strengths

- The ROC Curve offers an inclusive visual depiction of a model's discriminative power throughout all conceivable
classification thresholds, unlike other metrics that solely disclose model performance at one fixed threshold.
- Despite the proportions of the dataset, the AUC Score, which represents the entire ROC curve as a single data
point, continues to be consistent, proving to be the ideal choice for such situations.

### Limitations

- The primary limitation is that this test is exclusively structured for binary classification tasks, thus limiting
its application towards other model types.
- Furthermore, its performance might be subpar with models that output probabilities highly skewed towards 0 or 1.
- At the extreme, the ROC curve could reflect high performance even when the majority of classifications are
incorrect, provided that the model's ranking format is retained. This phenomenon is commonly termed the "Class
Imbalance Problem".