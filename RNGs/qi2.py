import numpy as np

def qi2Test(k, n, results):

    Fe = n / k     # frequencia esperada
    intervals = np.arange(0, 1, Fe/n, dtype=float)   # define intervalos
    frequency = np.zeros(k) 
    
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
        
    return x2