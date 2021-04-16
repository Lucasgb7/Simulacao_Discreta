import time
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.colors import NoNorm

def squares(ctr, key):
    y = x = ctr * key
    print("y = x = ctr * key:", hex(y))
    z = y + key
    print("z = y + key:", hex(z))
    # Circular Shift
    two5 = np.uint64(32) # 2^5
    x = x * x + y; x = (x >> two5) | (x << two5)
    print("1º Round:", hex(x))
    x = x * x + z; x = (x >> two5) | (x << two5)
    print("2º Round:", hex(x))
    x = x * x + y; x = (x >> two5) | (x << two5)
    print("3º Round:", hex(x))

    print("4º Round:", hex((x*x + z) >> two5))
    return (x*x + z) >> two5    
    
def draw(i):

    nx = int(math.sqrt(i))
    print("tamanho da imagem", nx)
    imagem = np.zeros((nx,nx), dtype=np.uint8)
    print("tam: ", i)
    p = 0
    ny = nx
    for i in range(nx):
        for j in range(ny):
            
            imagem[i,j] = pixelvet[p]
            #print(i, j, pixelvet[p])
            p += 1
        
    
    return imagem

if __name__ == "__main__":
    np.seterr(all='ignore') # ignora erros de overflow, divisao/zero, underflow, etc...
    key = np.uint64(0xfb9e125878fa6cb3)
    n = np.uint64(input("Defina o numero de itera??es: "))
    sum = np.uint64(0)
    pixelvet = []
    vetVal = []

    start = time.time()
    for i in range(n):
        print("-------------------- i =", i, "--------------------")
        result = squares(np.uint64(i), key)
        sum += result
        print(result)
        pixelvet.append(result)
        vetVal.append(result)
        
        
       
    end = time.time()
    print("================= RESULTADOS =================")
    print("Media: ", hex(sum//n))
    print("Tempo de simulacao: ", end - start)
    
    
    
    plt.figure("Gr?ficos",figsize=(15,12))
    plt.subplot(211)
    imagem = draw(n)
    plt.imshow(imagem, aspect="auto", cmap='gray', vmin=0, vmax=255,norm=NoNorm())
    plt.axis("off")
    plt.subplot(212)
    plt.plot(vetVal, 'ro')
    plt.grid(1)
    plt.show()