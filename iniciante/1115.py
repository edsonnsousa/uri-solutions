#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 17 2015
# 1115 - Quandrante
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1115
#
# ad-hoc
#

while True:
    x, y = map(int, raw_input().split())

    if x == 0 or y == 0: break

    if x > 0 and y > 0:
        print 'primeiro'
    elif x < 0 and y > 0:
        print 'segundo'
    elif x < 0 and y < 0:
        print 'terceiro'
    else:
        print 'quarto'
