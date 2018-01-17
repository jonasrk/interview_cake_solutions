import random

def rand7():
    return random.randint(1,7)

def rand5():
    sum = 0
    for i in range(0, 5):
        sum += rand7()
    return sum % 5 + 1

print(rand5())
