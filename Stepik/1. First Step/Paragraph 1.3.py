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


# ---------------------------------------------


a = 3
b = 4
print("a + b = ", a + b)
print("a / b = ", a / b)
print("a // b = ", a // b) # целочисленное деление
print("a ** b = ", a ** b) # a в степени b
print("a + b * a = ", a + b * a)
print("(a + b) * a = ", (a + b) * a)
print((a ** 2 + b ** 2) ** 0.5) # квадратный корень из суммы квадратов


# ---------------------------------------------


python_3_8 = "Язык программировния"
print(python_3_8)
velocity101 = 101
print(velocity101)
skorost101 = 101
print(skorost101)
true = True
print(true)
true1 = 1
print(true1)
dog = "Rex"
print(dog)

# ---------------------------------------------

a = b = 5
print(a)
# >>> a
# 5
print(b)
# >>> b
# 5
a = 10
print(a)
# >>> a
# 10
print(b)
# >>> b
# 5


# ---------------------------------------------


a = 10
print(id(a))  # 140736317433936
print(id(10))  # 140736317433936
print(id(2 + 3))  # 140736317433776
print(id(5 + 5))  # 140736317433936
b = a
print(id(b))  # 140736317433936
a = 5
print(id(a))  # 140736317433776
print(id(b))  # 140736317433936


# ---------------------------------------------


print(int(float("5.4")))
print(int(float("5.9")))
print(int(5.4))
print(int(5.9))

a = "4"
print(a)
print(type(a))
a = int(a)
print(a)
print(type(a))
a = float(a)
print(a)
print(type(a))

h = 5
m = 30
print(str(h) + " часов " + str(m) + " минут")
print(f'{h} часов {m} минут')


# ---------------------------------------------


print(round(4.4))
# >>> 4
print(round(4.6))
# >>> 5
print(round(4.5))
# >>> 4
print(round(3.5))
# >>> 4
print(round(4.5555, 3))
# >>> 4.556
print(round(4.5554, 3))
# >>> 4.555
print(round(4.4445, 3))
# >>> 4.444