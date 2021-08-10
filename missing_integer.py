"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""
# Derek's 1st Solution
# Score: 100%
def solution(A):
    A.sort()
    try:
        b = A.index(1)
    except:
        return 1
    for i in range(len(A)):
        if A[i] > 0:
            if A[i] == A[-1]:
                return A[i] + 1
            elif A[i] != A[i + 1] and A[i] + 1 != A[i + 1]:
                return A[i] + 1
    
    pass
print(solution([1, 3, 6, 4, 1, 2]))