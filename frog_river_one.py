"""
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
"""

# Generate a set for x
# For loop through length of array A
# Use Try and within use remove iterable of A into x
# except in case error is thrown
# run if statement at end of each loop for if length (x) = 0
# 


# Or use numpy prod() to multiply all values in array and check against factorial of x
# In for loop, set X[inc-1] = inc
# then use if stalihtement checking if values multiplied = factorial
"""
Derek's Solution 1:
Score 72%
def solution(X, A):
    g = [0] * X
    for i in range(len(A)):
        holder = A[i] - 1 
        g[holder] = 1
        if 0 not in g:
            return i
    return -1




    pass
print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
"""
"""
Derek's Solution 2:
Score 54%
def solution(X, A):
    g = [0] * X
    i = 0
    while X != 0 and i < len(A):
        holder = A[i] - 1 
        i += 1
        g[holder] = 1
    if sum(g) == X:
        return i - 1
    else:
        return -1


    pass
print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))

"""/

def solution(X, A):
    g = [0] * X
    i = 0
    while X != 0 and i < len(A):
        holder = A[i] - 1 
        i += 1
        if g[holder] < 1:
            g[holder] = 1
            X -= 1
    if X == 0:
        return i - 1
    else:
        return -1
print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))

