print("¡Bienvenido al sistema de gestión de espacios del Almacén Industrial!")

capacidad_total = 60
espacios_disponibles = 60

while True:

    print("=== MENÚ PRINCIPAL ===")
    print("1. Espacios disponibles")
    print("2. Ocupar espacio")
    print("3. Liberar espacio")
    print("4. Historial de ocupaciones")
    print("5. Salir")

    while True:
        try:
            opcion_menu = int(input("Ingrese una opción del menú: "))
            break
        except ValueError:
            print("Error. Debe ingresar un número entero positivo del 1 al 5.")

    match opcion_menu:

        case 1:
            print(f"Cantidad de espacios disponibles: {espacios_disponibles}.")

        case 2:
            while True:
                try:
                    espacios_ocupar = int(input("Ingrese la cantidad de espacios a ocupar: "))
                    if espacios_ocupar > 0 and espacios_ocupar <= espacios_disponibles:
                        espacios_disponibles = espacios_disponibles - espacios_ocupar
                        break
                    else:
                        print("Error. El valor debe ser mayor a cero y menor a la cantidad de espacios disponibles.")
                except ValueError:
                    print("Error. Ingrese un valor numérico.")

        case 3:
            while True:
                try:
                    espacios_liberar = int(input("Ingrese la cantidad de espacios a liberar: "))
                    if (espacios_liberar >= 0) and (espacios_liberar <= (capacidad_total - espacios_disponibles)): # acá el enunciado dice: "No supere la capacidad máxima (60 espacios)" por lo tanto debería ser capacidad_total, pero no tiene sentido porque aumenta la capacidad total sobre 60 asi que se usará espacios ocupados que es la capacidad total menos los espacios disponibles.
                        espacios_disponibles = espacios_disponibles + espacios_liberar
                        break
                    else:
                        print(f"Error. El valor debe ser mayor a cero y menor a la capacidad ocupada que es: {capacidad_total - espacios_disponibles}.")
                except ValueError:
                    print("Error. Ingrese un valor numérico.")

        case 4:
            print(f"Espacios disponibles: {espacios_disponibles}.")
            print(f"Espacios ocupados: {capacidad_total - espacios_disponibles}.")

        case 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            break

        case _:
            print("Error. Debe ingresar un valor del 1 al 5.")