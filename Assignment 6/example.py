# This program asks the user for a Fahrenheit temperature, 
# converts the given temperature to Celsius,
# and displays the results.
#
# References:
# https://www.mathsisfun.com/temperature-conversion.html
# https://en.wikibooks.org/wiki/Python_Programming


def get_fahrenheit():
    print("Enter Fahrenheit temperature:")
    fahrenheit = float(input())
    return fahrenheit


def calculate_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def display_result(fahrenheit, celsius):
    print(str(fahrenheit) + "° Fahrenheit is " + 
        str(celsius) + "° Celsius")


def main():
    fahrenheit = get_fahrenheit()
    celsius = calculate_celsius(fahrenheit)
    display_result(fahrenheit, celsius)


main()
