#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 20 2015
# 1240 - Encaixa ou Nao I
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1240
#
# math
#

nTests = int(raw_input())
for test in range(nTests):
    a, b = raw_input().split()
    if len(b) <= len(a) and b == a[-len(b):]:
        print 'encaixa'
    else:
        print 'nao encaixa'
