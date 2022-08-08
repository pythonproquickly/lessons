
RATE = 10
def globals():
    return {'rate': 10, 'value': 2, 'filename': 'x'}

def doit(factor: int) -> list:
    if rate == globals()['rate']:
        # do something
    return [1, 2, factor]


print(doit(1))
