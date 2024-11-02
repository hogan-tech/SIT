# Author: Hogan Lin
# Date: Nov 2nd 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program allows users to order a product by entering its name and quantity. 
# It calculates the total cost based on a fixed price and displays the order details.


from Product import Product


def calcTotal(product):
    """
    Description: Calculates the total cost of the product order.
    This function multiplies the number of units of the product by its price per unit 
    to determine the total cost and updates the product's total cost attribute.
    
    Parameters:
    - product (Product): The Product object containing details about the order, 
                         including units and price.
    
    Returns:
    - None: The function updates the product's total cost directly.
    """
    totalCost = product.get_units() * product.get_price()
    product.set_totalCost(totalCost)


def main():
    """
    Description: The main function manages the order process for a single product. 
    It prompts the user for the product name and quantity, sets a fixed price, 
    calculates the total cost using the calcTotal function, and displays the order summary.
    """
    # Create an instance of Product
    product = Product()

    name = input("Please enter the name of the product you wish to order: ")
    units = int(
        input("Please enter the number of units of product you wish to order: "))

    # Set product information
    product.set_name(name)
    product.set_units(units)
    product.set_price(9.99)  

    # Calculate the total cost
    calcTotal(product)

    print("\nYou ordered:")
    print(f"Name: {product.get_name()}")
    print(f"Units: {product.get_units()}")
    print(f"Price: ${product.get_price():.2f}")
    print(f"Total Cost: ${product.get_totalCost():.2f}")


if __name__ == "__main__":
    main()
