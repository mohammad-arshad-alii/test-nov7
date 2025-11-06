class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"



#create an object of Dog class, and call speak method
