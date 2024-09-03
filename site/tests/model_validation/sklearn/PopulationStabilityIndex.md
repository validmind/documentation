# PopulationStabilityIndex

Assesses the Population Stability Index (PSI) to quantify the stability of an ML model's predictions across
different datasets.

### Purpose

The Population Stability Index (PSI) serves as a quantitative assessment for evaluating the stability of a machine
learning model's output distributions when comparing two different datasets. Typically, these would be a
development and a validation dataset or two datasets collected at different periods. The PSI provides a measurable
indication of any significant shift in the model's performance over time or noticeable changes in the
characteristics of the population the model is making predictions for.

### Test Mechanism

The implementation of the PSI in this script involves calculating the PSI for each feature between the training and
test datasets. Data from both datasets is sorted and placed into either a predetermined number of bins or
quantiles. The boundaries for these bins are initially determined based on the distribution of the training data.
The contents of each bin are calculated and their respective proportions determined. Subsequently, the PSI is
derived for each bin through a logarithmic transformation of the ratio of the proportions of data for each feature
in the training and test datasets. The PSI, along with the proportions of data in each bin for both datasets, are
displayed in a summary table, a grouped bar chart, and a scatter plot.

### Signs of High Risk

- A high PSI value is a clear indicator of high risk. Such a value suggests a significant shift in the model
predictions or severe changes in the characteristics of the underlying population.
- This ultimately suggests that the model may not be performing as well as expected and that it may be less
reliable for making future predictions.

### Strengths

- The PSI provides a quantitative measure of the stability of a model over time or across different samples, making
it an invaluable tool for evaluating changes in a model's performance.
- It allows for direct comparisons across different features based on the PSI value.
- The calculation and interpretation of the PSI are straightforward, facilitating its use in model risk management.
- The use of visual aids such as tables and charts further simplifies the comprehension and interpretation of the
PSI.

### Limitations

- The PSI test does not account for the interdependence between features: features that are dependent on one
another may show similar shifts in their distributions, which in turn may result in similar PSI values.
- The PSI test does not inherently provide insights into why there are differences in distributions or why the PSI
values may have changed.
- The test may not handle features with significant outliers adequately.
- Additionally, the PSI test is performed on model predictions, not on the underlying data distributions which can
lead to misinterpretations. Any changes in PSI could be due to shifts in the model (model drift), changes in the
relationships between features and the target variable (concept drift), or both. However, distinguishing between
these causes is non-trivial.