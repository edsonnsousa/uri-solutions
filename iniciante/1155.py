#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 18 2015
# 1155 - Sequencia S
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1155
#
# ad-hoc
#

sum_serie = 0.0
for i in range(1, 101):
    sum_serie += 1.0 / i

print '%.2f' % sum_serie
