#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 17 2015
# 1144 - Sequencia Logica
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1144
#
# ad-hoc
#

lines = int(raw_input())
for n in range(1, lines + 1):
    print '%d %d %d' % (n, n ** 2, n ** 3) 
    print '%d %d %d' % (n, n ** 2 + 1, n ** 3 + 1) 
