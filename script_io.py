#!/usr/bin/env python3

# Eingaben über die Kommandozeile

# Einlesen eines Strings

name = input("Bitte geben Sie Ihren Namen ein:")
print ("Moin "+name+"!")

alter = int(input("Bitte geben Sie Ihr Alter ein:"))
print("Sie sind "+str(alter)+ " Jahre alt.")

jahre_bis_30 = 30 - alter
if jahre_bis_30 > 0:
  print("Sie werden in",jahre_bis_30,"Jahren 30")
else:
  print("Sie sind 30 oder älter")