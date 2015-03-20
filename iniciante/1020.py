#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1020 - Idade em Dias
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1020
#
# ad-hoc
#

day = int(raw_input())

year = day / 365
day %= 365
month = day / 30
day %= 30

print '%d ano(s)' % year
print '%d mes(es)' % month
print '%d dia(s)' % day
