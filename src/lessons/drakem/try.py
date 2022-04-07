import random
my_list = [random.randrange(1, 10, 1) for i in range(1000000)]
print(my_list)
# Creating an empty dictionary
freq = {}
for item in my_list:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1
for key, value in freq.items():
    print (“% d : % d”%(key, value))
