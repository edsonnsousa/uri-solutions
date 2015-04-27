#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 24 2015
# 1323 - Feynman
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1323
#
# math
#

while True:
    n = int(raw_input())

    if n == 0: break

    squares = 0
    for i in xrange(n):
        squares += (n - i) ** 2

    print squares
