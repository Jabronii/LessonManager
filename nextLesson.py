import webbrowser
from tkinter import messagebox
from main import *

messageText = None
flag = True
todaysData = None
for dayData in data:
    if currentWeekDay==int(dayData["day"]):
        flag = False
        todaysData = dayData["lessons"]
        break
if flag:
    messagebox.showerror("Помилка", "Сьогодні немає пар")
else:
    closestStartTime = time(23,59,59)
    currentlyALessonFlag = False
    lessonsEnded = True
    nextLessonName = None
    nextLessonURL = None
    for lesson in todaysData:
        if "parity" in lesson.keys() and not(int(lesson["keys"])==currentWeekParity):
            continue
        startTimeText = lesson["start"]
        endTimeText = lesson["end"]
        startTime = time(int(startTimeText[0:2]), int(startTimeText[3:5]))
        endTime = time(int(endTimeText[0:2]), int(endTimeText[3:5]))
        name = lesson["name"]
        url = lesson["URL"]
        if currentTime>startTime and currentTime<endTime:
            currentlyALessonFlag = True
            nextLessonName = name
            nextLessonURL = url
            break
        if currentTime<startTime and startTime<closestStartTime:
            closestStartTime = startTime
            nextLessonName = name
            nextLessonURL = url
            lessonsEnded = False
    if currentlyALessonFlag:
        webbrowser.open(nextLessonURL)
    else if not lessonsEnded:
        messagebox.showinfo("Помилка", "Урок ще не почався")