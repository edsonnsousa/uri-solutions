#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 27 2015
# 1064 - Positivos e Media
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1064
#
# ad-hoc
#

nums = []
for i in range(6):
    nums.append(float(raw_input()))

positives = 0
positive_sum = 0
for n in nums:
    if n > 0:
        positives += 1
        positive_sum += n

print '%d valores positivos' % positives
print '%.1f' % (positive_sum / float(positives))
