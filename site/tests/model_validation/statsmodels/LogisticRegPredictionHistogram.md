# LogisticRegPredictionHistogram

Generates and visualizes histograms of the Probability of Default predictions for both positive and negative
classes in training and testing datasets.

**Purpose**: This code is designed to generate histograms that display the Probability of Default (PD) predictions
for positive and negative classes in both the training and testing datasets. By doing so, it evaluates the
performance of a logistic regression model, particularly in the context of credit risk prediction.

**Test Mechanism**: The metric executes these steps to run the test:
- Firstly, it extracts the target column from both the train and test datasets.
- The model's predict function is then used to calculate probabilities.
- These probabilities are added as a new column to the training and testing dataframes.
- Histograms are generated for each class (0 or 1 in binary classification scenarios) within the training and
testing datasets.
- To enhance visualization, the histograms are set to have different opacities.
- The four histograms (two for training data and two for testing) are overlaid on two different subplot frames (one
for training and one for testing data).
- The test returns a plotly graph object displaying the visualization.

**Signs of High Risk**: Several indicators could suggest a high risk or failure in the model's performance. These
include:
- Significant discrepancies observed between the histograms of training and testing data.
- Large disparities between the histograms for the positive and negative classes.
- These issues could signal potential overfitting or bias in the model.
- Unevenly distributed probabilities may also indicate that the model does not accurately predict outcomes.

**Strengths**: This metric and test offer several benefits, including:
- The visual representation of the PD predictions made by the model, which aids in understanding the model's
behaviour.
- The ability to assess both the training and testing datasets, adding depth to the validation of the model.
- Highlighting disparities between multiple classes, providing potential insights into class imbalance or data
skewness issues.
- Particularly beneficial for credit risk prediction, it effectively visualizes the spread of risk across different
classes.

**Limitations**: Despite its strengths, the test has several limitations:
- It is specifically tailored for binary classification scenarios, where the target variable only has two classes;
as such, it isn't suited for multi-class classification tasks.
- This metric is mainly applicable for logistic regression models. It might not be effective or accurate when used
on other model types.
- While the test provides a robust visual representation of the model's PD predictions, it does not provide a
quantifiable measure or score to assess model performance.