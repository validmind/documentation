# StabilityAnalysisRandomNoise

Assesses the robustness of text embeddings models to random noise introduced via text perturbations.

### Purpose

The purpose of this test is to evaluate the robustness of a text embeddings model to random noise. It introduces
perturbations such as swapping adjacent words, inserting typos, deleting words, or inserting random words within
the text to determine how well the model performs under such noisy conditions.

### Test Mechanism

The test applies a series of pre-defined random perturbations to the text data. These perturbations include:

- Swapping two adjacent words using the `random_swap` function.
- Introducing a typo in a word using the `introduce_typo` function.
- Deleting a word using the `random_deletion` function.
- Inserting a random word at a random position using the `random_insertion` function.

A probability parameter dictates the likelihood of each perturbation being applied to the words in the text. The
text is initially tokenized into words, and selected perturbations are applied based on this probability.

### Signs of High Risk

- High error rates in model predictions or classifications after the introduction of random noise.
- Greater sensitivity to specific types of noise, such as typographical errors or word deletions.
- Significant change in loss function or accuracy metrics.
- Inconsistent model outputs for slightly perturbed inputs.

### Strengths

- Measures model robustness against noise, reflecting real-world scenarios where data may contain errors or
inconsistencies.
- Easy to implement with adjustable perturbation severity through a probability parameter.
- Identifies model sensitivity to specific types of noise, offering insights for model improvement.
- Useful for testing models designed to handle text data.

### Limitations

- May be ineffective for models that are inherently resistant to noise or designed to handle such perturbations.
- Pseudo-randomness may not accurately represent the real-world distribution of noise or typographical errors.
- Highly dependent on the probability parameter, requiring fine-tuning to achieve an optimal balance.
- Only assesses performance against noise in input data, not the ability to capture complex language structures or
semantics.
- Does not guarantee model performance on new, unseen, real-world data beyond the generated noisy test data.