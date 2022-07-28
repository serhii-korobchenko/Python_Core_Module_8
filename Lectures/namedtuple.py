import collections

Person = collections.namedtuple('Person', ['name', 'last_name', 'age', 'birth_place', 'post_index']) # Set up tuple`s category`
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')
person.name         # 'Mick'
person.post_index   # '01146'
person.age          # 35
person[3]           # 'Boston'
print(person.name)

