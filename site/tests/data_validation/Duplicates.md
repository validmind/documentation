# tests\data_validation\Duplicates

Tests dataset for duplicate entries, ensuring model reliability via data quality verification.

**Purpose**: The 'Duplicates' metric is designed to check for duplicate rows within the dataset provided to the
model. It serves as a measure of data quality, ensuring that the model isn't merely memorizing duplicate entries or
being swayed by redundant information. This is an important step in the pre-processing of data for both
classification and regression tasks.

**Test Mechanism**: This metric operates by checking each row for duplicates in the dataset. If a text column is
specified in the dataset, the test is conducted on this column; if not, the test is run on all feature columns. The
number and percentage of duplicates are calculated and returned in a DataFrame. Additionally, a test is passed if
the total count of duplicates falls below a specified minimum threshold.

**Signs of High Risk**:
- A high number of duplicate rows in the dataset. This can lead to overfitting where the model performs well on the
training data but poorly on unseen data.
- A high percentage of duplicate rows in the dataset. A large proportion of duplicate values could indicate that
there's a problem with data collection or processing.

**Strengths**:
- Assists in improving the reliability of the model's training process by ensuring the training data is not
contaminated with duplicate entries which can distort statistical analyses.
- Provides both absolute number and percentage value of duplicate rows, giving a thorough overview of data quality
- Highly customizable as it allows for setting a user-defined minimum threshold to determine if the test has been
passed.

**Limitations**:
- This test does not distinguish between benign duplicates (i.e., coincidental identical entries in different rows)
and problematic duplicates originating from data collection or processing errors.
- Since the test becomes more computationally intensive as the size of the dataset increases, it might not be
suitable for very large datasets.
- It can only check for exact duplicates and may miss semantically similar information packaged differently.