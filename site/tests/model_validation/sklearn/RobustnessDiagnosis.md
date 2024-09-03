# RobustnessDiagnosis

Assesses the robustness of a machine learning model by evaluating performance decay under noisy conditions.

### Purpose

The Robustness Diagnosis test aims to evaluate the resilience of a machine learning model when subjected to
perturbations or noise in its input data. This is essential for understanding the model's ability to handle
real-world scenarios where data may be imperfect or corrupted.

### Test Mechanism

This test introduces Gaussian noise to the numeric input features of the datasets at varying scales of standard
deviation. The performance of the model is then measured using a specified metric. The process includes:

- Adding Gaussian noise to numerical input features based on scaling factors.
- Evaluating the model's performance on the perturbed data using metrics like AUC for classification tasks and MSE
for regression tasks.
- Aggregating and plotting the results to visualize performance decay relative to perturbation size.

### Signs of High Risk

- A significant drop in performance metrics with minimal noise.
- Performance decay values exceeding the specified threshold.
- Consistent failure to meet performance standards across multiple perturbation scales.

### Strengths

- Provides insights into the model's robustness against noisy or corrupted data.
- Utilizes a variety of performance metrics suitable for both classification and regression tasks.
- Visualization helps in understanding the extent of performance degradation.

### Limitations

- Gaussian noise might not adequately represent all types of real-world data perturbations.
- Performance thresholds are somewhat arbitrary and might need tuning.
- The test may not account for more complex or unstructured noise patterns that could affect model robustness.