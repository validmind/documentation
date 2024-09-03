# ClusterPerformanceMetrics

Evaluates the performance of clustering machine learning models using multiple established metrics.

### Purpose

The `ClusterPerformanceMetrics` test is used to assess the performance and validity of clustering machine learning
models. It evaluates homogeneity, completeness, V measure score, the Adjusted Rand Index, the Adjusted Mutual
Information, and the Fowlkes-Mallows score of the model. These metrics provide a holistic understanding of the
model's ability to accurately form clusters of the given dataset.

### Test Mechanism

The `ClusterPerformanceMetrics` test runs a clustering ML model over a given dataset and then calculates six
metrics using the Scikit-learn metrics computation functions: Homogeneity Score, Completeness Score, V Measure,
Adjusted Rand Index (ARI), Adjusted Mutual Information (AMI), and Fowlkes-Mallows Score. It then returns the result
as a summary, presenting the metric values for both training and testing datasets.

### Signs of High Risk

- Low Homogeneity Score: Indicates that the clusters formed contain a variety of classes, resulting in less pure
clusters.
- Low Completeness Score: Suggests that class instances are scattered across multiple clusters rather than being
gathered in a single cluster.
- Low V Measure: Reports a low overall clustering performance.
- ARI close to 0 or Negative: Implies that clustering results are random or disagree with the true labels.
- AMI close to 0: Means that clustering labels are random compared with the true labels.
- Low Fowlkes-Mallows score: Signifies less precise and poor clustering performance in terms of precision and
recall.

### Strengths

- Provides a comprehensive view of clustering model performance by examining multiple clustering metrics.
- Uses established and widely accepted metrics from scikit-learn, providing reliability in the results.
- Able to provide performance metrics for both training and testing datasets.
- Clearly defined and human-readable descriptions of each score make it easy to understand what each score
represents.

### Limitations

- Only applies to clustering models; not suitable for other types of machine learning models.
- Does not test for overfitting or underfitting in the clustering model.
- All the scores rely on ground truth labels, the absence or inaccuracy of which can lead to misleading results.
- Does not consider aspects like computational efficiency of the model or its capability to handle high dimensional
data.