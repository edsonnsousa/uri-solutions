#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 18 2015
# 1164 - Numero Perfeito
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1164
# ad-hoc
#

def isPerfect(n):
    sum_divs = 0
    for i in xrange(1, (n / 2) + 1):
        if n % i == 0:
            sum_divs += i

    return sum_divs == n


nTestes = int(raw_input())
for nt in range(nTestes):
    n = int(raw_input())

    if isPerfect(n):
        print '%d eh perfeito' % n
    else:
        print '%d nao eh perfeito' % n

