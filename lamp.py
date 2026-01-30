# variveis: potencia, largura, comprimento,
# numeroLampadas
# a cada m² precisa de 3 watts // 
# a cada 3m² tem um bocal

# criar uma calculadora de qtde de lãmpadas necessárias para iluminar um cômodo 
# Para cada metro quadrado necessita-se de 3W 
# Para cada 3 metros quadrados haverá um bocal para acoplar uma lâmpada
# variáveis: potência, largura, comprimento
# número de lãmpadas em razão da área

import math

# para fazer uso de fórmulas matemáticas pré existente
potencia = int(input('Digite a potencia da lampada em watts: '))
largura = int(input('Digite a largura do comodo em metros: '))
comprimento = int(input('Digite a comprimento do comodo em metros: '))

# Etapa dos cálculos (estimar área total do comodo)
area = largura * comprimento

# Estimar potencia necessaria
potencia_necessaria = area * 3

# Estimar qtde de lampadas para alcançar a potencia_necessaria
numero_lampadas = \
math.ceil (potencia_necessaria/potencia)

# Estimar  número de bocais
numero_bocais = int(area/3)
print(40*'-')
print(f'Área do Cômodo: {area:.2f}m²')
print(f'Número de Lâmpadas: {numero_lampadas}')
print(f'Número de Bocais Estimados: {numero_bocais}')
