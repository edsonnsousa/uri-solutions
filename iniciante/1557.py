#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 20 2015
# 1557 - Matriz Quadrada III
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1557
# ad-hoc
#

while True:
    n = int(raw_input())

    if n == 0: break

    mat = [[1 for i in range(n)] for j in range(n)]
    for j in range(1, n):
        mat[0][j] = mat[0][j - 1] * 2

    for i in range(1, n):
        for j in range(n):
            if j == 0:
                mat[i][j] = mat[i - 1][j] * 2
            else:
                mat[i][j] = mat[i][j - 1] * 2
   
    max_len = len(str(mat[-1][-1]))
    for i in range(n):
        line = ['%*d' % (max_len, n) for n in mat[i]]
        print ' '.join(line)
    print
