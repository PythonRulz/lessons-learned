class Vehicle():
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
        

class Bus(Vehicle):
    capacity = 50

yellow_b = Bus('isd', 55, 225)
print(yellow_b.seating_capacity(capacity))
