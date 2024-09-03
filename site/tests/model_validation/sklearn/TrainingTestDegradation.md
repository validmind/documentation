# TrainingTestDegradation

Tests if model performance degradation between training and test datasets exceeds a predefined threshold.

### Purpose

The `TrainingTestDegradation` class serves as a test to verify that the degradation in performance between the
training and test datasets does not exceed a predefined threshold. This test measures the model's ability to
generalize from its training data to unseen test data, assessing key classification metrics such as accuracy,
precision, recall, and f1 score to verify the model's robustness and reliability.

### Test Mechanism

The code applies several predefined metrics, including accuracy, precision, recall, and f1 scores, to the model's
predictions for both the training and test datasets. It calculates the degradation as the difference between the
training score and test score divided by the training score. The test is considered successful if the degradation
for each metric is less than the preset maximum threshold of 10%. The results are summarized in a table showing
each metric's train score, test score, degradation percentage, and pass/fail status.

### Signs of High Risk

- A degradation percentage that exceeds the maximum allowed threshold of 10% for any of the evaluated metrics.
- A high difference or gap between the metric scores on the training and the test datasets.
- The 'Pass/Fail' column displaying 'Fail' for any of the evaluated metrics.

### Strengths

- Provides a quantitative measure of the model's ability to generalize to unseen data, which is key for predicting
its practical real-world performance.
- By evaluating multiple metrics, it takes into account different facets of model performance and enables a more
holistic evaluation.
- The use of a variable predefined threshold allows the flexibility to adjust the acceptability criteria for
different scenarios.

### Limitations

- The test compares raw performance on training and test data but does not factor in the nature of the data. Areas
with less representation in the training set might still perform poorly on unseen data.
- It requires good coverage and balance in the test and training datasets to produce reliable results, which may
not always be available.
- The test is currently only designed for classification tasks.