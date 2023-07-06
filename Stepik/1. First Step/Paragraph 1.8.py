a = ["a", "b", "c"]
print(a[0])
# >>> 'a'
print(a[1])
# >>> 'b'
print(a[-1])  # выбор первого справа элемента, как бы краткая запись a[ len(a) - 1 ]
# >>> 'c'
print(len(a))  # функция, которая выводит количество элементов списка
# >>> 3


d = [1, 2, 3, 4]
print(d[0] + d[1] + d[2] + d[3])
# >>> 10
print(sum(d))
# >>> 10

print("one two three".split())
# >>> ['one', 'two', 'three']
s = "one two three"
print(s.split())
# >>> ['one', 'two', 'three']


a, b, c = "1 2 3".split()
print(a)
# >>> '1'
print(int(a))
# >>> 1
print(b)
# >>> '2'
print(int(b))
# >>> 2
print(c)
# >>> '3'
print(int(c))
# >>> 3


# Дана строка (три числа, разделенные пробелом)
# 1 2 3
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(a + b + c)