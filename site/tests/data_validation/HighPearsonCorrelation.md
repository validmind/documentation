# HighPearsonCorrelation

Identifies highly correlated feature pairs in a dataset suggesting feature redundancy or multicollinearity.

**Purpose**: The High Pearson Correlation test measures the linear relationship between features in a dataset, with
the main goal of identifying high correlations that might indicate feature redundancy or multicollinearity.
Identification of such issue allows developers and risk management teams to properly deal with potential impacts on
the machine learning model's performance and interpretability.

**Test Mechanism**: The test works by generating pairwise Pearson correlations for all features in the dataset,
then sorting and eliminating duplicate and self-correlations. It assigns a Pass or Fail based on whether the
absolute value of the correlation coefficient surpasses a pre-set threshold (defaulted at 0.3). It lastly returns
the top ten strongest correlations regardless of passing or failing status.

**Signs of High Risk**:
- A high risk indication would be the presence of correlation coefficients exceeding the threshold.
- If the features share a strong linear relationship, this could lead to potential multicollinearity and model
overfitting.
- Redundancy of variables can undermine the interpretability of the model due to uncertainty over the authenticity
of individual variable's predictive power.

**Strengths**:
- The High Pearson Correlation test provides a quick and simple means of identifying relationships between feature
pairs.
- It generates a transparent output which not only displays pairs of correlated variables but also delivers the
Pearson correlation coefficient and a Pass or Fail status for each.
- It aids early identification of potential multicollinearity issues that may disrupt model training.

**Limitations**:
- The Pearson correlation test can only delineate linear relationships. It fails to shed light on nonlinear
relationships or dependencies.
- It is sensitive to outliers where a few outliers could notably affect the correlation coefficient.
- It is limited to identifying redundancy only within feature pairs. When three or more variables are linearly
dependent, it may fail to spot this complex relationship.
- The top 10 result filter might not fully capture the richness of the data; an option to configure the number of
retained results could be helpful.