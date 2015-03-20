#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 18 2015
# 1157 - Divisores I
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1157
# ad-hoc
#

n = int(raw_input())
for i in range(1, n + 1):
    if n % i == 0:
        print i
