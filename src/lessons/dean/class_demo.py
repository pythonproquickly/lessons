class Pet:
    def __init__(self, pet_type):
        self.pet_type = pet_type

    def speak(self):
        if self.pet_type == "dog":
            print("Woof")
        else:
            print("Meow")


rover = Pet("dog")
rover.speak()

mittens = Pet("cat")
mittens.speak()

print(type(rover))
