from main import *
from tkinter import messagebox

messageText = ""
todaysData = None
for dayData in data:
    if currentWeekDay==int(dayData["day"]):
        flag = False
        todaysData = dayData["lessons"]
        break
if not todaysData == None:
    for lesson in todaysData:
        if "parity" in lesson.keys() and not(int(lesson["parity"])==currentWeekParity):
            continue
        startTimeText = lesson["start"]
        endTimeText = lesson["end"]
        startTime = time(int(startTimeText[0:2]), int(startTimeText[3:5]))
        endTime = time(int(endTimeText[0:2]), int(endTimeText[3:5]))
        name = lesson["name"]
        messageText += startTimeText +" - "+ endTimeText +"\n"
        messageText += name + "\n\n"
if todaysData == None:
    messagebox.showinfo("", "Сьогодні немає пар")
else:
    messagebox.showinfo("Розклад", messageText)
#text