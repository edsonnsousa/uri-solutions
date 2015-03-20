#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1021 - Notas e Moedas
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1021
#
# ad-hoc
#

val = raw_input()
real, cents = map(int, val.split('.'))

values = [100, 50, 20, 10, 5, 2]
coins  = ['1.00', '0.50', '0.25', '0.10', '0.05', '0.01']
coins_cents = [100, 50, 25, 10, 5, 1]

print 'NOTAS:'
for v in values:
    print '%d nota(s) de R$ %d.00' % (real / v, v)
    real %= v

cents += real * 100

print 'MOEDAS:'
for i in xrange(len(coins_cents)):
    print '%d moeda(s) de R$ %s' % (cents / coins_cents[i], coins[i])
    cents %= coins_cents[i]
