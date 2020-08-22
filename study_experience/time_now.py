from datetime import datetime
import time

year = str(datetime.now().year)
month = str(datetime.now().month)
day = str(datetime.now().day)
hour = str(datetime.now().hour)
minute = str(datetime.now().minute)
second = str(datetime.now().second)

print(datetime.now())
print(f"{year}-{month}-{day} {hour}:{minute}:{second}")
print(time.strftime("%B %Y-%m-%d %H:%M:%S"))
