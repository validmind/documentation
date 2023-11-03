# RegressionModelSensitivityPlot

Tests the sensitivity of a regression model to variations in independent variables by applying shocks and
visualizing the effects.

**Purpose**: The Regression Sensitivity Plot metric is designed to perform sensitivity analysis on regression
models. This metric aims to measure the impact of slight changes (shocks) applied to individual variables on the
system's outcome while keeping all other variables constant. By doing so, it analyzes the effects of each
independent variable on the dependent variable within the regression model and helps identify significant risk
factors that could substantially influence the model's output.

**Test Mechanism**: This metric operates by initially applying shocks of varying magnitudes, defined by specific
parameters, to each of the model's features, one at a time. With all other variables held constant, a new
prediction is made for each dataset subjected to shocks. Any changes in the model's predictions are directly
attributed to the shocks applied. In the event that the transformation parameter is set to "integrate", initial
predictions and target values undergo transformation via an integration function before being plotted. Lastly, a
plot demonstrating observed values against predicted values for each model is generated, showcasing a distinct line
graph illustrating predictions for each shock.

**Signs of High Risk**:
- If the plot exhibits drastic alterations in model predictions consequent to minor shocks to an individual
variable, it may indicate high risk. This underscores potentially high model sensitivity to changes in that
variable, suggesting over-dependence on that variable for predictions.
- Unusually high or unpredictable shifts in response to shocks may also denote potential model instability or
overfitting.

**Strengths**:
- The metric allows identification of variables strongly influencing the model outcomes, paving the way for
understanding feature importance.
- It generates visual plots which make the results easily interpretable even to non-technical stakeholders.
- Beneficial in identifying overfitting and detecting unstable models that over-react to minor changes in variables.

**Limitations**:
- The metric operates on the assumption that all other variables remain unchanged during the application of a
shock. However, real-world situations where variables may possess intricate interdependencies may not always
reflect this.
- It is best compatible with linear models and may not effectively evaluate the sensitivity of non-linear model
configurations.
- The metric does not provide a numerical risk measure. It offers only a visual representation, which may invite
subjectivity in interpretation.