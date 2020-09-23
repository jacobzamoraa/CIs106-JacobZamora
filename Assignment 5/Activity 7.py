def age(dogsage):
    var_return = 7 * dogsage
    
    return var_return

def cleanUp():
    print("thank you for using this program")

# Main
# This is a program asking the user for their dogs name and age, converting the age to human years.
dogsname = input()
dogsage = int(input())
age = age(dogsage)
print(dogsname)
print(dogsage)
cleanUp()
