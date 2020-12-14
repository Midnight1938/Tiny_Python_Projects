def isYearLeap(year):

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def daysInMonth(year, month):

    if isYearLeap(year) and month == 2:
        return 29
    elif month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def dayOfYear(year, month, day):
    daysinPriorMonth = 0

    for i in range(month, 1, -1):
        daysinPriorMonth += daysInMonth(year, i-1)

    return daysinPriorMonth + day


print(dayOfYear(2000, 12, 31))