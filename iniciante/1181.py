#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 20 2015
# 1181 - Linha na Matriz
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1181
# ad-hoc
#

line = int(raw_input())
op = raw_input()
mat = [[0 for i in range(12)] for j in range(12)]
for i in range(12):
    for j in range(12):
        mat[i][j] = float(raw_input())

if op == 'S':
    print '%.1f' % (sum(mat[line]))
else:
    print '%.1f' % (sum(mat[line]) / 12)
