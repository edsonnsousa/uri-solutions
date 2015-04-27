#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 24 2015
# 1306 - Numerando Estradas
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1306
#
# math
#

import math

case = 1
while True:
    r, n = map(int, raw_input().split())

    if r == 0 and n == 0: break

    n_suffix = int(math.ceil(r / float(n)) - 1)
   
    if n_suffix <= 26:
        print 'Case %d: %d' % (case, n_suffix)
    else:
        print 'Case %d: impossible' % case
    
    case += 1
