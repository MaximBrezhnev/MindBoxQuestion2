import math
from typing import List

from base import Shape


class Triangle(Shape):
    """
    Класс для представления треугольника
    """

    def __init__(self, a: float, b: float, c: float) -> None:
        if not self.is_valid_triangle(a, b, c):
            raise ValueError("Triangle with these sides does not exist")

        self.a: float = a
        self.b: float = b
        self.c: float = c

    @staticmethod
    def is_valid_triangle(a: float, b: float, c: float) -> bool:
        """Проверяет, существует ли треугольник на основании 'неравенства треугольника'"""

        return a + b > c and a + c > b and b + c > a

    def get_area(self) -> float:
        """Возвращает площадь треугольника, используя формулу Герона"""

        s: float = (self.a + self.b + self.c) / 2
        return math.sqrt(
            s * (s - self.a) * (s - self.b) * (s - self.c)
        )

    def is_rectangular(self) -> bool:
        """Проверяет, является ли треугольник прямоугольным"""

        sorted_sides: List[float] = sorted([self.a, self.b, self.c])
        return sorted_sides[2]**2 == sorted_sides[1]**2 + sorted_sides[0]**2


class Circle(Shape):
    """Класс для представления круга"""

    def __init__(self, radius: float) -> None:
        self.radius: float = radius

    def get_area(self) -> float:
        """Возвращает площадь круга на основании его радиуса"""

        return math.pi * (self.radius ** 2)
