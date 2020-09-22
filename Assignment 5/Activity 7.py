def age(dogsage):
    var_return = 7 * dogsage
    
    return var_return

def cleanUp():
    print("thank you for using this program")

# Main
print("please enter dogsname")
dogsname = input()
print("please enter dogsage")
dogsage = int(input())
age = age(dogsage)
print(age(dogsage))
cleanUp()
