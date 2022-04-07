from collections import namedtuple
from collections import deque

overstock_items = [
    ["shoes", 29.05],
    ["socks", 12.00],
    ["hats", 19.05],
    ["shirts", 42.00],
    ["scarves", 2.05],
    ["vests", 11.00],
    ["t shirts", 8.05],
    ["coats", 34.00],
    ["long socks", 4.05],
    ["jumpers", 28.00],

]

split_prices = deque()

for item in overstock_items:
    if item[1] > 20.00:
        split_prices.append(item)
    else:
        split_prices.appendleft(item)

ClothesBundle = namedtuple('ClothesBundle', ['bundle_items', 'items_price'])
bundles = []

while len(split_prices) >= 5:
    temp_build = []
    for _ in range(3):
        temp_build.append(split_prices.popleft())
    for _ in range(2):
        temp_build.append(split_prices.pop())
    total_price = 0
    for i in range(5):
        total_price += temp_build[i][1]
    bundles.append(ClothesBundle(temp_build, total_price))

print(bundles)
