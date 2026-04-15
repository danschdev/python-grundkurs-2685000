#!/usr/bin/env python3

# Aufgabe: Erstellen Sie ein Skript, das die Länge eines Textes analysiert und Informationen darüber liefert.

# Das Skript soll folgende Funktionalität bieten:
# 1. Ein Pflichtargument (positional argument), das einen Text entgegennimmt.
# 2. Ein optionales Argument --details, das zusätzliche Informationen liefert:
#    - Anzahl der Wörter
# 3. Wenn das Argument --details nicht angegeben wird, soll nur die Anzahl der Zeichen ausgegeben werden.

# Beispiel:
# python3 script.py "Dies ist ein Beispieltext." --details
# Ausgabe:
# Zeichen: 27
# Wörter: 5

# Optional: Erweitern Sie das Skript, um auch die Anzahl der Vokale und Konsonanten zu zählen.

import argparse
import re

parser = argparse.ArgumentParser(description="Textlängenzähler")

parser.add_argument("text")
parser.add_argument("--details", action='store_true')

args = parser.parse_args()

zeichenlaenge = len(args.text)
print ("Zeichen:"+str(zeichenlaenge))
if(args.details):
    words = args.text.split()
    print("Wörter:"+str(len(words)))

    nichtvokale = len(re.sub('(?:a|e|i|o|u|A|E|I|O|U)','', args.text))

    print ("Vokale:"+str(zeichenlaenge-nichtvokale))
