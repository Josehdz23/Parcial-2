def menu():
    print("\n - - - - MENÚ - - - -\n1. Calcular el MCD de dos números\n2. Cadena repetida N veces\n3. Contar cuantas veces aparece una letra\n4. Convertir un número decimal a binario\n5. Calcular cuantos digitos tiene un número\n6. Salir")

def calcularMCD():
    while True:
        try:
            n1 = int(input("Ingrese el primer número: "))
            if n1 > 0:
                n2 = int(input("Ingrese el segundo número: "))
                if n2 > 0:
                    calculoMCD(n1, n2)
                    print(f"El MCD de {n1} y {n2} es: {calculoMCD(n1, n2)}")
            else:
                print("El 0 no está permitido ")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")
def calculoMCD(n1, n2):
    if n2 == 0:
        return n1
    else:
        return  calculoMCD(n2, n1 % n2)

def cadenaRepetida():
    while True:
        cadena = input("Ingrese una palabra: ")

def main():
    while True:
        try:
            menu()
            op = int(input("Seleccione una opción: "))
            match op:
                case 1:
                    calcularMCD()
                case 2:
                    cadenaRepetida()
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