import numpy as np
from method import mean, mean2, C_process
import time


if __name__ == "__main__":
    data = np.random.normal(0, 1, size = (10000, )).tolist()
    print("*"*10, "Use numpy", "*"*10)
    S = time.time()
    print(np.mean(data), end = ";/")
    E = time.time()
    print(E - S, "(s)")

    S = time.time()
    print("*"*10, "Use cythonized python to C", "*"*10)
    print(mean(data), end = ";/")
    E = time.time()
    print(E - S, "(s)")

    S = time.time()
    print("*"*10, "Use numpy and rewrite to C", "*"*10)
    print(mean2(data), end = ";/")
    E = time.time()
    print(E - S, "(s)")


    S = time.time()
    print("*"*10, "Use C", "*"*10)
    print(C_process(data), end = ";/")
    E = time.time()
    print(E - S, "(s)")
