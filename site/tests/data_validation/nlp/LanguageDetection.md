# LanguageDetection

Detects the language of each text entry in a dataset and visualizes the distribution of languages
as a histogram.

This method checks for a specified text column in the dataset's dataframe, uses a language detection
library to determine the language of each text entry, and returns a histogram plot of the language
distribution.

Args:
dataset (Dataset): A dataset object which must have a `df` attribute (a pandas DataFrame)
and a `text_column` attribute indicating the name of the column containing text. If the
`text_column` attribute is not set, a ValueError is raised.

Returns:
plotly.graph_objs._figure.Figure: A Plotly histogram plot showing the distribution of detected
languages across the dataset's text entries.

Raises:
ValueError: If the `text_column` is not specified in the dataset object.