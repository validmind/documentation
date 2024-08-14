# RobustnessDiagnosis

Evaluates the robustness of a machine learning model by injecting Gaussian noise to input data and measuring
performance.

**Purpose**:

The purpose of this test code is to evaluate the robustness of a machine learning model. Robustness refers to a
model's ability to maintain a high level of performance in the face of perturbations or changes—particularly
noise—added to its input data. This test is designed to help gauge how well the model can handle potential
real-world scenarios where the input data might be incomplete or corrupted.

**Test Mechanism**:

This test is conducted by adding Gaussian noise, proportional to a particular standard deviation scale, to numeric
input features of both the training and testing datasets. The model performance in the face of these perturbed
features is then evaluated using the ROC_AUC score. This process is iterated over a range of scale
factors. The resulting auc trend against the amount of noise introduced is illustrated with a line chart. A
predetermined threshold determines what level of auc decay due to perturbation is considered acceptable.

**Signs of High Risk**:
- Substantial decreases in auc when noise is introduced to feature inputs.
- The decay in auc surpasses the configured threshold, indicating that the model is not robust against input
noise.
- Instances where one or more elements provided in the features list don't match with the training dataset's
numerical feature columns.

**Strengths**:
- Provides an empirical measure of the model's performance in tackling noise or data perturbations, revealing
insights into the model's stability.
- Offers flexibility with the ability to choose specific features to perturb and control the level of noise applied.
- Detailed results visualization helps in interpreting the outcome of robustness testing.

**Limitations**:
- The default threshold for auc decay is set to 0.05, which is unlikely to be optimal for most use cases and
should be adjusted based on domain expertise to suit the needs of the specific model.
- Only numerical features are perturbed, leaving out non-numerical features, which can lead to an incomplete
analysis of robustness.
- The test is contingent on the assumption that the added Gaussian noise sufficiently represents potential data
corruption or incompleteness in real-world scenarios.