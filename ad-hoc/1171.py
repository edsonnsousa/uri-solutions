#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 7 2015
# 1171 - Frequencia de Numeros
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1171
#
# ad-hoc
#

qnt_nums = int(raw_input())

freq_nums = {}
for i in range(qnt_nums):
    num  = int(raw_input())

    if num in freq_nums:
        freq_nums[num] += 1
    else:
        freq_nums[num] = 1

freq_ordered = sorted(freq_nums.items())

for num, qnt in freq_ordered:
    print '%d aparece %d vez(es)' % (num, qnt)
