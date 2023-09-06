#!/usr/bin/python3


# Helper function to check if a number is prime
def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
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
    Determine the winner of the prime number game.

    Args:
        x (int): The number of rounds.
        nums (list of int): An array of integers representing 'n' 
                            for each round.

    Returns:
        str or None: The name of the player that won the most 
                        rounds (Maria, Ben), or None if the winner cannot be determined.
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
