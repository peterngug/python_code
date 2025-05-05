class Car:
    color = "red"  # Class variable
    model = "Toyota"  # Class variable

    def drive(self):
        print("Driving...")
        print(f"Car color: {self.color}")  # Access the class variable

# Create an instance of the Car class
my_car = Car()

# Call the instance method
my_car.drive()