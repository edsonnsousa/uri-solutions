#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 25 2015
# 1010 - Calculo Simples
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1010
#
# ad-hoc
#

a1, b1, c1 = map(float, raw_input().split())
a2, b2, c2 = map(float, raw_input().split())

print 'VALOR A PAGAR: R$ %.2f' % (b1*c1 + b2*c2)
