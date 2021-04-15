import time
import numpy as np

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

if __name__ == "__main__":
    np.seterr(all='ignore') # ignora erros de overflow, divisao/zero, underflow, etc...
    key = np.uint64(0xfb9e125878fa6cb3)
    n = np.uint64(2)
    sum = np.uint64(0)

    start = time.time()
    for i in range(n):
        print("-------------------- i =", i, "--------------------")
        sum += squares(np.uint64(i), key)

    end = time.time()
    print("================= RESULTADOS =================")
    print("Media: ", hex(sum//n))
    print("Tempo de simulacao: ", end - start)