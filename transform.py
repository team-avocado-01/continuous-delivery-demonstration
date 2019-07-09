import pandas
import sys


input_fp = './input/titanic.csv'
output_fp = './output/outliers.csv'


def doNothing():
    return 'Nothing to see here'


def readData(filepath):
    return pandas.read_csv(filepath)


def getOutliers(df, n_std_dev, col):
    mean = df[col].mean()
    print(mean)
    one_std_deviation = df[col].std()
    print(one_std_deviation)
    q = n_std_dev * one_std_deviation
    df_max = df[df[col] > mean + q]
    df_min = df[df[col] < mean - q]
    return pandas.concat([df_max, df_min])


def storeOutliers(df, filepath):
    df.to_csv(filepath)


if __name__ == '__main__':
    print('testing')
    df = readData(input_fp)
    df = getOutliers(df, float(sys.argv[1]), str(sys.argv[2]))
    storeOutliers(df, output_fp)
    print(df)
