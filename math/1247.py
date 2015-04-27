#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 24 2015
# 1247 - Guarda Costeira
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1247
#
# math
#

import math

while True:
    try:
        d, vf, vg = map(int, raw_input().split())
    except EOFError:
        break

    t_f = 12 / float(vf)
    t_g = (math.sqrt(d**2 + 144)) / float(vg)

    if t_g <= t_f:
        print 'S'
    else:
        print 'N'
