# You are given a date. Your task is to find what the day is on that date. Input A single line of
#  input containing the space separated month, day and year, respectively, in MM DD YYYY format.
# 08 05 2015 Output Output the correct day in capital letters. WEDNESDAY

import calendar
seq = input("Input a date:").split()
month, day, year = map(int, seq)
ans = calendar.weekday(year, month, day)
print(calendar.day_name[ans].upper())