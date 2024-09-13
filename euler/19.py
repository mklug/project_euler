
thirty_days = {9, 4, 6, 11}

def month_length(month, year):
    if month in thirty_days:
        return 30
    if month != 2:
        return 31
    
    # February.
    if year % 4 != 0:
        return 28
    if year % 100 == 0:
        if year % 400 == 0:
            return 29
        return 28
    return 29

# Date generator --> weekday : int, day : int, month : int, year : int.
# Weekday represented as 0,...,6 --> 0 is Sunday
def date_generator(weekday, day, month, year):

    while True:
        yield weekday, day, month, year

        weekday += 1
        weekday %= 7

        if month_length(month, year) == day:
            day = 1
            month += 1
            if month == 13:
                year += 1
                month = 1
        else:
            day += 1

if __name__ == '__main__':

    ans = 0
    for weekday, day, month, year in date_generator(1, 1, 1, 1900):
        if year >= 1901:
            if day == 1 and weekday == 0:
                ans += 1
        if (day, month, year) == (31, 12, 2000):
            break
    
    print(f'answer = {ans}')