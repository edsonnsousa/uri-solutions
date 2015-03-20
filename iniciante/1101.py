#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 17 2015
# 1101 - Sequencia de Numeros e Soma
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1101
#
# ad-hoc
#

while True:
    m, n = map(int, raw_input().split())

    if m <= 0 or n <= 0: break

    lowest = min(m, n)
    bigger = max(m, n)

    seq = range(lowest, bigger + 1)
    sum_seq = sum(seq)

    print '%s Sum=%d' % (' '.join(map(str, seq)), sum_seq)
