#ex1
def gen(n):
    for i in range(1, n + 1):
        yield i ** 2
        i += 1
print(*gen(int(input())))

#ex2
def gen(n):
    for i in range(0, n):
        if i % 2 == 0:
            yield i
        i += 1
print(*gen(int(input())), sep=",")

#ex3
def gen(n):
    for i in range(0, n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
        i += 1
print(*gen(int(input())))

#ex4
def squares(a, b):
    for i in range (a,b):
        yield i ** 2
        i += 1
a = int(input())
b = int(input())
print(*squares(a,b))

#ex5
def gen(n):
    for i in range (n, 0, -1):
        yield i
        i += 1
print(*gen(int(input())))