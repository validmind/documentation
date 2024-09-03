# Robustness

Assesses the robustness of prompts provided to a Large Language Model under varying conditions and contexts.

### Purpose

The Robustness test is meant to evaluate the resilience and reliability of prompts provided to a Language Learning
Model (LLM). The aim of this test is to guarantee that the prompts consistently generate accurate and expected
outputs, even in diverse or challenging scenarios.

### Test Mechanism

The Robustness test appraises prompts under various conditions, alterations, and contexts to ascertain their
stability in producing consistent responses from the LLM. Factors evaluated include different phrasings, inclusion
of potential distracting elements, and various input complexities. By default, the test generates 10 inputs for a
prompt but can be adjusted according to test parameters.

### Signs of High Risk

- If the output from the tests diverges extensively from the expected results, this indicates high risk.
- When the prompt doesn't give a consistent performance across various tests.
- A high risk is indicated when the prompt is susceptible to breaking, especially when the output is expected to be
of a specific type.

### Strengths

- The robustness test helps to ensure stable performance of the LLM prompts and lowers the chances of generating
unexpected or off-target outputs.
- This test is vital for applications where predictability and reliability of the LLM’s output are crucial.

### Limitations

- Currently, the test only supports single-variable prompts, which restricts its application to more complex models.
- When there are too many target classes (over 10), the test is skipped, which can leave potential vulnerabilities
unchecked in complex multi-class models.
- The test may not account for all potential conditions or alterations that could show up in practical use
scenarios.