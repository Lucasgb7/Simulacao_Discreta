import numpy as np
from random import randrange


def draw(value, probability):
    return int(np.random.choice(value, 1, replace=False, p=probability))

if __name__ == "__main__":
    # Criando os vetores de valores e suas probabilidades
    bearingLifeExpect = np.arange(1000, 2000, 100)
    probabilityLifeExpect = np.array([0.1, 0.13, 0.25, 0.13, 0.09, 0.12, 0.02, 0.06, 0.05, 0.05])
    waitingTimeArray = np.arange(5, 20, 5)
    probabilityWaitingTime = [0.6, 0.3, 0.1]

    simluationTime = 10000      # 10.000h
    bearing = [0,0,0]           # Rolamentos
    changingTime = [20, 30, 40] # Tempo de troca =  1: 20, 2: 30, 3: 40

    # Sorteia tempo de vida para os rolamentos
    for i in range(len(bearing)):
        bearing[i] = draw(bearingLifeExpect, probabilityLifeExpect)

    t = 0               # Contador para o tempo de simulacao
    brokenBearings = 0  # Numero de rolamentos quebrados
    totalCost = 0       # Custo total da simulacao

    commingEvent = []
    exitEvent = []


    print("--------------------------------\nDefina o numero de rolamentos a serem trocados: ")
    print("[1]: Troca UM rolamento quando algum rolamento quebra.")
    print("[2]: Troca TRÊS rolamentos quando algum rolamento quebra.")
    option = int(input("> "))
    print("--------------------------------")

    if option == 1:
        print("Simulação 1: Troca de UM rolamento por vez\n")
        print("--------------------------------")
        while t <= simluationTime:

            for i in range(len(bearing)):
                if bearing[i] == t:                                             # Caso rolamento atinga a vida util
                    newTime = draw(bearingLifeExpect, probabilityLifeExpect)    # Define um novo tempo de vida para o rolamento
                    print("---------------")
                    print("Rolamento[", i, "]")
                    print("Quebrou em: ", t, "h\tExpectativa de vida: ", bearing[i], "h")
                    print("Nova expectativa de vida: ", newTime, "h")
                    bearing[i] += newTime                                       # Soma lifetime anterior com novo para posteriormente
                    brokenBearings += 1                                         # Incrementa o numero de rolamentos quebrados

            if brokenBearings > 0:                                                      # Caso haja um rolamento quebrado
                waitingTime = draw(waitingTimeArray, probabilityWaitingTime)            # Atribui nova vida util
                spentTime = changingTime[brokenBearings-1]                              # Pega o tempo gasto para consertar os bearing
                cost = 5 * (waitingTime + spentTime) + spentTime + brokenBearings * 20   # Calcula o valor do concerto
                totalCost += cost


                print("Tempo concerto: ", spentTime,"\tTempo espera: ", waitingTime)
                print("Custo concerto: ", cost, "R$\tCusto total: ", totalCost, "R$")

                brokenBearings = 0

            t += 100

    elif option == 2:
        print("Simulação 2: Troca de TRÊS rolamento por vez\n")
        print("--------------------------------")
        while t <= simluationTime:

            for i in range(len(bearing)):
                if bearing[i] == t:
                    newTime1 = draw(bearingLifeExpect, probabilityLifeExpect)
                    newTime2 = draw(bearingLifeExpect, probabilityLifeExpect)
                    newTime3 = draw(bearingLifeExpect, probabilityLifeExpect)
                    print("---------------")
                    print("Rolamento[1]:")
                    print("Quebrou em: ", t, "h\tExpectativa de vida: ", bearing[0], "h")
                    print("Nova expectativa de vida: ", newTime1, "h")
                    print("---------------")
                    print("Rolamento[2]:")
                    print("Quebrou em: ", t, "h\tExpectativa de vida: ", bearing[1], "h")
                    print("Nova expectativa de vida: ", newTime2, "h")
                    print("---------------")
                    print("Rolamento[3]:")
                    print("Quebrou em: ", t, "h\tExpectativa de vida: ", bearing[2], "h")
                    print("Nova expectativa de vida: ", newTime3, "h")
                    print("---------------")
                    bearing[0] += newTime1
                    bearing[1] += newTime2
                    bearing[2] += newTime3

                    waitingTime = draw(waitingTimeArray, probabilityWaitingTime)
                    spentTime = changingTime[2]
                    cost = 5 * (waitingTime +spentTime) + spentTime + 3 * 20
                    totalCost += cost

                    print("Tempo concerto: ", spentTime,"\tTempo espera: ", waitingTime)
                    print("Custo concerto: ", cost, "R$\tCusto total: ", totalCost, "R$")
                    
            t += 100