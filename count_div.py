"""
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
"""
import math
def solution(A, B, K):
    Amod = A % K
    Bmod = B % K
    BK = math.floor(B / K )
    AK = math.floor(A / K)
    Value = BK - AK
    if Value == 0 and Amod == 0 and Bmod == 0:
        return 1
    elif Value != 0 and Amod != 0 and Bmod !=0:
        return BK - AK 
    elif Value != 0 and Amod == 0 and Bmod == 0:
        return BK - AK + 1
    elif Value != 0 and Amod == 0:
        return BK - AK + 1
    elif Value != 0 and Amod != 0:
        return BK - AK
    else:
        return 0




    for i in range(A, B + 1):
        if i % K == 0:
            count += 1
    return count

print(solution(6, 11, 2))