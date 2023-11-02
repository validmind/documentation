# OverfitDiagnosis

Detects and visualizes overfit regions in an ML model by comparing performance on training and test datasets.

**Purpose**: The OverfitDiagnosis test is devised to detect areas within a Machine Learning model that might be
prone to overfitting. It achieves this by comparing the model's performance on both the training and testing
datasets. These datasets are broken down into distinct sections defined by a Feature Space. Areas, where the model
underperforms by displaying high residual values or a significant amount of overfitting, are highlighted, prompting
actions for mitigation using regularization techniques such as L1 or L2 regularization, Dropout, Early Stopping or
data augmentation.

**Test Mechanism**: The metric conducts the test by executing the method 'run' on the default parameters and
metrics with 'accuracy' as the specified metric. It segments the feature space by binning crucial feature columns
from both the training and testing datasets. Then, the method computes the prediction results for each defined
region. Subsequently, the prediction's efficacy is evaluated, i.e., the model's performance gap (defined as the
discrepancy between the actual and the model's predictions) for both datasets is calculated and compared with a
preset cut-off value for the overfitting condition. A test failure presents an overfit model, whereas a pass
signifies a fit model. Meanwhile, the function also prepares figures further illustrating the regions with
overfitting.

**Signs of High Risk**: Indicators of a high-risk model are:
- A high 'gap' value indicating discrepancies in the training and testing data accuracy signals an overfit model.
- Multiple or vast overfitting zones within the feature space suggest overcomplication of the model.

**Strengths**:
- Presents a visual perspective by plotting regions with overfit issues, simplifying understanding of the model
structure.
- Permits a feature-focused assessment, which promotes specific, targeted modifications to the model.
- Caters to modifications of the testing parameters such as 'cut_off_percentage' and 'features_column' enabling a
personalized analysis.
- Handles both numerical and categorical features.

**Limitations**:
- Does not currently support regression tasks and is limited to classification tasks only.
- Ineffectual for text-based features, which in turn restricts its usage for Natural Language Processing models.
- Primarily depends on the bins setting, responsible for segmenting the feature space. Different bin configurations
might yield varying results.
- Utilization of a fixed cut-off percentage for making overfitting decisions, set arbitrarily, leading to a
possible risk of inaccuracy.
- Limitation of performance metrics to accuracy alone might prove inadequate for detailed examination, especially
for imbalanced datasets.