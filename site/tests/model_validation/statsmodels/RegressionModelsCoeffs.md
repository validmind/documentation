# RegressionModelsCoeffs

Compares feature importance by evaluating and contrasting coefficients of different regression models.

### Purpose

The 'RegressionModelsCoeffs' metric is utilized to evaluate and compare coefficients of different regression models
trained on the same dataset. By examining how each model weighted the importance of different features during
training, this metric provides key insights into which factors have the most impact on the model's predictions and
how these patterns differ across models.

### Test Mechanism

This test operates by extracting the coefficients of each regression model using the 'regression_coefficients()
method. These coefficients are then consolidated into a dataframe, with each row representing a model and columns
corresponding to each feature's coefficient. It must be noted that this test is exclusive to 'statsmodels' and 'R
models, other models will result in a 'SkipTestError'.

### Signs of High Risk

- Discrepancies in how different models weight the same features
- Unexpectedly high or low coefficients
- The test is inapplicable to certain models because they are not from 'statsmodels' or 'R' libraries

### Strengths

- Enables insight into the training process of different models
- Allows comparison of feature importance across models
- Through the review of feature coefficients, the test provides a more transparent evaluation of the model and
highlights significant weights and biases in the training procedure

### Limitations

- The test is only compatible with 'statsmodels' and 'R' regression models
- While the test provides contrast in feature weightings among models, it does not establish the most appropriate
or accurate weighting, thus remaining subject to interpretation
- It does not account for potential overfitting or underfitting of models
- The computed coefficients might not lead to effective performance on unseen data