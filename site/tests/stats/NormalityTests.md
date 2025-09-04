# NormalityTests

Performs multiple normality tests on numerical features to assess distribution normality.

### Purpose

This test evaluates whether numerical features follow a normal distribution using
various statistical tests. Understanding distribution normality is crucial for
selecting appropriate statistical methods and model assumptions.

### Test Mechanism

The test applies multiple normality tests:
- Shapiro-Wilk test: Best for small to medium samples
- Anderson-Darling test: More sensitive to deviations in tails
- Kolmogorov-Smirnov test: General goodness-of-fit test

### Signs of High Risk

- Multiple normality tests failing consistently
- Very low p-values indicating strong evidence against normality
- Conflicting results between different normality tests

### Strengths

- Multiple statistical tests for robust assessment
- Clear pass/fail indicators for each test
- Suitable for different sample sizes

### Limitations

- Limited to numerical features only
- Some tests sensitive to sample size
- Perfect normality is rare in real data