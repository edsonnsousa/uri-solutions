#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 24 2015
# 1761 - Decoracao Natalina
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1761
#
# math
#

import math

while True:
    try:
        a, b, c = map(float, raw_input().split())
    except EOFError:
        break

    x = ((b * math.tan(3.141592654 * a/ 180)) + c) * 5
    print '%.2f' % x
