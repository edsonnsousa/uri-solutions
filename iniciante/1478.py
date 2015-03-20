#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 20 2015
# 1478 - Matriz Quadrada II
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1478
# ad-hoc
#

while True:
    n = int(raw_input())

    if n == 0: break

    mat = [[1 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] += abs(j - i)

    for i in range(n):
        line = ['%3d' % n for n in mat[i]]
        print ' '.join(line)
    print
