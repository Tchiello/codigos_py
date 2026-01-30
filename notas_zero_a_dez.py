# Construa um programa que só aceite notas entre 0 e 10


nota = input(float("Digite uma nota entre zero e dez: "))

while nota >= 10 or nota <= 0:
    print ("Valor inválido, Digite novamente uma nota entre zero e dez: ")
    nota = input(float("Digite uma nota entre zero e dez: "))
    
    
    