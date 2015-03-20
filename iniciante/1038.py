#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1038 - Lanche
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1038
#
# ad-hoc
#

cod, qnt = map(int, raw_input().split())

prices = {1:4.0, 2:4.5, 3:5.0, 4:2.0, 5:1.5}
print 'Total: R$ %.2f' % (qnt * prices[cod])
