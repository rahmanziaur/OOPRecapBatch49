from Animal import Animal

class Cat(Animal):
    def __init__(self, name):
        self.name = name  # Public attribute

    def sound(self):
        return "Meow"

    def move(self):
        return "Jumps gracefully"

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name