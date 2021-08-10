"""
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
"""

"""
Derek's Solution 1:
Total Score: 55%
def solution(A):
    
    A.sort()
    for i in range(len(A)):
        if A[i] + 1 != A[i+1]:
            print(A[i] + 1)
            return A[i] + 1
    pass

solution([2, 3, 1, 5])
"""
# Derek's Solution 2:
def solution(A):
    N = len(A)
    sumA = sum(A)
    count = 0
    for x in range(1, N + 2):
        count += x
    return count - sumA
solution([2, 3, 1, 5])


# Zac's Solution
def zacsolution(A):
    sumA = sum(A)
    N = len(A)
    sumtotal = sum(range(1, N + 2))
    return sumtotal - sumA
zacsolution([2, 3, 1, 5])