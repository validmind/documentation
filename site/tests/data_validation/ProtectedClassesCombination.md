# ProtectedClassesCombination

Visualizes combinations of protected classes and their corresponding error metric differences.

### Purpose

This test aims to provide insights into how different combinations of protected classes affect various error metrics,
particularly the false negative rate (FNR) and false positive rate (FPR). By visualizing these combinations,
it helps identify potential biases or disparities in model performance across different intersectional groups.

### Test Mechanism

The test performs the following steps:
1. Combines the specified protected class columns to create a single multi-class category.
2. Calculates error metrics (FNR, FPR, etc.) for each combination of protected classes.
3. Generates visualizations showing the distribution of these metrics across all class combinations.

### Signs of High Risk

- Large disparities in FNR or FPR across different protected class combinations.
- Consistent patterns of higher error rates for specific combinations of protected attributes.
- Unexpected or unexplainable variations in error metrics between similar group combinations.

### Strengths

- Provides a comprehensive view of intersectional fairness across multiple protected attributes.
- Allows for easy identification of potentially problematic combinations of protected classes.
- Visualizations make it easier to spot patterns or outliers in model performance across groups.

### Limitations

- May become complex and difficult to interpret with a large number of protected classes or combinations.
- Does not provide statistical significance of observed differences.
- Visualization alone may not capture all nuances of intersectional fairness.