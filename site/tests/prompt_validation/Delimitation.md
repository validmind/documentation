# Delimitation

Evaluates the proper use of delimiters in prompts provided to Large Language Models.

### Purpose

The Delimitation Test aims to assess whether prompts provided to the Language Learning Model (LLM) correctly use
delimiters to mark different sections of the input. Well-delimited prompts help simplify the interpretation process
for the LLM, ensuring that the responses are precise and accurate.

### Test Mechanism

The test employs an LLM to examine prompts for appropriate use of delimiters such as triple quotation marks, XML
tags, and section titles. Each prompt is assigned a score from 1 to 10 based on its delimitation integrity. Prompts
with scores equal to or above the preset threshold (which is 7 by default, although it can be adjusted as
necessary) pass the test.

### Signs of High Risk

- Prompts missing, improperly placed, or incorrectly used delimiters, leading to misinterpretation by the LLM.
- High-risk scenarios with complex prompts involving multiple tasks or diverse data where correct delimitation is
crucial.
- Scores below the threshold, indicating a high risk.

### Strengths

- Ensures clarity in demarcating different components of given prompts.
- Reduces ambiguity in understanding prompts, especially for complex tasks.
- Provides a quantified insight into the appropriateness of delimiter usage, aiding continuous improvement.

### Limitations

- Only checks for the presence and placement of delimiters, not whether the correct delimiter type is used for the
specific data or task.
- May not fully reveal the impacts of poor delimitation on the LLM's final performance.
- The preset score threshold may not be refined enough for complex tasks and prompts, requiring regular manual
adjustment.