# KolmogorovSmirnov

Executes a feature-wise Kolmogorov-Smirnov test to evaluate alignment with normal distribution in datasets.

**Purpose**: This metric employs the Kolmogorov-Smirnov (KS) test to evaluate the distribution of a dataset's
features. It specifically gauges whether the data from each feature aligns with a normal distribution, a common
presumption in many statistical methods and machine learning models.

**Test Mechanism**: This KS test calculates the KS statistic and the corresponding p-value for each column in a
dataset. It achieves this by contrasting the cumulative distribution function of the dataset's feature with an
ideal normal distribution. Subsequently, a feature-by-feature KS statistic and p-value are stored in a dictionary.
The specific threshold p-value (the value below which we reject the hypothesis that the data is drawn from a normal
distribution) is not firmly set within this implementation, allowing for definitional flexibility depending on the
specific application.

**Signs of High Risk**:
- Elevated KS statistic for a feature combined with a low p-value. This suggests a significant divergence between
the feature's distribution and a normal one.
- Features with notable deviations. These could create problems if the applicable model makes assumptions about
normal data distribution, thereby representing a risk.

**Strengths**:
- The KS test is acutely sensitive to differences in the location and shape of the empirical cumulative
distribution functions of two samples.
- It is non-parametric and does not presuppose any specific data distribution, making it adaptable to a range of
datasets.
- With its focus on individual features, it offers detailed insights into data distribution.

**Limitations**:
- The sensitivity of the KS test to disparities in data distribution tails can be excessive. Such sensitivity might
prompt false alarms about non-normal distributions, particularly in situations where these tail tendencies are
irrelevant to the model.
- It could become less effective when applied to multivariate distributions, considering that it's primarily
configured for univariate distributions.
- As a goodness-of-fit test, the KS test does not identify specific types of non-normality, such as skewness or
kurtosis, that could directly impact model fitting.