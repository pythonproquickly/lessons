"""# immutable
mytuple = (1, 2)
mytuple[0] = 9
mystr = "abc"

# mutable
myset = {1, 3, 7}
myset.add(9)
assert myset == {1, 3, 7, 9}

mylist = [1, 2]
mylist[0] = 999
mdict = {}"""

"""mysuper_tuple = ([1, 2, 3], [999, 111])

mysuper_tuple[0][1] = 99999999

print(mysuper_tuple)

l1 = [1,2,3]
l2 = l1.copy()
l1.append(9999999)
print(l2)"""

long_list = range(100000000)


def cal(l):
    return sum(l)


cal(long_list)
