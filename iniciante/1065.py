#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 27 2015
# 1064 - Positivos e Media
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1064
#
# ad-hoc
#

nums = []
for i in range(5):
    nums.append(int(raw_input()))

evens = 0
for n in nums:
    if n % 2 ==  0:
        evens += 1

print '%d valores pares' % evens
