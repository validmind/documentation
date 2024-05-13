# tests\data_validation\BivariateHistograms

Generates bivariate histograms for paired features, aiding in visual inspection of categorical variables
distributions and correlations.

**Purpose**: This metric, dubbed BivariateHistograms, is primarily used for visual data analysis via the inspection
of variable distribution, specifically categorical variables. Its main objective is to ascertain any potential
correlations between these variables and distributions within each defined target class. This is achieved by
offering an intuitive avenue into gaining insights into the characteristics of the data and any plausible patterns
therein.

**Test Mechanism**: The working mechanism of the BivariateHistograms module revolves around an input dataset and a
series of feature pairs. It uses seaborn's histogram plotting function and matplotlib techniques to create
bivariate histograms for each feature pair in the dataset. Two histograms, stratified by the target column status,
are produced for every pair of features. This enables the telling apart of different target statuses through color
differentiation. The module also offers optional functionality for restricting the data by a specific status
through the target_filter parameter.

**Signs of High Risk**:
- Irregular or unexpected distributions of data across the different categories.
- Highly skewed data distributions.
- Significant deviations from the perceived 'normal' or anticipated distributions.
- Large discrepancies in distribution patterns between various target statuses.

**Strengths**:
- Owing to its simplicity, the histogram-based approach is easy to implement and interpret which translates to
quick insights.
- The metrics provides a consolidated view of the distribution of data across different target conditions for each
variable pair, thereby assisting in highlighting potential correlations and patterns.
- It proves advantageous in spotting anomalies, comprehending interactions among features, and facilitating
exploratory data analysis.

**Limitations**:
- Its simplicity may be a drawback when it comes to spotting intricate or complex patterns in data.
- Overplotting might occur when working with larger datasets.
- The metric is only applicable to categorical data, and offers limited insights for numerical or continuous
variables.
- The interpretation of visual results hinges heavily on the expertise of the observer, possibly leading to
subjective analysis.