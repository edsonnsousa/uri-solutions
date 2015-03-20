#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 20 2015
# 1541 - Construindo Casas
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1541
# ad-hoc
#

import math

while True:
    measures = map(int, raw_input().split())

    if len(measures) == 1: break

    m2 = (measures[0] * measures[1] * 100.0) / measures[2]
    print '%d' % (math.sqrt(m2))
