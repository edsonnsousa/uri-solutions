#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 6 2015
# 1070 - Seis Numeros Impares
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1070
#
# ad-hoc
#
 
x = int(raw_input())
 
if x % 2 != 0:
    impares = range(x, x + 12, 2)
else:
    impares = range(x + 1, x + 13, 2)
 
for n in impares:
    print n
