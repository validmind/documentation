# StabilityAnalysisKeyword

Evaluates robustness of embedding models to keyword swaps in the test dataset.

### Purpose

This test metric is used to evaluate the robustness of text embedding machine learning models to keyword swaps. A
keyword swap is a scenario where instances of certain specified keywords in the dataset are replaced with other
specified words (usually synonyms). The purpose of this metric is to ensure that these models maintain performance
stability even when the input data slightly deviates, imitating real-world variability.

### Test Mechanism

The test mechanism involves a perturbation of the dataset used in testing the model. Each instance of a specific
word found in the dataset is replaced with the corresponding word as specified in a 'keyword_dict' mapping. The
model is then re-run with the perturbed dataset and the results are compared with the non-perturbed dataset. This
comparison quantifies the extent to which keyword swaps impact the model's performance.

### Signs of High Risk

- A significant drop in model performance after keyword swaps indicates a high risk of model failure in real-world
scenarios.
- The model results being heavily reliant on specific word choices instead of capturing the context properly.

### Strengths

- This test provides a way to measure model robustness to small changes in input data, which reinforces its
applicability and reliability in real-world scenarios.
- This test encourages a model to understand the context of a sentence rather than memorizing specific words.
- It helps to detect overfitting - a situation where a model performs well on training data but poorly on new or
slightly altered data.

### Limitations

- It may not fully address semantic differences that can be introduced through keyword swaps. That is, the
replacement words might not preserve the exact semantic meaning of the original words.
- It only tests for changes in keywords (word-level alterations) and might not expose model limitations related to
structural data changes.
- It assumes that the provided 'keyword_dict' is an accurate representation of possible real-world variations,
which might not always be the case.