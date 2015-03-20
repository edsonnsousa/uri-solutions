#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1046 - Tempo de Jogo
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1046
#
# ad-hoc
#

start, stop = map(int, raw_input().split())

if start == stop:
    print 'O JOGO DUROU 24 HORA(S)'
elif start < stop:
    print 'O JOGO DUROU %d HORA(S)' % (stop - start)
else:
    print 'O JOGO DUROU %d HORA(S)' % (24 - start + stop)
