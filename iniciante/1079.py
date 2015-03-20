#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 27 2015
# 1079 - Medias Ponderadas
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1079
#
# ad-hoc
#

nTests = int(raw_input())

for nt in range(nTests):
    a, b, c = map(float, raw_input().split())
    print '%.1f' % (a * 0.2 + b * 0.3 + c *0.5)
