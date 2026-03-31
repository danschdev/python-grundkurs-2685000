#!/usr/bin/env python3

# Aufgabe: Programmieren Sie einen einfachen Taschenrechner

# Ihr Taschenrechner soll folgende Funktionen unterstützen:
# - Addition (+)
# - Subtraktion (-)
# - Multiplikation (*)
# - Division (/)

# Der Benutzer sollte aufgefordert werden, zwei Zahlen einzugeben.
# Anschließend sollte der Benutzer die gewünschte Operation wählen können.

# Beispielablauf:
# 1. Benutzer gibt die erste Zahl ein.
# 2. Benutzer gibt die zweite Zahl ein.
# 3. Benutzer wählt die Operation (+, -, *, /).
# 4. Das Programm führt die Berechnung durch und gibt das Ergebnis aus.

# Optional: Erweitern Sie den Taschenrechner um weitere Funktionen wie Potenzierung oder Modulo.

operator = input("Geben Sie den Operator ein")
operand1 = float(input("Geben Sie die erste Zahl ein"))
operand2 = float(input("Geben Sie die zweite Zahl ein"))

if (operator == "+"):
  print(operand1 + operand2)
elif (operator == "-"):
  print(operand1 - operand2)
elif (operator == "*"):
  print(operand1 * operand2)
elif (operator == "/"):
  print(operand1 / operand2)
elif (operator == "^" or operator == "**"):
  print(operand1 ** operand2)
elif (operator == "%"):
  print(operand1 % operand2)
else:
  print("Ungültige Eingabe")