# --- ASSOCIATION ---
# Association represents a relationship between objects. Here, a Person 'has-a' pet (but they are independent).
class Person:
    pet = None           # No pet initially
    def __init__(self, name):
        self.name = name #variable

    def adopt_pet(self, pet):
        """Associates a pet (Dog, Cat, etc.) with the person."""
        self.pet = pet
