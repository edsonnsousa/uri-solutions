#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1045 - Tipos de Triangulos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1045
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1044
#
# ad-hoc
#

sides = map(float, raw_input().split())
sides.sort(reverse = True)
a = sides[0]
b = sides[1]
c = sides[2]

if a >= b + c:
    print 'NAO FORMA TRIANGULO'
else:
    if a**2 == b**2 + c**2:
        print 'TRIANGULO RETANGULO'
    if a**2 > b**2 + c**2:
        print 'TRIANGULO OBTUSANGULO'
    if a**2 < b**2 + c**2:
        print 'TRIANGULO ACUTANGULO'
    if a == b == c:
        print 'TRIANGULO EQUILATERO'
    elif a == b or a == c or b == c:
        print 'TRIANGULO ISOSCELES'
