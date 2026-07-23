"""Task 4: Demonstrate Polymorphism with different classes having the same method name."""

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Chirp!"

def animal_speak(animal):
    """Polymorphic function that calls speak() on any animal object."""
    return animal.speak()

# Test
if __name__ == "__main__":
    animals = [Dog(), Cat(), Bird()]
    for animal in animals:
        print(f"{animal.__class__.__name__} says: {animal_speak(animal)}")
        print("Program Started")
