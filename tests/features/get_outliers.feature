Scenario: Searching for outliers
  Given a specific set of titanic passengers
    |PassengerId|Survived|Pclass|Name |Sex|Age |Ticket|Fare|Cabin|Embarked|
    |     1     |   1    |   1  |Alice| F | 22 |  A   |500 |  D  | Portsm |
    |     2     |   0    |   2  |Bob  | M | 24 |  B5  |200 |  L  | London |
    |     3     |   1    |   3  |Carol| F | 156 |  Y   |400 |  M  | Glasgow|

  When we search for those with statistically extraordinary age
  Then we observe
    |PassengerId|Survived|Pclass|Name |Sex|Age |Ticket|Fare|Cabin|Embarked|
    |     3     |   1    |   3  |Carol| F | 156 |  Y   |400 |  M  | Glasgow|
