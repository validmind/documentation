# NegativeInstruction

Evaluates and grades the use of affirmative, proactive language over negative instructions in LLM prompts.

### Purpose

The Negative Instruction test is utilized to scrutinize the prompts given to a Large Language Model (LLM). The
objective is to ensure these prompts are expressed using proactive, affirmative language. The focus is on
instructions indicating what needs to be done rather than what needs to be avoided, thereby guiding the LLM more
efficiently towards the desired output.

### Test Mechanism

An LLM is employed to evaluate each prompt. The prompt is graded based on its use of positive instructions with
scores ranging between 1-10. This grade reflects how effectively the prompt leverages affirmative language while
shying away from negative or restrictive instructions. A prompt that attains a grade equal to or above a
predetermined threshold (7 by default) is regarded as adhering effectively to the best practices of positive
instruction. This threshold can be custom-tailored through the test parameters.

### Signs of High Risk

- Low score obtained from the LLM analysis, indicating heavy reliance on negative instructions in the prompts.
- Failure to surpass the preset minimum threshold.
- The LLM generates ambiguous or undesirable outputs as a consequence of the negative instructions used in the
prompt.

### Strengths

- Encourages the usage of affirmative, proactive language in prompts, aiding in more accurate and advantageous
model responses.
- The test result provides a comprehensible score, helping to understand how well a prompt follows the positive
instruction best practices.

### Limitations

- Despite an adequate score, a prompt could still be misleading or could lead to undesired responses due to factors
not covered by this test.
- The test necessitates an LLM for evaluation, which might not be available or feasible in certain scenarios.
- A numeric scoring system, while straightforward, may oversimplify complex issues related to prompt designing and
instruction clarity.
- The effectiveness of the test hinges significantly on the predetermined threshold level, which can be subjective
and may need to be adjusted according to specific use-cases.