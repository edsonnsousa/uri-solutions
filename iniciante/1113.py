#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 17 2015
# 1113 - Crescente e Decrescente
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1113
#
# ad-hoc
#

while True:
    m, n = map(int, raw_input().split())

    if m == n: break

    if m < n:
        print 'Crescente'
    else:
        print 'Decrescente'
