# FeatureDrift

<<<<<<< HEAD
**Purpose**: The Feature Drift test aims to evaluate how much the distribution of features has shifted over time between two
=======
**Purpose**:

The Feature Drift test aims to evaluate how much the distribution of features has shifted over time between two
>>>>>>> 288b4b4d084a2f1df4336824b20d6ef2cebe0ba8
datasets, typically training and monitoring datasets. It uses the Population Stability Index (PSI) to quantify this
change, providing insights into the model's robustness and the necessity for retraining or feature engineering.

**Test Mechanism**:

This test calculates the PSI by:
- Bucketing the distributions of each feature in both datasets.
- Comparing the percentage of observations in each bucket between the two datasets.
- Aggregating the differences across all buckets for each feature to produce the PSI score for that feature.

The PSI score is interpreted as:
- PSI < 0.1: No significant population change.
- PSI < 0.2: Moderate population change.
- PSI >= 0.2: Significant population change.

**Signs of High Risk**:

- PSI >= 0.2 for any feature, indicating a significant distribution shift.
- Consistently high PSI scores across multiple features.
- Sudden spikes in PSI in recent monitoring data compared to historical data.

**Strengths**:

- Provides a quantitative measure of feature distribution changes.
- Easily interpretable thresholds for decision-making.
- Helps in early detection of data drift, prompting timely interventions.

**Limitations**:

- May not capture more intricate changes in data distribution nuances.
- Assumes that bucket thresholds (quantiles) adequately represent distribution shifts.
- PSI score interpretation can be overly simplistic for complex datasets.