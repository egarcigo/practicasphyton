# Programa para validar la longitud de una palabra

# Solicita la palabra al usuario
palabra = input("Ingresa una palabra: ")  # Recoge la palabra ingresada por el usuario
longitud = len(palabra)  # Calcula la longitud de la palabra

# Verifica la longitud de la palabra e imprime el mensaje correspondiente
if 4 <= longitud <= 8:
    print("La palabra es correcta.")  # Imprime si la longitud está entre 4 y 8
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.")  # Imprime si la longitud es menor que 4
else:
    print(f"Sobran letras. Tiene {longitud} letras.")  # Imprime si la longitud es mayor que 8

# Programa para determinar el cuadrante de un punto

# Solicita las coordenadas al usuario
x = float(input("Ingrese X: "))  # Recoge el valor de X ingresado por el usuario y lo convierte a flotante
y = float(input("Ingrese Y: "))  # Recoge el valor de Y ingresado por el usuario y lo convierte a flotante

# Verifica que ninguna coordenada sea 0 y determina el cuadrante
if x == 0 or y == 0:
    print("Ninguna coordenada puede ser cero.")  # Imprime un mensaje si X o Y es cero
elif x > 0 and y > 0:
    print("El punto se encuentra en el cuadrante I.")  # Cuadrante I si ambos valores son positivos
elif x < 0 and y > 0:
    print("El punto se encuentra en el cuadrante II.")  # Cuadrante II si X es negativo y Y positivo
elif x < 0 and y < 0:
    print("El punto se encuentra en el cuadrante III.")  # Cuadrante III si ambos valores son negativos
else:
    print("El punto se encuentra en el cuadrante IV.")  # Cuadrante IV si X es positivo y Y negativo