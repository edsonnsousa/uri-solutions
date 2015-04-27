#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 20 2015
# 1197 - Volta a Faculdade de Fisica
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1197
#
# math
#

while True:
    try:
        v, t = map(int, raw_input().split())
        print 2 * v * t
    except EOFError:
        break
