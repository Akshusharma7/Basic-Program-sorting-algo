'''
Write a function which take week day as an input and number between 0 to 6 and retuen the next days from the current days of the week

example : if tuesday and 2 are input then output should be thrusday
'''

def week_num(day,n):
    week = ["mon","tue","wed","thu","fri","sat","sun"]
    ind = week.index(day)

    next_day = (n+ind)%7 # remainder between o to 6
    days = week[next_day]
    return days

print(week_num("tue",2)) #Thrusday
