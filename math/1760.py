#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 24 2015
# 1760 - Floco de Neve de Koch
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1760
#
# math
#

import math

while True:
    try:
        l = int(raw_input())
    except EOFError:
        break

    koch_area = 2 * math.sqrt(3) * (l ** 2) / 5
    print '%.2f' % koch_area
