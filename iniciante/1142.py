#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 17 2015
# 1142 - PUM
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1142
#
# ad-hoc
#

lines = int(raw_input())
for n in range(lines):
    base = n * 4
    print '%d %d %d PUM' % (base + 1, base + 2, base + 3) 
