#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 27 2015
# 1066 - Pares, Impares, Positivos e Negativos
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1066
#
# ad-hoc
#

nums = []
for i in range(5):
    nums.append(int(raw_input()))

even = 0
odd = 0
pos = 0
neg = 0
for n in nums:
    if n % 2 == 0 :
        even += 1
    else:
        odd += 1

    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1

print '%d valor(es) par(es)' % even
print '%d valor(es) impar(es)' % odd
print '%d valor(es) positivo(s)' % pos
print '%d valor(es) negativo(s)' % neg
