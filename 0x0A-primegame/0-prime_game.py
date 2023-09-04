#!/usr/bin/python3


# Helper function to generate prime numbers up
# to n using the Sieve of Eratosthenes algorithm
def sieve_of_eratosthenes(n):
    # Create a list to store whether each number is prime
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            # Mark multiples of p as non-prime
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Collect the prime numbers
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes


# Main function to determine the winner
def isWinner(x, nums):
    # Find the maximum number in the input list
    max_num = max(nums)

    # Precompute a list of prime numbers up to the maximum number
    primes = sieve_of_eratosthenes(max_num)

    # Create a list to store the count of prime numbers in the input list
    prime_count = [0] * (max_num + 1)

    # Mark the prime numbers in the prime_count list
    for num in nums:
        prime_count[num] = 1

    # Count how many multiples of each prime number exist in the input list
    for prime in primes:
        for multiple in range(prime, max_num + 1, prime):
            prime_count[multiple] += 1

    # Initialize counters for Maria and Ben's wins
    maria_wins = 0
    ben_wins = 0

    # Calculate the winners for each round based on prime count parity
    for num in nums:
        if prime_count[num] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Compare the total wins and determine the overall winner or return None
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
