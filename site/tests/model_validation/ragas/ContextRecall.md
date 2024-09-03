# ContextRecall

Context recall measures the extent to which the retrieved context aligns with the
annotated answer, treated as the ground truth. It is computed based on the `ground
truth` and the `retrieved context`, and the values range between 0 and 1, with higher
values indicating better performance.

To estimate context recall from the ground truth answer, each sentence in the ground
truth answer is analyzed to determine whether it can be attributed to the retrieved
context or not. In an ideal scenario, all sentences in the ground truth answer
should be attributable to the retrieved context.


The formula for calculating context recall is as follows:
$$
\\text{context recall} = {|\\text{GT sentences that can be attributed to context}| \\over |\\text{Number of sentences in GT}|}
$$

### Configuring Columns

This metric requires the following columns in your dataset:

- `question` (str): The text query that was input into the model.
- `contexts` (List[str]): A list of text contexts which are retrieved and which
will be evaluated to make sure they contain all items in the ground truth.
- `ground_truth` (str): The ground truth text to compare with the retrieved contexts.

If the above data is not in the appropriate column, you can specify different column
names for these fields using the parameters `question_column`, `contexts_column`
and `ground_truth_column`.

For example, if your dataset has this data stored in different columns, you can
pass the following parameters:
```python
{
question_column": "question",
contexts_column": "context_info
ground_truth_column": "my_ground_truth_col",
}
```

If the data is stored as a dictionary in another column, specify the column and key
like this:
```python
pred_col = dataset.prediction_column(model)
params = {
contexts_column": f"{pred_col}.contexts",
ground_truth_column": "my_ground_truth_col",
}
```

For more complex situations, you can use a function to extract the data:
```python
pred_col = dataset.prediction_column(model)
params = {
contexts_column": lambda x: [x[pred_col]["context_message"]],
ground_truth_column": "my_ground_truth_col",
}
```