#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Feb 26 2015
# 1049 - Animal
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1049
#
# ad-hoc
#

class1 = raw_input()
class2 = raw_input()
class3 = raw_input()

if class1 == 'vertebrado':
    if class2 == 'ave':
        if class3 == 'carnivoro':
            print 'aguia'
        else:
            print 'pomba'
    else:
        if class3 == 'onivoro':
            print 'homem'
        else:
            print 'vaca'
else:
    if class2 == 'inseto':
        if class3 == 'hematofago':
            print 'pulga'
        else:
            print 'lagarta'
    else:
        if class3 == 'hematofago':
            print 'sanguessuga'
        else:
            print 'minhoca'
