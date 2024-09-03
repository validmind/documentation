# PredictionCorrelation

Assesses correlation changes between model predictions from reference and monitoring datasets to detect potential
target drift.

### Purpose

To evaluate the changes in correlation pairs between model predictions and features from reference and monitoring
datasets. This helps in identifying significant shifts that may indicate target drift, potentially affecting model
performance.

### Test Mechanism

This test calculates the correlation of each feature with model predictions for both reference and monitoring
datasets. It then compares these correlations side-by-side using a bar plot and a correlation table. Significant
changes in correlation pairs are highlighted to signal possible model drift.

### Signs of High Risk

- Significant changes in correlation pairs between the reference and monitoring predictions.
- Notable differences in correlation values, indicating a possible shift in the relationship between features and
the target variable.

### Strengths

- Provides visual identification of drift in feature relationships with model predictions.
- Clear bar plot comparison aids in understanding model stability over time.
- Enables early detection of target drift, facilitating timely interventions.

### Limitations

- Requires substantial reference and monitoring data for accurate comparison.
- Correlation does not imply causation; other factors may influence changes.
- Focuses solely on linear relationships, potentially missing non-linear interactions.