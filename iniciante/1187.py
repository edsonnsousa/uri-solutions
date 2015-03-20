#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 20 2015
# 1187 - Area Superior
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1187
# ad-hoc
#

op = raw_input()
mat = [[0 for i in range(12)] for j in range(12)]
for i in range(12):
    for j in range(12):
        mat[i][j] = float(raw_input())

sum_above = 0
for i in range(12):
    for j in range(12):
        if i + j <= 10 and j > i:
            sum_above += mat[i][j]

if op == 'S':
    print '%.1f' % (sum_above)
else:
    print '%.1f' % (sum_above / float(30))
