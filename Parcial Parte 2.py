def menu():
    print("\n - - - - MENÚ - - - -\n1. Calcular el MCD de dos números\n2. Cadena repetida N veces\n3. Contar cuantas veces aparece una letra\n4. Convertir un número decimal a binario\n5. Calcular cuantos digitos tiene un número\n6. Salir")

def main():
    while True:
        try:
            menu()
            op = int(input("Seleccione una opción: "))
            match op:
                case 1:
                    print("Opción 1")
                case 2:
                    print("Opción 2")
                case 3:
                    print("Opción 3")
                case 4:
                    print("Opción 4")
                case 5:
                    print("Opción 5")
                case 6:
                    print("Saliendo . . .")
                    break
                case _:
                    print("Esa opción no existe, reintente")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")
main()