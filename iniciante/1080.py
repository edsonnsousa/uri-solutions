#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 27 2015
# 1080 - Maior e Posicao
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1080
#
# ad-hoc
#

n = int(raw_input())
pos_atual = 1
great = n
pos_great = pos_atual

for i in xrange(99):
    n = int(raw_input())
    pos_atual += 1
    if n > great:
        great = n
        pos_great = pos_atual

print great
print pos_great
