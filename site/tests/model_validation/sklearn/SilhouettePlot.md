# SilhouettePlot

Calculates and visualizes Silhouette Score, assessing the degree of data point suitability to its cluster in ML
models.

### Purpose

This test calculates the Silhouette Score, which is a model performance metric used in clustering applications.
Primarily, the Silhouette Score evaluates how similar a data point is to its own cluster compared to other
clusters. The metric ranges between -1 and 1, where a high value indicates that the object is well matched to its
own cluster and poorly matched to neighboring clusters. Thus, the goal is to achieve a high Silhouette Score,
implying well-separated clusters.

### Test Mechanism

The test first extracts the true and predicted labels from the model's training data. The test runs the Silhouette
Score function, which takes as input the training dataset features and the predicted labels, subsequently
calculating the average score. This average Silhouette Score is printed for reference. The script then calculates
the silhouette coefficients for each data point, helping to form the Silhouette Plot. Each cluster is represented
in this plot, with color distinguishing between different clusters. A red dashed line indicates the average
Silhouette Score. The Silhouette Scores are also collected into a structured table, facilitating model performance
analysis and comparison.

### Signs of High Risk

- A low Silhouette Score, potentially indicating that the clusters are not well separated and that data points may
not be fitting well to their respective clusters.
- A Silhouette Plot displaying overlapping clusters or the absence of clear distinctions between clusters visually
also suggests poor clustering performance.

### Strengths

- The Silhouette Score provides a clear and quantitative measure of how well data points have been grouped into
clusters, offering insights into model performance.
- The Silhouette Plot provides an intuitive, graphical representation of the clustering mechanism, aiding visual
assessments of model performance.
- It does not require ground truth labels, so it's useful when true cluster assignments are not known.

### Limitations

- The Silhouette Score may be susceptible to the influence of outliers, which could impact its accuracy and
reliability.
- It assumes the clusters are convex and isotropic, which might not be the case with complex datasets.
- Due to the average nature of the Silhouette Score, the metric does not account for individual data point
assignment nuances, so potentially relevant details may be omitted.
- Computationally expensive for large datasets, as it requires pairwise distance computations.