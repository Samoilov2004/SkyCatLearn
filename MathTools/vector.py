class Vector:
    def __init__(self, components):
        if not isinstance(components, list):
            raise TypeError("Components must be a list")
        self.components = components

    def __repr__(self):
        # Строковое представление вектора
        return f"Vector({self.components})"

    def __add__(self, other):
        # Сложение двух векторов
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension")
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        # Вычитание одного вектора из другого
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension")
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, scalar):
        # Умножение вектора на скаляр
        return Vector([a * scalar for a in self.components])

    def __rmul__(self, scalar):
        # Умножение скаляра на вектор. Эквивалентно прошлому методу.
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        # Деление вектора на скаляр
        return Vector([a / scalar for a in self.components])

    def __eq__(self, other):
        # Проверка равенства векторов
        return self.components == other.components

    def dot(self, other):
        # Скалярное умножение двух векторов
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension")
        return sum(a * b for a, b in zip(self.components, other.components))

    def norm(self):
        # Евклидова норма вектора
        return (sum(a ** 2 for a in self.components))

    def len(self):
        return len(self.components)