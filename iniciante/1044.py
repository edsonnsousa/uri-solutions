#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1044 - Multiplos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1044
#
# ad-hoc
#

a, b = map(int, raw_input().split())

if a % b == 0 or b % a == 0:
    print 'Sao Multiplos'
else:
    print 'Nao sao Multiplos'
