class Circle:

    VALID_COLORS = ['red', 'blue', 'green']

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if new_radius > 0:
            self._radius = new_radius
        else:
            print("Invalid radius")

    radius = property(get_radius, set_radius)

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            print(f"{new_color.title()} is not a valid color")
        
    color = property(get_color, set_color)
    
my_circle = Circle(5, "blue")
your_circle = Circle(10, 'red')

print(f"My circle has a radius of {my_circle.radius} and a color of {my_circle.color}")
print(f"Your circle has a radius of {your_circle.radius} and a color of {your_circle.color}")

my_circle.radius = 16
your_circle.color ="purple"
my_circle.radius = 16
your_circle.color ="green"

print(f"My circle has a radius of {my_circle.radius} and a color of {my_circle.color}")
print(f"Your circle has a radius of {your_circle.radius} and a color of {your_circle.color}")
