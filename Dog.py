from Animal import Animal

class Dog(Animal):
    def __init__(self, name):
        self.__name = name  # Private attribute

    def sound(self):
        return "Bark"

    def move(self):
        return "Runs on four legs"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name