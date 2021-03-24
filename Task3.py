import datetime
year = int(input("Enter a year here: "))
month = int(1)
day = int(1)
mondays = []
target_year = year
while target_year == year:
  while month < 13:
    day = 1
    try:
      while day < 8:
        date_time.datetime(year, month, day)
        if date_time.strftime("%a") == 'Mon':
          mondays.append(date_time.date_time("%b %d %Y %I:%M %p"))
        day =+ 1
    except Exception:
      month += 1
  year += 1
  
  print(mondays)
