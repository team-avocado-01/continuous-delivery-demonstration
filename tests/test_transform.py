from src.transform import *
import pandas as pd


# # Dummy test; should pass regardless of how good our code is
# def test_doNothing():
#     assert doNothing() == 'Nothing to see here'


# # Tests whether the getOutliers function correctly does so
# def test_getOutliers():
#     data1 = {'col1': [1, 1, 1, 1, 1, 99999999],
#              'col2': [1, 1, 1, 1, 1, 1],
#              'col3': [2, 2, 1.9, 2, 2, 2]}
#     df1 = pd.DataFrame(data=data1)
#     # Test an obvious outlier:
#     assert getOutliers(df1, 1, 'col1').equals(df1[df1['col1'] == 99999999])
#     # Test when there's no outliers:
#     assert getOutliers(df1, 1, 'col2').empty
#     assert getOutliers(df1, 999, 'col1').empty
#     # Test checking for tiny variations; sigma very small:
#     assert getOutliers(df1, 0.001, 'col2').empty


# # Ensures we are checking for outliers a valid number of standard deviations from the mean
# def test_num_std_devs():
#     assert num_std_devs > 0

def test_getOutliers(exampleData):
    """
    getOutliers() extracts a subset of a DataFrame containing elements which are a specified no.
    of standard deviations from the mean.
    """
    # Arrange (Our data is already in the necessary form...)
    categories = exampleData.columns
    std_dev_range = range(-5, 6)
    outputs = []

    # Act
    for cat in categories:
        for std_devs in std_dev_range:
            outputs.append(getOutliers(exampleData, std_devs, cat))

    print(outputs)

    # Assert


if __name__ == '__main__':
    test_getOutliers(exampleData)
