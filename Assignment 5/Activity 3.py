def cleanUp():
    print("Thank you for using this program.")

def displayresults():
    print("displayresults", end='', flush=True)

def feet(miles):
    var_return = 5280 * miles
    
    return var_return

def imputmiles():
    print("type in the miles you aregoing to be using to convert to yards, inches, feet.")

def inches(miles):
    var_return = 63360 * miles
    
    return var_return

def miles(miles):
    miles = int(input())
    
    return Return

def yards(miles):
    var_return = 1760 * miles
    
    return var_return

# Main
# This is a program converting miles to yards, inches and feet.
imputmiles()
miles = int(input())
yards = int(input())
inches = int(input())
feet = int(input())
yards = yards(miles)
inches = inches(miles)
feet = feet(miles)
displayresults()
print(yards * miles)
print(inches * miles)
print(feet * miles)
cleanUp()
