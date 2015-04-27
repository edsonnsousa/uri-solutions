#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 20 2015
# 1436 - Jogo do Tijolo
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1436
#
# math
#

nTests = int(raw_input())
for test in range(1, nTests + 1):
    ages = map(int, raw_input().split())
    print 'Case %d: %d' % (test, ages[len(ages) / 2])
