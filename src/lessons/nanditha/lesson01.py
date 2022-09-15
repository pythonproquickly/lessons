name = "this is a string"
another ='kkkkkkk'

print(type(name))


new_name = name + "xxxx"
print(new_name)

words = name.split(',')

print(words)

name = "this is a string"
words = name.split(' ')

for word in words:
    print(word)

print('next')

print("-" * 4)

mystring = "ab1cd"
print(mystring[2])

#mystring[2] = "x"
# immutable

mylist = ['a', 'b', 1, 'c', 'd']

mylist[2] = "x"
print(mylist)

mylist = mylist + [3,4,5]
print(mylist)

name = "andy miles"
print(name[2:])

