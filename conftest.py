import pytest
import pandas as pd
from src.transform import *


def titanicData():
    """
    Setup code;
    Creates a sample DataFrame, similar to our titanic dataset.
    """

    Name = ['Alice', 'Bob', 'Charlie', ' Dave', 'Emma']
    Age = ['25', '43', '65', '999', '-1']
    Sex = ['f', 'm', 'm', 'm', 'f']
    Embarked = ['C', 'S', 'P', 'Q', 'P']
    df = pd.DataFrame(list(zip(Name, Age, Sex, Embarked)),
                      columns=['Name', 'Age', 'Sex', 'Embarked'])
