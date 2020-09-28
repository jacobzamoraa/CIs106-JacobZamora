def get_months(a):
    months=a*12;
    return months;
def get_days(a):
    days=a*365;
    return days;
def get_hours(a):
    hours=a*12*365*24;
    return hours;
def get_seconds(a):
    seconds=a*12*365*24*60*60;
    return seconds;
years=int(input("enter years: "))
print("Months old",get_months(years))
print("Days old",get_days(years))
print("Hours old",get_hours(years))
print("Seconds old",get_seconds(years))

def get_annual(a,b):
    annual=a*b*52;
    return annual;
def get_monthly(a,b):
    monthly=(a*b*52)/12;
    return monthly;
def get_weekly(a,b):
    weekly=a*b*40;
    return weekly;
hours=int(input("enter hours: "))
rate=int(input("enter rate: "))
print("Annual salary",get_annual(hours,rate))
print("Monthly salary",get_monthly(hours,rate))
print("Weekly salary",get_weekly(hours,rate))
