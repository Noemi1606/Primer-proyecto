#Pide al usuario que ingrese un número entero positivo y muestra todos los números desde 1 hasta el número ingresado, uno por uno, utilizando un bucle while.

def contar_hasta_n():

  while True:
    try: 
      entrada_usuario = input("Por favor, ingrese un número entero positivo: ")
      
      numero_limite = int(entrada_usuario)  

      if numero_limite <= 0:
        print("¡Oops! El número debe ser positivo (mayor que 0). Intenta de nuevo.")
      else:
        break 
    except ValueError:
      print("¡Eso no es un número entero! Por favor, ingresa un número, como 5 o 10.")

  print(f"\n¡A contar! Desde 1 hasta {numero_limite}:")
  
  contador = 1 
  
  while contador <= numero_limite:
    print(contador)
    contador += 1   

if __name__ == "__main__":
  contar_hasta_n()
