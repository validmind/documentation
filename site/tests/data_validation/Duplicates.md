# Duplicates

Checks for and quantifies the presence of duplicate entries in the dataset or a specified column.

**Purpose**: The Duplicates test is designed to assess the data quality of an ML model by identifying any duplicate
entries in the data set. It focuses on seeking out duplication in a specified text column or among the primary keys
of the data set, which could have serious implications for the performance and integrity of the model. Duplicate
entries could potentially skew the data distribution and influence model training inaccurately.

**Test Mechanism**: This test operates by calculating the total number of duplicate entries in the data set. The
algorithm will count duplicates within the 'text_column' if this property is specified. If primary keys are
defined, the test will also be applied on them. The count of duplicates ('n_duplicates') is then compared to a
predefined minimum threshold (the default 'min_threshold' is set at 1) to determine whether the test has passed or
not. The results include the total number of duplicates as well as the percentage of duplicate rows in comparison
to the overall dataset ('p_duplicates').

**Signs of High Risk**:
- A large amount of duplicates, particularly those exceeding the predefined minimum threshold, point toward a high
risk situation.
- Overrepresentation of certain data which can lead to skewed results.
- Indication of inefficient data collecting techniques leading to data redundancy.
- Models that fail this test predominantly may necessitate a closer examination of their data preprocessing methods
or source data.

**Strengths**:
- The Duplicates test is highly adaptable, being capable of being used with both text data and tabular data formats.
- It is able to provide results both numerically and as a percentage of the total data set, allowing for a broader
understanding of the extent of duplication.
- Its utility lies in effectively flagging any data quality issues that could potentially upset model performance
and generate erroneous predictions.

**Limitations**:
- The Duplicates test solely targets exact duplication in entries, meaning it may overlook near-duplicates or
normalized forms of entries that might also affect data distribution and model integrity.
- Data variations caused by errors, phrasing changes, or inconsistencies may not be detected.
- A substantial number of duplicates in a datasets may not always denote poor data quality, as this can be
dependent on the nature of the data and the problem being addressed.