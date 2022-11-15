class Vehicle():

    def __init__(self, type):
        self.type = type
    # end __init__
# end class Vehicle

class Automobile(Vehicle):

    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    # end __init__
# end class Automobile

print("Please enter information describing a car.")
car = Automobile("car", input("Enter year: "), 
    input("Enter make: "), input("Enter model: "), 
    input("Enter number of doors (2 or 4): "), 
    input("Enter roof type (solid or sun roof): "))

print("Car info:")
print(f"Vehicle type: {car.type}\nYear: {car.year}\nMake: {car.make}\n\
Model: {car.model}\nNumber of doors: {car.doors}\n\
Type of roof: {car.roof}")