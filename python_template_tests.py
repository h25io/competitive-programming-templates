from python_template import *
import collections
import fractions
import math
import random
import sys
import queue

def testBinarySearchInt(cases = 100, limitSize = 100, limitDomain = 10000):

    ok = 0
    ko = 0
    total = 0

    for it in range(cases):
        taille = random.randint(10, limitSize)
        l = sorted([random.randint(0, limitDomain) for i in range(taille)])

        type = random.randint(0,1)

        z = random.randint(min(l), max(l))


        isKo = False

        if(type == 1):
            l = l[::-1]
            p = lambda x: l[x] >= z
            res = binarySearchInt(p, 0, taille-1)

            for i in range(taille):
                if((l[i] >= z and i > res) or (l[i] < z and i <= res)):
                    isKo = True
                    break
        else:
            p = lambda x: l[x] >= z
            res = binarySearchInt(p, 0, taille-1)

            for i in range(taille):
                if((l[i] >= z and i < res) or (l[i] < z and i >= res)):
                    isKo = True
                    break
        total += 1
        if(isKo):
            ko += 1
        else:
            ok += 1
    print('Test binarySearchInt : %d / %d'%(ok, total))

def testFastMatrixPow():
    ok = 0
    ko = 0
    total = 0
    (gauche, droite) = (1,1)
    for i in range(30):
        m = fastMatrixPow([[0,1],[1,1]],i)
        if(gauche != m[1][1]):
            ko += 1
        else:
            ok += 1
        (gauche,droite) = (droite,gauche+droite)


        total += 1
    print('Test fastMatrixPow : %d / %d'%(ok, total))


testFastMatrixPow()