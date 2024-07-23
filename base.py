from abc import ABC
from abc import abstractmethod


class Shape(ABC):
    """
    Абстрактный класс, на основании которого
    реализованы классы геометрических фигур
    """

    @abstractmethod
    def get_area(self) -> float:
        """
        Абстрактный метод, не позволяющий реализовать класс,
        представляющий геометрическую фигуру, не создав
        метод по вычислению ее площади
        """

        pass
