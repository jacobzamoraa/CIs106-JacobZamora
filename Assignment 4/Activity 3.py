d_miles = int(input("Input distance in miles: "))
d_inches = d_miles * 63360
d_feet = d_miles * 5280
d_yards = d_miles * 1760
print("The distance in inches is %i inches." %d_inches)
print("The distance in feet is %.2f feet." % d_feet)
print("The distance in yards is %.2f yards." % d_yards)
