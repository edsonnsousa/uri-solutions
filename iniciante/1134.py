#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 17 2015
# 1134 - Tipo de Combustivel
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1134
#
# ad-hoc
#


alcool = 0
gasolina = 0
diesel = 0
while True:
    fuel = int(raw_input())

    if fuel == 1:
        alcool += 1
    elif fuel == 2:
        gasolina += 1
    elif diesel == 3:
        diesel += 1
    elif fuel == 4:
        break

print 'MUITO OBRIGADO'
print 'Alcool: %d' % alcool
print 'Gasolina: %d' % gasolina
print 'Diesel: %d' % diesel
