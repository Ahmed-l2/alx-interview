#!/usr/bin/python3
"""Module for minOperations"""


def minOperations(n):
    """
    a method that calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    # If n is less than 2, there's nothing to do.
    if n < 2:
        return 0
    
    # Initialize a counter to keep track of the operations.
    counter = 0
    
    # Start with the smallest prime number, which is 2.
    i = 2
    
    # While n is greater than 1, keep dividing it by i.
    while n > 1:
        # Inside the loop, we check if the current number divides n. If it does
        # we increment the counter and divide n by this number. and we continue
        # this until it no longer divides evenly.
        while n % i == 0:
            counter += i
            n /= i
        # Move on to the next prime number.
        i += 1
    
    # Return the total number of operations (sum of prime factors).
    return counter
