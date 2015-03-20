#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 18 2015
# 1156 - Sequencia S II
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1156
# ad-hoc
#

sum_serie = 0.0
dem = 1
for i in range(1, 40, 2):
    sum_serie += float(i) / dem
    dem *= 2

print '%.2f' % sum_serie
