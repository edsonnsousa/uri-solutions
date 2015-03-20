#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 20 2015
# 1564 - Vai Ter Copa?
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1564
# ad-hoc
#

while True:
    try:
        n = int(raw_input())
    except EOFError:
        break

    if n == 0:
        print 'vai ter copa!'
    else:
        print 'vai ter duas!'
