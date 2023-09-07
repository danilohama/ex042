"""Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
EQUILATERO: Todos os lados iguais
ISÓSCELES: Dois lados iguais
ESCALENO: Todos os lados diferentes
"""
r1 = float(input('\33[0;49;34mPrimeiro segmento\33[0m: '))
r2 = float(input('\33[0;49;34mSegundo segmento\33[0m: '))
r3 = float(input('\33[0;49;34mTerceiro segmento\33[0m: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \33[0;49;92mPODEM FORMAR\33[0m um TRIÂNGULO', end=' ')
    if r1 == r2 == r3:
        print('\33[0;49;33mEQUILÁTERO!\33[0m')
    elif r1 != r2 != r3 != r1:
        print('\33[0;49;33mESCALENO!\33[0m')
    else:
        print('\33[0;49;33mISÓSCELES\33[0m')
else:
    print('Os segmentos acima \33[0;49;31NÃO PODEM FORMAR\33[0m um Triângulo')
