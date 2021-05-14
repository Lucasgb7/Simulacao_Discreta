import numpy as np
import time
import qi2

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
    #iteracoes = 1000

    n = np.uint64(input("Numero de iteracoes (n): "))
    k = int(input("Numero de categorias (k): "))
    gl = k - 1; print("Grau de Liberdade (GL): ", gl)
    p = float(input("Probabilidade de sucesso: ")) 
    results = []
    #start = time.time()
    for i in range(n):
        w = wichmann(x, y, z)
        y += 1
        z += 2
        print("w(", i, ") = ", y)
        results.append(w)

    #end = time.time()
    x2, intervals = qi2.qi2Test(k, n, results)
         
    print("================= RESULTADOS =================")
    #print("Tempo de simulacao: ", end - start)
    pIndex = qi2.getProbabilityIndex(p)
    x2Max = qi2.table[gl-1][pIndex]
    print("x2Max: ", x2Max)
    print("x2:" , x2)