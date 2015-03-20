#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 20 2015
# 1179 - Preenchimento de Vetor IV
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1179
# ad-hoc
#

even = []
odd = []
for i in range(15):
    n = int(raw_input())
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

    if len(odd) == 5:
        for j in range(5):
            print 'impar[%d] = %d' % (j, odd[j])
        odd = []
    if len(even) == 5:
        for j in range(5):
            print 'par[%d] = %d' % (j, even[j])
        even = []
        
for i in range(len(odd)):
    print 'impar[%d] = %d' % (i, odd[i])

for i in range(len(even)):
    print 'par[%d] = %d' % (i, even[i])
