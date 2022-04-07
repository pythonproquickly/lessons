# why use __init__ ?
# if you need instance variables class scoped variables are confusing
# look at subtleties of this...

class OneWay:
    a = 1
    b = []


oneway = OneWay()
assert oneway.a == 1

oneway2 = OneWay()
assert oneway2.a == 1

oneway.a += 1
assert oneway.a != oneway2.a
assert oneway.a == 2
assert oneway2.a == 1

oneway.b.append("1")
assert oneway.b == ["1"]
assert oneway2.b == oneway.b


class TwoWay:
    def __init__(self):
        self.a = 1
        self.b = []


twoway = TwoWay()
twoway2 = TwoWay()

twoway.b.append(["1"])
assert twoway.b != twoway2.b
