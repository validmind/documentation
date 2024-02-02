# PDRatingClassPlot

Assesses and visualizes credit risk distribution across different rating classes within a dataset via default
probabilities.

**Purpose**: The purpose of the Probability of Default (PD) Rating Class Plot test is to measure and evaluate the
distribution of calculated default probabilities across different rating classes. This is critical for
understanding and inferring credit risk and can provide insights into how effectively the model is differentiating
between different risk levels in a credit dataset.

**Test Mechanism**: This metric is implemented via a visualization mechanism. It sorts the predicted probabilities
of defaults into user-defined rating classes defined in "rating_classes" in default parameters. When it has
classified the probabilities, it then calculates the average default rates within each rating class. Subsequently,
it produces bar plots for each of these rating classes, illustrating the average likelihood of a default within
each class. This process is executed separately for both the training and testing data sets. The classification of
predicted probabilities utilizes the pandas "cut" function, sorting and sectioning the data values into bins.

**Signs of High Risk**:

- If lower rating classes present higher average likelihoods of default than higher rating classes
- If there is poor differentiation between the averages across the different rating classes
- If the model generates a significant contrast between the likelihoods for the training set and the testing set,
suggestive of model overfitting

**Strengths**:

- Presents a clear visual representation of how efficient the model is at predicting credit risk across different
risk levels
- Allows for rapid identification and understanding of model performance per rating class
- Highlights potential overfitting issues by including both training and testing datasets in the analysis

**Limitations**:

- Making an incorrect choice for the number of rating classes, either oversimplifying or overcomplicating the
distribution of default rates
- Relying on the assumption that the rating classes are effective at differentiating risk levels and that the
boundaries between classes truly represent the risk distribution
- Not accounting for data set class imbalance, which could cause skewed average probabilities
- Inability to gauge the overall performance of the model only based on this metric, emphasizing the requirement of
combining it with other evaluation metrics