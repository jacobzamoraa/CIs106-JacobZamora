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
print("please enter miles to convert to yards")
miles = int(input())
yards = yards(miles)
print(yards * miles)
print("please eneter miles to convert to inches")
inches = int(input())
inches = inches(miles)
print(inches * miles)
print("please enter miles to convert to feet")
feet = int(input())
feet = feet(miles)
print(feet * miles)
cleanUp()
