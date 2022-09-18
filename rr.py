def fib(n):
    f1, f2 = 1, 1
    while f2 < n:
        f1, f2 = f2, f1+f2
    return f1

def main():
    n = int(input())
    print((fib(n) % 10 + n % 10) % 10)


if __name__ == "__main__":
    main()

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
result = list(filter(lambda: True, primes))
print(result)

test1 = (result, input()) #, input().split())
def test(result, answer):
    if str(result) == answer:
        print(YES)
    else:
        print(NO)