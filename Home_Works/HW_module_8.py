""" Вам нужно реализовать полезную функцию для вывода списка коллег, 
которых надо поздравить с днём рождения на неделе.

У вас есть список словарей users, каждый словарь в нём обязательно 
имеет ключи name и birthday. Такая структура представляет модель списка 
пользователей с их именами и днями рождения. name — это строка с именем пользователя, 
а birthday — это datetime объект, в котором записан день рождения.

Ваша задача написать функцию get_birthdays_per_week, 
которая получает на вход список users и выводит в консоль (при помощи print) 
список пользователей, которых надо поздравить по дням.
 """
""" 
Inputs:
1. List of Dicts --> users:
    Dict ('name': XXX, 'birthday': XXX ---> datatime object)

users = [
    {'name': 'Bill', 'birthday': datetime(year=1980, month=7, day=29)},
    {'name': 'John', 'birthday': datetime(year=1978, month=7, day=30)},
    {'name': 'Glock', 'birthday': datetime(year=1922, month=7, day=31)},
    {'name': 'Avel', 'birthday': datetime(year=1945, month=8, day=1)},
    {'name': 'David', 'birthday': datetime(year=2008, month=8, day=2)},
    {'name': 'Avatar', 'birthday': datetime(year=1960, month=8, day=3)},
    {'name': 'Ivan', 'birthday': datetime(year=2005, month=8, day=4)}
]

Outputs:
1. Def get_birthdays_per_week (users):
    print : Monday: Bill, Jill
            Friday: Kim, Jan

Requirements: 
1. Weekend birthday --> congrats on MONDAY
2. Scope function work --> 1 week in futures
3. Week starts from MONDAY """

from datetime import datetime, timedelta
from collections import defaultdict

users = [
    {'name': 'Bill', 'birthday': datetime(year=1980, month=7, day=29)},
    {'name': 'John', 'birthday': datetime(year=1978, month=7, day=30)},
    {'name': 'Glock', 'birthday': datetime(year=1922, month=7, day=31)},
    {'name': 'Avel', 'birthday': datetime(year=1945, month=8, day=1)},
    {'name': 'David', 'birthday': datetime(year=2008, month=8, day=2)},
    {'name': 'Avatar', 'birthday': datetime(year=1960, month=8, day=3)},
    {'name': 'Ivan', 'birthday': datetime(year=2005, month=8, day=4)},
    {'name': 'Sonia', 'birthday': datetime(year=2001, month=8, day=1)}
]


def days_translation (day_num):
    days_translation = {
     'Monday':    0,
     'Tuesday' :  1,
     'Wednesday': 2,
     'Thursday' : 3,
     'Friday' :   4,
     'Saturday' : 5,
     'Sunday' :   6
}
    
    for key, value in days_translation.items():
        if value == day_num:
            res = key
            break
    
    return res 

def get_birthdays_per_week (users):

    current_date = datetime.now().date() ##
    finish_date = current_date + timedelta(days=7) # set up time horizont
    
    
    #print(current_date, '\n', finish_date)
    grouped_birthdays = defaultdict(list)

    for item in users:
        event_date = datetime (year = current_date.year, month = item['birthday'].month, day = item['birthday'].day).date() ##
        

        if event_date > current_date and event_date <= finish_date:
            if event_date.weekday() != 5 and event_date.weekday() != 6:
                grouped_birthdays[days_translation(event_date.weekday())].append(item['name']) ### ?????
            elif event_date.weekday() == 5:
                grouped_birthdays[days_translation(0)].append(item['name'])
            elif event_date.weekday() == 6:
                grouped_birthdays[days_translation(0)].append(item['name'])

    return grouped_birthdays

### Main BODY
if __name__ == '__main__':
    dict = get_birthdays_per_week (users)
    for key, value in dict.items():
        print("{:<10}: {:<20}" .format(key, ', '.join(map(str, value))))               
    
    
