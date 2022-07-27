from datetime import datetime


# str to date
td = "26.07.2022"
d = datetime.strptime(td, "%d.%m.%Y") # code here: https://plotly.github.io/static/images/dates-time-series-and-timestamp/timeSeriesFormat.png

#print(d1.date())
other_date = d.replace(year = 2022, month=3, day=11, hour  =11) 
print(other_date)

str_other_date = other_date.strftime("XY/fcd/Xm") 
str_other_date = other_date.strftime("%y/%d/%m %H:%M:%S") 
stn_other_date = other_date.strftime("%y year %d month %m %H:%M:%S") 
print(str_other_date) 
print(type(str_other_date))
