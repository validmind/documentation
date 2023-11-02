# WOEBinTable

Calculates and assesses the Weight of Evidence (WoE) and Information Value (IV) of each feature in a ML model.

**Purpose**: The Weight of Evidence (WoE) and Information Value (IV) test is intended to evaluate the predictive
power of each feature in the machine learning model. The test generates binned groups of values from each feature
in a dataset, computes the WoE value and the IV value for each bin. These values provide insights on the
relationship between each feature and the target variable and their contribution towards the predictive output of
the model.

**Test Mechanism**: The metric leverages the `scorecardpy.woebin` method to perform WoE-based automatic binning on
the dataset. Depending on the parameter `breaks_adj`, the method adjusts the cut-off points for binning numeric
variables. The bins are then used to calculate the WoE and IV. The metric requires a dataset with the target
variable defined. The metric outputs a dataframe that comprises the bin boundaries, WoE, and IV values for each
feature.

**Signs of High Risk**:
- High IV values, which denote variables with too much predictive power which might lead to overfitting
- Errors during the binning process, which might be due to inappropriate data types or poorly defined bins

**Strengths**:
- The WoE and IV test is highly effective for feature selection in binary classification problems, as it quantifies
how much predictive information is packed within each feature regarding the binary outcome
- The WoE transformation creates a monotonic relationship between the target and independent variables

**Limitations**:
- Mainly designed for binary classification tasks, therefore it might not be applicable or reliable for multi-class
classification or regression tasks
- If the dataset has many features or the features are not binnable or they are non-numeric, this process might
encounter difficulties
- This metric doesn't help in identifying if the predictive factor being observed is a coincidence or a real
phenomenon due to data randomness