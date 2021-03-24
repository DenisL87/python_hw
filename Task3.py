import datetime

year = int(input("Enter a year here: "))
month = int(1)
day = int(1)
mondays = []

while month < 13:
  try:
    to_check = datetime.datetime(year, month, day)
  except ValueError as error:
    month += 1
    day = 1
    continue
  if to_check.strftime('%a') == 'Mon':
    mondays.append(to_check.strftime("%Y-%m-%d %a"))
  day += 1
      
for i in mondays:
  print (i)
  
