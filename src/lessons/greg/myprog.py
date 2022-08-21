"""import funcs


print(funcs.addup(5, 6))
print(funcs.subtract(9, 3))"""

names = ["fred", "bill", "andy", "susan", "andy"]

"""new_names = []

for name in names:
    if len(name) == 4:
        new_names.append(name)

print(new_names)"""

gen = (name for name in names if len(name) == 4)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))