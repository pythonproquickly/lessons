import time
# scenario 1 - I built this, I test this
def doit_slowly(something):
    if something == "1":
        time.sleep(60)
        return True
    return False



# scenaro 2 - I built this, it uses doit_slowly

def do_something(number):
    return doit_slowly(number)
