'''
Write a function which take week day as an input and number between 0 to 6 and retuen the next days from the current days of the week
'''


def week_num(day,n):
    week = ["mon","tue","wed","thu","fri","sat","sun"]
    ind = week.index(day)

    next_day = (n+ind)%7
    days = week[next_day]
    return days

print(week_num("tue",2))
