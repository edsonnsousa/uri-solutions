#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 27 2015
# 1073 - Quadrado de Pares
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1073
#
# ad-hoc
#

n = int(raw_input())

for i in range(1, n + 1):
    if i % 2 == 0:
        print '%d^2 = %d' % (i, i**2)
