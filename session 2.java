def main():
    tamano = int(input("Ingrese un valor para tamaño (byte): "))
    superfie = int(input("Ingrese un valor para superficie (short): "))
    distance = int(input("Ingrese un valor para distancia (long): "))
    isActive_input = input("Ingrese true o false para isActive: ").lower()
    isActive = True if isActive_input == "true" else False
    salary = float(input("Ingrese un valor para salario (float): "))
    year = int(input("Ingrese un valor para año (int): "))
    pi = float(input("Ingrese un valor para pi (double): "))

    print("\nValores ingresados:")
    print("Tamaño:", tamano)
    print("Superficie:", superfie)
    print("Distancia:", distance)
    print("¿Está activo?:", isActive)
    print("Salario:", salary)
    print("Año:", year)
    print("El valor de pi es:", pi)

if __name__ == "__main__":
    main()
