# Ordstjernen-løser

Et enkelt Python-program som finner alle løsningsordene til VGs daglige spill [Ordstjernen](https://www.vg.no/spill/ordstjernen).

Jeg har brukt [modulen for regulære uttrykk](https://docs.python.org/3/library/re.html) fra Pythons standardbibliotek.

Programmet finner noen få ord som på tross av å oppfylle kravene i reglene, ikke blir godtatt av VG.

## Hvordan bruke programmet

Brukes ved å laste ned [ordliste.txt](https://github.com/taranjer/VG-ordstjerne-losning/blob/master/ordliste.txt) og [ordstjerne_solver.py](https://github.com/taranjer/VG-ordstjerne-losning/blob/master/ordstjerne_solver.py), og deretter kjøre ___ordstjerne_solver.py___ i en terminal. De to filene må være i samme mappe.

Eksempel på kjøring:
```sh
python ordstjerne_solver.py
```
```
Obligatorisk bokstav: i
Andre bokstaver i ordstjerna: adtcpy
Fant 25 gyldige ord:
apatitt, pippip, titida, datida, datid, atypi, titta, apati, tippa, acida, titid,
pippa, tidd, titt, pipa, acid, pica, tipi, tida, tita, tipp, city, ditt, dipp, pipp
```
## Kilde

Språkbankens norske ordbank(bokmål): [https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-5/](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-5/)
