# ClassImbalance

Evaluates and quantifies class distribution imbalance in a dataset used by a machine learning model.

### Purpose

The Class Imbalance test is designed to evaluate the distribution of target classes in a dataset that's utilized by
a machine learning model. Specifically, it aims to ensure that the classes aren't overly skewed, which could lead
to bias in the model's predictions. It's crucial to have a balanced training dataset to avoid creating a model
that's biased with high accuracy for the majority class and low accuracy for the minority class.

### Test Mechanism

This Class Imbalance test operates by calculating the frequency (expressed as a percentage) of each class in the
target column of the dataset. It then checks whether each class appears in at least a set minimum percentage of the
total records. This minimum percentage is a modifiable parameter, but the default value is set to 10%.

### Signs of High Risk

- Any class that represents less than the pre-set minimum percentage threshold is marked as high risk, implying a
potential class imbalance.
- The function provides a pass/fail outcome for each class based on this criterion.
- Fundamentally, if any class fails this test, it's highly likely that the dataset possesses imbalanced class
distribution.

### Strengths

- The test can spot under-represented classes that could affect the efficiency of a machine learning model.
- The calculation is straightforward and swift.
- The test is highly informative because it not only spots imbalance, but it also quantifies the degree of
imbalance.
- The adjustable threshold enables flexibility and adaptation to differing use-cases or domain-specific needs.
- The test creates a visually insightful plot showing the classes and their corresponding proportions, enhancing
interpretability and comprehension of the data.

### Limitations

- The test might struggle to perform well or provide vital insights for datasets with a high number of classes. In
such cases, the imbalance could be inevitable due to the inherent class distribution.
- Sensitivity to the threshold value might result in faulty detection of imbalance if the threshold is set
excessively high.
- Regardless of the percentage threshold, it doesn't account for varying costs or impacts of misclassifying
different classes, which might fluctuate based on specific applications or domains.
- While it can identify imbalances in class distribution, it doesn't provide direct methods to address or correct
these imbalances.
- The test is only applicable for classification operations and unsuitable for regression or clustering tasks.