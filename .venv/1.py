n_year = int(input())
whether_leap_year = None
if n_year % 400 == 0:
    whether_leap_year = True
elif n_year % 4 == 0 and n_year % 100 != 0:
    whether_leap_year = True
else:
    whether_leap_year = False
if whether_leap_year:
    print(366)
else:
    print(365)