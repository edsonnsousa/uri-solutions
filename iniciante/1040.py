#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1040 - Media 3
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1040
#
# ad-hoc
#

grades = map(float, raw_input().split())

avg = (grades[0]*2 + grades[1]*3 + grades[2]*4 + grades[3]*1) / 10.0
print 'Media: %.1f' % avg

if avg >= 7:
    print 'Aluno aprovado.'
elif avg < 5:
    print 'Aluno reprovado.'
else:
    print 'Aluno em exame.'
    n = float(raw_input())
    print 'Nota do exame: %.1f' % n
    new_avg = (avg + n) / 2
    if new_avg >= 5:
        print 'Aluno aprovado.'
    else:
        print 'Aluno reprovado.'
    print 'Media final: %.1f' % new_avg
