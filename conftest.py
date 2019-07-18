import pytest
import pandas as pd
import numpy as np
from src.transform import *


@pytest.fixture(params=[{"input": (0, "Age"),
                         "expected": list(range(1, 10))},
                        {"input": (1, "Age"),
                         "expected": [7, 8]},
                        {"input": (2, "Age"),
                         "expected": [6]},
                        {"input": (0, "Fare"),
                         "expected": list(range(1, 10))},
                        {"input": (1, "Fare"),
                         "expected": [2, 4, 7]},
                        {"input": (999, "Fare"),
                         "expected": []}])
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
