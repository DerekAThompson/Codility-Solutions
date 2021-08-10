"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].
"""

"""
Derek's First Solution:
Score: 56%
def solution (A):
    count = 0
    for i in range(len(A)):
        for z in range(i + 1, len(A)):
            if i + A[i] >= z - A[z]:
                count += 1
    if count <= 10000000:
        return count
    else:
        return -1
"""

"""
Derek's Second Solution:
Score: 56%
def solution (A):
    count = 0
    if len(A) == 0:
        return 0
    maxA = max(A)
    for i in range(len(A)):
        z = i + 1
        maxthresh = 0
        while maxthresh <= maxA and z < len(A):
            maxthresh += 1
            if i + A[i] >= z - A[z]:
                print("i: ", i, "   z: ", z)
                count += 1
            z += 1
    if count <= 10000000:
        return count
    else:
        return -1

print(solution([1, 5, 2, 1, 4, 0]))
"""

