#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 24 2015
# 1221 - Primo Rapido
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1221
#
# math
#i

import math

def isPrime(n):
    limit = int(math.ceil(math.sqrt(n)))
    for i in xrange(2, limit):
        if n % i == 0:
            return False
    return True


nTests = int(raw_input())
for nt in xrange(nTests):
    n = int(raw_input())
    if isPrime(n):
        print 'Prime'
    else:
        print 'Not Prime'
