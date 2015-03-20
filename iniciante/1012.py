#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1011 - Area
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1012
#
# ad-hoc
#

a, b, c = map(float, raw_input().split())

print 'TRIANGULO: %.3f' % (a * c / 2)
print 'CIRCULO: %.3f' % (3.14159 * (c ** 2))
print 'TRAPEZIO: %.3f' % ((a + b) * c / 2)
print 'QUADRADO: %.3f' % (b ** 2)
print 'RETANGULO: %.3f' % (a * b)
