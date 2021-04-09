import numpy as np
from random import randrange

# gera o numero de clientes com base na probabilidade
def numberCustomers(value):
    if value > 65:
        return 8
    elif value > 35 and value < 65:
        return 10
    elif value > 10 and value < 35:
        return 12
    else:
        return 14

# gera o numero de duzias por cliente com base na probabilidade
def numberBagelsPerCustomer(value):
    if value > 60:
        return 1
    elif value > 30 and value < 60:
        return 2
    elif value > 10 and value < 30:
        return 3
    else:
        return 4

if __name__ == "__main__":
    days = 15           # nº iteracoes
    bagelCost = 3.8     # custo de fabrica da duzia de baguete
    bagelPrice = 5.4    # preco da duzia de baguete
    bagelsAverage = 0
    for day in range(days):
        print("\nDia ", day)
        # Clientes
        value = randrange(100)
        customers = numberCustomers(value)
        print("Nº Clientes: ", customers)
        # Baguetes por cliente
        value = randrange(100)
        bagelsPerCustomer = numberBagelsPerCustomer(value)
        print("Baguetes/Cliente: ", bagelsPerCustomer)
        # Baguetes para assar
        bagelsToCook = customers * bagelsPerCustomer
        print("Baguetes para assar: ", bagelsToCook)

        bagelsAverage += bagelsToCook

    print("\n\nMedia de Baguetes: ", bagelsAverage/days)