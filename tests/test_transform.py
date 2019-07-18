from src.transform import *
import pandas as pd
import numpy as np


def test_getOutliers(titanicKnownOutliers):
    """
    getOutliers() produces a subset of a DataFrame containing elements which are a specified no.
    of standard deviations from the mean or more. We compare computed outliers to known-correct
    outliers for a range of inputs, for our sample dataset.
    """
    # Arrange
    std_dev = titanicKnownOutliers['input'][0]
    cat_col = titanicKnownOutliers['input'][1]
    d_frame = titanicKnownOutliers['data']

    # Act
    computed = getOutliers(d_frame, std_dev, cat_col).sort_values(by=['PassengerId'])
    expected = d_frame[d_frame['PassengerId'].isin(titanicKnownOutliers['expected'])]\
        .sort_values(by=['PassengerId'])

    # Assert
    assert computed.equals(expected)
