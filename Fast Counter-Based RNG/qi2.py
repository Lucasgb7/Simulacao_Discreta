import numpy as np

def qi2Test(gl, n, results):

    Fe = n / gl     # frequencia esperada
    intervals = np.arange(0, 1, Fe/n, dtype=float)   # define intervalos
    frequency = np.zeros(gl) 
    
    
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
    for i in range(gl):
        x2 += ((frequency[i] - Fe)**2)/Fe
        
    return x2