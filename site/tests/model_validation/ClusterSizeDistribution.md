# ClusterSizeDistribution

Compares and visualizes the distribution of cluster sizes in model predictions and actual data for assessing
clustering model performance.

**Purpose:** The purpose of the `ClusterSizeDistribution` metric is to assess the performance of clustering models.
It does this by comparing the distribution of cluster sizes in the predictions made by the model and the actual
data. Observing the cluster distribution helps gain insights into whether the model's output aligns well with the
actual dataset distribution.

**Test Mechanism:** The testing mechanism for `ClusterSizeDistribution` involves first running the clustering model
on the training dataset, storing predictions, and comparing these predictions with the actual output. The actual
and predicted outputs are then converted into pandas dataframes, which conveniently enables the use of pandas
built-in functions to derive cluster size distributions. Two histograms are constructed from this data: one for the
actual distribution and one for the predicted distribution. These histograms are then plotted side-by-side for
visual comparison.

**Signs of High Risk:**
* Discrepancies between the actual cluster size distribution and the predicted cluster size distribution may
indicate high risk.
* An irregular distribution of data across clusters in the predicted outcomes points towards an inaccurate
prediction model.
* A high number of outlier clusters could indicate that the model has trouble correctly grouping data.

**Strengths:**
* `ClusterSizeDistribution` provides a visual and intuitive way to compare the performance of the clustering model
against the actual data.
* This metric can effectively reveal where the model might be over- or underestimating cluster sizes.
* It works well with any clustering models, making it a versatile comparison tool.

**Limitations:**
* The metric assumes that the actual cluster distribution is optimal, which may not always be the case.
* It relies heavily on visual comparison, which might be subjective and may not provide a precise numerical measure
of model performance.
* The metric might not fully capture other important aspects of clustering such as cluster density, distances
between clusters, and the shape of clusters.