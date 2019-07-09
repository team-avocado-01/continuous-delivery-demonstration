Feature: Reading input data
  When we put in our input data, we should check that the resulting table
  has the right shape.

  Scenario:
    Given that we read in some Titanic data
        | number     | other number |
        | 0          | 4            |
        | 0          | -5           |
        | 0          | 0            |
     When summed with any "<other number>"
     Then we should return "<other number>"
