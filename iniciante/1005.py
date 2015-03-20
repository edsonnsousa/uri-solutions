#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 6 2015
# 1005 - Media 1
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1005
#
# math
#

a = float(raw_input())
b = float(raw_input())

media = (a * 3.5 / 11) + (b * 7.5 / 11)

if media > 10.0:
    media = 10.0

print 'MEDIA = %.5f' % media
