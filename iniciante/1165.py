#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 18 2015
# 1165 - Numero Primo
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1165
# ad-hoc
#

import math

def isPrime(n):
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

nTestes = int(raw_input())
for nt in range(nTestes):
    n = int(raw_input())
    
    if isPrime(n):
        print '%d eh primo' % n
    else:
        print '%d nao eh primo' % n

