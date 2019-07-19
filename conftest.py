import pytest
import pandas as pd
import numpy as np
from src.transform import *


@pytest.fixture()
def titanicSamples(request):
    """
    Simple fixture;
    Yields a sample dataset detailing survivors/unfortunates on RMS Titanic
    """
    fp = './sample-data/input/titanic.csv'
    print('Running setup code (if there actually was any...)')
    yield pd.read_csv(fp)
    print('Running teardown code (if there actually was any...)')
