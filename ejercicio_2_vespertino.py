cantidad_espacios_disponibles = 60
cantidad_espacios_ocupados = 0

print("¡Bienvenido al sistema de gestión de espacios del Almacén Industrial!")

while True:
    print("=== MENÚ PRINCIPAL ===")
    print("1. Espacios disponibles")
    print("2. Ocupar espacio")
    print("3. Liberar espacio")
    print("4. Historial de ocupaciones")
    print("5. Salir")

    while True:
        try: 
            opcion = int(input("Ingrese la opción a ejecutar: "))
            break
        except ValueError:
            print("Ingresa una opción valida")

    if opcion == 1:
        calculo_espacios_disponibles = cantidad_espacios_disponibles - cantidad_espacios_ocupados
        print(f"La cantidad de espacios disponibles es {calculo_espacios_disponibles}")

    elif opcion == 2:
        calculo_espacios_disponibles = cantidad_espacios_disponibles - cantidad_espacios_ocupados

        while True:
            try:
                espacios_ocupar = int(input("Ingresa la cantidad de espacios a ocupar: "))

                if espacios_ocupar > calculo_espacios_disponibles or espacios_ocupar <= 0:
                    print("Ingrese una cantidad menor o igual a la disponible y mayor a 0")
                else:
                    cantidad_espacios_ocupados = espacios_ocupar
                    break
                
            except ValueError:
                print("Ingrese una cantidad menor o igual a la disponible y mayor a 0")        

    elif opcion == 3:
        while True:
            try:

                espacios_liberar = int(input("Ingresa la cantidad de espacios a liberar: "))

                if espacios_liberar > 0 and espacios_liberar <= cantidad_espacios_ocupados:
                    cantidad_espacios_ocupados -= espacios_liberar
                    break
                else:
                    print("Los espacios a liberar deben ser igual o menor a los espacios utilizados y debe ser mayor a 0")
            
            except ValueError:
                print("Los espacios a liberar deben ser igual o menor a los espacios utilizados y debe ser mayor a 0")

    elif opcion == 4:
        print(f"La cantidad de espacios utilizados en la sesión es {cantidad_espacios_ocupados}")

    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break

    else:
        print("Ingresa una opción valida")