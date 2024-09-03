# PredictionProbabilitiesHistogram

Assesses the predictive probability distribution for binary classification to evaluate model performance and
potential overfitting or bias.

### Purpose

The Prediction Probabilities Histogram test is designed to generate histograms displaying the Probability of
Default (PD) predictions for both positive and negative classes in training and testing datasets. This helps in
evaluating the performance of a logistic regression model, particularly for credit risk prediction.

### Test Mechanism

The metric follows these steps to execute the test:
- Extracts the target column from both the train and test datasets.
- Uses the model's predict function to calculate probabilities.
- Adds these probabilities as a new column to the training and testing dataframes.
- Generates histograms for each class (0 or 1) within the training and testing datasets.
- Sets different opacities for the histograms to enhance visualization.
- Overlays the four histograms (two for training and two for testing) on two different subplot frames.
- Returns a plotly graph object displaying the visualization.

### Signs of High Risk

- Significant discrepancies between the histograms of training and testing data.
- Large disparities between the histograms for the positive and negative classes.
- Potential overfitting or bias indicated by significant issues.
- Unevenly distributed probabilities suggesting inaccurate model predictions.

### Strengths

- Offers a visual representation of the PD predictions made by the model, aiding in understanding its behavior.
- Assesses both the training and testing datasets, adding depth to model validation.
- Highlights disparities between classes, providing insights into class imbalance or data skewness.
- Effectively visualizes risk spread, which is particularly beneficial for credit risk prediction.

### Limitations

- Specifically tailored for binary classification scenarios and not suited for multi-class classification tasks.
- Mainly applicable to logistic regression models, and may not be effective for other model types.
- Provides a robust visual representation but lacks a quantifiable measure to assess model performance.