from datetime import datetime

date = "Feb 12 2019 2:41PM"
date = datetime.strptime(date, '%b %d %Y %I:%M%p')
print(date)


# import datetime

# date = "Feb 12 2019 2:41PM"
# date = date.split(" ")
# time = date[-1].split(':')
# months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, "Jul": 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

# month = date[0]
# if month in months:
#   month = months[month]
# day = int(date[1])
# year = int(date[2])
# hours = int(time[0])
# minutes = time[1]
# if minutes[-2:] == 'PM':
#   if hours == 12:
#     hours = 0
#   else:
#     hours += 12
# minutes = int(minutes[0:-2])

# date_time = datetime.datetime(year, month, day, hours, minutes)
# print(date_time.strftime("%Y-%m-%d %H:%M:%S"))
