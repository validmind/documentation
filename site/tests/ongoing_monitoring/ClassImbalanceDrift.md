# ClassImbalanceDrift

Evaluates drift in class distribution between reference and monitoring datasets.

### Purpose

The Class Imbalance Drift test is designed to detect changes in the distribution of target classes
over time. By comparing class proportions between reference and monitoring datasets, this test helps
identify whether the population structure remains stable in production. This is crucial for
understanding if the model continues to operate under similar class distribution assumptions and
whether retraining might be necessary due to significant shifts in class balance.

### Test Mechanism

This test proceeds by calculating class percentages for both reference and monitoring datasets.
It computes the proportion of each class and quantifies drift as the percentage difference in these
proportions between datasets. The test provides both visual and numerical comparisons of class
distributions, with special attention to changes that exceed the specified drift threshold.
Population stability is assessed on a class-by-class basis.

### Signs of High Risk

- Large shifts in class proportions exceeding the threshold
- Systematic changes affecting multiple classes
- Appearance of new classes or disappearance of existing ones
- Significant changes in minority class representation
- Reversal of majority-minority class relationships
- Unexpected changes in class ratios

### Strengths

- Provides clear visualization of distribution changes
- Identifies specific classes experiencing drift
- Enables early detection of population shifts
- Includes standardized drift threshold evaluation
- Supports both binary and multiclass problems
- Maintains interpretable percentage-based metrics

### Limitations

- Does not account for feature distribution changes
- Cannot identify root causes of class drift
- May be sensitive to small sample sizes
- Limited to target variable distribution only
- Requires sufficient samples per class
- May not capture subtle distribution changes