import MathTools as mt

# Пример использования класса Vector
v1 = mt.Vector([1, 2, 3])
v2 = mt.Vector([4, 5, 6])
v1 + v2
v1 * v2

v3 = v1 + v2

# Пример использования модуля my_math
print(f"pi = {mt.pi}")
print(f"e = {mt.e}")
print(f"sin(pi/2) = {mt.sin(mt.pi / 2)}")
print(f"cos(pi) = {mt.cos(mt.pi)}")