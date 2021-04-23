import time
import numpy as np

def xorShift(y, a, b, c):
    y ^= np.uint32(y << a)
    y ^= np.uint32(y >> b)
    y ^= np.uint32(y << c)

    return y

if __name__ == "__main__":
    np.seterr(all='ignore')
    seed = 2463534242
    a, b, c = 13, 17, 15
    iteracoes = 1000
    y = np.uint32(seed)

    start = time.time()
    for i in range(iteracoes):
        y = xorShift(y, a, b, c)
        print("y(", i, ") = ", y)
         
    end = time.time()
    print("Tempo de simulacao: ", end - start)