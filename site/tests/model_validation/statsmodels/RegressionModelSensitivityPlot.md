# RegressionModelSensitivityPlot

Assesses the sensitivity of a regression model to changes in independent variables by applying shocks and
visualizing the impact.

### Purpose

The Regression Sensitivity Plot test is designed to perform sensitivity analysis on regression models. This test
aims to measure the impact of slight changes (shocks) applied to individual variables on the system's outcome while
keeping all other variables constant. By doing so, it analyzes the effects of each independent variable on the
dependent variable within the regression model, helping identify significant risk factors that could substantially
influence the model's output.

### Test Mechanism

This test operates by initially applying shocks of varying magnitudes, defined by specific parameters, to each of
the model's features, one at a time. With all other variables held constant, a new prediction is made for each
dataset subjected to shocks. Any changes in the model's predictions are directly attributed to the shocks applied.
If the transformation parameter is set to "integrate," initial predictions and target values undergo transformation
via an integration function before being plotted. Finally, a plot demonstrating observed values against predicted
values for each model is generated, showcasing a distinct line graph illustrating predictions for each shock.

### Signs of High Risk

- Drastic alterations in model predictions due to minor shocks to an individual variable, indicating high
sensitivity and potential over-dependence on that variable.
- Unusually high or unpredictable shifts in response to shocks, suggesting potential model instability or
overfitting.

### Strengths

- Helps identify variables that strongly influence model outcomes, aiding in understanding feature importance.
- Generates visual plots, making results easily interpretable even to non-technical stakeholders.
- Useful in identifying overfitting and detecting unstable models that react excessively to minor variable changes.

### Limitations

- Operates on the assumption that all other variables remain unchanged during the application of a shock, which may
not reflect real-world interdependencies.
- Best compatible with linear models and may not effectively evaluate the sensitivity of non-linear models.
- Provides a visual representation without a numerical risk measure, potentially introducing subjectivity in
interpretation.