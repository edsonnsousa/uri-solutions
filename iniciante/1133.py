#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 17 2015
# 1133 - Resto da Divisao
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1133
#
# ad-hoc
#

x = int(raw_input())
y = int(raw_input())

lowest = min(x, y)
biggest = max(x, y)

for n in range(lowest + 1, biggest):
    if n % 5 == 2 or n % 5 == 3:
        print n
