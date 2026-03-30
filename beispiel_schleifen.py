#!/user/bin/env python3

zahlen = [1,2,3,4,5]
for zahl in zahlen:
  print ("Zahl aus der Liste:", zahl)

for i in range(1,6): #Letzter Wert 6 ist nicht inkludiert
  print("Aktueller Wert von i:", i)

count = 0
while count < 5:
  print("count ist",count)
  count += 1

countdown = 10
while countdown > 0:
  print ("countdown ist", countdown)
  countdown -= 1