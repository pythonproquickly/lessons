print("python is a {3} {2} {1} {0}!".format(
    "by all",
    "learned",
    "easily",
    "language"))

print("I always submit a {pr} {1} my assignment {0}.".format(
    "is done",
    "when",
    pr="pull request"))

print("Show {0:f} percent of a {1}".format(75, "number"))

print("Show {0:.3f} percent of a number".format(75.765367))

print("Show {0:.0f} percent of a number".format(75.765367))

print("I have {0:<4} errors and {1:^16}".format(5, "warnings"))

print("Show {0:5.0f} percent of a number".format(75.765367))

print("{:*^20s}".format("wrap me"))

for i in range(5,21):
    print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))
