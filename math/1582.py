#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 20 2015
# 1582 - O Teorema de Pitagoras
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1582
#
# math
#

def isTriple(sides):
    return sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def isPrimitive(sides):
    return gcd(sides[0], gcd(sides[1], sides[2])) == 1


while True:
    try:
        sides = map(int, raw_input().split())
        sides.sort()

        if isTriple(sides):
            if isPrimitive(sides):
                print 'tripla pitagorica primitiva'
            else:
                print 'tripla pitagorica'
        else:
            print 'tripla'

    except EOFError:
        break
