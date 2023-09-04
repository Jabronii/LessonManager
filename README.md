# Застосування
nextLesson.exe - при нажатті комбінації клавіш, якщо зараз триває пара, відкриває посилання на неї(напр. у зум). Якщо пари ще не почалися каже час до наступної пари.
todaysLessons.exe - показує графік занять на сьогодні.

# Як встановити
1) Завантажити [autohotkey]([url](https://www.autohotkey.com/)https://www.autohotkey.com/).
2) Скачати lessonManager.zip файл з release і розархівувати його у якусь папку.
3) У файлі lessonManager.ahk відредагувати посилання на nextLesson.exe та todaysLessons.exe щоб співпадало з їх розміщенням у вашій файловій системі
4) У lessonManager.ahk при бажанні змінити комбінації клавіш (по замовченню Ctrl+F9 та Ctrl+F10)
5) Відредагувати schedule.json щоб він співпадав з вашим графіком. Як воно працює має бути нескладно зрозуміти але треба врахувати: своє запишіть по такому формату як там написано; час має бути записаний hh:mm без скорочень; день тижня записаний у змінній day (0 = понеділок 1 = вівторок і тд); змінна parity відповідає за ті пари, що тільки по парним або непарним тижням, причому parity = 0 - парний тиждень а parity = 1 - непарний тиждень.
6) [Додати]([url](https://support.microsoft.com/en-us/windows/add-an-app-to-run-automatically-at-startup-in-windows-10-150da165-dcd9-7230-517b-cf3c295d89dd#:~:text=With%20the%20file%20location%20open,location%20to%20the%20Startup%20folder.)https://support.microsoft.com/en-us/windows/add-an-app-to-run-automatically-at-startup-in-windows-10-150da165-dcd9-7230-517b-cf3c295d89dd#:~:text=With%20the%20file%20location%20open,location%20to%20the%20Startup%20folder.) lessonManager.ahk до програм що запускаються при включенні компьютера. Щоб не перезапускати компьютер можна просто запустити цей файл вручну.
