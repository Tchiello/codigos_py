# Criar variáveis que se incrementem a partir da soma dos dois anteriores
# 3 números
# 2 anteriores, 1 "atual"

anterior = 1
atual = 2
proximo = atual + anterior 
while proximo <= 2000: # Se ao invés de colocar o próximo colocarmos o atual a sequência encerra-se antes de alcançar 2000
    anterior = atual
    atual = proximo
    print(proximo) #colocado como anterior ao cálculo do próximo vai fazer com que a sequência encerre-se antes de alcançar 2000
    proximo = atual + anterior
    
# outra maneira de resolver: fibo1, fibo2 = 0, 1
# while fibo1 <= 2000:
#     print(fibo1)
#     fibo1, fibo2 = fibo2, fibo1 + fibo2