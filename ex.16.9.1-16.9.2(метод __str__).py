# 16.9.1-16.9.2

class Rectangle:
    def __init__(self,x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Координаты {self.x} и {self.y}. Ширина {self.width}, высота {self.height}"

    def Area(self):
        return self.width * self.height

r = Rectangle(5, 10, 50, 100)
print(r)

r = Rectangle(5,10, 50, 100)
print(f"Площадь прямоугольника - {r.Area()}")
