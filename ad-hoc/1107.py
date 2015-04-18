#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Apr 7 2015
# 1107 - Escultura a Laser
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1107
#
# ad-hoc
#


while True:
    a, c = map(int, raw_input().split())

    if a == c == 0: break

    heights = map(int, raw_input().split())

    sweep = 0
    last_h = a
    for h in heights:
        if h < last_h:
            sweep += last_h - h
        last_h = h

    print sweep
