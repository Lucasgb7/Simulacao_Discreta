## Introdução

- Proposto por Bernard Widynski em 2020. ([Squares: A Fast Counter-Based RNG](https://arxiv.org/abs/2004.06278))
- Derivado do método: “Middle Square Weyl Sequence RNG”. ([Middle Square Weyl Sequence RNG](https://arxiv.org/abs/1704.00358))
- Utiliza transformação middle-square de von Neummann.
- Usa apenas 4 estados de “squaring”, diferentemente de Philox que utiliza 10.


## Algoritmo

```
def squares(ctr, key):
    y = x = ctr * key; z = y + key
    two5 = np.uint64(32) # 2^5
    x = x * x + y; x = (x >> two5) | (x << two5)
    x = x * x + z; x = (x >> two5) | (x << two5)
    x = x * x + y; x = (x >> two5) | (x << two5)

    return (x*x + z) >> two5    
```
- Substitui a sequência Weyl (w += s) por um contador multiplicado por uma chave.
- Se mutiplicarmos o contador e a chave e somarmos o quadrado, teremos o mesmo efeito da sêquência Weyl.
- A saída será uniforme e 2^64 valores aleatórios podem ser gerados por chave.
- São realizados quatro rodadas de “enquadramento” para ser suficiente ao passar nos testes estatísticos.

## Vantagens e Desvantagens
### Vantagens

- Significativamente mais rápido que o modelo Philox.
- Produz dados concretos e uniformes.
- Pode ser calculado com até 2 bilhões de chaves, sendo cada chave gerando até 2^64 valores aleatórios.

### Desvantagens

- Estudo recente (2020) e ainda não utilizado amplamente.

## Testes

- 300 testes BigCrush usando chaves aleatórias.
- Testes de correlação entre fluxos, testes de contador, testes de bits invertidos e testes de uniformidade. (Não especificado qual teste)
- 300 testes PractRand usando chaves aleatórias.
- Para obter 1 bilhão de números aleatórios, Philox demorou 2,21s enquanto esse durou 1,34s. (Intel Core i7-9700 3.0 GHz)

## Resultados obtidos

#### Grafico que gera cores através do range dos valores gerados
![Grafico1](https://raw.githubusercontent.com/Lucasgb7/Simulacao_Discreta/main/Fast%20Counter-Based%20RNG/resultados/grafico1.png)

N = 1048576; Tempo de Simulação = 703,27 segundos; (Intel Core i5-4690)

#### Grafico que gera cores através do range dos valores gerados
![Grafico2](https://raw.githubusercontent.com/Lucasgb7/Simulacao_Discreta/main/Fast%20Counter-Based%20RNG/resultados/grafico2.png)

N = 16; Tempo de Simulação = 0,029 segundos; (Intel Core i5-4690)

#### Grafico Scatter
![Grafico3](https://raw.githubusercontent.com/Lucasgb7/Simulacao_Discreta/main/Fast%20Counter-Based%20RNG/resultados/grafico3.png)

N = 125; Tempo de Simulação = 0,091 segundos; (Intel Core i5-4690)

## Autores

### Desenvolvedores do código

- [Lucas Jose da Cunha](https://github.com/Lucasgb7)
- [Luiz Alberto Zimmermann Zabel Martins Pinto](https://github.com/Luiz-Zimmermann)
          
### Autor do método

[Bernard Widynski](https://arxiv.org/search/cs?searchtype=author&query=Widynski%2C+B)
