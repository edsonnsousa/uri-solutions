#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 6 2015
# 1009 - Salario com Bonus
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1009
#
# ad-hoc
#

nome = raw_input()
salario = float(raw_input())
vendas = float(raw_input())

total = salario + vendas * 0.15

print 'TOTAL = R$ %.2f' % total
