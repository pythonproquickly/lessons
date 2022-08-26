l = 0
while l<11:
    l += 1
    mylist = [1,2,3,4,5,6,7,4,5,6,7,8,9,99,99,10]
    for num in mylist:
        if num % 2 == 0:
            mylist.remove(num)

print(mylist)