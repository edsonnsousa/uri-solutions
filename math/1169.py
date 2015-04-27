#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 20 2015
# 1169 - Trigo no Tabuleiro
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1169
#
# math
#

nTests = int(raw_input())
for test in range(nTests):
    x = int(raw_input())
    print '%d kg' % ((2 ** x) / 12000)
