# IQROutliersBarPlot

Visualizes outlier distribution across percentiles in numerical data using the Interquartile Range (IQR) method.

### Purpose

The InterQuartile Range Outliers Bar Plot (IQROutliersBarPlot) metric aims to visually analyze and evaluate the
extent of outliers in numeric variables based on percentiles. Its primary purpose is to clarify the dataset's
distribution, flag possible abnormalities in it, and gauge potential risks associated with processing potentially
skewed data, which can affect the machine learning model's predictive prowess.

### Test Mechanism

The examination invokes a series of steps:

1. For every numeric feature in the dataset, the 25th percentile (Q1) and 75th percentile (Q3) are calculated
before deriving the Interquartile Range (IQR), the difference between Q1 and Q3.
2. Subsequently, the metric calculates the lower and upper thresholds by subtracting Q1 from the `threshold` times
IQR and adding Q3 to `threshold` times IQR, respectively. The default `threshold` is set at 1.5.
3. Any value in the feature that falls below the lower threshold or exceeds the upper threshold is labeled as an
outlier.
4. The number of outliers are tallied for different percentiles, such as [0-25], [25-50], [50-75], and [75-100].
5. These counts are employed to construct a bar plot for the feature, showcasing the distribution of outliers
across different percentiles.

### Signs of High Risk

- A prevalence of outliers in the data, potentially skewing its distribution.
- Outliers dominating higher percentiles (75-100) which implies the presence of extreme values, capable of severely
influencing the model's performance.
- Certain features harboring most of their values as outliers, which signifies that these features might not
contribute positively to the model's forecasting ability.

### Strengths

- Effectively identifies outliers in the data through visual means, facilitating easier comprehension and offering
insights into the outliers' possible impact on the model.
- Provides flexibility by accommodating all numeric features or a chosen subset.
- Task-agnostic in nature; it is viable for both classification and regression tasks.
- Can handle large datasets as its operation does not hinge on computationally heavy operations.

### Limitations

- Its application is limited to numerical variables and does not extend to categorical ones.
- Relies on a predefined threshold (default being 1.5) for outlier identification, which may not be suitable for
all cases.
- Only reveals the presence and distribution of outliers and does not provide insights into how these outliers
might affect the model's predictive performance.
- The assumption that data is unimodal and symmetric may not always hold true. In cases with non-normal
distributions, the results can be misleading.