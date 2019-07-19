from src.transform import *
import pandas as pd
import numpy as np
import pytest

@pytest.mark.parametrize("input,expected", [((0, "Age"), list(range(1, 10))), ((1, "Age"), [6, 7, 8]), ((2, "Age"), [6]), ((0, "Fare"), list(range(1, 10))), ((1, "Fare"), [2, 4, 7]), ((999, "Fare"), []), ((1.23, "Age"), [6, 7, 8]), ((0.123, "Fare"), list(range(1, 10)))])
def test_getOutliers(input, expected, titanicSamples):
    """
    getOutliers() produces a subset of a DataFrame containing elements which are a specified no.
    of standard deviations from the mean or more. We compare computed outliers to known-correct
    outliers for a range of inputs, for our sample dataset.
    """
    # Arrange
    std_dev = input[0]
    cat_col = input[1]

    # Act
    computed = getOutliers(titanicSamples, std_dev, cat_col).sort_values(by=['PassengerId'])
    expected = titanicSamples[titanicSamples['PassengerId'].isin(expected)]\
        .sort_values(by=['PassengerId'])

    # Assert
    assert computed.equals(expected)
