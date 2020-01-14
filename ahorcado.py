#!/usr/bin/python3

from random import randint


# La imagen que se ve del ahorcado por cada fallo
def imgAhorcado():
    lista = []

    lista.append(" " * 5 + "_" * 7 + "\n" + " " * 5 + "|" + " " * 5 + "|\n" + " " *
                 5 + "|\n" + " " * 5 + "|\n" + " " * 5 + "|\n" + "_" * 5 + "|" + "_" * 6 + "\n")

    lista.append(" " * 5 + "_" * 7 + "\n" + " " * 5 + "|" + " " * 5 + "|\n" + " " * 5 + "|" +
                 " " * 5 + "0\n" + " " * 5 + "|\n" + " " * 5 + "|\n" + "_" * 5 + "|" + "_" * 6 + "\n")

    lista.append(" " * 5 + "_" * 7 + "\n" + " " * 5 + "|" + " " * 5 + "|\n" + " " * 5 + "|" +
                 " " * 4 + "\\0\n" + " " * 5 + "|\n" + " " * 5 + "|\n" + "_" * 5 + "|" + "_" * 6 + "\n")

    lista.append(" " * 5 + "_" * 7 + "\n" + " " * 5 + "|" + " " * 5 + "|\n" + " " * 5 + "|" +
                 " " * 4 + "\\0/\n" + " " * 5 + "|\n" + " " * 5 + "|\n" + "_" * 5 + "|" + "_" * 6 + "\n")

    lista.append(" " * 5 + "_" * 7 + "\n" + " " * 5 + "|" + " " * 5 + "|\n" + " " * 5 + "|" + " " *
                 4 + "\\0/\n" + " " * 5 + "|" + " " * 5 + "|\n" + " " * 5 + "|\n" + "_" * 5 + "|" + "_" * 6 + "\n")

    lista.append(" " * 5 + "_" * 7 + "\n" + " " * 5 + "|" + " " * 5 + "|\n" + " " * 5 + "|" + " " * 4 + "\\0/\n" +
                 " " * 5 + "|" + " " * 5 + "|\n" + " " * 5 + "|" + " " * 4 + "/\n" + "_" * 5 + "|" + "_" * 6 + "\n")

    lista.append(" " * 5 + "_" * 7 + "\n" + " " * 5 + "|" + " " * 5 + "|\n" + " " * 5 + "|" + " " * 4 + "\\0/\n" +
                 " " * 5 + "|" + " " * 5 + "|\n" + " " * 5 + "|" + " " * 4 + "/ \\\n" + "_" * 5 + "|" + "_" * 6 + "\n")

    return lista


def autor():
    return "Francisco Domínguez"


# Obtiene una palabra aleatoriamente
def damePalabra():
    palabras = ["MESA", "HABITACION", "COCINA",
                "PUENTE", "COCHE", "IGLESIA", "ORDENADOR"]
    return random.choice(palabras)


# Pinta un recuadro con un texto dentro
def recuadro(texto, h_char, v_char):
    print(h_char * (len(texto) + 4))
    print("{} {} {}".format(v_char, texto, v_char))
    print(h_char * (len(texto) + 4))


# Muestra tanto la imagen del ahorcado, la palabra oculta, los intentos fallidos y las letras usadas
def escena(pal, usadas, intentos):

    letras = ""

    palabraOculta = ""

    for x in range(len(usadas)):    # Añade a un str el array de letras usadas
        letras += usadas[x]

    print(listaNivelesAhorcado[intentos])

    # Para cada letra de palabra si ya la esta en el array de usadas la muestra y si no escribe un guión bajo
    for letra in pal:
        if letra in usadas:
            palabraOculta += letra
        else:
            palabraOculta += "_"

    print(palabraOculta)

    print("<{}> Intentos: {}".format(letras, intentos))


def pideLetra(usadas):
    while True:
        letra = input("Introduzca una letra: ").upper()
        if (letra in usadas):
            print("La letra ya la has introducido anteriormente.")
        elif letra.isalpha() == False:
            print("Error. Debes introducir una letra.")
        elif (len(letra) == 1):
            break
        else:
            print("Debes introducir solo un caracter.")

    return letra


def comprueba(palabra, usadas, letra, intentos):
    continuar = True
    gana = False

    usadas.append(letra)    #Añade la letra en usadas porque ya ha comprobado anteriormente que no se haya añadido

    if letra not in palabra:    #Si la letra no está en la palabra suma un fallo
        intentos += 1
    else:   #Gana lo pone en true y en el caso que no esté en usadas lo pone a False
        gana = True
        for l in palabra:
            if l not in usadas:
                gana = False

    if (gana == True or intentos >= 6):     #Comprueba siempre si termina ya sea porque gane o cumpla el máximo de fallos
        continuar = False

    return continuar, gana, usadas, intentos


listaNivelesAhorcado = imgAhorcado()
# Obtener una palabra a adivinar
palabra = damePalabra()

# Letras que ya se han usado
usadas = []

# intentos realizados
intentos = 0

# Mensaje de inicio
recuadro("Juego del Ahorcado - creado por " + autor(), "#", "#")
recuadro("Comienza el juego", "=", "|")

continuar = True
while continuar:
    escena(palabra, usadas, intentos)
    letra = pideLetra(usadas)
    continuar, gana, usadas, intentos = comprueba(
        palabra, usadas, letra, intentos)


print(listaNivelesAhorcado[intentos])
if gana:
    recuadro("Has ganado en {} intentos".format(intentos), "*", "*")
else:
    recuadro("Has perdido. La palabra era {}".format(palabra), "-", "|")
