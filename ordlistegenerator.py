# -*- coding: UTF-8 -*-

"""
Bruker fullformslista fra Språkbanken, og oppretter en ny fil som inneholder alle ord som består av fire bokstaver eller mer.

Eksempel på linje i fullformslista: (linje 27)
25	67750	syttende	adj <ordenstall> pos be ent normert	515	3	1996.01.01	4000	normert

Kilde:
https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-5/

"""
import re

fullformsliste = open('fullformsliste.txt',"rt") 
fullformsliste.readline()
ordlistefil = open("ordliste.txt", "a")
regex = re.compile("^[a-zæøå]*$")

while fullformsliste:
    linje = str(fullformsliste.readline())
    if linje == '':
        break
    norsk_ord = linje.split()[2]
    if regex.match(norsk_ord) and len(norsk_ord)>3:
        ordlistefil.write(linje.split()[2]+" ")

