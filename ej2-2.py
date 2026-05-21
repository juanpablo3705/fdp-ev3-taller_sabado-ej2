print("¡Bienvenido al sistema de gestión de espacios del Almacén Industrial!")

espacios_disponibles = 60
ocupaciones = 0
liberaciones = 0

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
            print("Error. Ingrese números, no letras.")

    match opcion_menu:

        case 1:
            print(f"Espacios disponibles: {espacios_disponibles}.")

        case 2:
            while True:
                try:
                    espacios_ocupar = int(input("Ingrese los espacios a ocupar: "))
                    if espacios_ocupar > 0 and espacios_ocupar <= espacios_disponibles:
                        espacios_disponibles = espacios_disponibles - espacios_ocupar
                        ocupaciones = ocupaciones + 1
                        break
                    else:
                        print(f"Error. Los espacios a ocupar deben ser mayores a cero y menores o iguales a los espacios disponibles que son {espacios_disponibles}.")
                except ValueError:
                    print("Error. Los espacios a ocupar solo pueden ser números.")

        case 3:
            while True:
                try:
                    espacios_liberar = int(input("Ingrese los espacios a liberar: "))
                    if espacios_liberar > 0 or espacios_liberar <= espacios_disponibles:
                        espacios_disponibles = espacios_disponibles + espacios_liberar
                        liberaciones = liberaciones + 1
                        break
                    else:
                        print("Error. Los espacios a liberar deben ser mayor a cero y menor o igual a los espacios disponibles.")
                except ValueError:
                    print("Error. Los espacios a liberar deben ser numeros no letras.")

        case 4:
            print(f"Se han hecho {ocupaciones} procesos de ocupaciones.")
            print(f"Se han hecho {liberaciones} procesos de liberaciones.")
            print(f"Espacios ocupados: {(60 - espacios_disponibles)}")
            print(f"Espacios disponibles: {espacios_disponibles}.")

        case 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            break

        case _:
            print("Error, debe ingresar opciones del 1 al 5.")