# 1.Question divisors
from math import *


def divisors_1(num):
    return [i for i in range(1, num+1) if num % i == 0]


def divisors_2(num):
    ls = set()
    for i in range(1,int(sqrt(num))+1):
        if num % i == 0:
            ls.add(i)
            ls.add(num // i)
    return ls


# Primality Test
def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 and n % 3 == 0:
        return False
    for i in range(5, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print(divisors_2(10000000))
print(divisors_1(10000000))
print(is_prime(3))
print(is_prime(5))
print(is_prime(7))
print(is_prime(3044567156798))

