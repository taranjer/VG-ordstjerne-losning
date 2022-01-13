# -*- coding: UTF-8 -*-
"""
Henter ordliste fra fullformslisten i norsk ordbank fra Språkbanken:
https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-5/
"""
import re

middle_letter = input("Obligatorisk bokstav: ")

start_and_end_regex = middle_letter

for letter in input("Andre bokstaver i ordstjerna: ").strip():
    start_and_end_regex += letter

regex = re.compile("^["+start_and_end_regex+"]*"+middle_letter+"["+start_and_end_regex+"]*$")

f = open('ordliste.txt',"rt") 

solution = set()

while f:
    norwegian_word = str(f.readline()).strip("\n")
    if norwegian_word == '':
        break
    if regex.match(norwegian_word) and len(norwegian_word)>3:
        solution.add(norwegian_word)

for i in sorted(list(solution), reverse=True, key=len): # De beste ordene skrives ut først.
    print(i, end=", ")
    
f.close()