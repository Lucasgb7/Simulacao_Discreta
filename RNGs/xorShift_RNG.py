import time
import numpy as np
import qi2

def xorShift(y):
    y ^= np.uint32(y << 13)
    y ^= np.uint32(y >> 17)
    y ^= np.uint32(y << 15)

    return y

if __name__ == "__main__":
    np.seterr(all='ignore')
    seed = 2464581242
    y = np.uint32(seed)
    #a, b, c = 13, 17, 15
    #iteracoes = 1000

    n = np.uint64(input("Numero de iteracoes (n): "))
    k = int(input("Numero de categorias (k): "))
    gl = k - 1; print("Grau de Liberdade (GL): ", gl)
    p = float(input("Probabilidade de sucesso: "))
    results = []
    #start = time.time()
    for i in range(n):
        y = (xorShift(y))
        aux = y / 4294967295        # normaliza resultado
        #print("Valor: ", aux)
        #print("y(", i, ") = ", aux)
        results.append(aux)
         
    #end = time.time()
    x2, intervals = qi2.qi2Test(k, n, results)

    print("================= RESULTADOS =================")
    #print("Tempo de simulacao: ", end - start)
    pIndex = qi2.getProbabilityIndex(p)
    x2Max = qi2.table[gl-1][pIndex]
    print("x2Max: ", x2Max)
    print("x2:" , x2)