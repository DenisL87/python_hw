import datetime

year = int(input("Enter a year here: "))
month = int(1)
day = int(1)
mondays = []
target_year = year
while target_year == year:
  datetime.datetime(year, month, day)
  while month < 13:
    try:
      if datetime.strftime("%a") == 'Mon':
        mondays.append(datetime.date_time("%Y-%m-%d"))
      day += 1
    except Exception:
      day = 1
      month += 1
  target_year += 1
  
print(mondays)
