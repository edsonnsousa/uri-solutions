#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1036 - Formula de Bhaskara
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1036
#
# ad-hoc
#

import math

a, b, c = map(float, raw_input().split())

delt = b**2 - 4*a*c
if delt < 0 or a == 0:
    print 'Impossivel calcular'
else:
    print 'R1 = %.5f' % ((-b + math.sqrt(delt)) / (2 * a))
    print 'R2 = %.5f' % ((-b - math.sqrt(delt)) / (2 * a))
