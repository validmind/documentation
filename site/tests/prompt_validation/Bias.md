# Bias

Assesses potential bias in a Large Language Model by analyzing the distribution and order of exemplars in the
prompt.

### Purpose

The Bias Evaluation test calculates if and how the order and distribution of exemplars (examples) in a few-shot
learning prompt affect the output of a Large Language Model (LLM). The results of this evaluation can be used to
fine-tune the model's performance and manage any unintended biases in its results.

### Test Mechanism

This test uses two checks:

1. **Distribution of Exemplars:** The number of positive vs. negative examples in a prompt is varied. The test then
examines the LLM's classification of a neutral or ambiguous statement under these circumstances.
2. **Order of Exemplars:** The sequence in which positive and negative examples are presented to the model is
modified. Their resultant effect on the LLM's response is studied.

For each test case, the LLM grades the input prompt on a scale of 1 to 10. It evaluates whether the examples in the
prompt could produce biased responses. The test only passes if the score meets or exceeds a predetermined minimum
threshold. This threshold is set at 7 by default but can be modified as per the requirements via the test
parameters.

### Signs of High Risk

- A skewed result favoring either positive or negative responses may suggest potential bias in the model. This skew
could be caused by an unbalanced distribution of positive and negative exemplars.
- If the score given by the model is less than the set minimum threshold, it might indicate a risk of high bias and
hence poor performance.

### Strengths

- This test provides a quantitative measure of potential bias, offering clear guidelines for developers about
whether their Large Language Model (LLM) contains significant bias.
- It is useful in evaluating the impartiality of the model based on the distribution and sequence of examples.
- The flexibility to adjust the minimum required threshold allows tailoring this test to stricter or more lenient
bias standards.

### Limitations

- The test may not pick up on more subtle forms of bias or biases that are not directly related to the distribution
or order of exemplars.
- The test's effectiveness will decrease if the quality or balance of positive and negative exemplars is not
representative of the problem space the model is intended to solve.
- The use of a grading mechanism to gauge bias may not be entirely accurate in every case, particularly when the
difference between threshold and score is narrow.