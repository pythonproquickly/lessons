def divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        raise ZeroDivisionError
    return result


print(divide(10, 2))
try:
    print(divide(2, 0))
except ZeroDivisionError:
    print("woops")

age = input("enter age: ")
try:
    # print(f"last year you were {age - 1}")
    age = 24
except TypeError:
    print(f"last year you were {int(age) - 1}")
except ZeroDivisionError:
    pass
else:
    print("doing else")
finally:
    print("finally")


def get_input():
    name = input("name?")
    age = input("age?")
    size = input("size")
    return {'name': name, 'age': age}


data = get_input()
valid = validate(data)

# ------
# dictionaries

countries = {'us': "United States of America", 'gb': "Great Britain"}
countries['mx'] = "Mexico"  # add
countries['us'] = 'USA'  # update

print(countries['us'])

# ===
people = ['fred', 47, 'pink']
