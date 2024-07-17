# Toxicity

Analyzes the toxicity of text data within a dataset using a pre-trained toxicity model.

This method loads a toxicity evaluation model and applies it to each text entry
in the specified column of the dataset's dataframe. It returns a KDE plot visualizing the distribution
of toxicity scores across the dataset.

Args:
dataset (Dataset): A dataset object which must have a `df` attribute (a pandas DataFrame)
and a `text_column` attribute indicating the name of the column containing text.

Returns:
matplotlib.figure.Figure: A KDE plot visualizing the distribution of toxicity scores.