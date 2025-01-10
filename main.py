from Car import Car
from Dog import Dog
from Cat import Cat
from Person import Person


def animal_behavior(animal):
    """This function works for any Animal instance."""
    print(f"{animal.sound()} and {animal.move()}")

if __name__ == "__main__":
    # Abstraction and Encapsulation
    # dog = Dog("Buddy")
    # print(f"The dog's name is {dog.get_name()}")
    # dog.set_name("Max")
    # print(f"The dog's new name is {dog.get_name()}")

    #Inheritance and Polymorphism
    cat = Cat("Big Mini")
    # animal_behavior(dog)  # Polymorphism: Dog behavior
    # animal_behavior(cat)  # Polymorphism: Cat behavior

    # Association
    # person = Person("Prodip")
    # person.adopt_pet(cat)  # Alice adopts a dog
    # print(f"{person.name} has adopted a pet named {person.pet.get_name()}.")

    # # Composition
    car = Car("Tesla Model S")
    print(car.start_car())
    print(car.stop_car())