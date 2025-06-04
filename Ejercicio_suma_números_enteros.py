#Escribe un programa que calcule la suma de todos los números enteros del 1 al 100 utilizando un bucle for

suma_total = 0 

for numero in range(1, 101):
  suma_total += numero 
print(f"La suma de los números del 1 al 100 es: {suma_total}")
