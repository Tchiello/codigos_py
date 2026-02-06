# Desenvolver um programa que guarde os dados de 5 pessoas que estão se 
# candidatando a uma vaga de emprego, 
# candidatos menores de 18 anos não podem participar. 
#➔ Os dados coletados são: nome, data de nascimento, telefone, e-mail, formação acadêmica.

# ...existing code...
import datetime
import re
import json
import os

DATE_FORMAT = "%d/%m/%Y"  # formato esperado para entrada de data
def calcula_idade(data_nasc_str):
    try:
        nasc = datetime.datetime.strptime(data_nasc_str, DATE_FORMAT).date()
    except ValueError:
        return None  # formato inválido
    hoje = datetime.date.today()
    idade = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))
    return idade

def email_valido(email):
    # checagem simples suficiente para a maioria dos casos de entrada manual
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) is not None

def telefone_valido(telefone):
    # remove caracteres comuns e verifica se restam apenas dígitos em quantidade razoável
    digitos = re.sub(r"[^\d]", "", telefone)
    return 8 <= len(digitos) <= 15

def coleta_candidato(numero):
    while True:
        print(f"\n--- Cadastro do candidato #{numero} ---")
        nome = input("Nome completo: ").strip()
        if not nome:
            print("Nome não pode ficar vazio.")
            continue

        data_nasc = input("Data de nascimento (DD/MM/AAAA): ").strip()
        idade = calcula_idade(data_nasc)
        if idade is None:
            print("Formato de data inválido. Use DD/MM/AAAA.")
            continue
        if idade < 18:
            print(f"Candidato tem {idade} anos. Menores de 18 não podem participar. Cadastro descartado.")
            return None  # sinaliza que este candidato não foi aceito

        telefone = input("Telefone (ex.: (11) 99999-9999 ou 11999999999): ").strip()
        if not telefone_valido(telefone):
            print("Telefone inválido. Insira apenas números ou formato comum.")
            continue

        email = input("E-mail: ").strip()
        if not email_valido(email):
            print("E-mail inválido. Tente novamente.")
            continue

        formacao = input("Formação acadêmica: ").strip()
        if not formacao:
            print("Formação não pode ficar vazia.")
            continue

        candidato = {
            "nome": nome,
            "data_nascimento": data_nasc,
            "idade": idade,
            "telefone": telefone,
            "email": email,
            "formacao": formacao
        }
        return candidato

def main():
    candidatos = []
    alvo = 5
    tentativa = 1
    print("Cadastro de 5 candidatos (menores de 18 anos não podem participar).")
    while len(candidatos) < alvo:
        resultado = coleta_candidato(len(candidatos) + 1)
        if resultado is None:
            # candidato menor de idade — não conta; permite tentar novamente
            tentativa += 1
            continue
        candidatos.append(resultado)

    # mostra resumo
    print("\n--- Candidatos cadastrados ---")
    for i, c in enumerate(candidatos, start=1):
        print(f"{i}. {c['nome']} — {c['idade']} anos — {c['email']} — {c['telefone']} — {c['formacao']}")

    # salva em arquivo JSON no mesmo diretório
    caminho = os.path.join(os.path.dirname(__file__), "candidatos.json")
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(candidatos, f, ensure_ascii=False, indent=2)
    print(f"\nDados salvos em: {caminho}")

if __name__ ==