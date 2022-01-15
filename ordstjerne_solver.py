# -*- coding: UTF-8 -*-
"""
Henter ordliste generert fra fullformslisten i norsk ordbank fra Språkbanken:
https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-5/

Ordlista består av alle gyldige ord med minst fire bokstaver.
"""

import re

midtbokstav = input("Obligatorisk bokstav: ").strip()

alle_bokstaver = midtbokstav+input("Andre bokstaver i ordstjerna: ").strip()

regex = re.compile("\\b["+alle_bokstaver+"]*"+midtbokstav+"["+alle_bokstaver+"]*\\b")


with open('ordliste.txt',"r") as fil:
    ordliste = fil.readline()

losning = set(regex.findall(ordliste))

print("Fant", len(losning), "gyldige ord:")

print(*(sorted(list(losning), reverse=True, key=len)), sep=", ")