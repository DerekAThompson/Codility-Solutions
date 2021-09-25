def solution(N):
    # write your code in Python 3.6
    currentGap = 0
    MaxGap = 0
    flip = 0
    binN = bin(N)[2:]
    for bit in range(len(binN)):
        if flip == 1 and binN[bit] == '0':
            currentGap += 1
        elif binN[bit] == '1':
            flip = 1
            if currentGap > MaxGap:
                MaxGap = currentGap
            currentGap = 0
    return MaxGap


print(solution(1041))
"""
Task Score: 100%
Correctness: 100%

"""