import numpy as np
from random import randrange, uniform

class Material():
    Type = 0
    Time = 0
    Weight = 0 
    TimeStamp = 0

    def __init__(self, Type):
        self.Type = Type

    def materialValues(self):
        if self.Type == 0:                  # Material A
            self.Weight = 200               # 200kg
            self.Time = int(uniform(3,8))   # 5 +- 2 (uniforme)
        elif self.Type == 1:                # Material B
            self.Weight = 100               # 100kg
            self.Time = 6                   # 6 (constante)
        else:                               # Material C
            self.Weight = 50                # 50kg
            if randrange(100) <= 33:        
                self.Time = 2               # P(2) = 0.33
            else:
                self.Time = 3               # P(3) = 0.67


if __name__ == "__main__":
    simulationTime = 60                             # Tempo de simulacao (min)
    totalWeight = 0                                 # Peso do elevador
    i = 0                                           # Contador de minutos
    averageTimeA = []                               # Calcular tempo medio Mat A
    averageTimeB = []                               # Calcular tempo medio Mat B
    movedMaterialC = 0                              # Contagem de Material C 
    materialsLift = []                              # Materiais dentro do elevador
    materialsQueue = []                             # Materiais na fila do elevador

    while i < simulationTime:
        print("\nTempo: ", int(i),"min")
        mat = Material(randrange(3))                # Criando material (0~2)=(A~C)
        mat.materialValues()                        # Definindo tempo e pesos
        mat.TimeStamp = i                           # Definindo tempo que o material chegou
        materialsQueue.append(mat)                  # Adicionando material na fila

        print("MAT[",mat.Type,"]")
        for m in materialsQueue:                    # Verifica a fila de materiais
            if m.Weight + totalWeight <= 400:       # Checa se pode entrar no elevador
                if m.Type == 1:
                    averageTimeB.append(i - m.TimeStamp)    # Monitora o material B
                materialsQueue.remove(m)
                materialsLift.append(m)
                totalWeight += m.Weight
                i = i + m.Time
                if m.Type == 0:                             # Monitorar Material A
                    m.TimeStamp = i
                elif m.Type == 2:                           # Monitorar Material C
                    movedMaterialC =+ 1

        print("-----------------------------------")
        waiting = []
        
        queue = []
        for m in materialsQueue:
            queue.append(m.Type)

        print("Fila:", queue)
        lift = []
        for m in materialsLift:
            lift.append(m.Type)
        print("Elevador:", lift)

        print("Peso elevador:", totalWeight,"kg")
        print("Tempo:", i,"min")
        print("-----------------------------------")

        if totalWeight == 400:  # Chega no peso maximo
            i = i + 4           # Tempo de subir, descarregar e descer
            totalWeight = 0

            for m in materialsLift:     
                if m.Type == 0: 
                    averageTimeA.append((i - 1) - m.TimeStamp)  # Monitora tempo total do Material A

            materialsLift.clear()   # Remove todos os itens do elevador

        i += 1
        
    print("\nTempo medio de transito Material A: ", sum(averageTimeA)/len(averageTimeA), "min")
    print("Tempo medio de espera do Material B: ", sum(averageTimeB)/len(averageTimeB), "min")
    print("Números de caixas de Material C: ", movedMaterialC)