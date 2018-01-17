import random

def rand7():
    return random.randint(1,7)

def rand5():
    rand = 8
    while rand > 5:
        rand = rand7()
    return rand

print(rand5())
