n = int(input())

s = set()

while n != 1 and n not in s:
    s.add(n)
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit ** 2
        n //= 10
    n = sum

print(n == 1)
