from transform import *


def test_doNothing():
    assert doNothing() == 'Nothing to see here'


def test_num_std_devs():
    assert num_std_devs > 0
