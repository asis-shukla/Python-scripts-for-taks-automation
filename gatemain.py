"""This file is for tracking time spent on the gate preparation
Author: Ashish Shukla
Date: 06 march 2018
"""

import datetime          # for taking date

print("1:Update values")
print("2:see status")

total_time = 1500*60   # total minutes decide to give
option = input("Choose your option:")

if option == "1":
    print("You choose to update")
    f = open("gateprep.txt", "a")
    print("Enter number of minutes:")
    today_minutes = int(input())
    now = datetime.datetime.now()
    today_year = now.year
    today_month = now.month
    today_day = now.day
    f.write(str(today_minutes) + "-" + str(today_day) + "-" + str(today_month) + "-" + str(today_year))
    f.write("\n")
    f.close()
    print("You update values successfully")
    exit(0)


elif option == "2":
    total_spent_minute_till_now = 0
    print("You choose to see status")
    f = open("gateprep.txt", "r")
    list_data = f.readlines()
    print("minute-date-month-year")
    for entry in list_data:
        print(entry, end="")
        minute, day, month, year = entry.split("-")
        total_spent_minute_till_now += int(minute)

    remaining_minute = total_time - total_spent_minute_till_now
    print("total time is: " + str(total_time))
    print("total spent minute till now is: " + str(total_spent_minute_till_now))
    print("total remaining time is: " + str(remaining_minute))
    per = total_spent_minute_till_now * 100 / total_time
    print("percent completed is: ", per)
    f.close()
    exit(1)


else:
    print("Try again, You choose wrong option")
    exit(2)
