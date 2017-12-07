def add(a, b):
    print(a+b)

def subtract(a, b):
    return a-b

def division(a, b = 0):
    if b is 0:
        b = 1

    return a/b

add(2,3)
print(subtract(455, 355))
print(division(3,))