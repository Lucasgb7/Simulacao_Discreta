import time
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.colors import NoNorm

def squares(ctr, key):
    y = x = ctr * key
    z = y + key
    two5 = np.uint64(32)
    x = x * x + y; x = (x >> two5) | (x << two5)
    x = x * x + z; x = (x >> two5) | (x << two5)
    x = x * x + y; x = (x >> two5) | (x << two5)

    return (x*x + z) >> two5    


def draw(i):
    nx = int(math.sqrt(i))
    #print("tamanho da imagem", nx)
    imagem = np.zeros((nx,nx), dtype=np.uint8)
    #print("tam: ", i)
    p = 0
    ny = nx
    for i in range(nx):
        for j in range(ny):
            
            imagem[i,j] = pixelvet[p]
            #print(i, j, pixelvet[p])
            p += 1
        
    
    return imagem

if __name__ == "__main__":
    np.seterr(all='ignore')             # ignora erros de overflow, divisao/zero, underflow, etc...
    key = np.uint64(0xf6235eca95b2c1e7)
    #sum = np.uint64(0)
    #pixelvet = []
    #vetVal = []

    n = np.uint64(input("Número de iterações (n): "))
    k = int(input("Frequência esperada (k): "))
    waitedValues = np.arange(0, 1, 0.1, dtype=float)
    frequency = np.zeros(10)
    #start = time.time()
    for i in range(n):
        # print("-------------------- i =", i, "--------------------")
        result = squares(np.uint64(i), key)
        result = result / (2**32)   # normaliza resultado de 32 bits
        print("[", i, "]:", result)

        if result > 0.0 and result < 0.1:
            frequency[0] +=1
        elif result > 0.1 and result < 0.2:
            frequency[1] +=1
        elif result > 0.2 and result < 0.3:
            frequency[2] +=1
        elif result > 0.3 and result < 0.4:
            frequency[3] +=1
        elif result > 0.4 and result < 0.5:
            frequency[4] +=1
        elif result > 0.5 and result < 0.6:
            frequency[5] +=1
        elif result > 0.6 and result < 0.7:
            frequency[6] +=1
        elif result > 0.7 and result < 0.8:
            frequency[7] +=1
        elif result > 0.8 and result < 0.9:
            frequency[8] +=1
        elif result > 0.9 and result < 1.0:
            frequency[9] +=1

        #pixelvet.append(result)
        #vetVal.append(result)
    
    x2 = 0
    for i in range(10):
        x2 += ((frequency[i] - k)**2)/k
       
    #end = time.time()
    print("================= RESULTADOS =================")
    #print("Media: ", hex(sum//n))
    #print("Tempo de simulacao: ", end - start)
    print("Frequencia: ", frequency)
    print("X^2: ", x2)
    print("V = (k - 1) = ", k - 1)
    print("Alpha = 0.05")

    '''
    plt.figure("Graficos",figsize=(15,12))
    plt.subplot(211)
    imagem = draw(n)
    plt.imshow(imagem, aspect="auto", cmap='gray', vmin=0, vmax=255,norm=NoNorm())
    plt.axis("off")
    plt.subplot(212)
    plt.plot(vetVal, 'ro')
    plt.grid(1)
    plt.show()
    '''