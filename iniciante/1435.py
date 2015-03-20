#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 20 2015
# 1435 - Matriz Quadrada I
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1435
# ad-hoc
#

while True:
    n = int(raw_input())

    if n == 0: break

    mat = [[1 for i in range(n)] for j in range(n)]
    for k in range(1, (n - 1) / 2 + 1):
        for i in range(k, n - k):
            for j in range(k, n - k):
                mat[i][j] += 1

    for i in range(n):
        line = ['%3d' % n for n in mat[i]]
        print ' '.join(line)
    print
