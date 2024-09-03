# HighPearsonCorrelation

Identifies highly correlated feature pairs in a dataset suggesting feature redundancy or multicollinearity.

### Purpose

The High Pearson Correlation test measures the linear relationship between features in a dataset, with the main
goal of identifying high correlations that might indicate feature redundancy or multicollinearity. Identification
of such issues allows developers and risk management teams to properly deal with potential impacts on the machine
learning model's performance and interpretability.

### Test Mechanism

The test works by generating pairwise Pearson correlations for all features in the dataset, then sorting and
eliminating duplicate and self-correlations. It assigns a Pass or Fail based on whether the absolute value of the
correlation coefficient surpasses a pre-set threshold (defaulted at 0.3). It lastly returns the top ten strongest
correlations regardless of passing or failing status.

### Signs of High Risk

- A high risk indication would be the presence of correlation coefficients exceeding the threshold.
- If the features share a strong linear relationship, this could lead to potential multicollinearity and model
overfitting.
- Redundancy of variables can undermine the interpretability of the model due to uncertainty over the authenticity
of individual variable's predictive power.

### Strengths

- Provides a quick and simple means of identifying relationships between feature pairs.
- Generates a transparent output that displays pairs of correlated variables, the Pearson correlation coefficient,
and a Pass or Fail status for each.
- Aids in early identification of potential multicollinearity issues that may disrupt model training.

### Limitations

- Can only delineate linear relationships, failing to shed light on nonlinear relationships or dependencies.
- Sensitive to outliers where a few outliers could notably affect the correlation coefficient.
- Limited to identifying redundancy only within feature pairs; may fail to spot more complex relationships among
three or more variables.
- The top 10 result filter might not fully capture the richness of the data; an option to configure the number of
retained results could be helpful.