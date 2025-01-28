# Author: Hogan Lin
# Date: Jan 24th 2025
# Github: https://github.com/hogan-tech/SIT/tree/main/Computing
# Note: Upload to github repo after deadline
# Description: temperature conversion

def fahrenheitToCelsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheitToCelsius(fahrenheit)
    print(f"Temperature in Celsius: {celsius}")


if __name__ == "__main__":
    main()
