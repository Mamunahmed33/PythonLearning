square = lambda x: x*x
sum = lambda a: sum(a)

def sum(a):
    s = 0

    for i in a:
        s += i
    return s


print(square(25))

l =[1,2,3,4,5]
print(sum(l))