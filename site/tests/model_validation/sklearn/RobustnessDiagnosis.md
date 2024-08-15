# RobustnessDiagnosis

Evaluate the robustness of a machine learning model to noise

Robustness refers to a model's ability to maintain a high level of performance in
the face of perturbations or changes (particularly noise) added to its input data.
This test is designed to help gauge how well the model can handle potential real-
world scenarios where the input data might be incomplete or corrupted.

## Test Methodology
This test is conducted by adding Gaussian noise, proportional to a particular standard
deviation scale, to numeric input features of the input datasets. The model's
performance on the perturbed data is then evaluated using a user-defined metric or the
default metric of AUC for classification tasks and MSE for regression tasks. The results
are then plotted to visualize the model's performance decay as the perturbation size
increases.

When using this test, it is highly recommended to tailor the performance metric, list
of scaling factors for the standard deviation of the noise, and the performance decay
threshold to the specific use case of the model being evaluated.

**Inputs**:
- model (VMModel): The trained model to be evaluated.
- datasets (List[VMDataset]): A list of datasets to evaluate the model against.

## Parameters
- metric (str, optional): The performance metric to be used for evaluation. If not
provided, the default metric is used based on the task of the model. Default values
are "auc" for classification tasks and "mse" for regression tasks.
- scaling_factor_std_dev_list (List[float], optional): A list of scaling factors for
the standard deviation of the noise to be added to the input features. The default
values are [0.1, 0.2, 0.3, 0.4, 0.5].
- performance_decay_threshold (float, optional): The threshold for the performance
decay of the model. The default value is 0.05.