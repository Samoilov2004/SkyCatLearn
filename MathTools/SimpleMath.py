pi = 3.141592653589793
e = 2.718281828459045
tau = 2 * pi
inf = float('inf')
nan = float('nan')

def sqrt(a):
	# Просто квадратный корень
	return a ** (1/2)

def log(x):
    # Вычисляет натуральный логарифм x с использованием ряда Тейлора.
    if x <= 0:
        raise ValueError("x must be positive")
    result = 0
    term = (x - 1) / (x + 1)
    n = 1
    while abs(term) > 1e-10:
        result += 2 * term / n
        term *= (x - 1) * (x - 1) / ((x + 1) * (x + 1))
        n += 2
    return result

# Тригонометрические функции

def sin(x):
    # Вычисляет синус угла x (в радианах) с использованием ряда Тейлора.
    result = 0
    term = x
    n = 1
    while abs(term) > 1e-10:
        result += term
        term = -term * x * x / ((2 * n) * (2 * n + 1))
        n += 1
    return result

def cos(x):
    # Вычисляет косинус угла x (в радианах) с использованием ряда Тейлора.
    result = 1
    term = 1
    n = 1
    while abs(term) > 1e-10:
        term = -term * x * x / ((2 * n - 1) * (2 * n))
        result += term
        n += 1
    return result

def tan(x):
    # Вычисляет тангенс угла x (в радианах).
    return sin(x) / cos(x)

def asin(x):
    # Вычисляет арксинус x с использованием ряда Тейлора.
    if x < -1 or x > 1:
        raise ValueError("x must be in the range [-1, 1]")
    result = x
    term = x
    n = 1
    while abs(term) > 1e-10:
        term = term * x * x * (2 * n - 1) * (2 * n - 1) / ((2 * n) * (2 * n + 1))
        result += term
        n += 1
    return result

def acos(x):
    # Вычисляет арккосинус x с использованием ряда Тейлора.
    if x < -1 or x > 1:
        raise ValueError("x must be in the range [-1, 1]")
    return pi / 2 - asin(x)

def atan(x):
    # Вычисляет арктангенс x с использованием ряда Тейлора.
    result = x
    term = x
    n = 1
    while abs(term) > 1e-10:
        term = -term * x * x * (2 * n - 1) / (2 * n + 1)
        result += term
        n += 1
    return result

def atan2(y, x):
    # Вычисляет арктангенс двух аргументов y и x.
    if x > 0:
        return atan(y / x)
    elif x < 0 and y >= 0:
        return atan(y / x) + pi
    elif x < 0 and y < 0:
        return atan(y / x) - pi
    elif x == 0 and y > 0:
        return pi / 2
    elif x == 0 and y < 0:
        return -pi / 2
    else:
        return nan

def sinh(x):
    # Вычисляет гиперболический синус x с использованием ряда Тейлора.
    result = x
    term = x
    n = 1
    while abs(term) > 1e-10:
        term = term * x * x / ((2 * n) * (2 * n + 1))
        result += term
        n += 1
    return result

def cosh(x):
    # Вычисляет гиперболический косинус x с использованием ряда Тейлора.
    result = 1
    term = 1
    n = 1
    while abs(term) > 1e-10:
        term = term * x * x / ((2 * n - 1) * (2 * n))
        result += term
        n += 1
    return result

def tanh(x):
    # Вычисляет гиперболический тангенс x.
    return sinh(x) / cosh(x)

def asinh(x):
    # Вычисляет гиперболический арксинус x.
    return log(x + sqrt(x * x + 1))

def acosh(x):
    # Вычисляет гиперболический арккосинус x.
    if x < 1:
        raise ValueError("x must be greater than or equal to 1")
    return log(x + sqrt(x * x - 1))

def atanh(x):
    # Вычисляет гиперболический арктангенс x.
    if x <= -1 or x >= 1:
        raise ValueError("x must be in the range (-1, 1)")
    return 0.5 * log((1 + x) / (1 - x))