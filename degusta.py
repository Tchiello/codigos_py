# gerar dados
# criar função gerar dados
import random


def gerar_dados(qtd, minimo, maximo):
    '''
    Função para gerar uma lista com 'qtd' elementos aleatórios entre 'minimo' e 'maximo'
    '''
    dados = []
    # Criar a lista fora do 'for'
    # O '_' é utilizado para indicar que a variável de controle do loop não será utilizada dentro do bloco de código.
    # É uma convenção comum em Python para indicar que a variável é descartável.
    # É apenas utilizada para executar o comando várias vezes
    for _ in range(qtd):
        dados.append(random.randint(minimo, maximo))
    return dados
# Processar dados -> fornecer nome com significado


def calcular_total(valores):
    return sum(valores)
    '''
    Função para calcular a soma total dos valores em uma lista
    '''
    # se não fosse usar uma função já existente:
    # def calcular_total(valores):
    #     total = 0
    #     for valor in valores:
    #         total += valor
    #         # (total = total + valor)
    #     return total


def calcular_media(valores):
    if not valores:
        return 0  # Evita divisão por zero
    total = calcular_total(valores)
    return total / len(valores)

    '''
    Função para calcular a média dos valores em uma lista
    Retorna zero se a lista estiver vazia
    '''
    # se não fosse usar uma função já existente:
    # def calcular_media(valores):
    #     total = calcular_total(valores)
    #     media = total / len(valores)
    #     return media


def calcular_amplitude(valores):
        maximo = max(valores)
        minimo = min(valores)
        return maximo - minimo

    '''
    Função para calcular a amplitude dos valores em uma lista
    Retorna zero se a lista estiver vazia
    '''
def calcular_projecao(valores, fator):
    pass

def exibir_resultados(dados):
     '''Mostra os dados e cálculos realizados'''
    print (f"Dados gerados: {dados}")
    print (f"Soma: {calcular_total(dados)}")
    media = calcular_media(dados)
    print (f"Média: {media:.2f}")
    print (f"Amplitude: {calcular_amplitude(dados)}")
def main():
     qtd = 10
     minimo = 0
     maximo = 100
     dados = gerar_dados(qtd, minimo, maximo)
     exibir_resultados(dados)
main()
