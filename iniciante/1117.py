#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Mar 17 2015
# 1117 - Validacao de Nota
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1117
#
# ad-hoc
#

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
