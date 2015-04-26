#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 25 2015
# 1392 - Lajotas Hexagonais
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1393
#
# math
#

while True:
    n = int(raw_input())

    if n == 0: break

    a = 0
    b = 1
    fib = 1
    for i in xrange(n):
        fib = a + b
        a = b
        b = fib

    print fib
