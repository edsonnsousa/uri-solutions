#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 17 2015
# 1143 - Quadrado e ao Cubo
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1143
#
# ad-hoc
#

lines = int(raw_input())
for n in range(1, lines + 1):
    print '%d %d %d' % (n, n ** 2, n ** 3) 
