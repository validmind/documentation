# PolarityAndSubjectivity

Analyzes the polarity and subjectivity of text data within a dataset.

This method processes a dataset containing textual data to compute the polarity and
subjectivity scores using TextBlob, and returns a Plotly scatter plot visualizing
these scores.

Args:
dataset (Dataset): A dataset object which must have a `df` attribute (a pandas DataFrame)
and a `text_column` attribute indicating the name of the column containing text.

Returns:
plotly.graph_objs._figure.Figure: A Plotly scatter plot of polarity vs subjectivity.