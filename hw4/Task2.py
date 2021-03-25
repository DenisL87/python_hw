# import datetime

# date_time = datetime.datetime(2019, 2, 12, 14, 41)

# print(date_time.strftime("%b %d %Y %I:%M %p"))
# print(date_time.strftime("%Y-%m-%d %H:%M:%S"))


import datetime

date = "Feb 12 2019 12:41PM"
year = None
month = None
day = None
hours = None
minutes = None

loop_count = 0
while loop_count < len(date):
  if date[loop_count] == " ":
    month = date[0:loop_count]
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
