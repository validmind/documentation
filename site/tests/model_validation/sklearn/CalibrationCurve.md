# CalibrationCurve

Evaluates the calibration of probability estimates by comparing predicted probabilities against observed
frequencies.

### Purpose

The Calibration Curve test assesses how well a model's predicted probabilities align with actual
observed frequencies. This is crucial for applications requiring accurate probability estimates,
such as risk assessment, decision-making systems, and cost-sensitive applications where probability
calibration directly impacts business decisions.

### Test Mechanism

The test uses sklearn's calibration_curve function to:
1. Sort predictions into bins based on predicted probabilities
2. Calculate the mean predicted probability in each bin
3. Compare against the observed frequency of positive cases
4. Plot the results against the perfect calibration line (y=x)
The resulting curve shows how well the predicted probabilities match empirical probabilities.

### Signs of High Risk

- Significant deviation from the perfect calibration line
- Systematic overconfidence (predictions too close to 0 or 1)
- Systematic underconfidence (predictions clustered around 0.5)
- Empty or sparse bins indicating poor probability coverage
- Sharp discontinuities in the calibration curve
- Different calibration patterns across different probability ranges
- Consistent over/under estimation in critical probability regions
- Large confidence intervals in certain probability ranges

### Strengths

- Visual and intuitive interpretation of probability quality
- Identifies systematic biases in probability estimates
- Supports probability threshold selection
- Helps understand model confidence patterns
- Applicable across different classification models
- Enables comparison between different models
- Guides potential need for recalibration
- Critical for risk-sensitive applications

### Limitations

- Sensitive to the number of bins chosen
- Requires sufficient samples in each bin for reliable estimates
- May mask local calibration issues within bins
- Does not account for feature-dependent calibration issues
- Limited to binary classification problems
- Cannot detect all forms of miscalibration
- Assumes bin boundaries are appropriate for the problem
- May be affected by class imbalance