# BoxPierce

Detects autocorrelation in time-series data through the Box-Pierce test to validate model performance.

### Purpose

The Box-Pierce test is utilized to detect the presence of autocorrelation in a time-series dataset.
Autocorrelation, or serial correlation, refers to the degree of similarity between observations based on the
temporal spacing between them. This test is essential for affirming the quality of a time-series model by ensuring
that the error terms in the model are random and do not adhere to a specific pattern.

### Test Mechanism

The implementation of the Box-Pierce test involves calculating a test statistic along with a corresponding p-value
derived from the dataset features. These quantities are used to test the null hypothesis that posits the data to be
independently distributed. This is achieved by iterating over every feature column in the time-series data and
applying the `acorr_ljungbox` function of the statsmodels library. The function yields the Box-Pierce test
statistic as well as the respective p-value, all of which are cached as test results.

### Signs of High Risk

- A low p-value, typically under 0.05 as per statistical convention, throws the null hypothesis of independence
into question. This implies that the dataset potentially houses autocorrelations, thus indicating a high-risk
scenario concerning model performance.
- Large Box-Pierce test statistic values may indicate the presence of autocorrelation.

### Strengths

- Detects patterns in data that are supposed to be random, thereby ensuring no underlying autocorrelation.
- Can be computed efficiently given its low computational complexity.
- Can be widely applied to most regression problems, making it very versatile.

### Limitations

- Assumes homoscedasticity (constant variance) and normality of residuals, which may not always be the case in
real-world datasets.
- May exhibit reduced power for detecting complex autocorrelation schemes such as higher-order or negative
correlations.
- It only provides a general indication of the existence of autocorrelation, without providing specific insights
into the nature or patterns of the detected autocorrelation.
- In the presence of trends or seasonal patterns, the Box-Pierce test may yield misleading results.
- Applicability is limited to time-series data, which limits its overall utility.