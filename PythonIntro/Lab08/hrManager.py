# Author: Hogan Lin
# Date: Nov 10th, 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: Manages employees, calculates payroll, and displays employee information for a small business.

from Worker import Worker
from Supervisor import Supervisor


def calcTotalPay(employeeList) -> float:
    """
    Calculate the total payroll for all employees.
    :param employeeList: List of Worker and Supervisor objects.
    :return: Total pay for all employees, based on a 40-hour workweek.
    """
    totalPay = 0  # Initialize total payroll amount
    for employee in employeeList:  # Iterate over each employee in the list
        totalPay += employee.calcPay(40)  # Calculate and add weekly pay (40 hours) for each employee
    return totalPay  # Return the total payroll


def listEmployees(employeeList):
    """
    Output information for each employee in the list.
    :param employeeList: List of Worker and Supervisor objects.
    """
    for employee in employeeList:  # Iterate over each employee in the list
        # Print general employee information
        print(f"Name: {employee.get_name()}")
        print(f"ID: {employee.get_id()}")
        print(f"Pay Rate: ${employee.get_pay_rate():.2f}")
        
        # Check if employee is a Worker or Supervisor and display specific information
        if isinstance(employee, Worker):  # If employee is a Worker, display shift details
            shift = "Day Shift" if employee.get_shift() == 1 else "Night Shift"
            print(f"Shift: {shift}")
        elif isinstance(employee, Supervisor):  # If employee is a Supervisor, display level
            print(f"Level: {employee.get_level()}")


def main():
    """
    Main function to add employees, list them, and calculate total pay.
    Prompts user to input the number of employees, their details, and employee type.
    Outputs employee details and the total payroll for all employees.
    """
    employeeList = []  # List to store Worker and Supervisor objects
    numEmployees = int(input("How many employees would you like to add: "))

    while numEmployees > 0:  # Loop until all employees are added
        # Ask user to specify employee type
        empType = input("Would you like to add a worker or a supervisor: ").lower()
        
        if empType == "worker":  # Process Worker details
            name = input("Please enter the name of the worker: ")
            empId = int(input("Please enter the ID of the worker: "))
            payRate = float(input("Please enter the pay rate of the worker: "))
            shift = int(input("Please enter the shift of the worker (1 for day, 2 for night): "))
            
            # Create Worker object and add to employee list
            employeeList.append(Worker(name, empId, payRate, shift))
            numEmployees -= 1  # Decrement employee count
            print()  # Print blank line for readability
            
        elif empType == "supervisor":  # Process Supervisor details
            name = input("Please enter the name of the supervisor: ")
            empId = int(input("Please enter the ID of the supervisor: "))
            payRate = float(input("Please enter the pay rate of the supervisor: "))
            level = int(input("Please enter the level of the supervisor: "))
            
            # Create Supervisor object and add to employee list
            employeeList.append(Supervisor(name, empId, payRate, level))
            numEmployees -= 1  # Decrement employee count
            print()  # Print blank line for readability
            
        else:  # Handle invalid input for employee type
            print(f"{empType} is not a worker or supervisor. Try again!\n")

    # Output the list of employees and their details
    print("\nEmployee List:")
    listEmployees(employeeList)  # Call function to list employee information

    # Calculate and display total payroll cost
    totalPay = calcTotalPay(employeeList)  # Call function to calculate total pay
    print(f"The total cost of all of the worker's pay is ${totalPay:.2f}")


if __name__ == "__main__":
    main()  # Execute main function if script is run directly
