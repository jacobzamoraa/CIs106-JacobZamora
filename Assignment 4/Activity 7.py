# This is a program asking the user for their dogs name and asking for
# a dogs age to covert to human years.

print("Enter dog's name:")
dogs_name = input()

print("Enter dog's age:")
dogs_age = int(input())

age = 7 * dogs_age

print(dogs_name + " is " + str(age) + " years old in dog years.")
