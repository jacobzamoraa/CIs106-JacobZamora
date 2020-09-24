def age(dogsage):
    var_return = 7 * dogsage
    
    return var_return

def cleanUp():
    print("thank you for using this program")

def displayResults():
    print("results are")

def dogsName():
    print("imput dogs name")

# Main
# This is a program asking the user for their dogs name and age, converting the age to human years.
dogsName()
dogsname = input()
dogsage = int(input())
age = age(dogsage)
displayResults()
print(dogsname)
print(dogsage)
cleanUp()
