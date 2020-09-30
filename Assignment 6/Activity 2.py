# This is a program that ask the user how old
# they are in years and converts it to months,
# days, hours and seconds.


def get_months(a):
    months = a*12
    return months


def get_days(a):
    days = a*365
    return days


def get_hours(a):
    hours = a*12*365*24
    return hours


def get_seconds(a):
    seconds = a*12*365*24*60*60
    return seconds
years = int(input("enter years: "))


def main(a):
    months = get_months
    days = get_days
    hours = get_hours
    seconds = get_seconds
    display_results(months, days, hours, seconds)
print("Months old", get_months(years))
print("Days old", get_days(years))
print("Hours old", get_hours(years))
print("Seconds old", get_seconds(years))
