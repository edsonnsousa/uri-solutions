#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Apr 15 2015
# 1308 - Guerreiros Etruscos Nunca Jogam Xadrez
#
# math
#

import math

def lines(n):
    return int((-1 + math.sqrt(1 + 8 * n)) / 2)

nTests = int(raw_input())
for nt in xrange(1, nTests + 1):
    n = int(raw_input())
    print lines(n)
