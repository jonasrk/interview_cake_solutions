def fib(x):

    last = 0
    second_last = 1
    current = 1

    for i in range(0, x):
        second_last = last
        last = current
        current = last + second_last

    return current

print(fib(10000))