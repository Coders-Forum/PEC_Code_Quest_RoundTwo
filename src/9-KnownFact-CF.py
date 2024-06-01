a, b = map(int, input().split())

if a == b:
    print(1)
elif a > b:
    print(fact(a, b + 1))
else:
    print(fact(b, a + 1))

def fact(n,s):
    f = 1
    for i in range(s, n + 1):
        f *= i
    return f
