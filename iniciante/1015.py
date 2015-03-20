#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1015 - Distancia Entre Dois Pontos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1015
#
# ad-hoc
#

import math

x1, y1 = map(float, raw_input().split())
x2, y2 = map(float, raw_input().split())

print '%.4f' % (math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
