# examen_notas.py
import sys

# Lista de estudiantes y sus notas
notas = {}

def registrar_nota():
    nombre = input("Nombre del estudiante: ")
    while True:
        try:
            nota = float(input("Nota (1.0 a 7.0): "))
            if 1.0 <= nota <= 7.0:
                break
            else:
                print("Por favor, ingresa una nota válida entre 1.0 y 7.0.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    notas[nombre] = nota
    print(f"Nota registrada para {nombre}: {nota}")

def calcular_promedio():
    if not notas:
        print("No hay notas registradas.")
        return
    promedio = sum(notas.values()) / len(notas)
    print(f"El promedio de las notas es: {promedio:.2f}")

def mostrar_notas():
    if not notas:
        print("No hay notas registradas.")
        return
    for nombre, nota in notas.items():
        print(f"{nombre}: {nota}")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Registrar nota")
        print("2. Ver todas las notas")
        print("3. Calcular promedio")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            registrar_nota()
        elif opcion == '2':
            mostrar_notas()
        elif opcion == '3':
            calcular_promedio()
        elif opcion == '4':
            print("¡Adiós!")
            sys.exit()
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()