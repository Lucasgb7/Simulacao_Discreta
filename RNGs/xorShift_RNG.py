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

    n = int(input("Número de iterações (n): "))
    k = int(input("Número de categorias (k): "))  
    results = []
    #start = time.time()
    for i in range(n):
        y = (xorShift(y))
        aux = y / 4294967295        # normaliza resultado
        #print("Valor: ", aux)
        #print("y(", i, ") = ", aux)
        results.append(aux)
         
    #end = time.time()
    x2 = qi2.qi2Test(k, n, results)


    print("================= RESULTADOS =================")
    #print("Tempo de simulacao: ", end - start)
    print("X²: ", x2)
    print("Graus de Liberdade (GL):", k - 1)
    print("Significância: 0.05")