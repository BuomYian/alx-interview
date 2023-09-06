#!/usr/bin/python3


# Helper function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Main function to determine the winner
def isWinner(x, nums):
    """
    Prime number game

    Args:
        x: The number of rounds
        nums: An array of n

    Returns:
        Name of the player that won the most rounds
    """
    if not nums or x <= 0:
        return None

    # Initialize counters for Maria and Ben's wins
    maria_wins = 0
    ben_wins = 0

    # Iterate through each round
    for n in nums:
        # Count the number of prime numbers in the current round
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))

        # Determine the winner of the round based on prime count parity
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Compare the total wins and determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
