# Given by problem:
"""An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

My_original_Solution
def solution(A, K):
    # Value to hold (len(A)
    N = int(len(A))

    # List to hold newly rotated values
    place_holder = [0] * N

    # Loop to cycle through each item in list A
    for i in range(N):

        # if Statement to determine if rotating by K would exceed len(n) or if K is negative
        if i + K >= N or K < 0:
            # J is a value for the rotated location to be set within new List place_holder
            J = (i + K) % N
            # A of position i is rotated to be in new position J within new List place_holder
            place_holder[J] = A[i]
            # Rotataion
        else:
            J = i + K
            place_holder[J] = A[i]
    return(place_holder)

    pass
"""


# Requirements:
# Create a new placeholder array for new values.
# place_holder  = []
# Need if statement to determine if rotation of K would exceed A.
# Need for loop to look at each position in A
# for i in range(len(A)):
# Need if statement to determine if rotation of K from spot i would exceed len (A).
# If not, rotate variables to new position
# If it would, starting from position 0, rotate by N mod i+k

# K = len(N) % K
"""
def solution(A, K):



    # Value to hold (len(A)
    length_A= int(len(A))

    # List rotated_list to hold newly rotated values sized to same size of List A
    rotated_list = [0] * length_A

    # Loop to cycle through each item in list A
    for i in range(length_A):

        # J is a value for the rotated location to be set within new List rotated_list
        new_index = (i + K) % length_A

        # A of position i is rotated to be in new position J within new List rotated_list
        rotated_list[new_index] = A[i]


    return(rotated_list)
result = solution([1, 2, 3, 4], 5)
print(result)
"""


"""
New solution as of 02/08/2022 going through problems again.
Reduced O(n) to O(1)

"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(A, K):
    if len(A) == 0:
        return []
    if abs(K) > len(A):
        K = K % len(A)
    elif K == len(A):
        return A
    A = A[-K:] + A[:-K]

    return A
