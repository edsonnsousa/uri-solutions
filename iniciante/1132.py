#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 17 2015
# 1132 - Multiplos de 13
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1132
#
# ad-hoc
#

x = int(raw_input())
y = int(raw_input())

lowest = min(x, y)
biggest = max(x, y)

sum_mult_13 = 0
for n in range(lowest, biggest + 1):
    if n % 13 != 0:
        sum_mult_13 += n

print sum_mult_13
