#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 25 2015
# 1457 - Oraculo de Alexandria
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1457
#
# math
#

nTests = int(raw_input())
for nt in xrange(nTests):
    n = raw_input()
    k = n.count('!')
    n = int(n.rstrip('!'))

    fact = n
    mult = 1
    while True:
        if n - (mult * k) < 1: break
        fact *= n - (mult * k)
        mult += 1

    print fact
