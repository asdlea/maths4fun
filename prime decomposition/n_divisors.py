############################
#   Prime decompostition   #
############################

# for the sake of shortness I'm harcoding the first 10 primes
import timeit
primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]


# 1st method
# given a positive int > 1, let's find the divisors by prime decomposition
r = dict({x: 0 for x in primes})


def prime_factorization(n):
    for x in primes[1:]:
        if n % x != 0:
            pass
        else:
            if n/x not in primes[1:]:
                r[x] += 1
                return prime_factorization(n/x)
            else:
                r[n/x] += 1
    return r


print(*[f'{x}:{y};'.format(x, y)
        for x, y in prime_factorization(12).items() if y > 0])
