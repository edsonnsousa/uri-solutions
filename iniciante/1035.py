#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1035 - Teste de Selecao 1
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1035
#
# ad-hoc
#

a, b, c, d = map(int, raw_input().split())

if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
    print 'Valores aceitos'
else:
    print 'Valores nao aceitos'
