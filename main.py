import webbrowser
from tkinter import messagebox
import json

#load json file
f = open("schedule.json")
data = json.load(f)
print(data[0]["day"])

#webbrowser.open("https://knu-ua.zoom.us/j/81813357520?pwd=YWdqcThmWVdqdy9zNWp3NDdrcVpBUT09")
#messagebox.showinfo("перевірка", "перевірка")
#print("TEST")