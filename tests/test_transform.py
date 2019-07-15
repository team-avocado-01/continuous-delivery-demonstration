from src.transform import *
import pandas as pd


# Dummy test; should pass regardless of how good our code is
def test_doNothing():
    assert doNothing() == 'Nothing to see here'


# Tests whether the getOutliers function correctly does so
def test_getOutliers():
    data1 = {'col1': [1, 1, 1, 1, 1, 99999999],
             'col2': [1, 1, 1, 1, 1, 1],
             'col3': [2, 2, 1.9, 2, 2, 2]}
    df1 = pd.DataFrame(data=data1)
    # Test an obvious outlier:
    assert getOutliers(df1, 1, 'col1').equals(df1.iloc[5])
    # Test when there's no outliers:
    assert getOutliers(df1, 1, 'col2').equals(pd.DataFrame())
    # Test checking for tiny variations; sigma very small:
    assert getOutliers(df1, 0.001, 'col3').equals(df1.iloc[2])


# Ensures we are checking for outliers a valid number of standard deviations from the mean
def test_num_std_devs():
    assert num_std_devs > 0
