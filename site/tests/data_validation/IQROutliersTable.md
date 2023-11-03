# IQROutliersTable

Determines and summarizes outliers in numerical features using Interquartile Range method.

**Purpose**: The "Interquartile Range Outliers Table" (IQROutliersTable) metric has been designed for identifying
and summarizing outliers within numerical features of a dataset using the Interquartile Range (IQR) method. The
purpose of this exercise is crucial in the pre-processing of data as outliers can substantially distort the
statistical analysis and debilitate the performance of machine learning models.

**Test Mechanism**: The IQR, which is the range separating the first quartile (25th percentile) from the third
quartile (75th percentile), is calculated for each numerical feature within the dataset. An outlier is defined as a
data point falling below the "Q1 - 1.5 * IQR" or above "Q3 + 1.5 * IQR" range. The metric then computes the number
of outliers along with their minimum, 25th percentile, median, 75th percentile, and maximum values for each
numerical feature. If no specific features are chosen, the metric will apply to all numerical features in the
dataset. The default outlier threshold is set to 1.5, following the standard definition of outliers in statistical
analysis, although it can be customized by the user.

**Signs of High Risk**:
- High risk is indicated by a large number of outliers in multiple features.
- Outliers that are significantly distanced from the mean value of variables could potentially signal high risk.
- Data entry errors or other data quality issues could be manifested through extremely high or low outlier values.

**Strengths**:
- It yields a comprehensive summary of outliers for each numerical feature within the dataset. This enables the
user to pinpoint features with potential quality issues.
- The IQR method is not overly affected by extremely high or low outlier values as it is based on quartile
calculations.
- The versatility of this metric grants the ability to customize the method to work on selected features and set a
defined threshold for outliers.

**Limitations**:
- The metric might cause false positives if the variable of interest veers away from a normal or near-normal
distribution, notably in the case of skewed distributions.
- It does not extend to provide interpretation or recommendations for tackling outliers and relies on the user or a
data scientist to conduct further analysis of the results.
- As it only functions on numerical features, it cannot be used for categorical data.
- For data that has undergone heavy pre-processing, was manipulated, or inherently possesses a high kurtosis (heavy
tails), the pre-set threshold may not be optimal for outlier detection.