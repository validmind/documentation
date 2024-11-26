# ContextEntityRecall

Evaluates the context entity recall for dataset entries and visualizes the results.

### Overview

This metric gives the measure of recall of the retrieved context, based on the
number of entities present in both `reference` and `retrieved_contexts` relative to the
number of entities present in the `reference` alone. Simply put, it is a measure
of what fraction of entities are recalled from `reference`. This metric is
useful in fact-based use cases like tourism help desk, historical QA, etc. This
metric can help evaluate the retrieval mechanism for entities, based on comparison
with entities present in `reference`, because in cases where entities matter,
we need the `retrieved_contexts` which cover them.

### Formula

To compute this metric, we use two sets, $GE$ and $CE$, representing the set of
entities present in `reference` and set of entities present in `retrieved_contexts`
respectively. We then take the number of elements in intersection of these sets and
divide it by the number of elements present in the $GE$, given by the formula:

$$
\\text{context entity recall} = \\frac{| CE \\cap GE |}{| GE |}
$$

### Configuring Columns

This metric requires the following columns in your dataset:

- `retrieved_contexts` (List[str]): A list of text contexts which will be evaluated to make
sure if they contain the entities present in the `reference`.
- `reference` (str): The ground truth text from which the entities will be
extracted and compared with the entities in the `retrieved_contexts`.

If the above data is not in the appropriate column, you can specify different column
names for these fields using the parameters `retrieved_contexts_column`, and `reference_column`.

For example, if your dataset has this data stored in different columns, you can
pass the following parameters:
```python
{
retrieved_contexts_column": "context_info",
reference_column": "my_ground_truth_col",
}
```

If the data is stored as a dictionary in another column, specify the column and key
like this:
```python
pred_col = dataset.prediction_column(model)
params = {
retrieved_contexts_column": f"{pred_col}.contexts",
reference_column": "my_ground_truth_col",
}
```

For more complex situations, you can use a function to extract the data:
```python
pred_col = dataset.prediction_column(model)
params = {
retrieved_contexts_column": lambda row: [row[pred_col]["context_message"]],
reference_column": "my_ground_truth_col",
}
```