#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1043 - Triangulo
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1043
#
# ad-hoc
#

sides = map(float, raw_input().split())

sorted_sides = sorted(sides)
if sorted_sides[2] < sorted_sides[0] + sorted_sides[1]:
    print 'Perimetro = %.1f' % sum(sides)
else:
    area = (sides[0] + sides[1]) * sides[2] / 2.0
    print 'Area = %.1f' % area
