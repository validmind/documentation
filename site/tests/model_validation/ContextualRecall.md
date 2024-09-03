# ContextualRecall

Evaluates a Natural Language Generation model's ability to generate contextually relevant and factually correct
text, visualizing the results through histograms and bar charts, alongside compiling a comprehensive table of
descriptive statistics for contextual recall scores.

### Purpose

The Contextual Recall metric is used to evaluate the ability of a natural language generation (NLG) model to
generate text that appropriately reflects the given context or prompt. It measures the model's capability to
remember and reproduce the main context in its resulting output. This metric is critical in natural language
processing tasks, as the coherency and contextuality of the generated text are essential.

### Test Mechanism

The function starts by extracting the true and predicted values from the provided dataset and model. It then
tokenizes the reference and candidate texts into discernible words or tokens using NLTK. The token overlap between
the reference and candidate texts is identified, and the Contextual Recall score is computed by dividing the number
of overlapping tokens by the total number of tokens in the reference text. Scores are calculated for each test
dataset instance, resulting in an array of scores. These scores are visualized using a histogram and a bar chart to
show score variations across different rows. Additionally, a table of descriptive statistics (mean, median,
standard deviation, minimum, and maximum) is compiled for the contextual recall scores, providing a comprehensive
summary of the model's performance.

### Signs of High Risk

- Low contextual recall scores could indicate that the model is not effectively reflecting the original context in
its output, leading to incoherent or contextually misaligned text.
- A consistent trend of low recall scores could suggest underperformance of the model.

### Strengths

- Provides a quantifiable measure of a model's adherence to the context and factual elements of the generated
narrative.
- Visual representations (histograms and bar charts) make it easier to interpret the distribution and trends of
contextual recall scores.
- Descriptive statistics offer a concise summary of the model's performance in generating contextually relevant
texts.

### Limitations

- The focus on word overlap could result in high scores for texts that use many common words, even when these texts
lack coherence or meaningful context.
- This metric does not consider the order of words, which could lead to overestimated scores for scrambled outputs.
- Models that effectively use infrequent words might be undervalued, as these words might not overlap as often.