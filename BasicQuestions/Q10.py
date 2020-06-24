from datetime import datetime

monthYear = '2020-08'
month_generated = datetime.strptime(monthYear, "%Y-%m")
month = month_generated.month
year = month_generated.year
print (month)
print (year)
