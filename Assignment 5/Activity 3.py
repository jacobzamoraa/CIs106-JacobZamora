def cleanUp():
    print("Thank you for using this program.")

def feet(miles):
    var_return = 5280 * miles
    
    return var_return

def inches(miles):
    var_return = 63360 * miles
    
    return var_return

def yards(miles):
    var_return = 1760 * miles
    
    return var_return

# Main
# This is a program converting miles to yards, inches and feet.
print("please enter miles to convert to yards,inches,feet")
miles = int(input())
inches = int(input())
feet = int(input())
yards = yards(miles)
inches = inches(miles)
feet = feet(miles)
print(yards * miles)
print(inches * miles)
print(feet * miles)
cleanUp()
