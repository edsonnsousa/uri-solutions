#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 27 2015
# 1097 - Sequencia IJ 3
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1097
#
# ad-hoc
#

for i, j in zip(range(1, 10, 2), range(7, 16, 2)):
    print 'I=%d J=%d' % (i, j)
    print 'I=%d J=%d' % (i, j - 1)
    print 'I=%d J=%d' % (i, j - 2)
