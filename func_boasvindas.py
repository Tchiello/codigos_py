# Se ao invés de nome usasse outro apelido dentro da função ainda assim ela funcionaria
# Neste caso o nome dado não importa, contudo a ordem dos parâmetros deve ser respeitada
def boas_vindas(nome):
    return print(f"Seja bem-vindo(a), {nome}!")
nome = input("Digite seu nome: ")
boas_vindas(nome)
# chama-se a função informado sobre qual variável (nome) ela deve trabalhar
