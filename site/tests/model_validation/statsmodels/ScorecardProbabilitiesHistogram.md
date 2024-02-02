# ScorecardProbabilitiesHistogram

Evaluates risk classification of a model by visualizing the distribution of default probability across score
buckets.

**Purpose**: The Scorecard Probabilities Histogram, a specific metric used within the credit risk domain, is
designed to evaluate and visualize risk classification of a model. It aims at examining the distribution of the
probability of default across varied score buckets, with the score buckets being categories that entities (e.g.,
loan applicants) are classed under based on their predicted default risks. The key idea is to ensure that the model
accurately classifies entities into appropriate risk categories (score buckets) and aptly represents their default
probabilities.

**Test Mechanism**: The mechanism behind the Scorecard Probabilities Histogram includes several steps. It starts
with the calculation of default probabilities by the 'compute_probabilities' method, where the resulting
probability is added as a fresh column to the input dataset. Following that, scores are computed using these
probabilities, a target score, target odds, and a Points to Double the odds (pdo) factor by the 'compute_scores
method. These scores are then bucketed via the 'compute_buckets' method. A histogram is then plotted for each score
bucket, with default probabilities as the x-axis and their frequency as the y-axis - implemented within the
plot_probabilities_histogram' method. This entire process is executed distinctly for both training and testing
datasets.

**Signs of High Risk**:
- A significant overlap of different score buckets in the histogram indicates that the model is not efficiently
distinguishing between various risk categories.
- If very high or low probabilities are commonplace across all buckets, the model's predictions could be skewed.

**Strengths**:
- The Scorecard Probabilities Histogram allows for the visualization and analysis of the predicted default risk
distribution across different risk classes, thereby facilitating a visual inspection of the model's performance and
calibration for various risk categories.
- It provides a means to visualize how these classifications are distributed on the training and testing datasets
separately, contributing to a better comprehension of model generalization.

**Limitations**:
- The Scorecard Probabilities Histogram assumes linear and equally spaced risk categories, which might not always
hold true.
- If there are too few or too many score buckets, the visualization may not convey sufficient information.
- While it effectively illustrates the distribution of probabilities, it does not provide adequate numerical
metrics or threshold to definitively evaluate the model's performance. A more accurate evaluation necessitates its
usage in conjunction with other metrics and tools including the confusion matrix, AUC-ROC, Precision, Recall, and
so forth.