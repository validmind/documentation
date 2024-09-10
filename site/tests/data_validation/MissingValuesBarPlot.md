# MissingValuesBarPlot

Assesses the percentage and distribution of missing values in the dataset via a bar plot, with emphasis on
identifying high-risk columns based on a user-defined threshold.

### Purpose

The 'MissingValuesBarPlot' metric provides a color-coded visual representation of the percentage of missing values
for each column in an ML model's dataset. The primary purpose of this metric is to easily identify and quantify
missing data, which are essential steps in data preprocessing. The presence of missing data can potentially skew
the model's predictions and decrease its accuracy. Additionally, this metric uses a pre-set threshold to categorize
various columns into ones that contain missing data above the threshold (high risk) and below the threshold (less
risky).

### Test Mechanism

The test mechanism involves scanning each column in the input dataset and calculating the percentage of missing
values. It then compares each column's missing data percentage with the predefined threshold, categorizing columns
with missing data above the threshold as high-risk. The test generates a bar plot in which columns with missing
data are represented on the y-axis and their corresponding missing data percentages are displayed on the x-axis.
The color of each bar reflects the missing data percentage in relation to the threshold: grey for values below the
threshold and light coral for those exceeding it. The user-defined threshold is represented by a red dashed line on
the plot.

### Signs of High Risk

- Columns with higher percentages of missing values beyond the threshold are high-risk. These are visually
represented by light coral bars on the bar plot.

### Strengths

- Helps in quickly identifying and quantifying missing data across all columns of the dataset.
- Facilitates pattern recognition through visual representation.
- Enables customization of the level of risk tolerance via a user-defined threshold.
- Supports both classification and regression tasks, sharing its versatility.

### Limitations

- It only considers the quantity of missing values, not differentiating between different types of missingness
(Missing completely at random - MCAR, Missing at random - MAR, Not Missing at random - NMAR).
- It doesn't offer insights into potential approaches for handling missing entries, such as various imputation
strategies.
- The metric does not consider possible impacts of the missing data on the model's accuracy or precision.
- Interpretation of the findings and the next steps might require an expert understanding of the field.