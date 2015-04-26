#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 24 2015
# 1028 - Figurinhas
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1028
#
# math
#

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

nTests = int(raw_input())
for nt in xrange(nTests):
    ricardo, vicente = map(int, raw_input().split())
    print gcd(ricardo, vicente)
