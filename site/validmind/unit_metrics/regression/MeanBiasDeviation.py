# Copyright © 2023-2024 ValidMind Inc. All rights reserved.
# See the LICENSE file in the root of this repository for details.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

import numpy as np

from validmind import tags, tasks


@tags("regression")
@tasks("regression")
def MeanBiasDeviation(model, dataset):
    """Calculates the mean bias deviation for a regression model."""
    return np.mean(dataset.y - dataset.y_pred(model))
