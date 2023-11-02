# ScatterPlot

Creates a scatter plot matrix to visually analyze feature relationships, patterns, and outliers in a dataset.

**Purpose**: The ScatterPlot metric is designed to offer a visual analysis of a given dataset by constructing a
scatter plot matrix encapsulating all the dataset's features (or columns). Its primary function lies in unearthing
relationships, patterns, or outliers across different features, thus providing both quantitative and qualitative
insights into the multidimensional relationships within the dataset. This visual assessment aids in understanding
the efficacy of the chosen features for model training and their overall suitability.

**Test Mechanism**: Using the seaborn library, the ScatterPlot class creates the scatter plot matrix. The process
includes retrieving all columns from the dataset, verifying their existence, and subsequently generating a pairplot
for these columns. A kernel density estimate (kde) is utilized to present a smoother, univariate distribution along
the grid's diagonal. The final plot is housed in an array of Figure objects, each wrapping a matplotlib figure
instance for storage and future usage.

**Signs of High Risk**:
- The emergence of non-linear or random patterns across different feature pairs. This may suggest intricate
relationships unfit for linear presumptions.
- A lack of clear patterns or clusters which might point to weak or non-existent correlations among features, thus
creating a problem for certain model types.
- The occurrence of outliers as visual outliers in your data can adversely influence the model's performance.

**Strengths**:
- It offers insight into the multidimensional relationships among multiple features.
- It assists in identifying trends, correlations, and outliers which could potentially affect the model's
performance.
- As a diagnostic tool, it can validate whether certain assumptions made during the model-creation process, such as
linearity, hold true.
- The tool's versatility extends to its application for both regression and classification tasks.

**Limitations**:
- Scatter plot matrices may become cluttered and hard to decipher as the number of features escalates, resulting in
complexity and confusion.
- While extremely proficient in revealing pairwise relationships, these matrices may fail to illuminate complex
interactions that involve three or more features.
- These matrices are primarily visual tools, so the precision of quantitative analysis may be compromised.
- If not clearly visible, outliers can be missed, which could negatively affect model performance.
- It assumes that the dataset can fit into the computer's memory, which might not always be valid particularly for
extremely large datasets.