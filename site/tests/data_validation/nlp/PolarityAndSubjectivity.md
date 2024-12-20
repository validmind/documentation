# PolarityAndSubjectivity

Analyzes the polarity and subjectivity of text data within a given dataset to visualize the sentiment distribution.

### Purpose

The Polarity and Subjectivity test is designed to evaluate the sentiment expressed in textual data. By analyzing
these aspects, it helps to identify the emotional tone and subjectivity of the dataset, which could be crucial in
understanding customer feedback, social media sentiments, or other text-related data.

### Test Mechanism

This test uses TextBlob to compute the polarity and subjectivity scores of textual data in a given dataset. The
mechanism includes:

- Iterating through each text entry in the specified column of the dataset.
- Applying the TextBlob library to compute the polarity (ranging from -1 for negative sentiment to +1 for positive
sentiment) and subjectivity (ranging from 0 for objective to 1 for subjective) for each entry.
- Creating a scatter plot using Plotly to visualize the relationship between polarity and subjectivity.

### Signs of High Risk

- High concentration of negative polarity values indicating prevalent negative sentiments.
- High subjectivity scores suggesting the text data is largely opinion-based rather than factual.
- Disproportionate clusters of extreme scores (e.g., many points near -1 or +1 polarity).

### Strengths

- Quantifies sentiment and subjectivity which can provide actionable insights.
- Visualizes sentiment distribution, aiding in easy interpretation.
- Utilizes well-established TextBlob library for sentiment analysis.

### Limitations

- Polarity and subjectivity calculations may oversimplify nuanced text sentiments.
- Reliance on TextBlob which may not be accurate for all domains or contexts.
- Visualization could become cluttered with very large datasets, making interpretation difficult.