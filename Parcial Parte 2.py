from os import write


def menu():
    print("\n - - - - MENÚ - - - -\n1. Calcular el MCD de dos números\n2. Cadena repetida N veces\n3. Contar cuántas veces aparece una letra\n4. Convertir un número decimal a binario\n5. Calcular cuántos dígitos tiene un número\n6. Salir")

def calcularMCD():
    while True:
        try:
            n1 = int(input("\nIngrese el primer número: "))
            if n1 > 0:
                n2 = int(input("Ingrese el segundo número: "))
                if n2 > 0:
                    print(f"El MCD de {n1} y {n2} es: {calculoMCD(n1, n2)}")
                    break
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
        cadena = input("\nIngrese una palabra: ")
        if cadena or cadena.isspace():
            while True:
                try:
                    veces = int(input("Ingrese las veces que se repetira la palabra: "))
                    if veces > 0:
                        print(f"La cadena repetida {veces} veces es: {repetirCadena(cadena,veces)}")
                        break
                    else:
                        print("Dato inválido de veces, reintente")
                except Exception as ex:
                    print(f"Ha ocurrido un error: {ex}")
            break
        else:
            print("La palabra no es valida, reintente")

def repetirCadena(cadena, veces):
    if veces == 0:
        return ""
    else:
        return cadena + repetirCadena(cadena, veces - 1)

def contarLetra():
    while True:
        cadena = input("\nIngrese una palabra: ").lower()
        if cadena or cadena.isspace():
            while True:
                letra = input("Ingrese una letra: ").lower()
                if len(letra) == 1:
                    print(f"La letra {letra} aparece {letraContada(cadena,letra)} veces")
                    break
                else:
                    print("Solo debe de ser una letra, reintente")
            break
        else:
            print("La palabra no es valida, reintente")

def letraContada(cadena, letra, contador = 0, aux = 0):
    if contador == len(cadena):
        return aux
    else:
        if letra == cadena[contador]:
            aux = aux + 1
        return letraContada(cadena, letra, contador + 1, aux)

def convertirBinario():
    while True:
        try:
            n = int(input("\nIngrese un número para convertirlo a binario: "))
            if n > 0:
                print(f"El número {n} en binario es: {binario(n)}")
                break
            else:
                print("El número ingresado no es válido, reintente")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")

def binario(n, listaBinario = []):
    if n == 0:
        listaBinario.reverse()
        return listaBinario
    else:
        if n % 2 == 0:
            listaBinario.append(0)
        else:
            listaBinario.append(1)
        return binario(n // 2, listaBinario)

def contarDigitos():
    while True:
        try:
            n = int(input("\nIngrese un número: "))
            if n > 0:
                print(f"El número {n} tiene {contadorDig(n)} dígitos")
                break
            else:
                print("No es valido el número")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")

def contadorDig(n, cont = 0):
    if n == 0:
        return cont
    else:
        return contadorDig(n // 10, cont + 1)

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
                    contarLetra()
                case 4:
                    convertirBinario()
                case 5:
                    contarDigitos()
                case 6:
                    print("Saliendo . . .")
                    break
                case _:
                    print("Esa opción no existe, reintente")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")
main()