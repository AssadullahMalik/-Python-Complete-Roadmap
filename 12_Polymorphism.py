class Bird:
    def sound(self):
        print("Chirp")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

make_sound(Bird())
make_sound(Cat())
