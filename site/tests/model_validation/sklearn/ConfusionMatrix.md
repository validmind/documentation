# ConfusionMatrix

Evaluates and visually represents the classification ML model's predictive performance using a Confusion Matrix
heatmap.

### Purpose

The Confusion Matrix tester is designed to assess the performance of a classification Machine Learning model. This
performance is evaluated based on how well the model is able to correctly classify True Positives, True Negatives,
False Positives, and False Negatives - fundamental aspects of model accuracy.

### Test Mechanism

The mechanism used involves taking the predicted results (`y_test_predict`) from the classification model and
comparing them against the actual values (`y_test_true`). A confusion matrix is built using the unique labels
extracted from `y_test_true`, employing scikit-learn's metrics. The matrix is then visually rendered with the help
of Plotly's `create_annotated_heatmap` function. A heatmap is created which provides a two-dimensional graphical
representation of the model's performance, showcasing distributions of True Positives (TP), True Negatives (TN),
False Positives (FP), and False Negatives (FN).

### Signs of High Risk

- High numbers of False Positives (FP) and False Negatives (FN), depicting that the model is not effectively
classifying the values.
- Low numbers of True Positives (TP) and True Negatives (TN), implying that the model is struggling with correctly
identifying class labels.

### Strengths

- It provides a simplified yet comprehensive visual snapshot of the classification model's predictive performance.
- It distinctly brings out True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives
(FN), thus making it easier to focus on potential areas of improvement.
- The matrix is beneficial in dealing with multi-class classification problems as it can provide a simple view of
complex model performances.
- It aids in understanding the different types of errors that the model could potentially make, as it provides
in-depth insights into Type-I and Type-II errors.

### Limitations

- In cases of unbalanced classes, the effectiveness of the confusion matrix might be lessened. It may wrongly
interpret the accuracy of a model that is essentially just predicting the majority class.
- It does not provide a single unified statistic that could evaluate the overall performance of the model.
Different aspects of the model's performance are evaluated separately instead.
- It mainly serves as a descriptive tool and does not offer the capability for statistical hypothesis testing.
- Risks of misinterpretation exist because the matrix doesn't directly provide precision, recall, or F1-score data.
These metrics have to be computed separately.