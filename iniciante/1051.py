#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 27 2015
# 1051 - Imposto de Renda
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1051
#
# ad-hoc
#

salary = float(raw_input())

if salary <= 2000:
    print 'Isento'
elif salary <= 3000:
    print 'R$ %.2f' % ((salary - 2000) * 0.08)
elif salary <= 4500:
    print 'R$ %.2f' % (80 + (salary - 3000) * 0.18)
else:
    print 'R$ %.2f' % (350 + (salary - 4500) * 0.28)
