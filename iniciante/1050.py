#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 27 2015
# 1050 - DDD
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1050
#
# ad-hoc
#

codes = {61:'Brasilia', 71:'Salvador', 11:'Sao Paulo', 21:'Rio de Janeiro', 32:'Juiz de Fora', 19:'Campinas', 27:'Vitoria', 31:'Belo Horizonte'}

ddd = int(raw_input())

if ddd in codes:
    print codes[ddd]
else:
    print 'DDD nao cadastrado'
