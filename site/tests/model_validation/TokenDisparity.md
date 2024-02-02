# TokenDisparity

Assess and visualize token count disparity between model's predicted and actual dataset.

**Purpose**:
The Token Disparity metric is designed to assess the distributional congruence between the model's predicted
outputs and the actual data. This is achieved by constructing histograms that illustrate the disparity in token
count between the two columns. Additionally, this metric is used to measure the model's verbosity in comparison to
the genuine dataset.

**Test Mechanism**:
The mechanism of running this test involves tokenizing both columns: one containing the actual data and the other
containing the model's predictions. The BERT tokenizer is used for tokenizing the contents of each column. After
tokenization, tokens in each column are counted and represented in two distinct histograms to facilitate the
visualization of token count distribution in the actual and predicted data. To quantify the difference in
distribution, the histogram of the actual tokens is compared with the histogram of the predicted tokens.

**Signs of High Risk**:
High risk or potential failure in model performance may be suggested by:

- Significant incongruities in distribution patterns between the two histograms.
- Marked divergence of the predicted histogram from the reference histogram, indicating that the model may be
generating output with unexpected verbosity.
- This might result in an output that has a significantly higher or lower number of tokens than expected.

**Strengths**:
Strengths of the Token Disparity metric include:

- It provides a clear and visual comparison of predicted versus actual token distributions, enhancing understanding
of the model's output consistency and verbosity.
- It is able to detect potential issues with the model's output generation capability, such as over-production or
under-production of tokens compared to the actual data set.

**Limitations**:
Limitations of the Token Disparity metric include:

- The metric focuses solely on token count, disregarding the semantics behind those tokens. Consequently, it may
miss out on issues related to relevance or meaningfulness of produced tokens.
- The assumption that similar token count between predicted and actual data suggests accurate output, which is not
always the case.
- Dependence on the BERT tokenizer, which may not always be the optimum choice for all types of text data.