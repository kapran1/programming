class Polynomial:
    def __init__(self, *coefficients): # Создает многочлен
        self.coefficients = []

        if len(coefficients) == 1:
            data = coefficients[0]

            if isinstance(data, Polynomial):
                self.coefficients = list(data.coefficients)

            elif isinstance(data, list):
                self.coefficients = list(data)

            elif isinstance(data, dict):
                if data:
                    max_pow = max(data)
                    self.coefficients = [0] * (max_pow + 1)
                    for power in data:
                        self.coefficients[power] = data[power]
                else:
                    self.coefficients = [0]

            else:
                self.coefficients = [data]

        else:
            self.coefficients = list(coefficients)

        while len(self.coefficients) > 1 and self.coefficients[-1] == 0:
            self.coefficients.pop()

        if not self.coefficients:
            self.coefficients = [0]

    def __repr__(self):
        return f"Polynomial {self.coefficients}" # Возращает строку для разработчика 

    def __str__(self): # Красивая записать вида многочлена для пользователя
        result = ""

        for power in range(len(self.coefficients) - 1, -1, -1):
            coef = self.coefficients[power]

            if coef == 0:
                continue

            sign = "-" if coef < 0 else "+"
            abs_coef = abs(coef)

            if power == 0:
                body = str(abs_coef)
            else:
                if abs_coef == 1:
                    coef_str = ""
                else:
                    coef_str = str(abs_coef)

                if power == 1:
                    body = coef_str + "x"
                else:
                    body = f"{coef_str}x^{power}"

            if result == "":
                if sign == "-":
                    result = "-" + body
                else:
                    result = body
            else:
                result += f" {sign} {body}"

        if result == "":
            return "0"

        return result

    def __eq__(self, other): # Сравнение многочленов
        if isinstance(other, (int, float)):
            other = Polynomial(other)
        if not isinstance(other, Polynomial):
            return False
        return self.coefficients == other.coefficients

    def __add__(self, other): # Сложение многочленов
        if isinstance(other, (int, float)):
            other = Polynomial(other)
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coef = [0] * max_len

        for i in range(max_len):
            c1 = self.coefficients[i] if i < len(self.coefficients) else 0
            c2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coef[i] = c1 + c2
        return Polynomial(new_coef)

    def __radd__(self, other): # Сложение многочлена с числом
        return self.__add__(other)

    def __neg__(self): # Возвращает многочлен с противоположными коэффициентами
        new_coef = [-c for c in self.coefficients]
        return Polynomial(new_coef)

    def __sub__(self, other): # Вычитание многочленов
        return self + (-other)

    def __rsub__(self, other):# Вычитание числа из многочлена
        return (-self) + other

    def __call__(self, x): # Вычисляет значение многочлена в точке x
        result = 0
        for power in range(len(self.coefficients)):
            result += self.coefficients[power] * x ** power
        return result

    def degree(self): # Возвращает степень многочлена
        return len(self.coefficients) - 1

    def der(self, d=1): # Возвращает производную многочлена d-го порядка
        coefs = list(self.coefficients)
        for _ in range(d):
            coefs = [i * coefs[i] for i in range(1, len(coefs))]
        return Polynomial(coefs)

    def __mul__(self, other): # Умножение многочленов
        if isinstance(other, (int, float)):
            other = Polynomial(other)
        new_coef = [0] * (len(self.coefficients) + len(other.coefficients) - 1)

        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                new_coef[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(new_coef)

    def __rmul__(self, other): #    
        return self.__mul__(other)

    def __iter__(self): # Возвращает итератор для многочлена
        self.index = 0
        return self

    def __next__(self): # Возвращает следующую пару (степень, коэффициент) многочлена
        if self.index >= len(self.coefficients):
            raise StopIteration
        pair = (self.index, self.coefficients[self.index])
        self.index += 1
        return pair

print(repr(Polynomial(1, 2, 3)))
print(Polynomial({0: 1, 1: 2, 2: 3}))
print(Polynomial(5))
print(5.5 * Polynomial())