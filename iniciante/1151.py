#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 18 2015
# 1151 - Fibonacci Facil
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1151
#
# ad-hoc
#

fib = [0, 1]
for i in range(44):
    fib.append(fib[-2] + fib[-1])

n = int(raw_input())
print ' '.join(map(str, fib[:n]))
