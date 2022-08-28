from hashlib import new
import demo_class

# demo_class.Class.method()
new_car = demo_class.Vehicle("bmw")
print(new_car.name)

new_car.move()
