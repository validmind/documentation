# MinimumAccuracy

Checks if the model's prediction accuracy meets or surpasses a specified threshold.

**Purpose**: The Minimum Accuracy test’s objective is to verify whether the model's prediction accuracy on a
specific dataset meets or surpasses a predetermined minimum threshold. Accuracy, which is simply the ratio of right
predictions to total predictions, is a key metric for evaluating the model's performance. Considering binary as
well as multiclass classifications, accurate labeling becomes indispensable.

**Test Mechanism**: The test mechanism involves contrasting the model's accuracy score with a pre-set minimum
threshold value, default value being 0.7. The accuracy score is computed utilizing sklearn’s `accuracy_score`
method, where the true label `y_true` and predicted label `class_pred` are compared. If the accuracy score is above
the threshold, the test gets a passing mark. The test returns the result along with the accuracy score and
threshold used for the test.

**Signs of High Risk**:
- The risk level for this test surges considerably when the model is unable to achieve or surpass the predefined
score threshold.
- When the model persistently scores below the threshold, it suggests a high risk of inaccurate predictions, which
in turn affects the model’s efficiency and reliability.

**Strengths**:
- One of the key strengths of this test is its simplicity, presenting a straightforward measure of the holistic
model performance across all classes.
- This test is particularly advantageous when classes are balanced.
- Another advantage of this test is its versatility as it can be implemented on both binary and multiclass
classification tasks.

**Limitations**:
- When analyzing imbalanced datasets, certain limitations of this test emerge. The accuracy score can be misleading
when classes in the dataset are skewed considerably.
- This can result in favoritism towards the majority class, consequently giving an inaccurate perception of the
model performance.
- Another limitation is its inability to measure the model's precision, recall, or capacity to manage false
positives or false negatives.
- The test majorly focuses on overall correctness and may not be sufficient for all types of model analytics.