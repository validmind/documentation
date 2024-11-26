# ContextPrecisionWithoutReference

Context Precision Without Reference is a metric used to evaluate the relevance of
retrieved contexts compared to the expected response for a given user input. This
metric compares each retrieved context (or chunk) with the response to estimate
if the retrieved context is relevant.

This metric can be used when you have both retrieved contexts and associated
reference contexts for a `user_input`. Using a Language Model (LLM), it determines
the relevance of each retrieved context by comparing it directly with the response,
producing scores between 0 and 1, where higher scores indicate better precision in
retrieving relevant contexts.

### Configuring Columns

This metric requires the following columns in your dataset:

- `user_input` (str): The user query or input to the model.
- `retrieved_contexts` (List[str]): A list of text contexts retrieved for the
user input that will be evaluated for relevance.
- `response` (str): The model’s output response associated with the user input.

If your dataset stores this data in different columns, you can specify alternate
column names using the parameters `user_input_column`, `retrieved_contexts_column`,
and `response_column`.

Example configuration for custom column names:
```python
{
user_input_column": "user_query",
retrieved_contexts_column": "retrieved_texts",
response_column": "model_output",
}
```

For datasets with data stored as dictionaries in other columns, specify the
column and key like so:
```python
pred_col = dataset.prediction_column(model)
params = {
retrieved_contexts_column": f"{pred_col}.contexts",
response_column": f"{pred_col}.response",
}
```

Alternatively, for complex situations, you may use a function to extract data:
```python
pred_col = dataset.prediction_column(model)
params = {
retrieved_contexts_column": lambda x: [x[pred_col]["context_message"]],
response_column": "my_response_col",
}
```