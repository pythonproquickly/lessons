from helper_functions import process_csv_supplies
from collections import deque

# The first row is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]

# Here is a sample of 2 elements in csv_data:
# [ ['nylon', '10', 'unimportant'], ['wool', '1', 'important'] ]

# Write your code below!
supplies_deque = deque()

for item in csv_data:

    if item[2] == "important":
        supplies_deque.appendleft(item)

    else:
        supplies_deque.append(item)

ordered_important_supplies = deque()
i = 1

while i <= 25:
    p_item = supplies_deque.popleft()
    ordered_important_supplies.append(p_item)
    i = i + 1

for item in ordered_important_supplies:
    print(item)

ordered_unimportant_supplies = deque()
j = 1

while j <= 10:  # NOTE j not i
    t_item = supplies_deque.pop()
    ordered_unimportant_supplies.append(t_item)
    j = j + 1

for item in ordered_unimportant_supplies:
    print(item)
