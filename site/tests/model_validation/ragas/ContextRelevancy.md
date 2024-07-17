# ContextRelevancy

Evaluates the context relevancy metric for entries in a dataset and visualizes the
results.

This metric gauges the relevancy of the retrieved context, calculated based on both
the `question` and `contexts`. The values fall within the range of (0, 1), with
higher values indicating better relevancy.

Ideally, the retrieved context should exclusively contain essential information to
address the provided query. To compute this, we initially estimate the value of by
identifying sentences within the retrieved context that are relevant for answering
the given question. The final score is determined by the following formula:

$$
\\text{context relevancy} = {|S| \\over |\\text{Total number of sentences in retrieved context}|}
$$

### Configuring Columns

This metric requires the following columns in your dataset:
- `question` (str): The text query that was input into the model.
- `contexts` (List[str]): A list of text contexts which are retrieved and which
will be evaluated to make sure they are relevant to the question.

If the above data is not in the appropriate column, you can specify different column
names for these fields using the parameters `question_column` and `contexts_column`.

For example, if your dataset has this data stored in different columns, you can
pass the following parameters:
```python
{
question_column": "question",
contexts_column": "context_info
}
```

If the data is stored as a dictionary in another column, specify the column and key
like this:
```python
pred_col = dataset.prediction_column(model)
params = {
contexts_column": f"{pred_col}.contexts",
}
```

For more complex situations, you can use a function to extract the data:
```python
pred_col = dataset.prediction_column(model)
params = {
contexts_column": lambda x: [x[pred_col]["context_message"]],
}
```