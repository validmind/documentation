# ScoreProbabilityAlignment

Analyzes the alignment between credit scores and predicted probabilities.

### Purpose

The Score-Probability Alignment test evaluates how well credit scores align with
predicted default probabilities. This helps validate score scaling, identify potential
calibration issues, and ensure scores reflect risk appropriately.

### Test Mechanism

The test:
1. Groups scores into bins
2. Calculates average predicted probability per bin
3. Tests monotonicity of relationship
4. Analyzes probability distribution within score bands

### Signs of High Risk

- Non-monotonic relationship between scores and probabilities
- Large probability variations within score bands
- Unexpected probability jumps between adjacent bands
- Poor alignment with expected odds-to-score relationship
- Inconsistent probability patterns across score ranges
- Clustering of probabilities at extreme values
- Score bands with similar probability profiles
- Unstable probability estimates in key decision bands

### Strengths

- Direct validation of score-to-probability relationship
- Identifies potential calibration issues
- Supports score band validation
- Helps understand model behavior
- Useful for policy setting
- Visual and numerical results
- Easy to interpret
- Supports regulatory documentation

### Limitations

- Sensitive to bin selection
- Requires sufficient data per bin
- May mask within-bin variations
- Point-in-time analysis only
- Cannot detect all forms of miscalibration
- Assumes scores should align with probabilities
- May oversimplify complex relationships
- Limited to binary outcomes