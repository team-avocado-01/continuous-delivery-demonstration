import pytest
import pandas as pd
from src.transform import *


"""
Define test cases here. Each dict has two key/value pairs:
    {"input": (Number_of_std_devs, Column_to_check),
    "output": [PassengerIDs, of, outlying, passengers]}
"""


@pytest.fixture(params=[{"input": (0, "Age"),
                         "expected": list(range(1, 10))},
                        {"input": (1, "Age"),
                         "expected": [6, 7, 8]},
                        {"input": (2, "Age"),
                         "expected": [6]},
                        {"input": (0, "Fare"),
                         "expected": list(range(1, 10))},
                        {"input": (1, "Fare"),
                         "expected": [2, 4, 7]},
                        {"input": (999, "Fare"),
                         "expected": []},
                        {"input": (1.23, "Age"),
                         "expected": [6, 7, 8]},
                        {"input": (0.123, "Fare"),
                         "expected": list(range(1, 10))}])
def titanicKnownOutliers(request):
    """
    Setup code;
    Yields a set of known outliers and the corresponding parameters that are
    expected to produce them from our titanic dataset.

    Inputs are tuples of (n_std_dev, column_name)
    """
    fp = './sample-data/input/titanic.csv'
    print('Running setup code (if there actually was any...)')
    request.param['data'] = pd.read_csv(fp)
    yield request.param
    print('Running teardown code (if there actually was any...)')
