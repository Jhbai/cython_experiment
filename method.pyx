import numpy as np
cimport numpy as np

cdef extern from "algorithm.h" :
    double C_mean(double* arr, int n);

def C_process(List):
    cdef int n = len(List)
    cdef np.ndarray[double, ndim = 1] arr = np.array(List, dtype = np.float64)
    cdef double* c_arr = <double*> arr.data
    for i in range(n):
        c_arr[i] = List[i]
    res = C_mean(c_arr, n)
    return res

def mean(List):
    S = 0
    for ele in List:
        S += ele
    S /= len(List)
    return S

def mean2(List):
    return np.mean(List)

