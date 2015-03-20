#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 17 2015
# 1131 - Grenais
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1131
#
# ad-hoc
#


wins_inter = 0
wins_gremio = 0
draws = 0
while True:
    inter, gremio = map(int, raw_input().split())

    if inter > gremio:
        wins_inter += 1
    elif inter < gremio:
        wins_gremio += 1
    else:
        draws += 1

    print 'Novo grenal (1-sim 2-nao)'
    repeat = raw_input()

    if repeat == '2':
        break

print '%d grenais' % (wins_inter + wins_gremio + draws)
print 'Inter:%d' % wins_inter
print 'Gremio:%d' % wins_gremio
print 'Empates:%d' % draws

if wins_inter > wins_gremio:
    print 'Inter venceu mais'
elif wins_inter < wins_gremio:
    print 'Gremio venceu mais'
else:
    print 'Nao houve vencedor'
