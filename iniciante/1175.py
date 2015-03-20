#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 20 2015
# 1175 - Troca em Vetor I
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1175
# ad-hoc
#

N = []
for i in range(20):
    N.append(raw_input())

N.reverse()

for i in range(20):
    print 'N[%d] = %s' % (i, N[i])
