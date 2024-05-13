# tests\data_validation\Skewness

Evaluates the skewness of numerical data in a machine learning model and checks if it falls below a set maximum
threshold.

**Purpose**: The purpose of the Skewness test is to measure the asymmetry in the distribution of data within a
predictive machine learning model. Specifically, it evaluates the divergence of said distribution from a normal
distribution. In understanding the level of skewness, we can potentially identify issues with data quality, an
essential component for optimizing the performance of traditional machine learning models in both classification
and regression settings.

**Test Mechanism**: This test calculates skewness of numerical columns in a dataset, which is extracted from the
DataFrame, specifically focusing on numerical data types. The skewness value is then contrasted against a
predetermined maximum threshold, set by default to 1. The skewness value under review is deemed to have passed the
test only if it is less than this maximum threshold; otherwise, the test is considered 'fail'. Subsequently, the
test results of each column, together with the skewness value and column name, are cached.

**Signs of High Risk**:

- The presence of substantial skewness levels that significantly exceed the maximum threshold is an indication of
skewed data distribution and subsequently high model risk.
- Persistent skewness in data could signify that the foundational assumptions of the machine learning model may not
be applicable, potentially leading to subpar model performance, erroneous predictions, or biased inferences.

**Strengths**:

- Fast and efficient identification of unequal data
- distributions within a machine learning model is enabled by the skewness test.
- The maximum threshold parameter can be adjusted to meet the user's specific needs, enhancing the test's
versatility.

**Limitations**:

- The test only evaluates numeric columns, which means that data in non-numeric columns could still include bias or
problematic skewness that this test does not capture.
- The test inherently assumes that the data should follow a normal distribution, an expectation which may not
always be met in real-world data.
- The risk grading is largely dependent on a subjective threshold, which may result in excessive strictness or
leniency depending upon selection. This factor might require expert input and recurrent iterations for refinement.