#!/usr/bin/python3
""" Python program to print all
    primes smaller than or equal to
    n using Sieve of Eratosthenes
"""


def SieveOfEratosthenes(n):
    """ Create a boolean array
     "prime[0..n]" and initialize
      all entries it as true.
     A value in prime[i] will
     finally be false if i is
     Not a prime, else true.
    """
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not
        # changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    final = []
    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            final.append(p)
    return final


def isWinner(x, nums):
    """Function to calculate winner of a game
        x is the number of rounds
        nums list with the value of each round
    """
    maria = 0
    ben = 0
    for i in range(x):
        n = nums[i]
        integer_set = [i for i in range(1, n+1)]
        prime_num = SieveOfEratosthenes(n)
        if len(prime_num) == 0:
            ben += 1
            continue
        if len(prime_num) % 2 == 0:
            ben += 1
            continue
        maria += 1
    if maria > ben:
        return 'Maria'
    else:
        return 'Ben'
