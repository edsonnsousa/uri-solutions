#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 19 2015
# 1029 - Fibonacci, How Many Calls?
# https://www.urionlinejudge.com.br/judge/en/problems/view/1029
#
# dp
#

value = [-1 for i in xrange(40)]
calls = [-1 for i in xrange(40)]

def fib(n):
    if value[n] != -1:
        return value[n], calls[n]

    if n == 0:
        value[n] = 0
        calls[n] = 1
        return 0, 1
    elif n == 1:
        value[n] = 1
        calls[n] = 1
        return 1, 1
    else:
        v1, c1 = fib(n - 1)
        v2, c2 = fib(n - 2)
        value[n] = v1 + v2
        calls[n] = 1 + c1 + c2
        return value[n], calls[n]

tests = int(raw_input())
for i in xrange(tests):
    n = int(raw_input())
    v, c = fib(n)
    print 'fib(%d) = %d calls = %d' % (n, c - 1, v)
