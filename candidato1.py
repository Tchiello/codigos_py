# módulo/biblioteca para trabalhar com datas
# importar os módulos necessários pegando apenas a parte que se faz necessária:
# "from 'modulo' import 'biblioteca'"

from datetime import datetime
candidatos = []
while len(candidatos) < 2:
    # strip remove espaços em branco desnecessários
    nome = input("Nome completo: ").strip()
    # isso é para forçar a ter algo escrito no campo de nome
    while len(nome) < 3:
        print("Nome inválido. Deve ter ao menos 3 caracteres.")
        nome = input("Nome completo: ").strip()
    data_nasc = input("Data de nascimento (DD/MM/AAAA): ")
    try:
        # converter a data em um objeto tipo data
        data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y")
        # restrição de idade
        hoje = datetime.now()
        hoje.year - data_nasc.year - \
            ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
        # cálculo para automatizar o cálculo se o candidato já fez aniversário neste ano retornando 0 ou 1
        idade = hoje.year - data_nasc.year - \
            ((hoje.month, hoje.day) < (data_nasc.month, data_nasc))
        if idade < 18:
            print(f"Candidato tem {idade} anos. Cadastro não permitido.")
            continue
    except ValueError:
        print("Data inválida. Use o formato DD/MM/AAAA.")
        continue
    telefone = input(
        "Telefone (ex.: (11) 99999-9999 ou 11999999999): ").strip()
    email = input("E-mail: ").strip()
    formacao = input("Formação Acadêmica: ").strip()
    pessoa = {'nome': nome, 'data_nascimento': data_nasc.strftime(
        "%d/%m/%Y"), 'telefone': telefone, 'email': email, 'formacao': formacao}
    # guardar a pessoa na lista de candidatos
    candidatos.append(pessoa)
# Fazer print dos candidatos
print(49*"-")
for candidato in candidatos:
    for chave, valor in candidato.items():
        print(f'{chave}: {valor}')
    print(49*"-")
