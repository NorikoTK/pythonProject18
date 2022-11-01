class Rectangle:
    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b

    def calculate_square(self):
        return self.a * self.b

    def calculator_perimeter(self):
        return (self.a + self.b) * 2

    def get_info(self):
        return f"Rectangle: a = {self.b}, b = {self.b}"


    def __del__(self):
        pass

rect1 = Rectangle(10,15)
rect2 = Rectangle(b=15, a=10)
rect3 = Rectangle(20)
rect4 = Rectangle()


