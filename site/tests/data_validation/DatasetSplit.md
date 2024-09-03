# DatasetSplit

Evaluates and visualizes the distribution proportions among training, testing, and validation datasets of an ML
model.

### Purpose

The DatasetSplit test is designed to evaluate and visualize the distribution of data among training, testing, and
validation datasets, if available, within a given machine learning model. The main purpose is to assess whether the
model's datasets are split appropriately, as an imbalanced split might affect the model's ability to learn from the
data and generalize to unseen data.

### Test Mechanism

The DatasetSplit test first calculates the total size of all available datasets in the model. Then, for each
individual dataset, the methodology involves determining the size of the dataset and its proportion relative to the
total size. The results are then conveniently summarized in a table that shows dataset names, sizes, and
proportions. Absolute size and proportion of the total dataset size are displayed for each individual dataset.

### Signs of High Risk

- A very small training dataset, which may result in the model not learning enough from the data.
- A very large training dataset and a small test dataset, which may lead to model overfitting and poor
generalization to unseen data.
- A small or non-existent validation dataset, which might complicate the model's performance assessment.

### Strengths

- The DatasetSplit test provides a clear, understandable visualization of dataset split proportions, which can
highlight any potential imbalance in dataset splits quickly.
- It covers a wide range of task types including classification, regression, and text-related tasks.
- The metric is not tied to any specific data type and is applicable to tabular data, time series data, or text
data.

### Limitations

- The DatasetSplit test does not provide any insight into the quality or diversity of the data within each split,
just the size and proportion.
- The test does not give any recommendations or adjustments for imbalanced datasets.
- Potential lack of compatibility with more complex modes of data splitting (for example, stratified or time-based
splits) could limit the applicability of this test.