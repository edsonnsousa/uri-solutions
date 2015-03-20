#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 18 2015
# 1159 - Soma de Pares Consecutivos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1159
# ad-hoc
#

while True:
    x = int(raw_input())

    if x == 0: break

    if x % 2 == 0:
        print sum(range(x, x + 10, 2))
    else:
        print sum(range(x + 1, x + 10 + 1, 2))
