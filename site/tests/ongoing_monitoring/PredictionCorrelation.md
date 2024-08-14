# PredictionCorrelation

**Purpose:**
The test is used to assess the correlation pairs for each feature between model predictions from reference and
monitoring datasets. The primary goal is to detect significant changes in these pairs, which may signal target
drift, leading to lower model performance.

**Test Mechanism:**
The test calculates the correlation of each feature with model predictions for both reference and monitoring
datasets. The test then compares these correlations side-by-side via a bar plot and a correlation table. Features
with significant changes in correlation pairs highlight potential risks of model drift.

**Signs of High Risk:**
- Significant changes in correlation pairs between the reference and monitoring predictions.
- Notable correlation differences indicating a potential shift in the relationship between features and the target
variable.

**Strengths:**
- Allows for visual identification of drift in feature relationships with model predictions.
- Comparison via a clear bar plot assists in understanding model stability over time.
- Helps in early detection of target drift, enabling timely interventions.

**Limitations:**
- May require substantial reference and monitoring data for accurate comparison.
- Correlation does not imply causation, and other factors might influence changes.
- The method solely focuses on linear relationships, potentially missing non-linear interactions.