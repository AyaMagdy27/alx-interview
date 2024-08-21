#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters """
    if n <= 1:
        return 0

    op = 0
    body_len = 1  # Starting with one 'H'
    
    while body_len < n:
        # If n is divisible by current length of body, do "Copy All" and "Paste"
        if n % body_len == 0:
            op += 2  # 1 for "Copy All" and 1 for "Paste"
            body_len *= 2
        else:
            # If not divisible, just do "Paste"
            op += 1
            body_len += body_len
    
    if body_len != n:
        return 0
    return op
