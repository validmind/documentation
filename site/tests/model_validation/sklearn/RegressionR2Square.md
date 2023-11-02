# RegressionR2Square

**Purpose**: The purpose of the RegressionR2Square Metric test is to measure the overall goodness-of-fit of a
regression model. Specifically, this Python-based test evaluates the R-squared (R2) and Adjusted R-squared (Adj R2)
scores: two statistical measures within regression analysis used to evaluate the strength of the relationship
between the model's predictors and the response variable.

**Test Mechanism**: The test deploys the 'r2_score' method from the Scikit-learn metrics module, measuring the R2
score on both training and test sets. This score reflects the proportion of the variance in the dependent variable
that is predictable from independent variables. The test also considers the Adjusted R2 score, accounting for the
number of predictors in the model, to penalize model complexity and thus reduce overfitting. The Adjusted R2 score
will be smaller if unnecessary predictors are included in the model.

**Signs of High Risk**: Indicators of high risk in this test may include a low R2 or Adjusted R2 score, which would
suggest that the model does not explain much variation in the dependent variable. The occurrence of overfitting is
also a high-risk sign, evident when the R2 score on the training set is significantly higher than on the test set,
indicating that the model is not generalizing well to unseen data.

**Strengths**: The R2 score is a widely-used measure in regression analysis, providing a sound general indication
of model performance. It is easy to interpret and understand, as it is essentially representing the proportion of
the dependent variable's variance explained by the independent variables. The Adjusted R2 score complements the R2
score well by taking into account the number of predictors in the model, which helps control overfitting.

**Limitations**: R2 and Adjusted R2 scores can be sensitive to the inclusion of unnecessary predictors in the model
(even though Adjusted R2 is intended to penalize complexity). Their reliability might also lessen in cases of
non-linear relationships or when the underlying assumptions of linear regression are violated. Additionally, while
they summarize how well the model fits the data, they do not provide insight on whether the correct regression was
used, or whether certain key assumptions have been fulfilled.