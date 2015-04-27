#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 24 2015
# 1304 - Velocidade Media
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1304
#
# math
#

import math

def calc_dist(last_time, time, speed):
    h1, m1, s1 = map(int, last_time.split(':'))
    h2, m2, s2 = map(int, time.split(':'))
    sec1 = (h1 * 3600) + (m1 * 60) + s1
    sec2 = (h2 * 3600) + (m2 * 60) + s2
    sec_diff = sec2 - sec1
    
    return speed * sec_diff / 3600.0


last_time = '00:00:00'
last_speed = 0
dist = 0.0
while True:
    try:
        data = raw_input().split()
    except EOFError:
        break

    if len(data) == 1:
        dist += calc_dist(last_time, data[0], last_speed)
        last_time = data[0]
        print '%s %.2f km' % (data[0], dist)
    else:
        dist += calc_dist(last_time, data[0], last_speed)
        last_time = data[0]
        last_speed = int(data[1])
