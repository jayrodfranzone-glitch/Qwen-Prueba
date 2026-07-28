"""Calculadora básica en Python."""

from operaciones import sumar, restar, multiplicar, dividir


def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n=== Calculadora ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def obtener_numero(mensaje):
    """Solicita un número al usuario."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número válido.")


def main():
    """Función principal que ejecuta la calculadora."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opción no válida. Intenta de nuevo.")
            continue

        num1 = obtener_numero("Ingresa el primer número: ")
        num2 = obtener_numero("Ingresa el segundo número: ")

        try:
            if opcion == "1":
                resultado = sumar(num1, num2)
                operacion = "+"
            elif opcion == "2":
                resultado = restar(num1, num2)
                operacion = "-"
            elif opcion == "3":
                resultado = multiplicar(num1, num2)
                operacion = "*"
            elif opcion == "4":
                resultado = dividir(num1, num2)
                operacion = "/"

            print(f"\nResultado: {num1} {operacion} {num2} = {resultado}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
