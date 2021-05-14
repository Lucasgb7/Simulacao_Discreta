import numpy as np
import matplotlib.pyplot as plt

def qi2Test(k, n, results):

    Fe = n / k # frequencia esperada
    # Adicionando um valor pequeno para que o ultimo valor entre no array resultante
    intervals = np.arange(0, 1+0.00000001, Fe/n, dtype=float)  # define intervalos
    frequency = np.zeros(k)    # armazena a frequencia de cada valor

    for value in results:
        for i in range(len(intervals)):
            if (i < len(intervals)-1):
                if value > intervals[i] and value < intervals[i+1]:
                    frequency[i] += 1
                else:
                    continue
            elif value > intervals[i] and value < 1.0:
                frequency[i] += 1
        
    print("Frequencia: ", frequency)
    
    x2 = 0
    for i in range(k):
        x2 += ((frequency[i] - Fe)**2)/Fe
        
    return x2, intervals

def histGraph(resultVets, vals):

    plt.hist(resultVets, vals, facecolor='green', rwidth=0.85)
    plt.xticks(vals)
    plt.xlabel('Intervalos')
    plt.ylabel('Frequencia')
    plt.tight_layout()
    plt.grid(True)
    plt.show()