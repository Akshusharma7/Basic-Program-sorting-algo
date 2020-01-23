


def week_num(day,n):
    week = ["mon","tue","wed","thu","fri","sat","sun"]
    ind = week.index(day)

    next_day = (n+ind)%7
    days = week[next_day]
    return days

print(week_num("tue",2))
