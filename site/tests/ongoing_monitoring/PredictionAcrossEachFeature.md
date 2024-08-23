# PredictionAcrossEachFeature

**Purpose:**
This test shows visually the prediction using reference data and monitoring data across each individual feature. If
there are significant differences in predictions across feature values from reference to monitoring dataset, then
further investigation is needed as the model is producing predictions that are different than what was observed
during the training of the model.

**Test Mechanism:**
The test creates scatter plots for each feature, comparing the reference dataset (used for training) with the
monitoring dataset (used in production). Each plot has two subplots: one for the reference data and one for the
monitoring data, visualizing the prediction probabilities. This allows for a visual comparison of the model's
behavior across different datasets.

**Signs of High Risk:**
- Significant discrepancies between the reference and monitoring subplots for the same feature
- Unexpected patterns or trends in monitoring data that weren't present in reference data

**Strengths:**
- Provides a clear visual representation of model performance across different features
- Allows for easy identification of features where the model's predictions have changed
- Facilitates quick detection of potential issues with the model when deployed in production

**Limitations:**
- Interpretation of scatter plots can be subjective and may require expertise
- Visualizations do not provide quantitative metrics for objective evaluation
- May not capture all types of distribution changes or issues with the model's predictions