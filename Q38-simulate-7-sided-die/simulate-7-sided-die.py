import random

def rand5():
    return random.randint(1,5)

def rand7():
    result = None
    found = False
    while not found:
        b0 = rand5()
        b1 = rand5()

        dec = b0 + 5 * b1

        if dec >= 1 and dec <= 7:
            result = dec
            found = True

    return result

print(rand7())
