#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 18 2015
# 1158 - Soma de Impares Consecutivos III
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1158
# ad-hoc
#

nTests = int(raw_input())
for nt in range(nTests):
    x, y = map(int, raw_input().split())

    if x % 2 == 1:
        print sum(range(x, x + 2*y, 2))
    else:
        print sum(range(x + 1, x + 2*y + 1, 2))

