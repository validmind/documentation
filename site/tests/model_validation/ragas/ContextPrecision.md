# ContextPrecision

Context Precision is a metric that evaluates whether all of the ground-truth
relevant items present in the contexts are ranked higher or not. Ideally all the
relevant chunks must appear at the top ranks. This metric is computed using the
`question`, `ground_truth` and the `contexts`, with values ranging between 0 and 1,
where higher scores indicate better precision.

$$
\\text{Context Precision@K} = \\frac{\\sum_{k=1}^{K} \\left( \\text{Precision@k} \\times v_k \\right)}{\\text{Total number of relevant items in the top } K \\text{ results}}
$$
$$
\\text{Precision@k} = {\\text{true positives@k} \\over  (\\text{true positives@k} + \\text{false positives@k})}
$$

Where $K$ is the total number of chunks in contexts and $v_k \\in \\{0, 1\\}$ is the
relevance indicator at rank $k$.

### Configuring Columns

This metric requires the following columns in your dataset:

- `user_input` (str): The text query that was input into the model.
- `retrieved_contexts` (List[str]): A list of text contexts which are retrieved and which
will be evaluated to make sure they contain relevant info in the correct order.
- `reference` (str): The ground truth text to compare with the retrieved contexts.

If the above data is not in the appropriate column, you can specify different column
names for these fields using the parameters `user_input_column`, `retrieved_contexts_column`
and `reference_column`.

For example, if your dataset has this data stored in different columns, you can
pass the following parameters:
```python
{
user_input_column": "question",
retrieved_contexts_column": "context_info",
reference_column": "my_ground_truth_col",
}
```

If the data is stored as a dictionary in another column, specify the column and key
like this:
```python
pred_col = dataset.prediction_column(model)
params = {
retrieved_contexts_column": f"{pred_col}.retrieved_contexts",
reference_column": "my_ground_truth_col",
}
```

For more complex situations, you can use a function to extract the data:
```python
pred_col = dataset.prediction_column(model)
params = {
retrieved_contexts_column": lambda x: [x[pred_col]["context_message"]],
reference_column": "my_ground_truth_col",
}
```