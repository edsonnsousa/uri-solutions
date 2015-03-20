#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 20 2015
# 1534 - Matriz 123
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1534
# ad-hoc
#

while True:
    try:
        n = int(raw_input())
    except EOFError:
        break

    mat = [['3' for i in range(n)] for j in range(n)]
    for i in range(n):
        mat[i][i] = '1'
        mat[i][-i - 1] = '2'
        print ''.join(mat[i])
