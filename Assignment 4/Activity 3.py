# Comments go here ...

miles = int(input("Input distance in miles: "))

inches = miles * 63360
feet = miles * 5280
yards = miles * 1760

print(f"The distance in inches is {inches} inches.")
print(f"The distance in feet is {feet:.2f} feet.")
print(f"The distance in yards is {yards:.2f} yards.")
