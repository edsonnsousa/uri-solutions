#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 7 2015
# 1105 - Sub-prime
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1105
#
# ad-hoc
#

def solve_case(bancs, debentures):
    reserves = map(int, raw_input().split())
    to_pay = [0 for i in xrange(bancs)]
    to_receive = [0 for i in xrange(bancs)]

    for i in xrange(debentures):
        debtor, creditor, value = map(int, raw_input().split())
        to_pay[debtor - 1] += value
        to_receive[creditor - 1] += value

    for i in xrange(bancs):
        if to_pay[i] > to_receive[i] + reserves[i]:
            return 'N'
    return 'S'


while True:
    bancs, debentures = map(int, raw_input().split())

    if bancs == 0 and debentures == 0: break

    print solve_case(bancs, debentures)
