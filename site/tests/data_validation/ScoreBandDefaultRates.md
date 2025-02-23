# ScoreBandDefaultRates

Analyzes default rates and population distribution across credit score bands.

### Purpose

The Score Band Default Rates test evaluates the discriminatory power of credit scores by analyzing
default rates across different score bands. This helps validate score effectiveness, supports
policy decisions, and provides insights into portfolio risk distribution.

### Test Mechanism

The test segments the score distribution into bands and calculates key metrics for each band:
1. Population count and percentage in each band
2. Default rate within each band
3. Cumulative statistics across bands
The results show how well the scores separate good and bad accounts.

### Signs of High Risk

- Non-monotonic default rates across score bands
- Insufficient population in critical score bands
- Unexpected default rates for score ranges
- High concentration in specific score bands
- Similar default rates across adjacent bands
- Unstable default rates in key decision bands
- Extreme population skewness
- Poor risk separation between bands

### Strengths

- Clear view of score effectiveness
- Supports policy threshold decisions
- Easy to interpret and communicate
- Directly links to business decisions
- Shows risk segmentation power
- Identifies potential score issues
- Helps validate scoring model
- Supports portfolio monitoring

### Limitations

- Sensitive to band definition choices
- May mask within-band variations
- Requires sufficient data in each band
- Cannot capture non-linear patterns
- Point-in-time analysis only
- No temporal trend information
- Assumes band boundaries are appropriate
- May oversimplify risk patterns