#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 6 2015
# 1060 - Numeros Positivos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1059
#
# ad-hoc
#

numeros = []
for i in range(6):
    num = float(raw_input())
    numeros.append(num)

count = 0
for n in numeros:
    if n > 0:
        count += 1

print '%d valores positivos' % count
