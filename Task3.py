import datetime

year = int(input("Enter a year here: "))
month = int(1)
day = int(1)
mondays = []
year_count = year

while year_count == year:
  to_check = datetime.datetime(year, month, day)
  while month < 13:
    try:
      if datetime.strftime("%a") == 'Mon':
        mondays.append(to_check.strftime("%Y-%m-%d %H:%M:%S %a"))
      day += 1
    except Exception:
      day = 1
      month += 1
  year_count += 1
  
print(mondays)
