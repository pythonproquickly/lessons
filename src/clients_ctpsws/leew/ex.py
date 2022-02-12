from collections import namedtuple


Student = namedtuple('Student', ['name', 'age', 'DOB', 'ID'])


s = Student('andy', '42', 'Feb 27', '9988')
andy = Student('andy2', '32', 'KKKK')
print(s)
print(s.name)

print(s.age)

