#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 20 2015
# 1589 - Bob Conduite
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1589
# ad-hoc
#

nTests = int(raw_input())
for nt in xrange(nTests):
    r1, r2 = map(int, raw_input().split())

    d = r1*2 + r2*2
    if d % 2 == 0:
        print d / 2
    else:
        print (d / 2) + 1
