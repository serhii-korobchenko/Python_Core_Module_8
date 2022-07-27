from datetime import datetime, timedelta

d = datetime.now()
interval = timedelta(days=4)
finish = d + interval
print(f"result is: {finish}")

birth_date = datetime(1957, 8, 23) 
t = datetime.now() - birth_date

print(t)



