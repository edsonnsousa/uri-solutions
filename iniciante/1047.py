#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1047 - Tempo de Jogo com Minutos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1047
#
# ad-hoc
#

h1, m1, h2, m2 = map(int, raw_input().split())

if h1 == h2 and m1 == m2:
    print 'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)'
elif h1 == h2:
    print 'O JOGO DUROU 0 HORA(S) E %d MINUTO(S)' % abs(m1 - m2)
elif h1 < h2:
    diff = (h2 - (h1 + 1)) * 60 + (60 - m1) + m2
    print 'O JOGO DUROU %d HORA(S) E %d MINUTO(S)' % (diff / 60, diff % 60)
else:
    diff = (24 - (h1 + 1)) * 60 + (60 - m1) + (h2 * 60) + m2
    print 'O JOGO DUROU %d HORA(S) E %d MINUTO(S)' % (diff / 60, diff % 60)
