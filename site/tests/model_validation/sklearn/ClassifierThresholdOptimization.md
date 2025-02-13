# ClassifierThresholdOptimization

Analyzes and visualizes different threshold optimization methods for binary classification models.

### Purpose

The Classifier Threshold Optimization test identifies optimal decision thresholds using various
methods to balance different performance metrics. This helps adapt the model's decision boundary
to specific business requirements, such as minimizing false positives in fraud detection or
achieving target recall in medical diagnosis.

### Test Mechanism

The test implements multiple threshold optimization methods:
1. Youden's J statistic (maximizing sensitivity + specificity - 1)
2. F1-score optimization (balancing precision and recall)
3. Precision-Recall equality point
4. Target recall achievement
5. Naive (0.5) threshold
For each method, it computes ROC and PR curves, identifies optimal points, and provides
comprehensive performance metrics at each threshold.

### Signs of High Risk

- Large discrepancies between different optimization methods
- Optimal thresholds far from the default 0.5
- Poor performance metrics across all thresholds
- Significant gap between achieved and target recall
- Unstable thresholds across different methods
- Extreme trade-offs between precision and recall
- Threshold optimization showing minimal impact
- Business metrics not improving with optimization

### Strengths

- Multiple optimization strategies for different needs
- Visual and numerical results for comparison
- Support for business-driven optimization (target recall)
- Comprehensive performance metrics at each threshold
- Integration with ROC and PR curves
- Handles class imbalance through various metrics
- Enables informed threshold selection
- Supports cost-sensitive decision making

### Limitations

- Assumes cost of false positives/negatives are known
- May need adjustment for highly imbalanced datasets
- Threshold might not be stable across different samples
- Cannot handle multi-class problems directly
- Optimization methods may conflict with business needs
- Requires sufficient validation data
- May not capture temporal changes in optimal threshold
- Single threshold may not be optimal for all subgroups

Args:
dataset: VMDataset containing features and target
model: VMModel containing predictions
methods: List of methods to compare (default: ['youden', 'f1', 'precision_recall'])
target_recall: Target recall value if using 'target_recall' method

Returns:
Dictionary containing:
- table: DataFrame comparing different threshold optimization methods
(using weighted averages for precision, recall, and f1)
- figure: Plotly figure showing ROC and PR curves with optimal thresholds