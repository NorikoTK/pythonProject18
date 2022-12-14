import random
from rectangle import Rectangle

class RectangleCreator:
    SECOND_SIDE_RANGE = 20
    FIRST_SIDE_RANGE = 10

    def get_rectangles(size):
        rectangles = []

        for _ in range(size):
            rect = Rectangle()
            rect.a = random.randint(1, RectangleCreator.FIRST_SIDE_RANGE)
            rect.b = random.randint(1, RectangleCreator.SECOND_SIDE_RANGE)
            rectangles.append(rect)

        return rectangles