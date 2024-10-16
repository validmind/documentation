# ProtectedClassesDisparity

Investigates disparities in model performance across different protected class segments.

### Purpose

This test aims to identify and quantify potential biases in model outcomes by comparing various performance metrics
across different segments of protected classes. It helps in assessing whether the model produces discriminatory
outcomes for certain groups, which is crucial for ensuring fairness in machine learning models.

### Test Mechanism

The test performs the following steps:
1. Calculates performance metrics (e.g., false negative rate, false positive rate, true positive rate) for each segment
of the specified protected classes.
2. Computes disparity ratios by comparing these metrics between different segments and a reference group.
3. Generates visualizations showing the disparities and their relation to a user-defined disparity tolerance threshold.
4. Produces a comprehensive table with various disparity metrics for detailed analysis.

### Signs of High Risk

- Disparity ratios exceeding the specified disparity tolerance threshold.
- Consistent patterns of higher error rates or lower performance for specific protected class segments.
- Statistically significant differences in performance metrics across segments.

### Strengths

- Provides a comprehensive view of model fairness across multiple protected attributes and metrics.
- Allows for easy identification of problematic disparities through visual and tabular representations.
- Customizable disparity tolerance threshold to align with specific use-case requirements.
- Applicable to various performance metrics, offering a multi-faceted analysis of model fairness.

### Limitations

- Relies on a predefined reference group for each protected class, which may not always be the most appropriate choice.
- Does not account for intersectionality between different protected attributes.
- The interpretation of results may require domain expertise to understand the implications of observed disparities.