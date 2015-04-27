#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 20 2015
# 1555 - Funcoes
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1555
#
# math
#

nTests = int(raw_input())
for test in range(nTests):
    x, y = map(int, raw_input().split())
    
    r = ((3 * x) ** 2) + (y ** 2)
    b = (2 * (x ** 2)) + ((5 * y) ** 2)
    c = -100 * x + (y ** 3)

    maxi = max(r, b, c)
    if maxi == r:
        print 'Rafael ganhou'
    elif maxi == b:
        print 'Beto ganhou'
    else:
        print 'Carlos ganhou'
