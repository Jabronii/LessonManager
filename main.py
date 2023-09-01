import json
from datetime import *

#load json file
f = open("schedule.json", encoding="utf-8")
data = json.load(f)

#get current date
weekCountStart = date(2023,9,3)
currentDate = date(datetime.now().year, datetime.now().month, datetime.now().day)
#currentDate = date(2023, 9, 4)
diff = currentDate-weekCountStart

#0 is even, 1 is odd
currentWeekParity = (diff.days//7)%2

#day numbers are monday = 0 tuesday = 1 wednesday = 2 thursday = 3 friday = 4
currentWeekDay = diff.days%7-1

#get current time
currentTime = time(datetime.now().hour, datetime.now().minute)