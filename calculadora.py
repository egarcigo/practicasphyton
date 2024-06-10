# Solicitar datos con mensajes claros
def solicitar_dato(mensaje: str, tipo: type):
    while True:
        try:
            return tipo(input(mensaje))
        except ValueError:
            print(f"Error: {mensaje}")

# Solicitud de datos con mensajes claros
Nombre = input('Ingresa tu nombre: ')
ApellidoPaterno = input('Ingresa tu apellido paterno: ')
ApellidoMaterno = input('Ingresa tu apellido materno: ')
Edad = solicitar_dato('Ingresa tu edad (número entero): ', int)
Peso = solicitar_dato('Ingresa tu peso (número decimal): ', float)
Estatura = solicitar_dato('Ingresa tu estatura (número decimal): ', float)

# Cálculo del índice de masa corporal
MasaCorporal = Peso / (Estatura ** 2)

print(f"Tu nombre es {Nombre} {ApellidoPaterno} {ApellidoMaterno} y tu índice de masa corporal es {MasaCorporal:.2f}")
