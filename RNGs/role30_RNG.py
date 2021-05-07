import matplotlib.pyplot as plt
import time
import qi2

# left XOR entre o cara do centro e da direita
def rule(array):
    return array[0] ^ (array[1] or array[2])
    

# primeira linha do mosaico
def init(largura):
    array = [0] * largura # inicio do mosaico, no começa inicializa com 1
    # se for impar, coloca 1 no meio
    if largura % 2:
        array[largura // 2] = 1
    else: # caso for par coloca so na metade (nao exata)
        array.insert(largura//2, 1)

    return array

def rule30(linhaAntiga):
    largura = len(linhaAntiga)
    linhaAntiga = [0] + linhaAntiga + [0]   # ajustar com zeros na direita e esquerda da linha
    novaLinha = []
    
    for i in range(largura):
        novaLinha.append( rule(linhaAntiga[i:i+3]) ) # coloca uma celula (1 ou 0)

    return novaLinha

# usa largura e quantos bits vai utilizar pra fazer essa largura
def applyRule(largura, bits):
    matriz = [init(largura)]

    colunaCentro = []
    colunaCentro.append(matriz[0][largura // 2])

    while not matriz[-1][0]:
        matriz.append(rule30(matriz[-1]))           # executa a regra na ultima linha
        colunaCentro.append(matriz[-1][largura // 2])  # atualiza o centro da matriz

    return [matriz, colunaCentro[-bits:]]

def listToString(s): 
    # initialize an empty string
    str1 = "" 
    # traverse in the string  
    for ele in s: 
        str1 += str(ele)  
    # return string  
    return str1

if __name__ == "__main__":
    seed = int(str(time.time_ns())[14:17])
    bits = 8

    #start = time.time()
    n = int(input("Número de iterações (n): "))
    k = int(input("Número de categorias (k): "))  
    results = []
    for i in range(n):
        time.sleep(1)
        result = applyRule((seed+bits)*2, bits)
        rng = listToString(result[1])
        rng = int(listToString(rng), 2)
        print(rng)
        results.append(rng)

    #end = time.time()
    '''
    x2 = qi2.qi2Test(k, n, results)

    print("================= RESULTADOS =================")
    #print("Tempo de simulacao: ", end - start)
    print("X²: ", x2)
    print("Graus de Liberdade (GL):", k - 1)
    print("Significância: 0.05")
    '''