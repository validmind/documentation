# ScoreBandsDrift

Analyzes drift in population distribution and default rates across score bands.

### Purpose

The Score Bands Drift test is designed to evaluate changes in score-based risk segmentation
over time. By comparing population distribution and default rates across score bands between
reference and monitoring datasets, this test helps identify whether the model's risk
stratification remains stable in production. This is crucial for understanding if the model's
scoring behavior maintains its intended risk separation and whether specific score ranges
have experienced significant shifts.

### Test Mechanism

This test proceeds by segmenting scores into predefined bands and analyzing three key metrics
across these bands: population distribution, predicted default rates, and observed default
rates. For each band, it computes these metrics for both reference and monitoring datasets
and quantifies drift as percentage changes. The test provides both detailed band-by-band
comparisons and overall stability assessment, with special attention to bands showing
significant drift.

### Signs of High Risk

- Large shifts in population distribution across bands
- Significant changes in default rates within bands
- Inconsistent drift patterns between adjacent bands
- Divergence between predicted and observed rates
- Systematic shifts in risk concentration
- Empty or sparse score bands in monitoring data

### Strengths

- Provides comprehensive view of score-based drift
- Identifies specific score ranges with instability
- Enables comparison of multiple risk metrics
- Includes both distribution and performance drift
- Supports business-relevant score segmentation
- Maintains interpretable drift thresholds

### Limitations

- Sensitive to choice of score band boundaries
- Requires sufficient samples in each band
- Cannot suggest optimal band adjustments
- May not capture within-band distribution changes
- Limited to predefined scoring metrics
- Complex interpretation with multiple drift signals