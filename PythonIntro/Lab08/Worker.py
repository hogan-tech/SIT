# Author: Hogan Lin
# Date: Nov 10th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: Defines a Worker class to store information about worker-type employees.

from Employee import Employee

class Worker(Employee):
    def __init__(self, name: str, employerId: int, payRate: float, shift: int):
        """Initialize a worker with name, ID, pay rate, and shift."""
        super().__init__(name, employerId, payRate)
        # Private variable
        self.__shift = shift  

    # Getter and Setter for shift
    def get_shift(self) -> int:
        return self.__shift

    def set_shift(self, shift: int):
        self.__shift = shift
