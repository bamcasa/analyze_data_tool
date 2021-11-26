import numpy as np
import copy

def solver(first,*args):
    equls = []
    equls.append(first)

    for i in args:
        equls.append(i)

    print(equls)

    n = len(first) - 1
    print(f"{n}원 연립 일차 방정식")

    matA = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matA[i][j] = equls[i][j]

    matj = copy.deepcopy(matA)

    detA = np.linalg.det(matA)

    result  = []

    for j in range(n):
        for i in range(n):
            matj[i][j] = equls[i][-1]
        detj = np.linalg.det(matj)
        result.append(detj/detA)

        matj = copy.deepcopy(matA)

    return result

result = solver([3, 2, 1, 4], [4, 3, 2, 7], [2, 1, 3, 5])
print(result)
