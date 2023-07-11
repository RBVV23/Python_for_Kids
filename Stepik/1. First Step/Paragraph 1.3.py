# Приоритеты операций ###
#
#    действия в круглых скобках - самый высокий приоритет
#    ** возведение в степень и - унарный минус
#    *    /    //    %
#    +    -
#########################

print(36 ** 1/2)
# >>> 18.0
# т.к. приоритет ** выше, чем приоритет /
print(36 ** (1/2)) # или 36 ** 0.5 # находим квадратный корень
# >>> 6.0    # Внимание! Результатом этого действия является вещественное число (число с точкой)
print(2 ** 3 ** 2) # т.к. вычисления в данном случае выполняются справа налево 2**3**2=2**(3**2)=512!
# >>> 512
# - унарный минус
# если унарные операторы расположены слева от **,
# то возведение в степень имеет больший приоритет,
# а если справа – то меньший. Например:
print(-10 ** 2) # унарный минус имеет меньший приоритет (расположен слева от **)
# >>> -100
print(10 ** -2) # унарный минус имеет больший приоритет (расположен справа от **)
# >>> 0.01
print(-10 ** -2)
# >>> -0.01
# Совет! Для надежности используйте скобки для расстановки приоритетов,
# или внимательно тестируйте варианты использования
print((-10) ** 2)

print(5 + 5)
# >>> 10
print((5 + 5) * 2)
# >>> 20
print((3 + 2) ** 2)
# >>> 25
print(100 ** (1/2)) # можно извлекать квадратный корень
# >>> 10.0  # Внимание! Результатом этого действия является вещественное число (число с точкой)
print(100 ** 0.5)
# >>> 10.0
print(27 ** (1/3))  # можно извлекать кубический корень (и др. корни)
# >>> 3.0

# Обязательны ли скобки при возведении в (1/2) или (1/3)?

print(f'81 ** 1/2 = {81 ** 1/2}')
print(f'81 ** (1/2) = {81 ** (1/2)}')
print(f'27 ** 1/3 = {27 ** 1/3}')
print(f'27 ** (1/3) = {27 ** (1/3)}')

# Что будет если скобки не поставить? Проверьте и объясните результат.

a = 3
b = 4
print("a + b = ", a + b)
print("a / b = ", a / b)
print("a // b = ", a // b) # целочисленное деление
print("a ** b = ", a ** b) # a в степени b
print("a + b * a = ", a + b * a)
print("(a + b) * a = ", (a + b) * a)
print((a ** 2 + b ** 2) ** 0.5) # квадратный корень из суммы квадратов

python_3_8 = "Язык программировния"
velocity101 = 101
skorost101 = 101
true = True
true1 = 1
dog = "Rex"