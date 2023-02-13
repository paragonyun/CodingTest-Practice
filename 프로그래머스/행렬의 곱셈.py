import numpy as np
def solution(arr1, arr2):
    arr1, arr2 = np.array(arr1), np.array(arr2)
    return np.matmul(arr1, arr2).tolist()

