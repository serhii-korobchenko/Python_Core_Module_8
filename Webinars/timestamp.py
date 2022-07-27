from datetime import datetime, MINYEAR, MAXYEAR 
d = datetime.now()

print(d.timestamp())	# к-сть секунл з 01.01.1970 unix_time: https://uk.wikipedia.org/wiki/%D0%A7%D0%B0%D1%81_Unix

print (d.toordinal()) #

print(MINYEAR) # 1
print(MAXYEAR) # 9999
print(d.ctime())# Tue Jul 26 20:30:12 2022



print(d.isoformat(sep="T"))

sec = str(d.timestamp()) 
print(sec)

restore_day = datetime.fromordinal(day) 
restore_iso = datetime.fromisoformat(iso)

print(f"restore.day: {restore_day}")


