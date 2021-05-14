import qi2

def fbn(option, array, mod, k, j):
    if option == 0:
        result = (array[j-1] + array[k-1]) % mod
    elif option == 1:
        result = (array[j-1] - array[k-1]) % mod
    elif option == 2:
        result = (array[j-1] * array[k-1]) % mod
    else:
        result = (array[j-1] ^ array[k-1]) % mod

    return result

seed = '123456789'
#j = int(input("J:"))
j = 1
#k = int(input("K:"))
k = 8
#mod = int(input("MOD:"))
mod = 1000
n = int(input("Numero de iteracoes:"))
categories = int(input("Numero de categorias: "))
results = []

array = []
for i in range(len(seed)):
    array.append(int(seed))

print("0: '+' \n1: '-' \n2: '*' \n3: '^'")
option = int(input("Defina a operação: "))
for i in range(n):
    result = fbn(option, array, mod, k, j)
    print("Resultado: ", result)
    array.remove(array[0])
    array.append(result)
    results.append(result)

x2 = qi2.qi2Test(categories, n, results)


print("================= RESULTADOS =================")
print("X^2: ", x2)
print("GL =", categories - 1)
print("Probabilidade = 0.05")