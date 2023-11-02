# RegressionCoeffsPlot

Visualizes regression coefficients with 95% confidence intervals to assess predictor variables' impact on response
variable.

**Purpose**: The Regression Coefficients with Confidence Intervals plot and metric aims to understand the impact of
predictor variables on the response variable in question. This understanding is achieved via the visualization and
analysis of the regression model by presenting the coefficients derived from the model along with their associated
95% confidence intervals. By doing so, it offers insights into the variability and uncertainty associated with the
model's estimates.

**Test Mechanism**: The test begins by extracting the estimated coefficients and their related standard errors from
the regression model under test. It then calculates and draws confidence intervals based on a 95% confidence level
(a standard convention in statistics). These intervals provide a range wherein the true value can be expected to
fall 95% of the time if the same regression were re-run multiple times with samples drawn from the same population.
This information is then visualized as a bar plot, with the predictor variables and their coefficients on the
x-axis and y-axis respectively and the confidence intervals represented as error bars.

**Signs of High Risk**:
* If the calculated confidence interval contains the zero value, it could mean the feature/coefficient in question
doesn't significantly contribute to prediction in the model.
* If there are multiple coefficients exhibiting this behavior, it might raise concerns about overall model
reliability.
* Very wide confidence intervals might indicate high uncertainty in the associated coefficient estimates.

**Strengths**:
* This metric offers a simple and easily comprehendible visualization of the significance and impact of individual
predictor variables in a regression model.
* By including confidence intervals, it enables an observer to evaluate the uncertainty around each coefficient
estimate.

**Limitations**:
* The test is dependent on a few assumptions about the data, namely normality of residuals and independence of
observations, which may not always be true for all types of datasets.
* The test does not consider multi-collinearity (correlation among predictor variables), which can potentially
distort the model and make interpretation of coefficients challenging.
* The test's application is limited to regression tasks and tabular datasets and is not suitable for other types of
machine learning assignments or data structures.