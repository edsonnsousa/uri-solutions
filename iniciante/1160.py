#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 18 2015
# 1160 - Crescimento Populacional
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1160
# ad-hoc
#

import math

nTestes = int(raw_input())

for nt in range(nTestes):
    Pa, Pb, G1, G2 = map(float, raw_input().split())

    years = 0
    while True:
        if Pa > Pb or years > 100: break
        
        Pa = math.floor(Pa + (Pa * G1) / 100.0)
        Pb = math.floor(Pb + (Pb * G2) / 100.0)
        years += 1

    if years <= 100:
        print '%d anos.' % years
    else:
        print 'Mais de 1 seculo.'

