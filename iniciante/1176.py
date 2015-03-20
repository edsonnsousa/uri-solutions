#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 20 2015
# 1176 - Fibonacci em Vetor
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1176
# ad-hoc
#

fib = [0, 1]
for i in range(60):
    fib.append(fib[-2] + fib[-1])


nTests = int(raw_input())
for nt in range(nTests):
    n = int(raw_input())
    print 'Fib(%d) = %d' % (n, fib[n])
