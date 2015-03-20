#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 17 2015
# 1118 - Varias Notas Com Validacao
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1118
#
# ad-hoc
#


def media():
    valid_notes = 0
    notes = []
    while True:
        note = float(raw_input())
    
        if 0 <= note <= 10:
            notes.append(note)
        else:
            print 'nota invalida'
    
        if len(notes) == 2:
            print 'media = %.2f' % ((notes[0] + notes[1]) / 2)
            break

    
media()
while True:
    print 'novo calculo (1-sim 2-nao)'
    repeat = raw_input()

    if repeat == '1':
        media()
    elif repeat == '2':
        break
