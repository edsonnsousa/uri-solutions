#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 20 2015
# 1170 - Blobs
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1170
#
# math
#

nTests = int(raw_input())
for test in range(nTests):
    x = float(raw_input())
    days = 0
    while x > 1:
        x /= 2
        days += 1

    print '%d dias' % days
