#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 27 2015
# 1075 - Resto 2
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1075
#
# ad-hoc
#

n = int(raw_input())

for i in xrange(2, 10000):
    if i % n == 2:
        print i
