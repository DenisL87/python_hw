import datetime

year = int(input("Enter a year here: "))
month = int(1)
day = int(1)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
mondays = []
year_count = year
to_check = datetime.datetime(year, month, day)

while month < 13:
  current_month = to_check.strftime('%b')
  try:
    for current_month in months:
      to_check = datetime.datetime(year, month, day)
      if to_check.strftime('%a') == 'Mon':
        mondays.append(to_check.strftime("%Y-%m-%d %a"))
      day += 1
  except:
    day = 1
  month += 1
  
print(mondays)
