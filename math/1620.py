#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 21 2015
# 1620 - Triangulacao de Delaunay
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1620
#
# math
#

while True:
    l = float(raw_input())

    if l == 0: break

    i = l + (l - 3)
    x = (i - l) / l
    print '%.6f' % x
