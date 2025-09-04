# OutlierDetection

Detects outliers in numerical features using multiple statistical methods.

### Purpose

This test identifies outliers in numerical features using various statistical
methods including IQR, Z-score, and Isolation Forest. It provides comprehensive
outlier detection to help identify data quality issues and potential anomalies.

### Test Mechanism

The test applies multiple outlier detection methods:
- IQR method: Values beyond Q1 - 1.5*IQR or Q3 + 1.5*IQR
- Z-score method: Values with |z-score| > threshold
- Isolation Forest: ML-based anomaly detection

### Signs of High Risk

- High percentage of outliers indicating data quality issues
- Inconsistent outlier detection across methods
- Extreme outliers that significantly deviate from normal patterns

### Strengths

- Multiple detection methods for robust outlier identification
- Customizable thresholds for different sensitivity levels
- Clear summary of outlier patterns across features

### Limitations

- Limited to numerical features only
- Some methods assume normal distributions
- Threshold selection can be subjective