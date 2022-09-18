def f(num):
    f = 1
    for i in range(1, num+1):
        f *= i
    return f

print(f(int(input())))
