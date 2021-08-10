"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""

"""
Derek's 1st Attempt:
Score 38%
def solution(A):
    N = len(A)
    counter = []
    for i in range(N):
        counter.append(abs(sum(A[: i]) - sum(A[i:])))
    return min(counter)




print(solution([3, 1, 2, 4, 3]))
"""

"""
Derek's 2nd Attempt:
Score 53%
def solution(A):
    N = len(A)
    counter = []
    for i in range(1, N):
        counter.append(abs(sum(A[: i]) - sum(A[i:])))
        print(counter)
    return min(counter)

print(solution([3, 1, 2, 4, 3]))
"""

"""
Derek's 3rd Attempt:
Score 43%
def solution(A):
    N = len(A)
    i = 1
    count = abs(sum(A[:i]) - sum(A[i:]))
    i += 1
    counter = abs(sum(A[:i]) - sum(A[i:]))
    while counter < count and i < N:
        count = counter
        i += 1
        counter = abs(sum(A[: i]) - sum(A[i:]))
    return count




print(solution([3, 1, 2, 4, 3]))
"""
"""
def solution(A):
    N = len(A)
    i = 1
    count = abs(sum(A[:i]) - sum(A[i:]))
    i += 1
    counter = abs(sum(A[:i]) - sum(A[i:]))
    while counter < count and i < N:
        count = counter
        i += 1
        counter = abs(count - A[i])
    return count




print(solution([3, 1, 2, 4, 3]))"""

def solution(A):
    N =len(A)
    inc = 1
    count = [0] * (N - 1)
    countlower = sum(A[: inc])
    countupper = sum(A[inc: ])
    count[inc - 1] = abs(countlower - countupper)
    for inc in range(1, N - 1):
        countlower += A[inc]
        countupper -= A[inc]
        count[inc] = abs(countlower - countupper)
    return min(count)
print(solution([3, 1, 2, 4, 3]))