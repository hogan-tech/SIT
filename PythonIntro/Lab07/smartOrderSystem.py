# Author: Hogan Lin
# Date: Nov 2nd 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This script implements an order management system using the SmartProduct class.
# It allows users to enter product details, calculates each product's total cost, and displays
# the total order cost in a formatted summary.

from SmartProduct import SmartProduct


def calcTotal(products):
    """
    Calculates the total cost of all products in the provided list.
    
    Parameters:
    products (list): A list of SmartProduct objects.

    Returns:
    float: The summed total cost of all products.
    """
    return sum(product.get_totalCost() for product in products)


def main():
    """
    Main function to interact with the user for ordering products.
    
    Prompts the user for the number of products to order, gathers details for each product, 
    creates SmartProduct instances, and displays an itemized order summary with the total cost.
    """
    # Prompt user for the number of products to order
    numProducts = int(input("How many products would you like to order: "))

    # Create a list to store SmartProduct objects
    products = []

    # Loop to gather product information
    for i in range(1, numProducts + 1):
        name = input(
            "Please enter the name of the product you wish to order: ")
        units = int(
            input("Please enter the number of units of product you wish to order: "))

        # Create a new SmartProduct with unique ID and add to the list
        product = SmartProduct(productId=i, name=name,
                               units=units, pricePerUnit=9.99)
        products.append(product)

    # Output each product's information
    print("You ordered:")
    for product in products:
        print(f"ID: {product.get_productId()}")
        print(f"Name: {product.get_name()}")
        print(f"Units: {product.get_units()}")
        print(f"Price: ${product.get_pricePerUnit():.2f}")
        print(f"Total Cost: ${product.get_totalCost():.2f}")

    # Calculate and display the total cost of the order
    totalCost = calcTotal(products)
    print(f"The total cost of your order is: ${totalCost:.2f}")


# Run the main function
if __name__ == "__main__":
    main()
