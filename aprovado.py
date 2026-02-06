def media(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


def verificar_nota():
    nota = float(input("Digite a nota (0 a 10): "))
    while nota < 0 or nota > 10:
            nota = float(input("Nota inválida. Por favor, digite uma nota entre 0 e 10: "))
    return nota
    
    
resultado = media(verificar_nota(), verificar_nota())
print(f"O aluno está {resultado}.")

    # if media >= 7:
    #     saida = "Aprovado"
    # else:
    #     saida = "Reprovado"
    # return saida

    # em vez de input float, poderia utilizar uma função para verificar se a nota está dentro do intervalo esperado 0 a 10
    # def verificar_nota():
    #     while True:
    #         try:
    #             nota = float(input("Digite a nota (0 a 10): "))
    #             if 0 <= nota <= 10:
    #                 return nota
    #             else:
    #                 print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
    #         except ValueError:
    #             print("Entrada inválida. Por favor, digite um número.")

    
  