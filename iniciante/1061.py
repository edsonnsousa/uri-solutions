#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 27 2015
# 1061 - Tempo de um Evento
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1061
#
# ad-hoc
#

def s_end_day(h, m, s):
    return 86400 - (h * 3600) - (m * 60) - s

day_info = raw_input().split()
d1 = int(day_info[1])
h1, m1, s1 = map(int, raw_input().split(' : '))

day_info = raw_input().split()
d2 = int(day_info[1])
h2, m2, s2 = map(int, raw_input().split(' : '))

diff_sec = (d2 - d1) * 86400 + (s_end_day(h1, m1, s1) - s_end_day(h2, m2, s2))

print '%d dia(s)' % (diff_sec / 86400)
diff_sec %= 86400

print '%d hora(s)' % (diff_sec / 3600)
diff_sec %= 3600

print '%d minuto(s)' % (diff_sec / 60)
print '%d segundo(s)' % (diff_sec % 60)

