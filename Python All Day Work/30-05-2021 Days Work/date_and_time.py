from datetime import date

my_date = date(2021, 5, 26)
print(my_date)
print(my_date.year)
print(my_date.month)
print(my_date.day)

current_date = date.today()
print('Todays date: ', current_date)
print(current_date.year)

# date.strftime(string format) this method
# Current date: 2021-05-26
# Formatted date: 26 May, 2021

formatted_date = current_date.strftime("%d %B, %Y")
print(formatted_date)


from datetime import time

my_time = time(10, 30, 50)
print(my_time)
print(my_time.hour)
print(my_time.minute)

# # time.strftime(string format) method
formatted_time = my_time.strftime('%I:%M:%S')
print(formatted_time)

from datetime import datetime
print(date(2021,12,25))
x = datetime.now()

print(x)

# method of datetime class: today(), now(), utcnow()
# Verifying utc time: https://time.is/GMT
print(datetime.today())
print(datetime.now())
print(datetime.utcnow())

my_datetime = datetime.now()
formatted_datetime = my_datetime.strftime('%I:%M:%S %p %d %B, %Y')
print(formatted_datetime)
