#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1019 - Conversao de Tempo
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1019
#
# ad-hoc
#

sec = int(raw_input())

hour = sec / 3600
sec %= 3600
minute = sec / 60
sec %= 60

print '%d:%d:%d' % (hour, minute, sec)
