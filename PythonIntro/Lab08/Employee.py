# Author: Hogan Lin
# Date: Nov 10th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: Defines a general Employee class to store basic employee information and calculate pay.

class Employee:
    def __init__(self, name: str, employerId: int, payRate: float):
        """Initialize an employee with name, ID, and pay rate."""
        self._name = name
        self._employerId = employerId
        self._payRate = payRate

    def calcPay(self, hours_worked: int) -> float:
        """Calculate and return the pay based on hours worked."""
        return self._payRate * hours_worked

    # Getter and Setter methods
    def get_name(self) -> str:
        return self._name

    def get_id(self) -> int:
        return self._employerId

    def get_pay_rate(self) -> float:
        return self._payRate

    def set_name(self, name: str):
        self._name = name

    def set_id(self, employerId: int):
        self._employerId = employerId

    def set_pay_rate(self, payRate: float):
        self._payRate = payRate
