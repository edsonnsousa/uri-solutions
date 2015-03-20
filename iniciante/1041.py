#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1041 - Coordenadas de um Ponto
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1041
#
# ad-hoc
#

x, y = map(float, raw_input().split())

if x == 0 and y == 0:
    print 'Origem'
elif x == 0:
    print 'Eixo Y'
elif y == 0:
    print 'Eixo X'
elif x > 0 and y > 0:
    print 'Q1'
elif x < 0 and y > 0:
    print 'Q2'
elif x < 0 and y < 0:
    print 'Q3'
else:
    print 'Q4'
