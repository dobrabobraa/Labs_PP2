def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))

for sq in squares(a, b):
    print(sq)
