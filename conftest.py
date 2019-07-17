import pytest
import pandas as pd
from src.transform import *


@pytest.fixture
def exampleData():
    """
    Setup code;
    Creates an example DataFrame, similar to our sample titanic dataset
    """

    #Name = ['Alice', 'Bob', 'Charlie', 'Dave', 'Emma']
    Age = ['25', '43', '65', '999', '-1']
    #Sex = ['f', 'm', 'm', 'm', 'f']
    #Embarked = ['C', 'S', 'P', 'Q', 'P']
    Survived = ['1', '1', '0', '0', '1']
    # return pd.DataFrame(list(zip(Name, Age, Sex, Embarked, Survived)),
    #                     columns=['Name', 'Age', 'Sex', 'Embarked', 'Survived'])
    return pd.DataFrame(list(zip(Age, Survived)), columns=['Age', 'Survived'])
