class Vehicle:
    def __init__(self, name):
        self.name = name
        
    def move(self):
        print("moving")


if __name__ == "__main__":
    car = Vehicle("toyota")
    car.move()
    print(car.name)
