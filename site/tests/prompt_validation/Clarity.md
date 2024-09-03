# Clarity

Evaluates and scores the clarity of prompts in a Large Language Model based on specified guidelines.

### Purpose

The Clarity evaluation metric is used to assess how clear the prompts of a Large Language Model (LLM) are. This
assessment is particularly important because clear prompts assist the LLM in more accurately interpreting and
responding to instructions.

### Test Mechanism

The evaluation uses an LLM to scrutinize the clarity of prompts, factoring in considerations such as the inclusion
of relevant details, persona adoption, step-by-step instructions, usage of examples, and specification of desired
output length. Each prompt is rated on a clarity scale of 1 to 10, and any prompt scoring at or above the preset
threshold (default of 7) will be marked as clear. It is important to note that this threshold can be adjusted via
test parameters, providing flexibility in the evaluation process.

### Signs of High Risk

- Prompts that consistently score below the clarity threshold
- Repeated failure of prompts to adhere to guidelines for clarity, including detail inclusion, persona adoption,
explicit step-by-step instructions, use of examples, and specification of output length

### Strengths

- Encourages the development of more effective prompts that aid the LLM in interpreting instructions accurately
- Applies a quantifiable measure (a score from 1 to 10) to evaluate the clarity of prompts
- Threshold for clarity is adjustable, allowing for flexible evaluation depending on the context

### Limitations

- Scoring system is subjective and relies on the AI’s interpretation of 'clarity
- The test assumes that all required factors (detail inclusion, persona adoption, step-by-step instructions, use of
examples, and specification of output length) contribute equally to clarity, which might not always be the case
- The evaluation may not be as effective if used on non-textual models