# tests\prompt_validation\Delimitation

Evaluates the proper use of delimiters in prompts provided to Large Language Models.

**Purpose:**
This test, dubbed the "Delimitation Test", is engineered to assess whether prompts provided to the Language
Learning Model (LLM) correctly use delimiters to mark different sections of the input. Well-delimited prompts
simplify the interpretation process for LLM, ensuring responses are precise and accurate.

**Test Mechanism:**
The test employs an LLM to examine prompts for appropriate use of delimiters such as triple quotation marks, XML
tags, and section titles. Each prompt is assigned a score from 1 to 10 based on its delimitation integrity. Those
with scores equal to or above the preset threshold (which is 7 by default, although it can be adjusted as
necessary) pass the test.

**Signs of High Risk:**

- The test identifies prompts where a delimiter is missing, improperly placed, or incorrect, which can lead to
misinterpretation by the LLM.
- A high-risk scenario may involve complex prompts with multiple tasks or diverse data where correct delimitation
is integral to understanding.
- Low scores (below the threshold) are a clear indicator of high risk.

**Strengths:**

- This test ensures clarity in the demarcation of different components of given prompts.
- It helps reduce ambiguity in understanding prompts, particularly for complex tasks.
- Scoring allows for quantified insight into the appropriateness of delimiter usage, aiding continuous improvement.

**Limitations:**

- The test only checks for the presence and placement of delimiter, not whether the correct delimiter type is used
for the specific data or task.
- It may not fully reveal the impacts of poor delimitation on LLM's final performance.
- Depending on the complexity of the tasks and prompts, the preset score threshold may not be refined enough,
requiring regular manual adjustment.