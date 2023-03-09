# Ayomide
import math

def sieve_primes(num):
    ls = [True for i in range(0, num+1)]
    ls[0] = ls[1] = False
    for i in range(2, num+1):
        if ls[i]:
            for j in range(i*i, num+1, i):
                ls[j] = False
    return ls


def nat_log_prime(x):
    return int(x/math.log(x))


def compare_both_algs(x):
    ls = sieve_primes(x)
    num_of_primes = nat_log_prime(x)
    count = 0
    for i, t in enumerate(ls):
        if t == True:
            count = count+1
    print("count of primes from sieve_primes: ", count)
    print("count of primes from nat_log_prime: ", num_of_primes)
    return count/num_of_primes


for i in range(10000, 1000000):
    print(compare_both_algs(i))
