#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 27 2015
# 1098 - Sequencia IJ 4
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1098
#
# ad-hoc
#

i = 0
j = 1
print 'I=%d J=%d' % (i, j)
print 'I=%d J=%d' % (i, j + 1) 
print 'I=%d J=%d' % (i, j + 2)
for n in range(2, 10, 2):
    print 'I=%d.%d J=%d.%d' % (i, n, j, n)
    print 'I=%d.%d J=%d.%d' % (i, n, j + 1, n)
    print 'I=%d.%d J=%d.%d' % (i, n, j + 2, n)

i += 1
j += 1

print 'I=%d J=%d' % (i, j)
print 'I=%d J=%d' % (i, j + 1)
print 'I=%d J=%d' % (i, j + 2)
for n in range(2, 10, 2):
    print 'I=%d.%d J=%d.%d' % (i, n, j, n)
    print 'I=%d.%d J=%d.%d' % (i, n, j + 1, n)
    print 'I=%d.%d J=%d.%d' % (i, n, j + 2, n)

i += 1
j += 1

print 'I=%d J=%d' % (i, j)
print 'I=%d J=%d' % (i, j + 1)
print 'I=%d J=%d' % (i, j + 2)
