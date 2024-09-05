#!/usr/bin/python3
"""Prime Game Algorith"""


def isWinner(x, nums):
    """
    Determines the winner of a game played x rounds.

    Args:
        x: Number of rounds.
        nums: List of integers where each integer represents
        the range of numbers for that round.

    Returns:
        The name of the player that won the most rounds
        ("Maria" or "Ben").
        If the winner cannot be determined, return None.
    """
    if x < 1 or not nums:
        return None

    def sieve_of_eratosthenes(n):
        """
        Helper function to generate prime numbers up to the
        maximum value in nums using the Sieve of Eratosthenes
        """
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime

    max_n = max(nums)

    primes = sieve_of_eratosthenes(max_n)

    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
