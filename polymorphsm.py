# Animals
class Dog:
    def move(self):
        print("Running 🐕")

class Fish:
    def move(self):
        print("Swimming 🐟")

# Vehicles
class Car:
    def move(self):
        print("Driving 🚗")

class Airplane:
    def move(self):
        print("Flying ✈️")

# Demonstrate movement
def main():
    creatures = [Dog(), Fish(), Car(), Airplane()]
    
    for obj in creatures:
        obj.move()

if __name__ == "__main__":
    main()