#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 20 2015
# 1198 - O Bravo Guerreiro Hashmat
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1198
#
# math
#

while True:
    try:
        x, y = map(int, raw_input().split())
        print abs(x - y)
    except EOFError:
        break
