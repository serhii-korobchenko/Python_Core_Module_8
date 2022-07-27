
from datetime import datetime

# create data time
date = datetime(year=2022, month = 7, day=26)
date = datetime(year=2022, month=7, day=26, hour=19, minute=38, second=35)

print(date)

print(date.date())
print(date.time())
print(date.now())
print(date.today())
print(date.isoformat()) # 2022-07-26T19:38:35



