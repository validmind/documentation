# StabilityAnalysisTranslation

Evaluates robustness of text embeddings models to noise introduced by translating the original text to another
language and back.

### Purpose

The purpose of this test is to assess the robustness of text embeddings models under the influence of noise. The
noise in this scenario is introduced by translating the original text into another language and then translating it
back to the original language. Any significant changes in the model's output between the original and
translated-then-retranslated texts can be indicators of the model's lack of robustness to noise.

### Test Mechanism

The test mechanism involves several steps:

1. Initialize the Marian tokenizer and model for both source and target languages.
2. Translate the data from the source language to the target language.
3. Translate the translated data back into the source language.
4. Compare the original data with the data that has been translated and back-translated to observe any significant
changes.

The threshold of this test output would then be determined by the tolerance level of the model to these potentially
noisy instances.

### Signs of High Risk

- Large discrepancies between the original and double-translated text, indicating a high level of risk and a lack
of robustness to noise.
- Translations that do not closely maintain the meaning and context of the original language, suggesting inadequate
robustness against this type of noise.

### Strengths

- An effective way to assess the model’s sensitivity and robustness to language translation noise.
- Provides a realistic scenario which the model might encounter in real-world applications by using translation to
introduce noise.
- Tests the model’s capacity to maintain semantic meaning under translational perturbations, extending beyond
simple lexical changes.

### Limitations

- Relies solely on translation-related noise, potentially overlooking other types of noise such as typographical
errors, grammatical mistakes, or random word substitutions.
- Inaccuracies or discrepancies in the translation process itself might influence the resultant robustness score
rather than reflect an inherent failing of the model.
- Predominantly language-dependent, thus might not fully capture robustness for languages with fewer resources or
those highly dissimilar to the source language.