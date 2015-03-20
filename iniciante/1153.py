#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 18 2015
# 1153 - Fatorial Simples
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1153
#
# ad-hoc
#

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

n = int(raw_input())
print fact(n)
