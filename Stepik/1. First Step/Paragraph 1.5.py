a = 1
b = 2
c = 3

print(a * 100 + b * 10 + c)
# >>> 123
print(str(a))
# >>> '1'
print(str(a) + str(b) + str(c))
# >>> '123'
print("{}{}{}".format(a, b, c))
# >>> '123'
print(int(str(a) + str(b) + str(c)))
# >>> 123


# ---------------------------------------------


n = int(input())
h = n // 60
print(h)


# ---------------------------------------------


n = int(input())
h = n // 60
m = n - h * 60
print(m)


# ---------------------------------------------


n = int(input())
n = n % (24 * 60)
h = n // 60
print(h)


# ---------------------------------------------


n = int(input())


