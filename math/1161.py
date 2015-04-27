#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 20 2015
# 1161 - Soma de Fatoriais
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1161
#
# math
#

fact = [1]
for i in range(1, 21):
    fact.append(i * fact[i - 1])

while True:
    try:
        m, n = map(int, raw_input().split())
        print fact[m] + fact[n]
    except EOFError:
        break
