# RegardScore

Assesses the sentiment and potential biases in text generated by NLP models by computing and visualizing regard
scores.

### Purpose

The `RegardScore` test aims to evaluate the levels of regard (positive, negative, neutral, or other) in texts
generated by NLP models. It helps in understanding the sentiment and bias present in the generated content.

### Test Mechanism

This test extracts the true and predicted values from the provided dataset and model. It then computes the regard
scores for each text instance using a preloaded `regard` evaluation tool. The scores are compiled into dataframes,
and visualizations such as histograms and bar charts are generated to display the distribution of regard scores.
Additionally, descriptive statistics (mean, median, standard deviation, minimum, and maximum) are calculated for
the regard scores, providing a comprehensive overview of the model's performance.

### Signs of High Risk

- Noticeable skewness in the histogram, especially when comparing the predicted regard scores with the target
regard scores, can indicate biases or inconsistencies in the model.
- Lack of neutral scores in the model's predictions, despite a balanced distribution in the target data, might
signal an issue.

### Strengths

- Provides a clear evaluation of regard levels in generated texts, aiding in ensuring content appropriateness.
- Visual representations (histograms and bar charts) make it easier to interpret the distribution and trends of
regard scores.
- Descriptive statistics offer a concise summary of the model's performance in generating texts with balanced
sentiments.

### Limitations

- The accuracy of the regard scores is contingent upon the underlying `regard` tool.
- The scores provide a broad overview but do not specify which portions or tokens of the text are responsible for
high regard.
- Supplementary, in-depth analysis might be needed for granular insights.