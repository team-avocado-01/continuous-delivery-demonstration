from src.transform import *


# Dummy test; should pass regardless of how good our code is
def test_doNothing():
    assert doNothing() == 'Nothing to see here'


def test_num_std_devs():
    assert num_std_devs > 0
