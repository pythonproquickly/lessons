myset = {}
mydict = {}

myset = set()
mydict = dict()

myset.add(1)
myset.add(9)
myset.add(1)
print(myset)

mydict["num"] = 1
print(mydict)

mylist = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4]
mynewlist = list(set(mylist))
print(mynewlist)
