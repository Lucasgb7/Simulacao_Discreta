import time 

# John von Neumann's Generator
def JVN(x):
    x = x ** 2
    x = x / 100
    x = x % 10000
    return int(x)

# Linear Congruential Generator
def LCG(x):
    return (a * x + c) % m

if __name__ == "__main__":
    # seed = 322
    simulationTime = 20
    # x = int(input("Valor inicial [X0]: "))
    x = 3
    # m = int(input("Módulo [M], M>0: "))
    m = 10
    # a = int(input("Multiplicador [A], M>A>0: "))
    a = 2
    # c = int(input("Incrementador [C], M>=C>=0: "))
    c = 0
    start = time.time()
    print(start)
    for i in range(simulationTime):
        # seed = JVN(seed)
        # print("Semente: ", seed)
        x = LCG(x)
        print('X[', i, ']: ', x)
        end = time.time()
    
    print("Tempo para o cálculo:", end - start)     