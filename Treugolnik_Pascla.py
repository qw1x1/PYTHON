def faktorial(num):
    f = 1
    for i in range(1, num+1):
        f *= i
    return f

def pascal(leen):
    l = []
    for i in range(0, leen):
        m = i + 1
        l.clear()
        for j in range(0, m):
            x = faktorial(i) / (faktorial(j) * faktorial(i - j))
            l.append(int(x))
        print(*l)

pascal(int(input()))
