# ClusterPerformance

Evaluates and compares a clustering model's performance on training and testing datasets using multiple defined
metrics.

**Purpose:** This metric, ClusterPerformance, evaluates the performance of a clustering model on both the training
and testing datasets. It assesses how well the model defines, forms, and distinguishes clusters of data.

**Test Mechanism:** The metric is applied by first predicting the clusters of the training and testing datasets
using the clustering model. Next, performance metrics, defined in the method `metric_info()`, are calculated
against the true labels of the datasets. The results for each metric for both datasets are then collated and
returned in a summarized table form listing each metric along with its corresponding train and test values.

**Signs of High Risk:**
- High discrepancy between the performance metric values on the training and testing datasets. This could signify
problems such as overfitting or underfitting.
- Low performance metric values on the training and testing datasets. There might be a problem with the model
itself or the chosen hyperparameters.
- If the model's performance deteriorates consistently across different sets of metrics, this may suggest a broader
issue with the model or the dataset.

**Strengths:**
- Tests the model's performance on both the training and testing datasets, which helps to identify issues such as
overfitting or underfitting.
- Allows for a broad range of performance metrics to be used, thus providing a comprehensive evaluation of the
model's clustering capabilities.
- Returns a summarized table, which makes it easy to compare the model's performance across different metrics and
datasets.

**Limitations:**
- The method `metric_info()` needs to be properly overridden in a subclass for this class to be used, and the
metrics to be used must be manually defined.
- The performance metrics are calculated on predicted cluster labels, so the metric may not capture the model's
performance well if the clusters are not well separated or if the model has difficulties with certain kinds of
clusters.
- Doesn't consider the computational and time complexity of the model. While the model may perform well in terms of
the performance metrics, it might be time or resource-intensive. This metric does not account for such scenarios.
- Because the comparison is binary (train and test), it might not capture scenarios where the performance changes
drastically under different circumstances or categories within the dataset.