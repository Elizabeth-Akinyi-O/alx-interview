#!/usr/bin/python3
"""
Implements Prime Game
"""


def isWinner(x, nums):
    """ Returns the winner in a prime game. """
    def sieve_of_eratosthenes(n):
        """Helper function to find all prime numbers up to
    n using the Sieve of Eratosthenes."""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime

    # Step 1: Precompute all primes up to 10000 (maximum possible n)
    max_num = max(nums) if nums else 0
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    # Step 2: Simulate each game
    for n in nums:
        if n == 1:
            # Ben wins automatically because no prime numbers are available
            ben_wins += 1
            continue
        # Count how many primes are in the range [1, n]
        primes_count = sum(primes[2:n+1])
        # If the count of primes is odd, Maria wins (since she starts first)
        # If it's even, Ben wins
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    # Step 3: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
