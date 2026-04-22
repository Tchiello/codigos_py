"""Analise numerologica simples de nomes proprios.

Tabela usada (conforme solicitado):
1: a, j, s
2: b, k, t
3: c, l, u
4: d, m, v
5: e, n, x
6: f, o, y
7: g, p, z
8: h, q
9: i, r
"""

from typing import Dict, List, Tuple


TABELA_NUMEROLOGICA: Dict[str, int] = {
    "a": 1,
    "j": 1,
    "s": 1,
    "b": 2,
    "k": 2,
    "t": 2,
    "c": 3,
    "l": 3,
    "u": 3,
    "d": 4,
    "m": 4,
    "v": 4,
    "e": 5,
    "n": 5,
    "x": 5,
    "f": 6,
    "o": 6,
    "y": 6,
    "g": 7,
    "p": 7,
    "z": 7,
    "h": 8,
    "q": 8,
    "i": 9,
    "r": 9,
}


def analisar_nome(nome: str) -> Tuple[int, List[Tuple[str, int]], List[str]]:
    """Retorna soma total, pares (letra, valor) e letras ignoradas."""
    soma = 0
    detalhes: List[Tuple[str, int]] = []
    ignoradas: List[str] = []

    for caractere in nome.lower():
        if not caractere.isalpha():
            continue

        if caractere in TABELA_NUMEROLOGICA:
            valor = TABELA_NUMEROLOGICA[caractere]
            soma += valor
            detalhes.append((caractere, valor))
        else:
            ignoradas.append(caractere)

    return soma, detalhes, ignoradas


def main() -> None:
    print("=== Analise Numerologica de Nome ===")
    nome = input("Digite um nome proprio: ").strip()

    if not nome:
        print("Nenhum nome foi informado.")
        return

    soma, detalhes, ignoradas = analisar_nome(nome)

    if not detalhes:
        print("Nao foi possivel calcular: nenhuma letra da tabela foi encontrada.")
        return

    expressao = " + ".join(str(valor) for _, valor in detalhes)
    letras_usadas = ", ".join(f"{letra}:{valor}" for letra, valor in detalhes)

    print(f"\nNome informado: {nome}")
    print(f"Correspondencias usadas: {letras_usadas}")
    print(f"Calculo: {expressao} = {soma}")

    if ignoradas:
        unicas = ", ".join(sorted(set(ignoradas)))
        print(f"Letras sem valor na tabela informada (ignoradas): {unicas}")


if __name__ == "__main__":
    main()
