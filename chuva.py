# Usando Python 3.6.5 @Jhonathan Ballesteros 03/12/2018
"""
Given an array of N non-negative colegers with maximum value A, representing height of blocks
sequentially arranged, where the width of each block is 1. Compute how much water can be trapped in
between blocks after raining.
"""
# largura das colunas, coleiros separados por espaços.
str = input("Separe a largura das colunas com espaços: ").split(' ')
# conversão de string para col
col = [int(num) for num in str]

# As duas colunas dos extremos definem a profundidade da piscina,
# sendo a menor delas a "profundidade total".
if col[0] > col[-1]:
    col[0] = col[-1]
else:
    col[-1] = col[0]

# Se alguma coluna for mais grande que a "profundidade total",
# podemos desconsiderar as larguras que superem esse valor.
for i in range(len(col)):
    if col[i] > col[0]:
        col[i] = col[0]

# cálculo da área total do retángulo
square = len(str) * col[0]
# cálculo da área com colunas
sum = sum(col)
# área com água
chuva = square - sum
print(f"A área coberta pela chuva é: {chuva}")
