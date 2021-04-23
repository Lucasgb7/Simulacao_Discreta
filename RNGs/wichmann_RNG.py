import numpy as np
import time

def wichmann(x, y, z):
    x = 171 * (x % 177) -  2 * (x / 177)
    y = 172 * (y % 177) - 35 * (y / 176)
    z = 170 * (z % 178) - 63 * (z / 178)

    if x < 0:
        x = x + 30269
    elif y < 0:
        y = y + 30307
    elif z < 0:
        z + z + 30323

    result = x/30269 + y/30307 + z/30323
    result = result - int(result)

    return result


if __name__ == "__main__":
    np.seterr(all='ignore')
    x = 1234
    y = x + 1
    z = y + 1
    iteracoes = 1000

    start = time.time()
    for i in range(iteracoes):
        w = wichmann(x, y, z)
        y += 1
        z += 2
        print("w(", i, ") = ", y)
         
    end = time.time()
    print("Tempo de simulacao: ", end - start)