# -*- coding: UTF-8 -*-
"""
Henter ordliste fra fullformslisten i norsk ordbank fra Språkbanken:
https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-5/
"""
import re

middle_letter = input("Obligatorisk bokstav: ")

all_letters = middle_letter+input("Andre bokstaver i ordstjerna: ").strip()

regex = re.compile("^["+all_letters+"]*"+middle_letter+"["+all_letters+"]*$")

f = open('ordliste.txt',"rt") 

solution = set()

while f:
    norwegian_word = str(f.readline()).strip("\n")
    if norwegian_word == '':
        break
    if regex.match(norwegian_word) and len(norwegian_word)>3:
        solution.add(norwegian_word)

print(*(sorted(list(solution), reverse=True, key=len)), sep=", ")

f.close()