# Given an array date[] = [d, m, y], where d denotes the day, 
# m denotes the month, and y denotes the year, Write a program 
# that calculates the day of the week for any particular date in 
# the past or future.

def day_of_week(date):

    day = date[0]
    month = date[1]
    year = date[2]

    if month < 3:
        month += 12
        year -= 1

    q = day
    m = month
    k = year % 100
    j = year // 100

    h = (q + (13 * (m + 1)) // 5 + k + (k // 4) + (j // 4) + (5 * j)) % 7
    
    days = [
        "Saturday",
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
    ]
    return days[h]

date = [7, 7, 2026]
print(day_of_week(date))