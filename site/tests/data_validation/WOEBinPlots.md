# WOEBinPlots

Generates visualizations of Weight of Evidence (WoE) and Information Value (IV) for understanding predictive power
of categorical variables in a data set.

### Purpose

This test is designed to visualize the Weight of Evidence (WoE) and Information Value (IV) for categorical
variables in a provided dataset. By showcasing the data distribution across different categories of each feature,
it aids in understanding each variable's predictive power in the context of a classification-based machine learning
model. Commonly used in credit scoring models, WoE and IV are robust statistical methods for evaluating a
variable's predictive power.

### Test Mechanism

The test implementation follows defined steps. Initially, it selects non-numeric columns from the dataset and
changes them to string type, paving the way for accurate binning. It then performs an automated WoE binning
operation on these selected features, effectively categorizing the potential values of a variable into distinct
bins. After the binning process, the function generates two separate visualizations (a scatter chart for WoE values
and a bar chart for IV) for each variable. These visual presentations are formed according to the spread of each
metric across various categories of each feature.

### Signs of High Risk

- Errors occurring during the binning process.
- Challenges in converting non-numeric columns into string data type.
- Misbalance in the distribution of WoE and IV, with certain bins overtaking others conspicuously. This could
denote that the model is disproportionately dependent on certain variables or categories for predictions, an
indication of potential risks to its robustness and generalizability.

### Strengths

- Provides a detailed visual representation of the relationship between feature categories and the target variable.
This grants an intuitive understanding of each feature's contribution to the model.
- Allows for easy identification of features with high impact, facilitating feature selection and enhancing
comprehension of the model's decision logic.
- WoE conversions are monotonic, upholding the rank ordering of the original data points, which simplifies analysis.

### Limitations

- The method is largely reliant on the binning process, and an inappropriate binning threshold or bin number choice
might result in a misrepresentation of the variable's distribution.
- While excellent for categorical data, the encoding of continuous variables into categorical can sometimes lead to
information loss.
- Extreme or outlier values can dramatically affect the computation of WoE and IV, skewing results.
- The method requires a sufficient number of events per bin to generate a reliable information value and weight of
evidence.