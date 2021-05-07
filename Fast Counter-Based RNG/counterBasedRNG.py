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

def saveFrequency(frequency, interval, result):
    for i in range(len(interval)):
        if (i < len(interval)-1):
            if result > interval[i] and result < interval[i+1]:
                frequency[i] += 1
            else:
                continue
        elif result > interval[i] and result < 1.0:
            frequency[i] += 1

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
    gl = int(input("Graus de liberdade (gl): "))
    Fe = n / gl     # frequencia esperada
    waitedValues = np.arange(0, 1, Fe/100, dtype=float)   # define intervalos
    frequency = np.zeros(gl)                            # frequencia com base no GL
    #start = time.time()
    for i in range(n):
        result = squares(np.uint64(i), key)
        result = result / (2**32)           # normaliza resultado de 32 bits
        #print("[", i, "]:", result)
        saveFrequency(frequency, waitedValues, result)
        #pixelvet.append(result)
        #vetVal.append(result)
    
    x2 = 0
    for i in range(10):
        x2 += ((frequency[i] - Fe)**2)/Fe
       
    #end = time.time()
    print("================= RESULTADOS =================")
    #print("Media: ", hex(sum//n))
    #print("Tempo de simulacao: ", end - start)
    print("Frequencia: ", frequency)
    print("X^2: ", x2)
    print("V =", gl - 1)
    print("Probabilidade = 0.05")

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