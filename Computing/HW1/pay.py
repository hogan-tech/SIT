# Author: Hogan Lin
# Date: Jan 24th 2025
# Github: https://github.com/hogan-tech/SIT/tree/main/Computing
# Note: Upload to github repo after deadline
# Description: computing wages
import math

def unfair_weekly_paycheck_amount(hours_worked: float) -> int:
    """
    Calculate unfair paycheck where hours are rounded down.
    
    :param hours_worked: Number of hours worked
    :return: Paycheck amount (rounded down)
    """
    return int(math.floor(hours_worked) * 15)


def fair_weekly_paycheck_amount(hours_worked: float) -> float:
    """
    Calculate fair paycheck with exact hours worked.
    
    :param hours_worked: Number of hours worked
    :return: Paycheck amount (precise calculation)
    """
    return round(hours_worked * 15, 2)  
