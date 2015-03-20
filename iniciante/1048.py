#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1048 - Aumento de Salario
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1048
#
# ad-hoc
#

def print_infos(salary, new_salary, percent):
    print 'Novo salario: %.2f' % new_salary
    print 'Reajuste ganho: %.2f' % (new_salary - salary)
    print 'Em percentual: %d %%' % percent

salary = float(raw_input())

if salary <= 400:
    print_infos(salary, salary * 1.15, 15)
elif salary <= 800:
    print_infos(salary, salary * 1.12, 12)
elif salary <= 1200:
    print_infos(salary, salary * 1.1, 10)
elif salary <= 2000:
    print_infos(salary, salary * 1.07, 7)
else:
    print_infos(salary, salary * 1.04, 4)
