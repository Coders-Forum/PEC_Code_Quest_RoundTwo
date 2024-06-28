def prime_factorization(n):
    factors = {}
   
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    if count > 0:
        factors[2] = count
    
   
    for i in range(3, int(n**0.5) + 1, 2):
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 0:
            factors[i] = count
    

    if n > 2:
        factors[n] = 1
    
    result = []
    for prime, power in sorted(factors.items()):
        if power == 1:
            result.append(f"{prime}")
        else:
            result.append(f"{prime}^{power}")
    
    return " * ".join(result)


n = int(input().strip())


print(prime_factorization(n))
