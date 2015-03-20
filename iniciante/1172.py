#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 18 2015
# 1172 - Substituicao em Vetor I
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1172
# ad-hoc
#

ints = []
for i in range(10):
    n = int(raw_input())
    print 'X[%d] = %d' % (i, 1 if n <= 0 else n)
