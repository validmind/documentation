# ContextEntityRecall

Evaluates the context entity recall for dataset entries and visualizes the results.

### Overview

This metric gives the measure of recall of the retrieved context, based on the
number of entities present in both `ground_truths` and `contexts` relative to the
number of entities present in the `ground_truths` alone. Simply put, it is a measure
of what fraction of entities are recalled from `ground_truths`. This metric is
useful in fact-based use cases like tourism help desk, historical QA, etc. This
metric can help evaluate the retrieval mechanism for entities, based on comparison
with entities present in `ground_truths`, because in cases where entities matter,
we need the `contexts` which cover them.

### Formula

To compute this metric, we use two sets, $GE$ and $CE$, representing the set of
entities present in `ground_truths` and set of entities present in `contexts`
respectively. We then take the number of elements in intersection of these sets and
divide it by the number of elements present in the $GE$, given by the formula:

$$
\\text{context entity recall} = \\frac{| CE \\cap GE |}{| GE |}
$$

### Configuring Columns

This metric requires the following columns in your dataset:

- `contexts` (List[str]): A list of text contexts which will be evaluated to make
sure if they contain the entities present in the ground truth.
- `ground_truth` (str): The ground truth text from which the entities will be
extracted and compared with the entities in the `contexts`.

If the above data is not in the appropriate column, you can specify different column
names for these fields using the parameters `contexts_column`, and `ground_truth_column`.

For example, if your dataset has this data stored in different columns, you can
pass the following parameters:
```python
{
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
contexts_column": lambda row: [row[pred_col]["context_message"]],
ground_truth_column": "my_ground_truth_col",
}
```