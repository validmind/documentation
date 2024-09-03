# ClusterSizeDistribution

Assesses the performance of clustering models by comparing the distribution of cluster sizes in model predictions
with the actual data.

### Purpose

The Cluster Size Distribution test aims to assess the performance of clustering models by comparing the
distribution of cluster sizes in the model's predictions with the actual data. This comparison helps determine if
the clustering model's output aligns well with the true cluster distribution, providing insights into the model's
accuracy and performance.

### Test Mechanism

The test mechanism involves the following steps:
- Run the clustering model on the provided dataset to obtain predictions.
- Convert both the actual and predicted outputs into pandas dataframes.
- Use pandas built-in functions to derive the cluster size distributions from these dataframes.
- Construct two histograms: one for the actual cluster size distribution and one for the predicted distribution.
- Plot the histograms side-by-side for visual comparison.

### Signs of High Risk

- Discrepancies between the actual cluster size distribution and the predicted cluster size distribution.
- Irregular distribution of data across clusters in the predicted outcomes.
- High number of outlier clusters suggesting the model struggles to correctly group data.

### Strengths

- Provides a visual and intuitive way to compare the clustering model's performance against actual data.
- Effectively reveals where the model may be over- or underestimating cluster sizes.
- Versatile as it works well with any clustering model.

### Limitations

- Assumes that the actual cluster distribution is optimal, which may not always be the case.
- Relies heavily on visual comparison, which could be subjective and may not offer a precise numerical measure of
performance.
- May not fully capture other important aspects of clustering, such as cluster density, distances between clusters,
and the shape of clusters.