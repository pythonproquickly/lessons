
import more_itertools

favorite_numbers = []
my_iterator = iter(favorite_numbers)
print(len(list(my_iterator)))
exit()

size_check = more_itertools.peekable(my_iterator)
if size_check:
    print("full")
    # Iterator is non-empty.
else:
    print("empty")
    # Iterator is empty.
