#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 18 2015
# 1154 - Idades
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1154
#
# ad-hoc
#

ages = []
while True:
    age = int(raw_input())
    if age < 0: break
    ages.append(age)

print '%.2f' % (sum(ages) / float(len(ages)))
