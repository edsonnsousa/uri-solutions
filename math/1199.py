#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 24 2015
# 1199 - Conversao Simples de Base
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1199
#
# math
#

while True:
    n = raw_input()

    if n[0] == '-': break

    if len(n) >= 2 and n[1] == 'x':
        print int(n, 0)
    else:
        h = hex(int(n))
        h = h[0:2] + h[2:].upper()
        print h
