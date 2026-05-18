print("¡Bienvenido al sistema de gestión de espacios del Almacén Industrial!")

espacios_disponibles = 60
espacios_ocupados = 0

while True:
    print("=== MENÚ PRINCIPAL ===")
    print("1. Espacios disponibles")
    print("2. Ocupar espacio")
    print("3. Liberar espacio")
    print("4. Historial de ocupaciones")
    print("5. Salir")

    # Solicitamos la opción de menú hasta que ingrese una opción valida
    while True:
        try:
            opcion = int(input("Ingrese la opción a ejecutar: "))
            break
        except Exception:
            print("Ingrese una opción valida")

    if (opcion == 1):
        calculo_espacios_disponibles = espacios_disponibles - espacios_ocupados
        print(f"Los espacios disponibles son {calculo_espacios_disponibles}")


    elif (opcion == 2):
        # Restamos a los espacios totales (60) los espacios ocupados
        calculo_espacios_disponibles = espacios_disponibles - espacios_ocupados

        # Solicitamos los espacios a utilizar
        while True:
            try:
                espacios_ocupar = int(input("Ingrese la cantidad de espacios a utilizar: "))
                break
            except Exception:
                print("La cantidad debe ser un número mayor que 0")

        # Debe ser mayor que 0 y menor o igual a la cantidad de espacios disponibles
        if espacios_ocupar > 0 and espacios_ocupar <= calculo_espacios_disponibles:
            espacios_ocupados += espacios_ocupar
            print(f"Has reservado {espacios_ocupar} espacios")
        else:
            print("La cantidad de espacios a ocupar supera la cantidad de espacios disponibles")

    elif (opcion == 3):

        # Solicitamos los espacios a liberar
        while True:
            try:
                espacios_liberar = int(input("Ingrese la cantidad de espacios a liberar:"))
                break
            except Exception:
                print("La cantidad de espacios a liberar deber ser un número mayor a 0")

        # Los espacios a liberar deben ser más de 1 y menor o igual a la cantidad de espacios ocupados
        if espacios_liberar > 0 and espacios_liberar <= espacios_ocupados:
            espacios_ocupados -= espacios_liberar
            print(f"Has liberado {espacios_liberar} espacios")
        else:
            print("La cantidad de espacios a liberar debe ser menor o igual a la cantidad de espacios utilizados.")

    elif (opcion == 4):
        print(f"Los espacios utilizados son {espacios_ocupados}")

    elif (opcion == 5):
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break
    else:
        print("Ingrese una opción valida")
    