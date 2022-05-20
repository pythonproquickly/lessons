tower1 = []
tower2 = []
tower3 = []

tower1.append("C")
tower1.append("B")
tower1.append("A")

print(tower1)

removed = tower1.pop()
print(removed)
print(tower1)

tower3.append(removed)
print(tower3)

tower2.append(tower1.pop())
print(tower1)
print(tower2)
print(tower3)
tower2.append(tower3.pop())
print(tower1)
print(tower2)
print(tower3)
