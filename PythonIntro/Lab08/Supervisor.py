# Author: Hogan Lin
# Date: Nov 10th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: Defines a Supervisor class to store information about supervisor-type employees.

from Employee import Employee


class Supervisor(Employee):
    def __init__(self, name: str, employerId: int, payRate: float, level: int):
        """Initialize a supervisor with name, ID, pay rate, and level."""
        super().__init__(name, employerId, payRate)
        # Private variable
        self.__level = level  
        

    def calcPay(self, hoursWorked: int) -> float:
        """Calculate pay with additional level-based bonus."""
        return (self._payRate * hoursWorked) + (1000.00 * self.__level)

    # Getter and Setter for level
    def get_level(self) -> int:
        return self.__level

    def set_level(self, level: int):
        self.__level = level
