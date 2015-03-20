#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 18 2015
# 1146 - Sequencias Crescentes
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1146
#
# ad-hoc
#

while True:
    n = int(raw_input())

    if n == 0: break

    print ' '.join(map(str, range(1, n + 1)))
