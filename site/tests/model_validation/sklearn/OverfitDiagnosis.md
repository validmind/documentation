# OverfitDiagnosis

Identify overfit regions in a model's predictions.

This test compares the model's performance on training versus test data, grouped by
feature columns. It calculates the difference between the training and test performance
for each group and identifies regions where the difference exceeds a specified threshold.

This test works for both classification and regression models and with a variety of
performance metrics. By default, it uses the AUC metric for classification models and
the MSE metric for regression models. The threshold for identifying overfit regions
defaults to 0.04 but should be adjusted based on the specific use case.

## Inputs
- `model` (VMModel): The ValidMind model object to evaluate.
- `datasets` (List[VMDataset]): A list of two VMDataset objects where the first dataset
is the training data and the second dataset is the test data.

## Parameters
- `metric` (str, optional): The performance metric to use for evaluation. Choose from:
accuracy', 'auc', 'f1', 'precision', 'recall', 'mse', 'mae', 'r2', 'mape'.
Defaults to 'auc' for classification models and 'mse' for regression models.
- `cut_off_threshold` (float, optional): The threshold for identifying overfit regions.
Defaults to 0.04.