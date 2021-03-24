import datetime

try:
  year = int(input("Enter a year here: "))
except:
  raise ValueError('Not a number')
month = 1
day = 1
mondays = []

while month < 13:
  try:
    to_check = datetime.datetime(year, month, day)
  except:
    month += 1
    day = 1
    continue
  if to_check.strftime('%a') == 'Mon':
    mondays.append(to_check.strftime("%Y-%m-%d %a"))
  day += 1
      
for i in mondays:
  print(i)
  
