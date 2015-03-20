#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 27 2015
# 1074 - Par ou Impar
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1074
#
# ad-hoc
#

n = int(raw_input())

for i in range(n):
    num = int(raw_input()) 
    if num == 0:
        print 'NULL'
    elif num % 2 == 0:
        if num > 0:
            print 'EVEN POSITIVE'
        else:
            print 'EVEN NEGATIVE'
    else:
        if num > 0:
            print 'ODD POSITIVE'
        else:
            print 'ODD NEGATIVE'

