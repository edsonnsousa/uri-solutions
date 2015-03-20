#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 17 2015
# 1116 - Dividindo X por Y
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1116
#
# ad-hoc
#

nTests = int(raw_input())

for nt in range(nTests):
    x, y = map(int, raw_input().split())

    if y == 0:
        print 'divisao impossivel'
    else:
        print '%.1f' % (x / float(y))
