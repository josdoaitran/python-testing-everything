# Need to convert from string to interger

import datetime

birth_year = input("Please input your birth year: ")

age = datetime.datetime.now().year - int(birth_year)

print("Your age: " + str(age))

###################

import datetime
now = datetime.datetime.now()
print (now.year, now.month, now.day, now.hour, now.minute, now.second)
