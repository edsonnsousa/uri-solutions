#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 27 2015
# 1094 - Experiencias
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1094
#
# ad-hoc
#

animals = {'C':0, 'R':0, 'S':0}

nTests = int(raw_input())

tot = 0
for nt in range(nTests):
    num_animal, kind = raw_input().split()
    animals[kind] += int(num_animal)
    tot += int(num_animal)

print 'Total: %d cobaias' % tot
print 'Total de coelhos: %d' % animals['C']
print 'Total de ratos: %d' % animals['R']
print 'Total de sapos: %d' % animals['S']
print 'Percentual de coelhos: %.2f %%' % (animals['C'] * 100.0 / tot)
print 'Percentual de ratos: %.2f %%' % (animals['R'] * 100.0 / tot)
print 'Percentual de sapos: %.2f %%' % (animals['S'] * 100.0 / tot)
