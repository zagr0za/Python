from random import randint


def random_list(a, b, c):
    w = [randint(a, b) for i in range(c)]
    print(w)


x = int(input("Введіть значення початку діапазону: "))
y = int(input("Введіть значення кінця діапазону: "))
z = int(input("Введіть кількість елементів у списку, що генерується: "))

random_list(int(x), int(y), int(z))
