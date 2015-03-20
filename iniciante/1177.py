#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 20 2015
# 1177 - Preenchimento de Vetor II
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1177
# ad-hoc
#

n = int(raw_input())

count = 0
for i in xrange(1000):
    if count == n:
        count = 0

    print 'N[%d] = %d' % (i, count)
    count += 1
