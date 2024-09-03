# KMeansClustersOptimization

Optimizes the number of clusters in K-means models using Elbow and Silhouette methods.

### Purpose

This metric is used to optimize the number of clusters used in K-means clustering models. It intends to measure and
evaluate the optimal number of clusters by leveraging two methodologies, namely the Elbow method and the Silhouette
method. This is crucial as an inappropriate number of clusters can either overly simplify or overcomplicate the
structure of the data, thereby undermining the effectiveness of the model.

### Test Mechanism

The test mechanism involves iterating over a predefined range of cluster numbers and applying both the Elbow method
and the Silhouette method. The Elbow method computes the sum of the minimum euclidean distances between data points
and their respective cluster centers (distortion). This value decreases as the number of clusters increases; the
optimal number is typically at the 'elbow' point where the decrease in distortion becomes less pronounced.
Meanwhile, the Silhouette method calculates the average silhouette score for each data point in the dataset,
providing a measure of how similar each item is to its own cluster compared to other clusters. The optimal number
of clusters under this method is the one that maximizes the average silhouette score. The results of both methods
are plotted for visual inspection.

### Signs of High Risk

- A high distortion value or a low silhouette average score for the optimal number of clusters.
- No clear 'elbow' point or plateau observed in the distortion plot, or a uniformly low silhouette average score
across different numbers of clusters, suggesting the data is not amenable to clustering.
- An optimal cluster number that is unreasonably high or low, suggestive of overfitting or underfitting,
respectively.

### Strengths

- Provides both a visual and quantitative method to determine the optimal number of clusters.
- Leverages two different methods (Elbow and Silhouette), thereby affording robustness and versatility in assessing
the data's clusterability.
- Facilitates improved model performance by allowing for an informed selection of the number of clusters.

### Limitations

- Assumes that a suitable number of clusters exists in the data, which may not always be true, especially for
complex or noisy data.
- Both methods may fail to provide definitive answers when the data lacks clear cluster structures.
- Might not be straightforward to determine the 'elbow' point or maximize the silhouette average score, especially
in larger and complicated datasets.
- Assumes spherical clusters (due to using the Euclidean distance in the Elbow method), which might not align with
the actual structure of the data.