# Copyright © 2023-2024 ValidMind Inc. All rights reserved.
# See the LICENSE file in the root of this repository for details.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

"""
Entrypoint for regression datasets
"""
import pandas as pd

__all__ = [
    "fred",
    "lending_club",
]


def identify_frequencies(df):
    """
    Identify the frequency of each series in the DataFrame.

    :param df: Time-series DataFrame
    :return: DataFrame with two columns: 'Variable' and 'Frequency'
    """
    frequencies = []
    for column in df.columns:
        series = df[column].dropna()
        if not series.empty:
            freq = pd.infer_freq(series.index)
            label = freq
        else:
            label = None

        frequencies.append({"Variable": column, "Frequency": label})

    freq_df = pd.DataFrame(frequencies)

    return freq_df


def resample_to_common_frequency(df, common_frequency="MS"):
    # Make sure the index is a datetime index
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)

    # Create an empty DataFrame to store the resampled data
    resampled_df = pd.DataFrame()

    # Iterate through each variable and resample it to the common frequency
    for column in df.columns:
        series = df[column].dropna()
        inferred_freq = pd.infer_freq(series.index)

        if inferred_freq is None or inferred_freq != common_frequency:
            resampled_series = df[column].resample(common_frequency).interpolate()
        else:
            resampled_series = df[column]

        resampled_df[column] = resampled_series

    return resampled_df
