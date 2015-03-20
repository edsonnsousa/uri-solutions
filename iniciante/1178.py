#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 20 2015
# 1178 - Preenchimento de Vetor III
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1178
# ad-hoc
#

n = float(raw_input())

for i in xrange(100):
    print 'N[%d] = %.4f' % (i, n)
    n /= 2
