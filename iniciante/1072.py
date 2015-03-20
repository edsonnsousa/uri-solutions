#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 27 2015
# 1072 - Intervalo 2
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1072
#
# ad-hoc
#

n = int(raw_input())
nums = []
for i in range(n):
    nums.append(int(raw_input()))

inside = 0
outside = 0
for n in nums:
    if 10 <= n <= 20:
        inside += 1
    else:
        outside += 1

print '%d in' % inside
print '%d out' % outside
