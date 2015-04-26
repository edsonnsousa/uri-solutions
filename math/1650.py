#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 25 2015
# 1650 - Pintura Preto e Branco
#
# math
#

def num_whites(n, m, c):
    if c == 1:
        return ((n * m) + 1) / 2
    else:
        return (n * m) / 2

while True:
    n, m, c = map(int, raw_input().split())

    if n == 0 and m == 0 and c == 0: break

    print num_whites(n - 7, m - 7, c)
