#ex1
from datetime import datetime, timedelta
date = datetime.now()
diff = date - timedelta(days = 5)
print("current date:", date)
print("after subsctracting:", diff)

#ex2
import datetime as dt
today = dt.datetime.today()
yesterday = today - dt.timedelta(days=1)
tomorrow = today + dt.timedelta(days=1)
print("today is" , today)
print("yesterday was", yesterday)
print("next day will be",tomorrow)

#ex3
import datetime as dt
print(dt.datetime.now().strftime("%Y-%m-%d %H:%M-%S"))

#ex4
from datetime import datetime
date_str1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date_str2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")
date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")
time_difference = abs((date2 - date1).total_seconds())
print(f"The difference between the two dates is {time_difference} seconds.")