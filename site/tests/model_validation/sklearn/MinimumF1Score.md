# MinimumF1Score

Evaluates if the model's F1 score on the validation set meets a predefined minimum threshold.

**Purpose:**
The main objective of this test is to ensure that the F1 score, a balanced measure of precision and recall, of the
model meets or surpasses a predefined threshold on the validation dataset. The F1 score is highly useful for
gauging model performance in classification tasks, especially in cases where the distribution of positive and
negative classes is skewed.

**Test Mechanism:**
The F1 score for the validation dataset is computed through the scikit-learn's metrics in Python. The scoring
mechanism differs based on the classification problem: for multi-class problems, macro averaging is used (metrics
are calculated separately and their unweighted mean is found), and for binary classification, the built-in f1_score
calculation is used. The obtained F1 score is then assessed against the predefined minimum F1 score that is
expected from the model.

**Signs of High Risk:**

- If a model returns an F1 score that is less than the established threshold, it is regarded as high risk.
- A low F1 score might suggest that the model is not finding an optimal balance between precision and recall, see:
it isn't successfully identifying positive classes while minimizing false positives.

**Strengths:**

- This metric gives a balanced measure of a model's performance by accounting for both false positives and false
negatives.
- It has a particular advantage in scenarios with imbalanced class distribution, where an accuracy measure can be
misleading.
- The flexibility of setting the threshold value allows for tailoring the minimum acceptable performance.

**Limitations:**

- The testing method may not be suitable for all types of models and machine learning tasks.
- Although the F1 score gives a balanced view of a model's performance, it presupposes an equal cost for false
positives and false negatives, which may not always be true in certain real-world scenarios. As a consequence,
practitioners might have to rely on other metrics such as precision, recall, or the ROC-AUC score that align more
closely with their specific requirements.