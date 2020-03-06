def odd(start, end):
    global i
    for i in range(start, end):
        if i % 2 == 1:
            print(i)


def even(start, end):
    global i
    for i in range(start, end):
        if i % 2 == 0:
            print(i)


even(1, 101)
odd(1, 101)