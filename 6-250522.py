from random import randint


def random_list():
    a = [randint(0, 7) for i in range(7)]
    print(a)


random_list()
