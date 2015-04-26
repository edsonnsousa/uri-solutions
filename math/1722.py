#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Apr 25 2015
# 1722 - Quantos Fibs?
#
# math
#

MAX = 10 ** 100

fibs = [1, 2]
def full_fib():
    while True:
        fibs.append(fibs[-1] + fibs[-2])
        if fibs[-1] >= MAX: break


while True:
    full_fib()

    a, b = map(long, raw_input().split())

    if a == b == 0: break

    aws = 0
    for i in xrange(len(fibs)):
        if a <= fibs[i] <= b:
            aws += 1

    print aws
