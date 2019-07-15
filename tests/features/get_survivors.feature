Scenario: Discovering Titanic survivors
  Given a specific set of titanic passengers
    |PassengerId|Survived|Pclass|Name |Sex|Age |Ticket|Fare|Cabin|Embarked|
    |     1     |   1    |   1  |Alice| F | 22 |  A   |500 |  D  | Portsm |
    |     2     |   0    |   2  |Bob  | M | 34 |  B5  |200 |  L  | London |
    |     3     |   1    |   3  |Carol| F | 83 |  Y   |400 |  M  | Glasgow|

  When we list only the survivors name, sex and age
  Then we observe
    |Name |Sex|Age |
    |Alice| F | 22 |
    |Carol| F | 83 |
