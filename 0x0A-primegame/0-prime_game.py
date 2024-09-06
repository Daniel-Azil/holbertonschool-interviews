#!/usr/bin/python3
"""
Determine the winner of the Prime Game
"""


def get_prime_numbers(n):
    """Generates a list of prime numbers from 1 to n (inclusive)
       Args:
        n (int): the upper limit of the range starting from 1
    """
    primes_list = []
    sieve = [True] * (n + 1)
    for num in range(2, n + 1):
        if sieve[num]:
            primes_list.append(num)
            for multiple in range(num, n + 1, num):
                sieve[multiple] = False
    return primes_list


def isWinner(x, nums):
    """
    Determines who wins the Prime Game after x rounds
    Args:
        x (int): number of rounds in the game
        nums (list): the upper limits of numbers used in each round
    Return:
        The name of the player who won the most rounds: 'Maria' or 'Ben'
        If no winner can be determined, returns None
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    maria_wins = ben_wins = 0
    for round in range(x):
        primes_in_round = get_prime_numbers(nums[round])
        if len(primes_in_round) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None
