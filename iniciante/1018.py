#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1018 - Cedulas
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1018
#
# ad-hoc
#

val = int(raw_input())
values = [100, 50, 20, 10, 5, 2, 1]

print val
for v in values:
    print '%d nota(s) de R$ %d,00' % (val / v, v)
    val %= v
