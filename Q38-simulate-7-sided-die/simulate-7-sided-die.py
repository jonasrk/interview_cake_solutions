import random

def rand5():
    return random.randint(1,5)

def rand01():
    res = 5
    while res > 2:
        res = rand5()
    return res - 1

def rand7():
    result = None
    found = False
    while not found:
        b0 = rand01()
        b1 = rand01()
        b2 = rand01()

        dec = b0 + 2 * b1 + 4 * b2

        if dec > 0:
            result = dec
            found = True

    return result

print(rand7())
