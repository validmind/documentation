# WOEBinTable

Assesses the Weight of Evidence (WoE) and Information Value (IV) of each feature to evaluate its predictive power
in a binary classification model.

### Purpose

The Weight of Evidence (WoE) and Information Value (IV) test is designed to evaluate the predictive power of each
feature in a machine learning model. This test generates binned groups of values from each feature, computes the
WoE and IV for each bin, and provides insights into the relationship between each feature and the target variable,
illustrating their contribution to the model's predictive capabilities.

### Test Mechanism

The test uses the `scorecardpy.woebin` method to perform automatic binning of the dataset based on WoE. The method
adjusts the cut-off points for binning numeric variables based on the parameter `breaks_adj`. The bins are then
used to calculate the WoE and IV values, effectively creating a dataframe that includes the bin boundaries, WoE,
and IV values for each feature. A target variable is required in the dataset to perform this analysis.

### Signs of High Risk

- High IV values, indicating variables with excessive predictive power which might lead to overfitting.
- Errors during the binning process, potentially due to inappropriate data types or poorly defined bins.

### Strengths

- Highly effective for feature selection in binary classification problems, as it quantifies the predictive
information within each feature concerning the binary outcome.
- The WoE transformation creates a monotonic relationship between the target and independent variables.

### Limitations

- Primarily designed for binary classification tasks, making it less applicable or reliable for multi-class
classification or regression tasks.
- Potential difficulties if the dataset has many features, non-binnable features, or non-numeric features.
- The metric does not help in distinguishing whether the observed predictive factor is due to data randomness or a
true phenomenon.