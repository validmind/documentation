# AspectCritic

Evaluates generations against the following aspects: harmfulness, maliciousness,
coherence, correctness, and conciseness.

### Overview:

This is designed to assess submissions against predefined and user-defined "aspects".
For each aspect, a judge LLM is prompted to critique a piece of generated text based
on a description of the aspect. The output of this evaluation is a binary (0/1 = yes/no)
score that indicates whether the submission aligns with the defined aspect or not.

### Inputs and Outputs:

The input to this metric is a dataset containing the input `user_input` (prompt to the LLM)
and the `response` (text generated by the LLM). Any retrieved `retrieved_contexts` can also be
included to enhance the evaluation.

The `user_input_column`, `response_column`, and `retrieved_contexts_column` parameters can be used to
specify the names or sources for the data that this metric will evaluate if the dataset
does not contain the required columns `user_input`, `response`, and `retrieved_contexts`.

By default, the aspects evaluated are harmfulness, maliciousness, coherence,
correctness, and conciseness. To change the aspects evaluated, the `aspects` parameter
can be set to a list containing any of these aspects.

To add custom aspects, the `additional_aspects` parameter can be passed as a list
of tuples where each tuple contains the aspect name and a description of the aspect
that the judge LLM will use to critique the submission.

The output of this metric is a table of scores for each aspect where the aspect score
is the number of "yes" scores divided by the total number of submissions:
$$
\\text{aspect score} = \\frac{\\text{number of "yes" scores}}{\\text{total number of submissions}}
$$

### Examples:

- **Mapping to Required Columns:** If the dataset does not contain the columns required
to run this metric (i.e., `user_input`, `response`, and `retrieved_contexts`), the

```python
pred_col = my_vm_dataset.prediction_column(my_vm_model)
run_test(
validmind.model_validation.ragas.AspectCritic",
inputs={"dataset": my_vm_dataset},
params={
user_input_column": "input_prompt",
response_column": f"{pred_col}.llm_output",
retrieved_contexts_column": "retrieval_model_prediction",
},
)
```

- **Custom Aspects:** To evaluate custom aspects, the `additional_aspects` parameter can
be set to a list of tuples where each tuple contains the aspect name and a description
of the aspect that the judge LLM will use to critique the submission. For example, to
evaluate whether the LLM-generated text has a "professional tone", the `additional_aspects`
parameter can be set like this:

```python
run_test(
validmind.model_validation.ragas.AspectCritic",
inputs={"dataset": my_vm_dataset},
params={
additional_aspects": [
("professionalism", "Does the text have a professional tone?"),
],
},
)
```