import datetime

date = "Feb 12 2019 2:41PM"
months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, "Jul": 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
year = None
month = None
day = None
hours = None
minutes = None

loop_count = 0
while loop_count < len(date):
  if date[loop_count] == " ":
    month = date[0:loop_count]
    if month in months:
      month = months[month]
    date = date[loop_count + 1:]
    loop_count = 0
    break
  loop_count += 1

while loop_count < len(date):
  if date[loop_count] == " ":
    day = int(date[0:loop_count])
    date = date[loop_count + 1:]
    loop_count = 0
    break
  loop_count += 1
  
while loop_count < len(date):
  if date[loop_count] == " ":
    year = int(date[0:loop_count])
    date = date[loop_count + 1:]
    loop_count = 0
    break
  loop_count += 1
  
while loop_count < len(date):
  if date[loop_count] == ":":
    hours = int(date[0:loop_count])
    if date[-1] == 'M' and date[-2] == "P":
      hours += 12
      if hours == 24:
        hours = 0
    date = date[loop_count + 1:]
    loop_count = 0
    break
  loop_count += 1

minutes = int(date[0:-2])

date_time = datetime.datetime(year, month, day, hours, minutes)
print(date_time.strftime("%Y-%m-%d %H:%M:%S"))
