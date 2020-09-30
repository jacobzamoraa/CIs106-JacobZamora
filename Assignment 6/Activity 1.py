def get_annual(a, b):
    annual = a*b*52
    return annual


def get_monthly(a, b):
    monthly = (a*b*52)/12
    return monthly


def get_weekly(a, b):
    weekly = a*b*40
    return weekly
hours = int(input("enter hours: "))
rate = int(input("enter rate: "))


def main(a, b):
    annual = get_annual(a, b)
    monthly = get_monthly(a, b)
    weekly = get_weekly(a, b)
    display_results(annual, monthly, weekly)
print("Annual salary", get_annual(hours, rate))
print("Monthly salary", get_monthly(hours, rate))
print("Weekly salary", get_weekly(hours, rate))

