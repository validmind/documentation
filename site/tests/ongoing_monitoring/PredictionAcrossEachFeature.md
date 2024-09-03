# PredictionAcrossEachFeature

Assesses differences in model predictions across individual features between reference and monitoring datasets
through visual analysis.

### Purpose

The Prediction Across Each Feature test aims to visually compare model predictions for each feature between
reference (training) and monitoring (production) datasets. It helps identify significant differences in prediction
patterns for further investigation and ensures the model's consistency and stability over time.

### Test Mechanism

The test generates scatter plots for each feature, comparing prediction probabilities between the reference and
monitoring datasets. Each plot consists of two subplots: one for reference data and one for monitoring data,
enabling visual comparison of the model's predictive behavior.

### Signs of High Risk

- Significant discrepancies between the reference and monitoring subplots for the same feature.
- Unexpected patterns or trends in monitoring data that were absent in reference data.

### Strengths

- Provides a clear visual representation of model performance across different features.
- Facilitates easy identification of features where the model's predictions have diverged.
- Enables quick detection of potential model performance issues in production.

### Limitations

- Interpretation of scatter plots can be subjective and may require expertise.
- Visualizations do not provide quantitative metrics for objective evaluation.
- May not capture all types of distribution changes or issues with the model's predictions.