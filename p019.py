"""You are given the following information, but you may prefer to do
some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?

"""
def firstOfMonth(untilYear):
    year = 1901
    day = 2 # 1 Jan 1901 was Tuesday
    while year < untilYear:
        yield day; day += 31;
        yield day; day += 29 if (year % 4 == 0 and not 
                                 (year % 100 == 0 and not
                                  year % 400 == 0)) else 28
        yield day; day += 31;
        yield day; day += 30;
        yield day; day += 31;
        yield day; day += 30;
        yield day; day += 31;
        yield day; day += 31;
        yield day; day += 30;
        yield day; day += 31;
        yield day; day += 30;
        yield day; day += 31;
        year += 1;

ans = sum(1 for day in firstOfMonth(2001) if day % 7 == 0)

print(ans)
