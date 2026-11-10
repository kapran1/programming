class Polynomial:
    def __init__(self, *coefficients):
        self.coefficients = []                      # здесь будем хранить коэффициенты

        if len(coefficients) == 1:                  # передан один аргумент
            data = coefficients[0]                  # берём его

            if isinstance(data, Polynomial):        # это другой многочлен?
                self.coefficients = list(data.coefficients)  # копируем его список

            elif isinstance(data, list):            # это список?
                self.coefficients = list(data)      # копируем список

            elif isinstance(data, dict):            # это словарь {степень: коэффициент}?
                if data:                            # словарь не пустой
                    max_pow = max(data)             # max по словарю берёт наибольший ключ (степень)
                    self.coefficients = [0] * (max_pow + 1)  # заготовка из нулей
                    for power in data:
                        self.coefficients[power] = data[power]  # ставим коэффициент на свою степень
                else:
                    self.coefficients = [0]         # пустой словарь, значит многочлен 0

            else:                                   # просто число, например Polynomial(5)
                self.coefficients = [data]

        else:                                       # аргументов несколько (или ноль)
            self.coefficients = list(coefficients)  # кортеж превращаем в список

        if not self.coefficients:                   # если список всё ещё пустой
            self.coefficients = [0]                 # то это многочлен 0

    def __repr__(self):
        return f"Polynomial {self.coefficients}"   # список кэфов
    def __str__(self):
        result = ""                                   # сюда будем дописывать члены многочлена

        # идём от старшей степени к 0: range(старт, стоп, шаг)
        # старт = len - 1 (последний индекс), стоп = -1 (до 0 включительно), шаг = -1 (назад)
        for power in range(len(self.coefficients) - 1, -1, -1):
            coef = self.coefficients[power]           # коэффициент при x^power

            if coef == 0:                             # нулевые члены пропускаем
                continue

            sign = "-" if coef < 0 else "+"           # знак запоминаем отдельно
            abs_coef = abs(coef)                      # дальше работаем с модулем числа

            if power == 0:                            # свободный член (без x)
                body = str(abs_coef)                  # просто число: 7
            else:
                if abs_coef == 1:                     # коэффициент 1 не пишем
                    coef_str = ""
                else:
                    coef_str = str(abs_coef)          # иначе пишем число: 4

                if power == 1:                        # первая степень: без "^1"
                    body = coef_str + "x"             # 4x или x
                else:
                    body = f"{coef_str}x^{power}"     # 4x^3 или x^3

            if result == "":                          # это самый первый записанный член
                if sign == "-":
                    result = "-" + body               # у первого члена минус липнет: -x^2
                else:
                    result = body                     # а плюс в начале не нужен
            else:                                     # не первый член
                result += f" {sign} {body}"           # добавляем " + 2x" или " - 7"

        if result == "":                              # ни один член не добавился
            return "0"                                # значит многочлен нулевой

        return result

    def __eq__(self, other):
        if isinstance(other, (int,float)):
            other = Polynomial(other)
        if not isinstance(other, Polynomial):
            return False
        return self.coefficients == other.coefficients  # Сравнение многочленов
    def __add__(self,other):
        if isinstance(other, (int, float)):
            other = Polynomial(other)
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coef = [0] * max_len

        for i in range(max_len):
            c1 = self.coefficients[i] if i < len(self.coefficients) else 0
            c2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coef[i] = c1 + c2
        return Polynomial(new_coef) # Сложение многочленов
    def __radd__(self, other):
        return self.__add__(other)
    def __neg__(self):
        new_coef = [-c for c in self.coefficients]
        return Polynomial(new_coef)
    def __sub__(self, other):
        pass
    def __rsub__(self, other):
        pass
    def __call__(self, x):
        pass
    def degree(self):
        pass
    def der(self, d=1):
        pass
    def __mul__(self, other):
        pass
    def __rmul__(self, other):
        pass
    def __iter__(self):
        pass
    def __next__(self):
        pass

# --- ПРОСТОЙ ТЕСТ __neg__ ---
p_neg_test = Polynomial(-2, 4, 3)  # 3x^2 + 4x - 2

print("Исходный многочлен:", p_neg_test)  # Покажет: 3x^2 + 4x - 2
print("С унарным минусом: ", -p_neg_test) # Должно напечатать: -3x^2 - 4x + 2
