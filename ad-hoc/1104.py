#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Apr 7 2015
# 1104 - Troca de Cartas
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1104
#
# ad-hoc
#


while True:
    a, b = map(int, raw_input().split())

    if a == b == 0: break

    cards_a = map(int, raw_input().split())
    cards_b = map(int, raw_input().split())

    op1 = len(set(cards_a) - set(cards_b))
    op2 = len(set(cards_b) - set(cards_a))

    print min(op1, op2)
