import pandas
import sys


# Filepaths
input_fp = './sample-data/input/titanic.csv'
output_fp = './sample-data/output/outliers.csv'


# Input parameters
num_std_devs = 1       # Number of standard deviations from the mean
col_analyse = 'Age'     # Which column are we checking for outliers?


# Does nothing - used for our dummy test
def doNothing():
    return 'Nothing to see here'


# Reads input csv data
def readData(filepath):
    return pandas.read_csv(filepath)


# this returns only those rows of a DF which are at least n_std_devs
# away from the mean; outliers.
def getOutliers(df, n_std_dev, col):
    mean = df[col].mean()
    one_std_deviation = df[col].std()
    q = n_std_dev * one_std_deviation
    df_max = df[df[col] > mean + q]
    df_min = df[df[col] < mean - q]
    return pandas.concat([df_max, df_min])


# Takes full titanic data and returns only survivors in the form:
# name, sex, age
# TODO - actually use the specified form for output
# Should write behavioral tests first, then demonstrate that they actually work
def getSurvivors(df):
    return df[df['Survived'] == 1]


# Saves the output to disk
def storeOutliers(df, filepath):
    df.to_csv(filepath)


# Main method - testing
if __name__ == '__main__':
    print('testing')
    df = readData(input_fp)
    print(getSurvivors(df))
    df = getOutliers(df, float(num_std_devs), str(col_analyse))
    storeOutliers(df, output_fp)
    print(df)
