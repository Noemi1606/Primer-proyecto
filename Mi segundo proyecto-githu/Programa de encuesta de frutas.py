#Realiza un programa que recoja las respuestas de varias personas sobre su fruta favorita. Al final, muestra cuántas veces se eligió cada fruta.
def encuesta_frutas():
    respuestas = {}

    while True:
        fruta = input("¿Cuál es tu fruta favorita? (Escribe 'fin' para terminar): ").strip().capitalize()
        if fruta.lower() == "fin":
            break
        if fruta in respuestas:
            respuestas[fruta] += 1
        else:
            respuestas[fruta] = 1

    print("\nResultados de la encuesta:")
    for fruta, cantidad in respuestas.items():
        print(f"{fruta}: {cantidad} votos")

if __name__ == "__main__":
    encuesta_frutas()
