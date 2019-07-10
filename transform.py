import pandas
import sys


# Filepaths
input_fp = './input/titanic.csv'
output_fp = './output/outliers.csv'


# Input parameters
num_std_devs = 2        # Number of standard deviations from the mean
col_analyse = 'Age'     # Which column are we checking?


# Does nothing
def doNothing():
    return 'Nothing to see here'


# Reads input csv data
def readData(filepath):
    return pandas.read_csv(filepath)


# This tests for outliers using std deviation and mean
def getOutliers(df, n_std_dev, col):
    mean = df[col].mean()
    print(mean)
    one_std_deviation = df[col].std()
    print(one_std_deviation)
    q = n_std_dev * one_std_deviation
    df_max = df[df[col] > mean + q]
    df_min = df[df[col] < mean - q]
    return pandas.concat([df_max, df_min])


# Saves the output to disk
def storeOutliers(df, filepath):
    df.to_csv(filepath)


# Main method - testing
if __name__ == '__main__':
    print('testing')
    df = readData(input_fp)
    df = getOutliers(df, float(num_std_devs), str(col_analyse))
    storeOutliers(df, output_fp)
    print(df)
