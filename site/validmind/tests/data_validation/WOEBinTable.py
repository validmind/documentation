# Copyright © 2023-2024 ValidMind Inc. All rights reserved.
# See the LICENSE file in the root of this repository for details.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

import pandas as pd
import scorecardpy as sc

from validmind import tags, tasks
from validmind.errors import SkipTestError
from validmind.vm_models import VMDataset


@tags("tabular_data", "categorical_data")
@tasks("classification")
def WOEBinTable(dataset: VMDataset, breaks_adj: list = None):
    """
    Assesses the Weight of Evidence (WoE) and Information Value (IV) of each feature to evaluate its predictive power
    in a binary classification model.

    ### Purpose

    The Weight of Evidence (WoE) and Information Value (IV) test is designed to evaluate the predictive power of each
    feature in a machine learning model. This test generates binned groups of values from each feature, computes the
    WoE and IV for each bin, and provides insights into the relationship between each feature and the target variable,
    illustrating their contribution to the model's predictive capabilities.

    ### Test Mechanism

    The test uses the `scorecardpy.woebin` method to perform automatic binning of the dataset based on WoE. The method
    accepts a list of break points for binning numeric variables through the parameter `breaks_adj`. If no breaks are
    provided, it uses default binning. The bins are then used to calculate the WoE and IV values, effectively creating
    a dataframe that includes the bin boundaries, WoE, and IV values for each feature. A target variable is required
    in the dataset to perform this analysis.

    ### Signs of High Risk

    - High IV values, indicating variables with excessive predictive power which might lead to overfitting.
    - Errors during the binning process, potentially due to inappropriate data types or poorly defined bins.

    ### Strengths

    - Highly effective for feature selection in binary classification problems, as it quantifies the predictive
    information within each feature concerning the binary outcome.
    - The WoE transformation creates a monotonic relationship between the target and independent variables.

    ### Limitations

    - Primarily designed for binary classification tasks, making it less applicable or reliable for multi-class
    classification or regression tasks.
    - Potential difficulties if the dataset has many features, non-binnable features, or non-numeric features.
    - The metric does not help in distinguishing whether the observed predictive factor is due to data randomness or a
    true phenomenon.
    """
    df = dataset.df

    non_numeric_cols = df.select_dtypes(exclude=["int64", "float64"]).columns
    df[non_numeric_cols] = df[non_numeric_cols].astype(str)

    try:
        bins = sc.woebin(df, dataset.target_column, breaks_list=breaks_adj)
    except Exception as e:
        raise SkipTestError(f"Error during binning: {e}")

    return {
        "Weight of Evidence (WoE) and Information Value (IV)": (
            pd.concat(bins.values(), keys=bins.keys())
            .reset_index()
            .drop(columns=["variable"])
            .rename(columns={"level_0": "variable"})
            .assign(bin_number=lambda x: x.groupby("variable").cumcount())
        )
    }
