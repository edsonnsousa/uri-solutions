#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 24 2015
# 1214 - Acima da Media
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1214
#
# math
#

nTests = int(raw_input())
for nt in xrange(nTests):
    grades = map(int, raw_input().split())
    avg = (sum(grades) - grades[0]) / float(grades[0])

    above = 0
    for i in xrange(1, len(grades)):
        if grades[i] > avg:
            above += 1

    print '%.3f%%' % ((float(above) / grades[0]) * 100)
