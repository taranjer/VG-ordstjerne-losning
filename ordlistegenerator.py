# -*- coding: UTF-8 -*-
import re

f = open('fullformsliste.txt',"rt") 
f.readline()
ordlistefil = open("ordliste.txt", "a")
regex = re.compile("^[a-zæøå]*$")

while f:
    linje = str(f.readline())
    if linje == '':
        break
    gyldigord = linje.split()[2]
    if regex.match(gyldigord) and len(gyldigord)>3:
        ordlistefil.write(linje.split()[2]+" ")

