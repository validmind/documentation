# SHAPGlobalImportance

Evaluates and visualizes global feature importance using SHAP values for model explanation and risk identification.

### Purpose

The SHAP (SHapley Additive exPlanations) Global Importance metric aims to elucidate model outcomes by attributing
them to the contributing features. It assigns a quantifiable global importance to each feature via their respective
absolute Shapley values, thereby making it suitable for tasks like classification (both binary and multiclass).
This metric forms an essential part of model risk management.

### Test Mechanism

The exam begins with the selection of a suitable explainer which aligns with the model's type. For tree-based
models like XGBClassifier, RandomForestClassifier, CatBoostClassifier, TreeExplainer is used whereas for linear
models like LogisticRegression, XGBRegressor, LinearRegression, it is the LinearExplainer. Once the explainer
calculates the Shapley values, these values are visualized using two specific graphical representations:

1. Mean Importance Plot: This graph portrays the significance of individual features based on their absolute
Shapley values. It calculates the average of these absolute Shapley values across all instances to highlight the
global importance of features.

2. Summary Plot: This visual tool combines the feature importance with their effects. Every dot on this chart
represents a Shapley value for a certain feature in a specific case. The vertical axis is denoted by the feature
whereas the horizontal one corresponds to the Shapley value. A color gradient indicates the value of the feature,
gradually changing from low to high. Features are systematically organized in accordance with their importance.

### Signs of High Risk

- Overemphasis on certain features in SHAP importance plots, thus hinting at the possibility of model overfitting
- Anomalies such as unexpected or illogical features showing high importance, which might suggest that the model's
decisions are rooted in incorrect or undesirable reasoning
- A SHAP summary plot filled with high variability or scattered data points, indicating a cause for concern

### Strengths

- SHAP does more than just illustrating global feature significance, it offers a detailed perspective on how
different features shape the model's decision-making logic for each instance.
- It provides clear insights into model behavior.

### Limitations

- High-dimensional data can convolute interpretations.
- Associating importance with tangible real-world impact still involves a certain degree of subjectivity.