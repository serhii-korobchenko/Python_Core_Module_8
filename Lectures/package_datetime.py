from datetime import datetime

# current_datetime
current_datetime = datetime.now()
print(current_datetime) # 

# datatime with atributes

print(current_datetime.year)        # 2020
print(current_datetime.month)       # 10
print(current_datetime.day)         # 09
print(current_datetime.hour)        # 22
print(current_datetime.minute)      # 32
print(current_datetime.second)      # 22
print(current_datetime.microsecond) # 819366

# datatime methods
print(current_datetime.date())  # 2020-10-09
print(current_datetime.time())  # 22:13:35.053819
# set up data 
d1 = datetime(year=2012, month=1, day=7, hour=14)
print(d1) # 2012-01-07 14:00:00

# find out day of week
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
print(seventh_day_2020.weekday())  # 1 - tuesday

# Comparing datatime
current_datetime = datetime.now()

next_month = datetime.now()

print(current_datetime < next_month)    # False

# data delta
