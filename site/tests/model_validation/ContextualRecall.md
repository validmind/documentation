# ContextualRecall

Evaluates a Natural Language Generation model's ability to generate contextually relevant and factually correct
text.

**Purpose**:
The Contextual Recall metric is used to evaluate the ability of a natural language generation (NLG) model to
generate text that appropriately reflects the given context or prompt. It measures the model's capability to
remember and reproduce the main context in its resulting output. This metric is critical in natural language
processing tasks, as the coherency and contextuality of the generated text are essential.

**Test Mechanism**:

1. **Preparation of Reference and Candidate Texts**:
- **Reference Texts**: Gather the reference text(s) which exemplify the expected or ideal output for a specific
context or prompt.
- **Candidate Texts**: Generate candidate text(s) from the NLG model under evaluation using the same context.
2. **Tokenization and Preprocessing**:
- Tokenize the reference and candidate texts into discernible words or tokens using libraries such as NLTK.
3. **Computation of Contextual Recall**:
- Identify the token overlap between the reference and candidate texts.
- The Contextual Recall score is computed by dividing the number of overlapping tokens by the total number of
tokens in the reference text. Scores are calculated for each test dataset instance, resulting in an array of
scores. These scores are then visualized using a line plot to show score variations across different rows.

**Signs of High Risk**:

- Low contextual recall scores could indicate that the model is not effectively reflecting the original context in
its output, leading to incoherent or contextually misaligned text.
- A consistent trend of low recall scores could suggest underperformance of the model.

**Strengths**:

- The Contextual Recall metric provides a quantifiable measure of a model's adherence to the context and factual
elements of the generated narrative.
- This metric finds particular value in applications requiring deep comprehension of context, such as text
continuation or interactive dialogue systems.
- The line plot visualization provides a clear and intuitive representation of score fluctuations.

**Limitations**:

- Despite its effectiveness, the Contextual Recall could fail to comprehensively assess the performance of NLG
models. Its focus on word overlap could result in high scores for texts that use many common words, even when these
texts lack coherence or meaningful context.
- This metric does not consider the order of words, which could lead to overestimated scores for scrambled outputs.
- Models that effectively use infrequent words might be undervalued, as these words might not overlap as often.