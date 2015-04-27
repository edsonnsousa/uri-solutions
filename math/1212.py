#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 24 2015
# 1212 - Aritmetica Primaria
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1212
#
# math
#

while True:
    a, b = map(int, raw_input().split())

    if a == 0 and b == 0: break

    a = '%09d' % int(a)
    b = '%09d' % int(b)
    
    num_carrys = 0
    carry = 0
    for i in xrange(9):
        s = int(a[-i - 1]) + int(b[-i -1]) + carry
        if s >= 10:
            carry = 1
            num_carrys += 1
        else:
            carry = 0

    if num_carrys == 0:
        print 'No carry operation.'
    elif num_carrys == 1:
        print '1 carry operation.'
    else:
        print '%d carry operations.' % num_carrys

