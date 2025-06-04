#Escribe un programa que pida al usuario ingresar una contraseña y repita la solicitud mientras la contraseña ingresada sea incorrecta. El programa debe continuar hasta que el usuario ingrese la contraseña correcta. Utiliza una estructura whilepara simular un do while.
contrasena_correcta = "secreto123"
contrasena_ingresada = "" # Inicializamos con un valor incorrecto para asegurar que el bucle se ejecute al menos una vez

while contrasena_ingresada != contrasena_correcta:
    contrasena_ingresada = input("Por favor, ingresa la contraseña: ")
    if contrasena_ingresada != contrasena_correcta:
        print("Contraseña incorrecta. Inténtalo de nuevo.")

print("¡Contraseña correcta! Acceso concedido.")