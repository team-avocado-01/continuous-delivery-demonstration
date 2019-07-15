from src.transform import *
import pandas as pd


# Dummy test; should pass regardless of how good our code is
def test_doNothing():
    assert doNothing() == 'Nothing to see here'


def test_getOutliers():
    data1 = {'col1': [1, 1, 1, 1, 1, 99999999],
             'col2': [1, 1, 1, 1, 1, 1],
             'col3': [1, 1, 1, 1, 1, 1]}
    df1 = pd.DataFrame(data=data1)
    assert getOutliers(df1, 1, col1) == df1.iloc[6]


def test_num_std_devs():
    assert num_std_devs > 0
