import datetime

# DATE

""""date1 = datetime.date(2020, 1, 21)
print(date1)
print(date1.year)
print(date1.month)
print(date1.day)
print(datetime.MINYEAR)
print(datetime.MAXYEAR)
# .weekday'de haftanın gününü 0'dan başlatıp 6'ya kadar gider.
print(date1.weekday())
# .isoweekday'de haftanın gününü 1'den başlatıp 7'ye kadar gider.
print(date1.isoweekday())
print(date1.isocalendar())"""

# TIME

"""time1 = datetime.time(10, 11, 12, 875987)
print(time1)
print(time1.hour)
print(time1.minute)
print(time1.second)
print(time1.microsecond)"""

# DATETIME

"""time2 = datetime.datetime(2000, 12, 23, 22, 20, 56, 123331)
print(time2)
print(time2.year)

timenow = datetime.datetime.now()"""

"""print(timenow.strftime('%Y/%B/%d'))     # '%...' gösterimleri için dökümantasyona bak.

birthday = datetime.date(1996, 8, 21)   # doğum günü hesaplama
tdelta = timenow-birthday
print(type(tdelta))
print(tdelta)
"""
tdelta2 = datetime.timedelta(hours=10)
print(timenow + tdelta2)
print(timenow)
